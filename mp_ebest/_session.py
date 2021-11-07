# -*- coding=utf-8 -*-
"""
주요 기능: 
    - ebest XING-API 로그인
    - 

사용례: 
    - 
"""

##@@@ 모듈 import
##============================================================

##@@ Built-In 모듈
##------------------------------------------------------------
import os, sys
import time

##@@ Package 모듈
##------------------------------------------------------------
import yaml
import pythoncom
from win32com.client import DispatchWithEvents

##@@ User 모듈
##------------------------------------------------------------
sys.path.append(os.path.join(os.path.dirname(__file__), '../../_public'))
from utils_basic import (
    _read_file, 
    _write_file, 
    _create_folder,
    _project_dicts
)

from utils_xlsx import (
    read_xsheet, 
    write_xsheet,
)

sys.path.append(os.path.join(os.path.dirname(__file__), '../_config'))
from configs import (
    # ACCOUNT_EBEST, 
    _account
)

##@@@ 전역 상수/변수
##============================================================

# ##@@ path, 
# ##------------------------------------------------------------

# ## 계정account 정보가 있는 폴더
# CONIFIG_FOLDER = os.path.join(os.path.abspath('../_config/')).replace("\\", "/")

# ##@@@ 보조 함수
# ##============================================================

# ##@@ 아이디/비밀번호 설정
# ##------------------------------------------------------------

# def _set_login(mode="DEMO", division="주식"):
#     return globals()[f"ACCOUNT_EBEST"][mode]  ## TODO: ACCOUNT_{division}_{agency.upper()}


##@@ 세션 핸들러
##------------------------------------------------------------
class _SessionHandler:
    def OnLogin(self, code, msg):
        """ 서버와의 로그인이 끝나면 실행되는 함수
            @arg code[str] 서버에서 받은 메시지 코드
            @arg msg[str] 서버에서 받은 메시지 정보
        """
        self.waiting = False
        # self.waiting = True
    
        if code == '0000':
            print('[*] 로그인 성공')
        else:
            print(f'[*] 로그인 실패 : {msg}')
    
    def OnDisconnect(self):
        """ 서버와의 연결이 끊어졌을 때 실행되는 함수
        """
        self.waiting = False
        print('[*] 서버와의 연결이 끊어졌습니다')


##@@@ 실행 함수
##============================================================

##@@ 세션
##------------------------------------------------------------

class Session():
    _session = DispatchWithEvents('XA_Session.XASession', _SessionHandler)
    def __init__(self, mode="DEMO"):
        """ 로그인
        """
        # NOTE: 동일 mode의 연결이 있으면 pass
        if self._session.IsConnected() and self._session.mode == mode:
            # print(f"이미 '{mode}'로 로그인 중입니다.")
            pass
            # self._session.DisconnectServer()
        else:
            config = _account(mode=mode)
            if self._session.IsConnected():
                print(f"로그인 모드를 '{self._session.mode}'에서 '{mode}'로 변경합니다.")

            # 로그인
            print(f"ebest로 로그인합니다.")
            url = {
                'r': 'hts.ebestsec.co.kr',
                'd': 'demo.ebestsec.co.kr',
                'a': '127.0.0.1'
            }.get(mode.lower()[:1], 'demo.ebestsec.co.kr')
            port = 20001
            cert = '' if url == 'demo.ebestsec.co.kr' else config['cert']

            print(f"{mode}, {config}")
            # 로그인 요청을 보낸다
            self._session.mode = mode  # NOTE: 동일 모드 로그인 확인용
            # self._session.id = id  # NOTE: 동일 아이디 로그인 확인용
            self._session.waiting = True
            self._session.ConnectServer(url, port)
            self._session.Login(config['id'], config['pw'], cert, 0, 0)

            while self._session.waiting:
                pythoncom.PumpWaitingMessages()


if __name__ == "__main__":
    pass
    s1 = Session(mode="DEMO")
    time.sleep(2)
    print(f"{id(s1)}")
    s1 = Session(mode="REAL")
    time.sleep(2)
    print(f"{id(s1)}")
    s1 = Session(mode="REAL")
    time.sleep(2)
    print(f"{id(s1)}")
    s1 = Session(mode="ACE")
    print(f"{id(s1)}")
    
    # l = _set_login(mode='DEMO', division='주식')
    # l = _set_login_xlsx(mode='DEMO', division='주식')
    # print(l)
