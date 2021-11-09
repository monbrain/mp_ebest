
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
PACKED_JSON_FILE = "packed_ebest_api.json"
SPEC_DICT_FILE = "sample.py"

BLOCK_VAR = "EBEST_API_SPECS"  # python에 삽입할 block 시작 문자열

ADDED_MAIN_FIELDS = {  # master json에 추가될 필드
    "res_type": "",  # res 종류: TR|Real
    "desc_devCenter": "",  # API 설명(devCenter)
    "usage": "fetch", # 사용용도: fetch|tranaction|search|check
    "priority": "3",  # 우선순위: 1|2|3|4|5 클수록 우선순위 높음
    "market": "KRX",  # KOSPI / KOSDAQ / KRX: KOSPI + KOSDAQ
    "item": "",  # 거래 아이템: 현물|선물|옵션
    "remark": "",  # 비고: API 특징
    "limit_1sec": "",  # 요청 제한: 1sec당 req 횟수 
    "limit_10min": "",  # 요청 제한: 10min당 req 횟수
    "included": ""  # 사용(포함)된 파일: 예) fetch.py
}

##@@@ Private Function
##============================================================

##@@ util function TODO: mp_util에서 import
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
    """파일로 저장(파일 확장자(json/csv/xlsx/...)별 저장 방법 자동 지정)

    Args:
        data ([type]): [description]
        path ([type]): [description]

    Returns:
        [type]: [description]
    """
    if '.json' in path[-6:]:
        json.dump(data, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=4)
        return True
    else:
        with open(path, "w", encoding="utf-8") as f:
            f.write(data)
            f.close
        return True


def _load_from_cloud():
    pass


def _save_to_cloud():
    pass


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


def _split_inblock_packed_json(val):
    # "shcode": " ##단축코드@@"
    part = val.split("##")
    default = part[0].strip()
    desc = part[1].split("@@")[0].strip()
    attr = part[1].split("@@")[1].strip()
    return (desc, attr, default)


def _split_outblock_packed_json(val):
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
    desc = part.split("@@")[0].strip()
    attr = part.split("@@")[1].strip()
    return (desc, attr, nick)


def _search_field_index_master_json(res_code="", block_type="input", block_name="InBlock", query={"name": ""}, master={}):
    """master json에서 (res_code, block_type, block_name, query)를 만족하는 field의 list index

    Args:
        res_code (str, optional): [description]. Defaults to "".
        block_type (str, optional): [description]. Defaults to "input".
        block_name (str, optional): [description]. Defaults to "InBlock".
        query (dict, optional): [description]. Defaults to {"name": ""}.
        master (dict, optional): [description]. Defaults to {}.

    Returns:
        [type]: [description]
    """
    for index, field in enumerate(master[res_code][block_type][block_name]['fields']):
        if field[list(query.keys())[0]] == list(query.values())[0]:
            return index
    return False


def _update_inblock_master_json(res_code="", block_name="InBlock", field_name="", field_val="", master={}):
    # field_name: <field_name>, field_val: "<default>##<desc>@@<attr>"
    (desc, attr, default) = _split_inblock_packed_json(field_val)
    # @@@
    index = _search_field_index_master_json(res_code=res_code, block_type="input", block_name=block_name, query={"name": field_name}, master=master)
    # _update_master_block_val(res_code, block_type, block_name, index, field_name, key, val) @@@
    master[res_code]['input'][block_name]['fields'][index]['desc'] = desc
    master[res_code]['input'][block_name]['fields'][index]['attr'] = attr
    master[res_code]['input'][block_name]['fields'][index]['default'] = default


def _update_outblock_master_json(res_code="", block_name="InBlock", field_name="", field_val="", master={}):
    use = 1
    if '#' in field_name:
        field_name = field_name.replace("#", "")
        use = 0
    (desc, attr, nick) = _split_outblock_packed_json(field_val)

    index = _search_field_index_master_json(res_code=res_code, block_type="output", block_name=block_name, query={"name": field_name}, master=master)
    master[res_code]['output'][block_name]['fields'][index]['desc'] = desc
    master[res_code]['output'][block_name]['fields'][index]['attr'] = attr
    master[res_code]['output'][block_name]['fields'][index]['nick'] = nick
    master[res_code]['output'][block_name]['fields'][index]['use'] = use


# _update_master_block_val(res_code, block_type, block_name, index, field_name, val)


##@@ data extract/convert function
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

    def parse_field(line, block_type):
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

            if block_type == "input":
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
        res_code = fname.replace('.res','')

        meta[res_code] = parse_file(
            _load_from_file(os.path.join(src, fname), type="list", encoding="cp949")
            # open(os.path.join(src, fname), encoding="cp949").readlines()
        )

        for key, val in ADDED_MAIN_FIELDS.items():
            meta[res_code][key] = val

        if len(res_code) < 4 or '_' in res_code:
            meta[res_code]['res_type'] = "Real"
        else:
            meta[res_code]['res_type'] = "TR"

        meta[res_code]['desc_devCenter'] = meta[res_code]['desc']


    return meta


def _packed_json_from_master_json(src={}):
    """master_json 파일 -> packed_json(json 형식 유지/comment 삽입)

    Args:
        src (dict, optional): [description]. Defaults to None.
        dst (dict, optional): [description]. Defaults to None.
        query (None|list|str, optional): Query에 해당하는 Res에 대한 packed json 
    """

    packed = {}
    for res_code, data in src.items():
        out = {}
        for block_type, v0 in data.items():
            if block_type == 'desc':
                desc = v0
                continue
            out[block_type] = {}
            for block_name, block_val in v0.items():
                out[block_type][block_name] = {}
                for field_name, field_val in block_val.items():
                    if field_name == 'fields' and block_type == 'input':
                        for field in field_val:
                            out[block_type][block_name][field['name']] = f"{field['default']}##{field['desc']}@@{field['attr']}"
                    if field_name == 'fields' and block_type == 'output':
                        for field in field_val:
                            use_tag = "#" if field['use'] == 0 else ""
                            out[block_type][block_name][f"{use_tag}{field['name']}"] = f"{field['nick']}`{field['type']}##{field['desc']}@@{field['attr']}"
            packed[f"{res_code}##{desc}"] = out

    return packed


def _spec_dict_from_packed_json(src=""):
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


def _packed_json_from_spec_dict(src=""):
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


def _master_json_from_packed_json(src={}, dst={}):
    """master_json <- packed json

    Args:
        src (str, ""): [description]. Defaults to None.

    Returns:
        [type]: [description]
    """

    # dst = {}
    for res_code, data in src.items():
        (code, _desc) = res_code.split("#", 1)
        # out = {}
        for block_type, v0 in data.items():
            # out[block_type] = {}
            for block_name, block_val in v0.items():
                # out[block_type][block_name] = {}
                for field_name, field_val in block_val.items():
                    if block_type == 'input':
                        _update_inblock_master_json(res_code=code, block_name=block_name, field_name=field_name, field_val=field_val, master=dst)
                        # # field_name: <field_name>, field_val: "<default>##<desc>@@<attr>"
                        # (desc, attr, default) = _split_inblock_packed_json(field_val)
                        # # @@@
                        # index = _search_field_index_master_json(res_code=code, block_type=block_type, block_name=block_name, query={"name": field_name}, master=dst)
                        # # _update_master_block_val(res_code, block_type, block_name, index, field_name, key, val) @@@
                        # dst[res_code][block_type][block_name]['fields'][index]['desc'] = desc
                        # dst[res_code][block_type][block_name]['fields'][index]['attr'] = attr
                        # dst[res_code][block_type][block_name]['fields'][index]['default'] = default

                    if block_type == 'output':
                        _update_outblock_master_json(res_code=code, block_name=block_name, field_name=field_name, field_val=field_val, master=dst)
                        # name = field_name
                        # use = 1
                        # if '#' in field_name:
                        #     name = name.replace("#", "")
                        #     use = 0
                        # (desc, attr, nick) = _split_outblock_packed_json(field_val)

                        # index = _search_field_index_master_json(res_code=code, block_type=block_type, block_name=block_name, query={"name": field_name}, master=dst)
                        # # _update_master_block_val(res_code, block_type, block_name, index, field_name, key, val) @@@
                        # dst[res_code][block_type][block_name]['fields'][index]['desc'] = desc
                        # dst[res_code][block_type][block_name]['fields'][index]['attr'] = attr
                        # dst[res_code][block_type][block_name]['fields'][index]['nick'] = nick

            # dst[f"{res_code}##{desc}"] = out

    return dst


def _master_json_from_spec_dict(src={}, dst={}):
    """master_json <- packed json

    Args:
        src (str, ""): [description]. Defaults to None.

    Returns:
        [type]: [description]
    """
    src = _packed_json_from_spec_dict(src=src)
    return _master_json_from_packed_json(src=src, dst=dst)


def _spec_dict_from_master_json(src={}):
    """master_json <- packed json

    Args:
        src (str, ""): [description]. Defaults to None.

    Returns:
        [type]: [description]
    """
    src = _packed_json_from_master_json(src=src)
    return _spec_dict_from_packed_json(src=src)


##@@ query from master json
##------------------------------------------------------------
def _find_res_code_from_master_json(src={}, query={}):
    if query == {}:
        return list(src.keys())

    rs = []
    for res_code, res_val in src.items():
        if res_val[list(query.keys())[0]] == list(query.values())[0]:
            rs.append(res_code)
    
    return rs


def _find_main_fields_from_master_json(src={}, query={}):
    rs = []
    excluded_fields = ["input", "output"]
    for res_code, res_val in src.items():
        unit = {"res_code": res_code}
        for field_name, field_val in res_val.items():
            if not field_name in excluded_fields:
                unit[field_name] = field_val
        rs.append(unit)
    return rs

    # for res_code, res_val in src.items():
    #     if res_val[list(query.keys())[0]] == list(query.values())[0]:
    #         rs.append(res_code)
    
    # return rs


##@@@ Public Class/function
##============================================================

def init_ebest_api():
    ## NOTE: _master_json_from_res_folder
    src = _master_json_from_res_folder(user_data=True)
    _save_to_file(src, f"{JSON_FOLDER}{MASTER_USER_FILE}")

    # _save_to_file(_packed_json_from_master_json(src=src), f"{JSON_FOLDER}{PACKED_JSON_FILE}")


def insert_res_block_to_py():
    pass



if __name__ == "__main__":
    pass

    ## NOTE: _master_json_from_res_folder
    # data = _master_json_from_res_folder(user_data=True)
    # _save_to_file(data, f"{JSON_FOLDER}{MASTER_USER_FILE}")

    ## NOTE: _packed_json_from_master_json
    # path = f"{JSON_FOLDER}{MASTER_USER_FILE}"
    # src = _load_from_file(path=path, type="dict")
    # data = _packed_json_from_master_json(src)
    # _save_to_file(data, f"{JSON_FOLDER}{PACKED_JSON_FILE}")

    ## NOTE: _spec_dict_from_packed_json
    # path = f"{JSON_FOLDER}{PACKED_JSON_FILE}"
    # src = _load_from_file(path=path, type="str")
    # data = _spec_dict_from_packed_json(src)
    # _save_to_file(data, f"{JSON_FOLDER}{SPEC_DICT_FILE}")

    ## NOTE: _packed_json_from_spec_dict
    # path = f"{JSON_FOLDER}{SPEC_DICT_FILE}"
    # src = _load_from_file(path=path, type="str")
    # data = _packed_json_from_spec_dict(src)
    # _save_to_file(data, "packed_sample.json")

    ## NOTE: _master_json_from_packed_json
    # src = _load_from_file(path="packed_sample_.json", type="dict")
    # dst = _load_from_file(path=f"{JSON_FOLDER}{MASTER_USER_FILE}", type="dict")
    # data = _master_json_from_packed_json(src=src, dst=dst)
    # path = "master_sample.json"
    # _save_to_file(data, path)

    ## NOTE: _master_json_from_spec_dict(src={}, dst={})
    # src = _load_from_file(path="sample_.py", type="str")
    # dst = _load_from_file(path=f"{JSON_FOLDER}{MASTER_USER_FILE}", type="dict")
    # data = _master_json_from_spec_dict(src=src, dst=dst)
    # path = "master_sample2.json"
    # _save_to_file(data, path)


    ## NOTE: _find_res_code_from_master_json
    src = _load_from_file(path=f"{JSON_FOLDER}{MASTER_USER_FILE}", type="dict")
    # query = {"desc": "ETF호가잔량(B7)"}
    query = {}
    # data = _find_res_code_from_master_json(src=src, query=query)
    data =_find_main_fields_from_master_json(src=src, query=query)
    path = "main_fields.json"
    _save_to_file(data, path)

    ## NOTE: Public Function
    # init_ebest_api()