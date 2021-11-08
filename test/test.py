import os, sys, re, json

XINGAPI_PATH = '/eBEST/xingAPI/'

def _input_default(name="", type="char"):
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

    # '"sdate": " "': '"sdate": datetime.now().strftime' + "('%Y%m%d')",  # 조회 시작일
    # '"edate": " "': '"edate": datetime.now().strftime' + "('%Y%m%d')",  # 조회 종료일
    # '"comp_yn": " "': '"comp_yn": "Y"',  # 압축 전송 여부
    # '"shcode": " "': '"shcode": "005930"',  # 종목코드
    # '"qrycnt": 0': '"qrycnt": 2000',  # 1회 조회 건수
    # '"ncnt": 0': '"ncnt": 1',  # 틱(분)개수 단위?

    return default

# REPLACEMETS_INBLOCKS3 = {
#     '"sdate": " "': '"sdate": datetime.now().strftime' + "('%Y%m%d')",  # 조회 시작일
#     '"edate": " "': '"edate": datetime.now().strftime' + "('%Y%m%d')",  # 조회 종료일
#     '"comp_yn": " "': '"comp_yn": "Y"',  # 압축 전송 여부
#     '"shcode": " "': '"shcode": "005930"',  # 종목코드
#     '"qrycnt": 0': '"qrycnt": 2000',  # 1회 조회 건수
#     '"ncnt": 0': '"ncnt": 1',  # 틱(분)개수 단위?
# }


def init_res_all_json(from_path=XINGAPI_PATH, to_path="res_all.json"):
    """모든 res 파일 -> json 파일

    """
    meta = {}
    
    fnames = filter(
        lambda x: not re.match(r'.*\_\d+\.res$', x),
        os.listdir(os.path.join(from_path, 'res'))
    )

    def parse_field(line, inout):
        cols = line.split(',')
        desc = cols[0].strip()
        size = cols[4].strip()
        attr = ""

        if ":" in desc and "(" in desc:
            (desc, attr) = desc.split("(", 1)
            attr = attr[:-1] + " "
        if "/*" in size:
            (size, _attr) = size.split("/*", 1)
            attr += _attr.replace("*/", "")
        
        ## TODO: attr: "0:시간1:일자"  -> "0: 시간, 1: 일자"
        
        r = {
            'name': cols[1].strip(),
            'desc': desc,  # TODO: "desc": "시장구분(1:코스피2:코스닥3:선물4:콜옵션5:풋옵션6:주식선물)" -> "desc": "시장구분", "attr": "1:코스피..."
            'type': cols[3].strip(),
            'size': size, # TODO: "size": "1/*1:ETF(투자회사형)2:ETF(수익증권형)3:ETN4:손실제한ETN*/", -> "size": "1", "attr": "@@ 1:EFT..."
            'attr': attr.strip(), # field 속성 NOTE: 사용자 추가(편집) 필드, 필드 속성 메모
        }

        if inout == "input":
            r['default'] = _input_default(name=cols[1].strip(), type=cols[3].strip())  # field 디폴트값(inblock용) NOTE: API 요청시 input 디폴트값 지정
        else:
            r['nick'] = cols[1].strip()  # field 별칭(outblock용) NOTE: 사용자 추가(편집) 필드, API 응답후 response key 변경
            r['use'] = 1  # field 사용 여부(outblock용) NOTE: 사용자 추가(편집) 필드, 0: 사용 안함, 1: 사용

        return r


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
            open(os.path.join(XINGAPI_PATH, 'res/', fname), encoding="cp949").readlines()
        )
    
    json.dump(meta, open(to_path, "w", encoding="utf-8"), ensure_ascii=False, indent=4)


def pack_res_all_json(from_path="res_all.json", to_path="packed_res_all.json"):
    """res_all json 파일 -> blocks로 사용할 json

    Args:
        from_path (str, optional): [description]. Defaults to "res_all.json".
        to_path (str, optional): [description]. Defaults to "packed_res_all.json".
    """
    with open(from_path, encoding="utf-8") as f:
        res_all = json.load(f)

    packed = {}
    for res_code, data in res_all.items():
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
                            out[k0][k1][field['name']] = f"{field['default']}##{field['desc']} @@{field['attr']}"
                        # out[k0][k1] = {
                        #     field['name']: f"{field['default']}##{field['desc']} @@{field['attr']}"
                        #     for field in v2
                        # }
                    if k2 == 'fields' and k0 == 'output':
                        for field in v2:
                            use_tag = "#" if field['use'] == 0 else ""
                            out[k0][k1][f"{use_tag}{field['name']}"] = f"{field['nick']}`{field['type']}##{field['desc']} @@{field['attr']}"
            packed[f"{res_code}##{desc}"] = out

    json.dump(packed, open(to_path, "w", encoding="utf-8"), ensure_ascii=False, indent=4)



def dict_string_from_res_json(from_path="packed_res_all.json", to_path="dict_string.py"):
    parsed = "\nblocks = "
    with open(from_path, "r", encoding="utf-8") as f:
        for line in f.readlines():
            parsed += re.sub(r'##(.*)?"(.+)', r'"\2 ## \1', line.replace('"#', '# "')) # + "\n"

    with open(to_path, "w", encoding="utf-8") as f:
        f.write(parsed + "\n")


def pack_res_from_dict_string(from_path="dict_string.py", to_path="packed_res_all_2.json"):

    with open(from_path, "r", encoding="utf-8") as f:
        content = f.read()

    regex = "blocks *= *\{[\S\n ]*?\n\}\n"
    blocks_content = re.findall(regex, content)[0].replace("blocks = ", "")
    out_content = re.sub(r' # *"', ' "#', blocks_content)
    out_content = re.sub(r'" *: *\{ *#+ *(.+)', r'##\1": {', out_content)
    out_content = re.sub(r'", *#+ *(.+)', r'##\1",', out_content)
        
    with open(to_path, "w", encoding="utf-8") as f:
        f.write(out_content + "\n")


def update_blocks_from_packed_json(from_path="packed_res_all_2.json", to_path="dict_string.py"):

    replace_content = "1234567890"  

    with open(to_path, "r+", encoding="utf-8") as f:
        content = f.read()
        print(f"len(content): {len(content)}")

        regex = "blocks *= *\{[\S\n ]*?\n\}\n"  
        blocks_content = re.findall(regex, content)[0]
        print(len(blocks_content))
        print(f"len(blocks_content): {len(blocks_content)}")

        # # content = content.replace(blocks_content, replace_content)
        content = content.replace(blocks_content, replace_content)
        print(content)
        print(f"len(content): {len(content)}")
        # f.write(content + "\n")


    # out_content = re.sub(r' # *"', ' "#', blocks_content)
    # out_content = re.sub(r'" *: *\{ *#+ *(.+)', r'##\1": {', out_content)
    # out_content = re.sub(r'", *#+ *(.+)', r'##\1",', out_content)
        
    # with open(to_path, "w", encoding="utf-8") as f:
    #     f.write(out_content + "\n")


# 2. dict -> json
# ": *\{ *#+ *(.+)	##$1": {
# ", *#+ *(.+)	##$1",

    # with open(to_path, "w", encoding="utf-8") as f:
    #     f.write(parsed)

#     o_block = o_block[o_block[:20].index('{'):]  # NOTE: 'blocks = ' 제거하기 위해 첫번째 '{' 위치 찾음

#     return literal_eval(_replace_re(replace_dict=REPLACEMETS_BLOCKS2, string=o_block))



# init_res_all_json()
# pack_res_all_json()
# dict_string_from_res_json()
# pack_res_from_dict_string()
update_blocks_from_packed_json()



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
