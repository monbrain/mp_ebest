
# -*- coding=utf-8 -*-
"""
주요 기능: 
    - Process XingAPI Query

사용례: 
    - 
"""

##@@@ Package/Module
##============================================================

##@@ Built-In Package/Module
##------------------------------------------------------------
import os, sys, re, json

##@@ External Package/Module
##------------------------------------------------------------


##@@ User Package/Module
##------------------------------------------------------------

##@@@ Constant/Varible
##============================================================

##@@ path, var
##------------------------------------------------------------

# RES_FOLDER = '/eBEST/xingAPI/'
RES_FOLDER = "C:/eBEST/xingAPI/res/"
JSON_FOLDER = ""
PY_FOLDER = ""
MASTER_USER_FILE = "master_ebest_api.json"
MASTER_ORGN_FILE = "__master_ebest_api.json"
PACK_JSON_FILE = "packed_ebest_api.json"
SPEC_DICT_FILE = "sample.py"

BLOCK_VAR = "EBEST_API_SPECS"  # python에 삽입할 block 시작 문자열


##@@@ Private Function
##============================================================

##@@ util function
##------------------------------------------------------------
def _load_from_file(path, type="str", encoding="utf-8"):
    """[summary]

    Args:
        path ([type]): [description]
        type (str, "str"): str(content)|list(line)|dict(json)
        encoding (str, "utf-8"): utf-8|cp949|euc-kr
    """
    f = open(path, "r", encoding=encoding)
    if type == "str":
        data = f.read()
    elif type == "list":
        data = f.readlines()
    elif type == "dict":
        data = json.load(f)
    else:
        data = f.read()
    f.close()

    return data


def _save_to_file(data, path):
    if '.json' in path[-6:]:
        json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=4)
        return True
    else:
        with open(path, "w", encoding="utf-8") as f:
            f.write(data)
            f.close
        return True

##@@ sub function
##------------------------------------------------------------
def _input_default(name="", type="char"):
    """res input 디폴트값 지정

    Args:
        name (str, optional): [description]. Defaults to "".
        type (str, optional): [description]. Defaults to "char".

    Returns:
        [type]: [description]
    """
    ## type별 디폴트값
    if type == 'long' or type == 'int':
        default = 0
    elif type == 'double' or type == 'float':
        default = 0.0
    else:  # 'char', 'string'
        default = ' '
    
    ## name별 디폴트값
    if name == "comp_yn":
        default = "Y"
    elif name == "qrycnt":
        default = 2000
    elif name == "ncnt":
        default = 1

    return default

    # '"sdate": " "': '"sdate": datetime.now().strftime' + "('%Y%m%d')",  # 조회 시작일
    # '"edate": " "': '"edate": datetime.now().strftime' + "('%Y%m%d')",  # 조회 종료일
    # '"comp_yn": " "': '"comp_yn": "Y"',  # 압축 전송 여부
    # '"shcode": " "': '"shcode": "005930"',  # 종목코드
    # '"qrycnt": 0': '"qrycnt": 2000',  # 1회 조회 건수
    # '"ncnt": 0': '"ncnt": 1',  # 틱(분)개수 단위?


def _split_inblock_pack_json(val):
    # "shcode": " ##단축코드@@"
    part = val.split("##")
    default = part[0].strip()
    desc = part[1].split("@@")[0].strip()
    attr = part[1].split("@@")[1].strip()
    return (desc, attr, default)


def _split_outblock_pack_json(val):
    # "#hotime": "ht`char##호가시간@@ Remark 변경",
    # "name": "hotime",
    # "desc": "호가시간",
    # "type": "char",
    # "size": "6",
    # "attr": "",
    # "nick": "hotime",
    # "use": 1
    nick = val.split("`")[0]
    part = val.split("##")[1].strip()
    desc = part[1].split("@@")[0].strip()
    attr = part[1].split("@@")[1].strip()
    return (desc, attr, nick)


def _search_field_index_master_json(res_code="", k0="input", k1="InBlock", query={"name": ""}, master={}):
    """master json에서 (res_code, k0, k1, query)를 만족하는 field의 list index

    Args:
        res_code (str, optional): [description]. Defaults to "".
        k0 (str, optional): [description]. Defaults to "input".
        k1 (str, optional): [description]. Defaults to "InBlock".
        query (dict, optional): [description]. Defaults to {"name": ""}.
        master (dict, optional): [description]. Defaults to {}.

    Returns:
        [type]: [description]
    """
    for index, field in enumerate(master[res_code][k0][k1]['fields']):
        if field[list(query.keys())[0]] == list(query.values())[0]:
            return index
    return False




# _update_master_block_val(res_code, k0, k1, index, k2, val)

##@@ data process function
##------------------------------------------------------------

def _master_json_from_res_folder(src=RES_FOLDER, user_data=True):
    """src 폴더 내의 res 파일 -> master json 파일

    Args:
        src ([type], optional): [description]. Defaults to RES_FOLDER.
        dst ([type], optional): [description]. Defaults to f"{JSON_FOLDER}{MASTER_FILE}".
        user_data (bool, optional): True: 사용자 추가/편집 데이터 적용/False: 원본 데이터 Defaults to False.

    Returns:
        [type]: [description]
    """
    meta = {}

    fnames = filter(
        lambda x: not re.match(r'.*\_\d+\.res$', x),
        os.listdir(src)
    )

    def parse_field(line, inout):
        cols = line.split(',')
        name = cols[1].strip()
        desc = cols[0].strip()
        type = cols[3].strip()
        size = cols[4].strip()

        fields = {
            'name': name,
            'desc': desc,
            'type': type,
            'size': size
        }

        if user_data:  ## NOTE: 사용자 추가/편집 데이터 적용
            attr = ""
            if ":" in desc and "(" in desc:
                (desc, attr) = desc.split("(", 1)  # NOTE: "desc": "시장구분(1:코스피2:코스닥3:선물4:콜옵션5:풋옵션6:주식선물)" -> "desc": "시장구분", "attr": "1:코스피..."
                attr = attr[:-1] + " "  # field 속성 NOTE: 사용자 추가(편집) 필드, 필드 속성 메모
            if "/*" in size:
                (size, _attr) = size.split("/*", 1)  # # TODO: "size": "1/*1:ETF(투자회사형)2:ETF(수익증권형)3:ETN4:손실제한ETN*/", -> "size": "1", "attr": "@@ 1:EFT..."
                attr += _attr.replace("*/", "")

            attr = attr.strip()   ## TODO: attr: "0:시간1:일자"  -> "0: 시간, 1: 일자"
            fields = dict(fields, **dict(desc=desc, size=size, attr=attr))

            if inout == "input":
                fields['default'] = _input_default(name=cols[1].strip(), type=cols[3].strip())  # field 디폴트값(inblock용) NOTE: API 요청시 input 디폴트값 지정
            else:
                fields['nick'] = cols[1].strip()  # field 별칭(outblock용) NOTE: 사용자 추가(편집) 필드, API 응답후 response key 변경
                fields['use'] = 1  # field 사용 여부(outblock용) NOTE: 사용자 추가(편집) 필드, 0: 사용 안함, 1: 사용

        return fields

    def parse_file(lines):
        parsed = {}
        lines = list(map(lambda x: x.replace('\t','').replace('\n','').replace(';','').strip(), lines))
        lines = list(filter(lambda x:x, lines))

        for i in range(len(lines)):
            if '.Func' in lines[i] or '.Feed' in lines[i]:
                parsed['desc'] = lines[i].split(',')[1].strip()
            elif lines[i] == 'begin':
                latest_begin = i
            elif lines[i] == 'end':
                block_info = lines[latest_begin-1].split(',')
                
                if not block_info[2] in parsed:
                    parsed[block_info[2]] = {}

                ## NOTE: input/output에 따라 분기
                parsed[block_info[2]][block_info[0]] = {
                    'occurs': 'occurs' in block_info,
                    'fields': list(map(lambda x: parse_field(x, block_info[2]), lines[latest_begin+1:i]))
                }

        return parsed
    
    for fname in fnames:
        meta[fname.replace('.res','')] = parse_file(
            _load_from_file(os.path.join(src, fname), type="list", encoding="cp949")
            # open(os.path.join(src, fname), encoding="cp949").readlines()
        )

    return meta


def _pack_json_from_meta_json(src={}):
    """meta_json 파일 -> pack_json(json 형식 유지/comment 삽입)

    Args:
        src (dict, optional): [description]. Defaults to None.
        dst (dict, optional): [description]. Defaults to None.
        query (None|list|str, optional): Query에 해당하는 Res에 대한 packed json 
    """

    packed = {}
    for res_code, data in src.items():
        out = {}
        for k0, v0 in data.items():
            if k0 == 'desc':
                desc = v0
                continue
            out[k0] = {}
            for k1, v1 in v0.items():
                out[k0][k1] = {}
                for k2, v2 in v1.items():
                    if k2 == 'fields' and k0 == 'input':
                        for field in v2:
                            out[k0][k1][field['name']] = f"{field['default']}##{field['desc']}@@{field['attr']}"
                    if k2 == 'fields' and k0 == 'output':
                        for field in v2:
                            use_tag = "#" if field['use'] == 0 else ""
                            out[k0][k1][f"{use_tag}{field['name']}"] = f"{field['nick']}`{field['type']}##{field['desc']}@@{field['attr']}"
            packed[f"{res_code}##{desc}"] = out

    return packed


def _spec_dict_from_pack_json(src=""):
    """res spec dict(python 변수용) <- packed json

    Args:
        src (str, ""): [description]. Defaults to None.

    Returns:
        str: [description]
    """
    content = f"{BLOCK_VAR} = "  # block 시작 문자열

    for line in src.splitlines():
        content += re.sub(r'##(.*)?"(.+)', r'"\2 ## \1', line.replace('"#', '# "')) + "\n"

    return content


def _pack_json_from_spec_dict(src=""):
    """res spec dict(python 변수용) <- packed json

    Args:
        src (str, ""): [description]. Defaults to None.

    Returns:
        dict(json): [description]
    """
    regex = BLOCK_VAR + " *= *\{[\S\n ]*?\n\}\n"  ## NOTE: python에 삽입된 block 내용
    # blocks_content = re.findall(regex, content)[0].replace("blocks = ", "")
    data = re.findall(regex, src)[0].split("=", 1)[1].strip()
    data = re.sub(r' # *"', ' "#', data)
    data = re.sub(r'" *: *\{ *#+ *(.+)', r'##\1": {', data)
    data = re.sub(r'", *#+ *(.+)', r'##\1",', data)

    return json.loads(data)


def _master_json_from_pack_json(src={}, dst={}):
    """master_json <- packed json

    Args:
        src (str, ""): [description]. Defaults to None.

    Returns:
        [type]: [description]
    """

    dst = {}
    for res_code, data in src.items():
        (code, _desc) = res_code.split("#", 1)
        out = {}
        for k0, v0 in data.items():
            out[k0] = {}
            for k1, v1 in v0.items():
                out[k0][k1] = {}
                for k2, v2 in v1.items():
                    if k0 == 'input':
                        # k2: <field_name>, v2: "<default>##<desc>@@<attr>"
                        (desc, attr, default) = _split_inblock_pack_json(v2)
                        # @@@
                        index = _search_field_index_master_json(res_code=code, k0=k0, k1=k1, query={"name": k2}, master=dst)
                        # _update_master_block_val(res_code, k0, k1, index, k2, key, val) @@@
                        dst[res_code][k0][k1]['fields'][index]['desc'] = desc
                        dst[res_code][k0][k1]['fields'][index]['attr'] = attr
                        dst[res_code][k0][k1]['fields'][index]['default'] = default

                    if k0 == 'output':
                        name = k2
                        use = 1
                        if '#' in k2:
                            name = name.replace("#", "")
                            use = 0
                        (desc, attr, nick) = _split_outblock_pack_json(v2)

                        index = _search_field_index_master_json(res_code=code, k0=k0, k1=k1, query={"name": k2}, master=dst)
                        # _update_master_block_val(res_code, k0, k1, index, k2, key, val) @@@
                        dst[res_code][k0][k1]['fields'][index]['desc'] = desc
                        dst[res_code][k0][k1]['fields'][index]['attr'] = attr
                        dst[res_code][k0][k1]['fields'][index]['nick'] = nick

            dst[f"{res_code}##{desc}"] = out

    return dst


##@@@ Public Class/function
##============================================================

def update_blocks_from_packed_json(src="packed_meta_json_2.json", dst="dict_string.py", query=None):

    replace_content = _spec_dict_from_pack_json(src=src, dst=None, query=query, save=False)

    with open(dst, "r", encoding="utf-8") as f:
        content = f.read()
        f.close()
        # print(f"len(content): {len(content)}")

        regex = "blocks *= *\{[\S\n ]*?\n\}\n"  
        blocks_content = re.findall(regex, content)[0]
        print(f"len(blocks_content): {len(blocks_content)}")

        # # content = content.replace(blocks_content, replace_content)
        content = content.replace(blocks_content, replace_content)
        print(content)
        print(f"len(content): {len(content)}")

    
    with open(dst, "w", encoding="utf-8") as f:
        f.write(content + "\n")


    # out_content = re.sub(r' # *"', ' "#', blocks_content)
    # out_content = re.sub(r'" *: *\{ *#+ *(.+)', r'##\1": {', out_content)
    # out_content = re.sub(r'", *#+ *(.+)', r'##\1",', out_content)
        
    # with open(dst, "w", encoding="utf-8") as f:
    #     f.write(out_content + "\n")

if __name__ == "__main__":
    pass

    ## NOTE: _master_json_from_res_folder
    # data = _master_json_from_res_folder(user_data=True)
    # _save_to_file(data, f"{JSON_FOLDER}{MASTER_USER_FILE}")

    ## NOTE: _pack_json_from_meta_json
    # path = f"{JSON_FOLDER}{MASTER_USER_FILE}"
    # src = _load_from_file(path=path, type="dict")
    # data = _pack_json_from_meta_json(src)
    # _save_to_file(data, f"{JSON_FOLDER}{PACK_JSON_FILE}")

    ## NOTE: _spec_dict_from_pack_json
    # path = f"{JSON_FOLDER}{PACK_JSON_FILE}"
    # src = _load_from_file(path=path, type="str")
    # data = _spec_dict_from_pack_json(src)
    # _save_to_file(data, f"{JSON_FOLDER}{SPEC_DICT_FILE}")

    ## NOTE: _pack_json_from_spec_dict
    # path = f"{JSON_FOLDER}{SPEC_DICT_FILE}"
    # src = _load_from_file(path=path, type="str")
    # data = _pack_json_from_spec_dict(src)
    # _save_to_file(data, "packed_sample.json")

    path = f"{JSON_FOLDER}{MASTER_USER_FILE}"
    master = _load_from_file(path=path, type="dict")
    # print(master["B7_"])
    # "B7_", "output", "OutBlock", 
    index = _search_field_index_master_json(res_code="B7_", k0="output", k1="OutBlock", query={"name": "lp_offerho1"}, master=master)
    print(f"index: {index}")
    # _pack_json_from_spec_dict()
    # _pack_json_from_spec_dict(src=None, dst="packed_sample.json")
    # update_blocks_from_packed_json()

    # path = f"{JSON_FOLDER}{PACK_JSON_FILE}"
    # _save_to_file(data, path)



# 1. json file line -> dict line
# line = re.sub(r'##(.*)?"(.+)', r'"$2 ## $1', line.replace('"#', '# "')

# 2. dict -> json
# ": *\{ *#+ *(.+)	##$1": {
# ", *#+ *(.+)	##$1",


# def _blocks_dict_from_file(path=''):
#     """
#     path의 파일에서 blocks의 dict값을 반환
#     """
#     content = _read_file(path)  # NOTE: 편집할 파일 내용 읽어옴

#     regex = "blocks *= *\{[\S\n ]*?\n\}\n"  # NOTE: blocks = {...} 부분(읽어올 dict 부분)
#     o_block = re.findall(regex, content)[0]
#     o_block = o_block[o_block[:20].index('{'):]  # NOTE: 'blocks = ' 제거하기 위해 첫번째 '{' 위치 찾음

#     return literal_eval(_replace_re(replace_dict=REPLACEMETS_BLOCKS2, string=o_block))


