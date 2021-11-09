
## test python

EBEST_API_SPECS = {
    "B7_": { ## ETF호가잔량(B7)
        "input": {
            "InBlock": {
                "shcode": " ##단축코드 @@  테스트0"
            }
        },
        "output": {
            "OutBlock": {
                # "hotime": "hot`char", ## 호가시간 @@ 테스트1
                # "lp_offerho1": "lp_offerho1`long", ## LP매도호가수량1@@
                # "lp_bidho1": "lp_bidho1`long", ## LP매수호가수량1 @@ 테스트2
                "lp_offerho2": "lp_offerho2`long", ## LP매도호가수량2@@
                "lp_bidho2": "lp_bidho2`long", ## LP매수호가수량2@@
                "lp_offerho3": "lp_offerho3`long", ## LP매도호가수량3@@
                "lp_bidho3": "lp_bidho3`long", ## LP매수호가수량3@@
                # "lp_offerho4": "lp_offerho4`long", ## LP매도호가수량4@@
                # "lp_bidho4": "lp_bidho4`long", ## LP매수호가수량4@@
                "lp_offerho5": "lp_offerho5`long", ## LP매도호가수량5@@
                "lp_bidho5": "lp_bidho5`long", ## LP매수호가수량5@@
                "lp_offerho6": "lp_offerho6`long", ## LP매도호가수량6@@
                "lp_bidho6": "lp_bidho6`long", ## LP매수호가수량6@@
                "lp_offerho7": "lp_offerho7`long", ## LP매도호가수량7@@
                "lp_bidho7": "lp_bidho7`long", ## LP매수호가수량7@@
                "lp_offerho8": "lp_offerho8`long", ## LP매도호가수량8@@
                "lp_bidho8": "lp_bidho8`long", ## LP매수호가수량8@@
                "lp_offerho9": "lp_offerho9`long", ## LP매도호가수량9@@
                "lp_bidho9": "lp_bidho9`long", ## LP매수호가수량9@@
                "lp_offerho10": "lp_offerho10`long", ## LP매도호가수량10@@
                "lp_bidho10": "lp_bidho10`long", ## LP매수호가수량10@@
                "shcode": "shcode`char", ## 단축코드@@
                "offerho1": "offerho1`long", ## 매도호가1@@
                "bidho1": "bidho1`long", ## 매수호가1@@
                "offerrem1": "offerrem1`long", ## 매도호가잔량1@@
                "bidrem1": "bidrem1`long", ## 매수호가잔량1@@
                "offerho2": "offerho2`long", ## 매도호가2@@
                "bidho2": "bidho2`long", ## 매수호가2@@
                "offerrem2": "offerrem2`long", ## 매도호가잔량2@@
                "bidrem2": "bidrem2`long", ## 매수호가잔량2@@
                "offerho3": "offerho3`long", ## 매도호가3@@
                "bidho3": "bidho3`long", ## 매수호가3@@
                "offerrem3": "offerrem3`long", ## 매도호가잔량3@@
                "bidrem3": "bidrem3`long", ## 매수호가잔량3@@
                "offerho4": "offerho4`long", ## 매도호가4@@
                "bidho4": "bidho4`long", ## 매수호가4@@
                "offerrem4": "offerrem4`long", ## 매도호가잔량4@@
                "bidrem4": "bidrem4`long", ## 매수호가잔량4@@
                "offerho5": "offerho5`long", ## 매도호가5@@
                "bidho5": "bidho5`long", ## 매수호가5@@
                "offerrem5": "offerrem5`long", ## 매도호가잔량5@@
                "bidrem5": "bidrem5`long", ## 매수호가잔량5@@
                "offerho6": "offerho6`long", ## 매도호가6@@
                "bidho6": "bidho6`long", ## 매수호가6@@
                "offerrem6": "offerrem6`long", ## 매도호가잔량6@@
                "bidrem6": "bidrem6`long", ## 매수호가잔량6@@
                "offerho7": "offerho7`long", ## 매도호가7@@
                "bidho7": "bidho7`long", ## 매수호가7@@
                "offerrem7": "offerrem7`long", ## 매도호가잔량7@@
                "bidrem7": "bidrem7`long", ## 매수호가잔량7@@
                "offerho8": "offerho8`long", ## 매도호가8@@
                "bidho8": "bidho8`long", ## 매수호가8@@
                "offerrem8": "offerrem8`long", ## 매도호가잔량8@@
                "bidrem8": "bidrem8`long", ## 매수호가잔량8@@
                "offerho9": "offerho9`long", ## 매도호가9@@
                "bidho9": "bidho9`long", ## 매수호가9@@
                "offerrem9": "offerrem9`long", ## 매도호가잔량9@@
                "bidrem9": "bidrem9`long", ## 매수호가잔량9@@
                "offerho10": "offerho10`long", ## 매도호가10@@
                "bidho10": "bidho10`long", ## 매수호가10@@
                "offerrem10": "offerrem10`long", ## 매도호가잔량10@@
                "bidrem10": "bidrem10`long", ## 매수호가잔량10@@
                "totofferrem": "totofferrem`long", ## 총매도호가잔량@@
                "totbidrem": "totbidrem`long", ## 총매수호가잔량@@
                "donsigubun": "donsigubun`char", ## 동시호가구분@@
                "alloc_gubun": "alloc_gubun`char##배분적용구분@@"
            }
        }
    },
    "BMT": { ## 시간대별투자자매매추이(BMT)
        "input": {
            "InBlock": {
                "upcode": " ##업종코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "tjjtime": "tjjtime`char", ## 수신시간@@
                "tjjcode1": "tjjcode1`char", ## 투자자코드1(개인)@@
                "msvolume1": "msvolume1`long", ## 매수 거래량1@@
                "mdvolume1": "mdvolume1`long", ## 매도 거래량1@@
                "msvol1": "msvol1`long", ## 거래량 순매수1@@
                "msvalue1": "msvalue1`long", ## 매수 거래대금1@@
                "mdvalue1": "mdvalue1`long", ## 매도 거래대금1@@
                "msval1": "msval1`long", ## 거래대금 순매수1@@
                "tjjcode2": "tjjcode2`char", ## 투자자코드2(외국인)@@
                "msvolume2": "msvolume2`long", ## 매수 거래량2@@
                "mdvolume2": "mdvolume2`long", ## 매도 거래량2@@
                "msvol2": "msvol2`long", ## 거래량 순매수2@@
                "msvalue2": "msvalue2`long", ## 매수 거래대금2@@
                "mdvalue2": "mdvalue2`long", ## 매도 거래대금2@@
                "msval2": "msval2`long", ## 거래대금 순매수2@@
                "tjjcode3": "tjjcode3`char", ## 투자자코드3(기관계)@@
                "msvolume3": "msvolume3`long", ## 매수 거래량3@@
                "mdvolume3": "mdvolume3`long", ## 매도 거래량3@@
                "msvol3": "msvol3`long", ## 거래량 순매수3@@
                "msvalue3": "msvalue3`long", ## 매수 거래대금3@@
                "mdvalue3": "mdvalue3`long", ## 매도 거래대금3@@
                "msval3": "msval3`long", ## 거래대금 순매수3@@
                "tjjcode4": "tjjcode4`char", ## 투자자코드4(증권)@@
                "msvolume4": "msvolume4`long", ## 매수 거래량4@@
                "mdvolume4": "mdvolume4`long", ## 매도 거래량4@@
                "msvol4": "msvol4`long", ## 거래량 순매수4@@
                "msvalue4": "msvalue4`long", ## 매수 거래대금4@@
                "mdvalue4": "mdvalue4`long", ## 매도 거래대금4@@
                "msval4": "msval4`long", ## 거래대금 순매수4@@
                "tjjcode5": "tjjcode5`char", ## 투자자코드5(투신)@@
                "msvolume5": "msvolume5`long", ## 매수 거래량5@@
                "mdvolume5": "mdvolume5`long", ## 매도 거래량5@@
                "msvol5": "msvol5`long", ## 거래량 순매수5@@
                "msvalue5": "msvalue5`long", ## 매수 거래대금5@@
                "mdvalue5": "mdvalue5`long", ## 매도 거래대금5@@
                "msval5": "msval5`long", ## 거래대금 순매수5@@
                "tjjcode6": "tjjcode6`char", ## 투자자코드6(은행)@@
                "msvolume6": "msvolume6`long", ## 매수 거래량6@@
                "mdvolume6": "mdvolume6`long", ## 매도 거래량6@@
                "msvol6": "msvol6`long", ## 거래량 순매수6@@
                "msvalue6": "msvalue6`long", ## 매수 거래대금6@@
                "mdvalue6": "mdvalue6`long", ## 매도 거래대금6@@
                "msval6": "msval6`long", ## 거래대금 순매수6@@
                "tjjcode7": "tjjcode7`char", ## 투자자코드7(보험)@@
                "msvolume7": "msvolume7`long", ## 매수 거래량7@@
                "mdvolume7": "mdvolume7`long", ## 매도 거래량7@@
                "msvol7": "msvol7`long", ## 거래량 순매수7@@
                "msvalue7": "msvalue7`long", ## 매수 거래대금7@@
                "mdvalue7": "mdvalue7`long", ## 매도 거래대금7@@
                "msval7": "msval7`long", ## 거래대금 순매수7@@
                "tjjcode8": "tjjcode8`char", ## 투자자코드8(종금)@@
                "msvolume8": "msvolume8`long", ## 매수 거래량8@@
                "mdvolume8": "mdvolume8`long", ## 매도 거래량8@@
                "msvol8": "msvol8`long", ## 거래량 순매수8@@
                "msvalue8": "msvalue8`long", ## 매수 거래대금8@@
                "mdvalue8": "mdvalue8`long", ## 매도 거래대금8@@
                "msval8": "msval8`long", ## 거래대금 순매수8@@
                "tjjcode9": "tjjcode9`char", ## 투자자코드9(기금)@@
                "msvolume9": "msvolume9`long", ## 매수 거래량9@@
                "mdvolume9": "mdvolume9`long", ## 매도 거래량9@@
                "msvol9": "msvol9`long", ## 거래량 순매수9@@
                "msvalue9": "msvalue9`long", ## 매수 거래대금9@@
                "mdvalue9": "mdvalue9`long", ## 매도 거래대금9@@
                "msval9": "msval9`long", ## 거래대금 순매수9@@
                "tjjcode10": "tjjcode10`char", ## 투자자코드10(선물업자)@@
                "msvolume10": "msvolume10`long", ## 매수 거래량10@@
                "mdvolume10": "mdvolume10`long", ## 매도 거래량10@@
                "msvol10": "msvol10`long", ## 거래량 순매수10@@
                "msvalue10": "msvalue10`long", ## 매수 거래대금10@@
                "mdvalue10": "mdvalue10`long", ## 매도 거래대금10@@
                "msval10": "msval10`long", ## 거래대금 순매수10@@
                "tjjcode11": "tjjcode11`char", ## 투자자코드11(기타)@@
                "msvolume11": "msvolume11`long", ## 매수 거래량11@@
                "mdvolume11": "mdvolume11`long", ## 매도 거래량11@@
                "msvol11": "msvol11`long", ## 거래량 순매수11@@
                "msvalue11": "msvalue11`long", ## 매수 거래대금11@@
                "mdvalue11": "mdvalue11`long", ## 매도 거래대금11@@
                "msval11": "msval11`long", ## 거래대금 순매수11@@
                "upcode": "upcode`char", ## 업종코드@@
                "tjjcode0": "tjjcode0`char", ## 투자자코드0(사모펀드)@@
                "msvolume0": "msvolume0`long", ## 매수 거래량0@@
                "mdvolume0": "mdvolume0`long", ## 매도 거래량0@@
                "msvol0": "msvol0`long", ## 거래량 순매수0@@
                "msvalue0": "msvalue0`long", ## 매수 거래대금0@@
                "mdvalue0": "mdvalue0`long", ## 매도 거래대금0@@
                "msval0": "msval0`long##거래대금 순매수0@@"
            }
        }
    },
    "BM_": { ## 업종별투자자별매매현황(BM)
        "input": {
            "InBlock": {
                "upcode": " ##업종코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "tjjcode": "tjjcode`char", ## 투자자코드@@
                "tjjtime": "tjjtime`char", ## 수신시간@@
                "msvolume": "msvolume`long", ## 매수 거래량@@
                "mdvolume": "mdvolume`long", ## 매도 거래량@@
                "msvol": "msvol`long", ## 거래량 순매수@@
                "p_msvol": "p_msvol`long", ## 거래량 순매수 직전대비@@
                "msvalue": "msvalue`long", ## 매수 거래대금@@
                "mdvalue": "mdvalue`long", ## 매도 거래대금@@
                "msval": "msval`long", ## 거래대금 순매수@@
                "p_msval": "p_msval`long", ## 거래대금 순매수 직전대비@@
                "upcode": "upcode`char##업종코드@@"
            }
        }
    },
    "C01": { ## 선물주문체결
        "input": {
            "InBlock": {}
        },
        "output": {
            "OutBlock": {
                "lineseq": "lineseq`long", ## 라인일련번호@@
                "accno": "accno`char", ## 계좌번호@@
                "user": "user`char", ## 조작자ID@@
                "seq": "seq`long", ## 일련번호@@
                "trcode": "trcode`char", ## trcode@@
                "megrpno": "megrpno`char", ## 매칭그룹번호@@
                "boardid": "boardid`char", ## 보드ID@@
                "memberno": "memberno`char", ## 회원번호@@
                "bpno": "bpno`char", ## 지점번호@@
                "ordno": "ordno`char", ## 주문번호@@
                "ordordno": "ordordno`char", ## 원주문번호@@
                "expcode": "expcode`char", ## 종목코드@@
                "yakseq": "yakseq`char", ## 약정번호@@
                "cheprice": "cheprice`float", ## 체결가격@@
                "chevol": "chevol`long", ## 체결수량@@
                "sessionid": "sessionid`char", ## 세션ID@@
                "chedate": "chedate`char", ## 체결일자@@
                "chetime": "chetime`char", ## 체결시각@@
                "spdprc1": "spdprc1`float", ## 최근월체결가격@@
                "spdprc2": "spdprc2`float", ## 차근월체결가격@@
                "dosugb": "dosugb`char", ## 매도수구분@@
                "accno1": "accno1`char", ## 계좌번호1@@
                "sihogagb": "sihogagb`char", ## 시장조성호가구분@@
                "jakino": "jakino`char", ## 위탁사번호@@
                "daeyong": "daeyong`char", ## 대용주권계좌번호@@
                "mem_filler": "mem_filler`char", ## mem_filler1@@
                "mem_accno": "mem_accno`char##mem_accno@@"
            }
        }
    },
    "CD0": { ## 상품선물실시간상하한가(D0)
        "input": {
            "InBlock": {
                "futcode": " ##단축코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "gubun": "gubun`char", ## 접속매매여부@@
                "dy_gubun": "dy_gubun`char", ## 실시간가격제한여부@@
                "dy_uplmtprice": "dy_uplmtprice`float", ## 실시간상한가@@
                "dy_dnlmtprice": "dy_dnlmtprice`float", ## 실시간하한가@@
                "futcode": "futcode`char##단축코드@@"
            }
        }
    },
    "CDPCQ04700": { ## 계좌 거래내역
        "input": {
            "CDPCQ04700InBlock1": {
                "RecCnt": "0", ## 레코드갯수@@
                "QryTp": " ", ## 조회구분@@
                "AcntNo": " ", ## 계좌번호@@
                "Pwd": " ", ## 비밀번호@@
                "QrySrtDt": " ", ## 조회시작일@@
                "QryEndDt": " ", ## 조회종료일@@
                "SrtNo": "0", ## 시작번호@@
                "PdptnCode": " ", ## 상품유형코드@@
                "IsuLgclssCode": " ", ## 종목대분류코드@@
                "IsuNo": " ##종목번호@@"
            }
        },
        "output": {
            "CDPCQ04700OutBlock1": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "QryTp": "QryTp`char", ## 조회구분@@
                "AcntNo": "AcntNo`char", ## 계좌번호@@
                "Pwd": "Pwd`char", ## 비밀번호@@
                "QrySrtDt": "QrySrtDt`char", ## 조회시작일@@
                "QryEndDt": "QryEndDt`char", ## 조회종료일@@
                "SrtNo": "SrtNo`long", ## 시작번호@@
                "PdptnCode": "PdptnCode`char", ## 상품유형코드@@
                "IsuLgclssCode": "IsuLgclssCode`char", ## 종목대분류코드@@
                "IsuNo": "IsuNo`char##종목번호@@"
            },
            "CDPCQ04700OutBlock2": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "AcntNm": "AcntNm`char##계좌명@@"
            },
            "CDPCQ04700OutBlock3": {
                "AcntNo": "AcntNo`char", ## 계좌번호@@
                "TrdDt": "TrdDt`char", ## 거래일자@@
                "TrdNo": "TrdNo`long", ## 거래번호@@
                "TpCodeNm": "TpCodeNm`char", ## 구분코드명@@
                "SmryNo": "SmryNo`char", ## 적요번호@@
                "SmryNm": "SmryNm`char", ## 적요명@@
                "CancTpNm": "CancTpNm`char", ## 취소구분@@
                "TrdQty": "TrdQty`long", ## 거래수량@@
                "Trtax": "Trtax`long", ## 거래세@@
                "FcurrAdjstAmt": "FcurrAdjstAmt`double", ## 외화정산금액@@
                "AdjstAmt": "AdjstAmt`long", ## 정산금액@@
                "OvdSum": "OvdSum`long", ## 연체합@@
                "DpsBfbalAmt": "DpsBfbalAmt`long", ## 예수금전잔금액@@
                "SellPldgRfundAmt": "SellPldgRfundAmt`long", ## 매도담보상환금@@
                "DpspdgLoanBfbalAmt": "DpspdgLoanBfbalAmt`long", ## 예탁담보대출전잔금액@@
                "TrdmdaNm": "TrdmdaNm`char", ## 거래매체명@@
                "OrgTrdNo": "OrgTrdNo`long", ## 원거래번호@@
                "IsuNm": "IsuNm`char", ## 종목명@@
                "TrdUprc": "TrdUprc`double", ## 거래단가@@
                "CmsnAmt": "CmsnAmt`long", ## 수수료@@
                "FcurrCmsnAmt": "FcurrCmsnAmt`double", ## 외화수수료금액@@
                "RfundDiffAmt": "RfundDiffAmt`long", ## 상환차이금액@@
                "RepayAmtSum": "RepayAmtSum`long", ## 변제금합계@@
                "SecCrbalQty": "SecCrbalQty`long", ## 유가증권금잔수량@@
                "CslLoanRfundIntrstAmt": "CslLoanRfundIntrstAmt`long", ## 매도대금담보대출상환이자금액@@
                "DpspdgLoanCrbalAmt": "DpspdgLoanCrbalAmt`long", ## 예탁담보대출금잔금액@@
                "TrxTime": "TrxTime`char", ## 처리시각@@
                "Inouno": "Inouno`long", ## 출납번호@@
                "IsuNo": "IsuNo`char", ## 종목번호@@
                "TrdAmt": "TrdAmt`long", ## 거래금액@@
                "ChckAmt": "ChckAmt`long", ## 수표금액@@
                "TaxSumAmt": "TaxSumAmt`long", ## 세금합계금액@@
                "FcurrTaxSumAmt": "FcurrTaxSumAmt`double", ## 외화세금합계금액@@
                "IntrstUtlfee": "IntrstUtlfee`long", ## 이자이용료@@
                "MnyDvdAmt": "MnyDvdAmt`long", ## 배당금액@@
                "RcvblOcrAmt": "RcvblOcrAmt`long", ## 미수발생금액@@
                "TrxBrnNo": "TrxBrnNo`char", ## 처리지점번호@@
                "TrxBrnNm": "TrxBrnNm`char", ## 처리지점명@@
                "DpspdgLoanAmt": "DpspdgLoanAmt`long", ## 예탁담보대출금액@@
                "DpspdgLoanRfundAmt": "DpspdgLoanRfundAmt`long", ## 예탁담보대출상환금액@@
                "BasePrc": "BasePrc`double", ## 기준가@@
                "DpsCrbalAmt": "DpsCrbalAmt`long", ## 예수금금잔금액@@
                "BoaAmt": "BoaAmt`long", ## 과표@@
                "MnyoutAbleAmt": "MnyoutAbleAmt`long", ## 출금가능금액@@
                "BcrLoanOcrAmt": "BcrLoanOcrAmt`long", ## 수익증권담보대출발생금@@
                "BcrLoanBfbalAmt": "BcrLoanBfbalAmt`long", ## 수익증권담보대출전잔금@@
                "BnsBasePrc": "BnsBasePrc`double", ## 매매기준가@@
                "TaxchrBasePrc": "TaxchrBasePrc`double", ## 과세기준가@@
                "TrdUnit": "TrdUnit`long", ## 거래좌수@@
                "BalUnit": "BalUnit`long", ## 잔고좌수@@
                "EvrTax": "EvrTax`long", ## 제세금@@
                "EvalAmt": "EvalAmt`long", ## 평가금액@@
                "BcrLoanRfundAmt": "BcrLoanRfundAmt`long", ## 수익증권담보대출상환금@@
                "BcrLoanCrbalAmt": "BcrLoanCrbalAmt`long", ## 수익증권담보대출금잔금@@
                "AddMgnOcrTotamt": "AddMgnOcrTotamt`long", ## 추가증거금발생총액@@
                "AddMnyMgnOcrAmt": "AddMnyMgnOcrAmt`long", ## 추가현금증거금발생금액@@
                "AddMgnDfryTotamt": "AddMgnDfryTotamt`long", ## 추가증거금납부총액@@
                "AddMnyMgnDfryAmt": "AddMnyMgnDfryAmt`long", ## 추가현금증거금납부금액@@
                "BnsplAmt": "BnsplAmt`long", ## 매매손익금액@@
                "Ictax": "Ictax`long", ## 소득세@@
                "Ihtax": "Ihtax`long", ## 주민세@@
                "LoanDt": "LoanDt`char", ## 대출일@@
                "CrcyCode": "CrcyCode`char", ## 통화코드@@
                "FcurrAmt": "FcurrAmt`double", ## 외화금액@@
                "FcurrTrdAmt": "FcurrTrdAmt`double", ## 외화거래금액@@
                "FcurrDps": "FcurrDps`double", ## 외화예수금@@
                "FcurrDpsBfbalAmt": "FcurrDpsBfbalAmt`double", ## 외화예수금전잔금액@@
                "OppAcntNm": "OppAcntNm`char", ## 상대계좌명@@
                "OppAcntNo": "OppAcntNo`char", ## 상대계좌번호@@
                "LoanRfundAmt": "LoanRfundAmt`long", ## 대출상환금액@@
                "LoanIntrstAmt": "LoanIntrstAmt`long", ## 대출이자금액@@
                "AskpsnNm": "AskpsnNm`char", ## 의뢰인명@@
                "OrdDt": "OrdDt`char", ## 주문일자@@
                "TrdXchrat": "TrdXchrat`double", ## 거래환율@@
                "RdctCmsn": "RdctCmsn`double", ## 감면수수료@@
                "FcurrStmpTx": "FcurrStmpTx`double", ## 외화인지세@@
                "FcurrElecfnTrtax": "FcurrElecfnTrtax`double", ## 외화전자금융거래세@@
                "FcstckTrtax": "FcstckTrtax`double##외화증권거래세@@"
            },
            "CDPCQ04700OutBlock4": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "PnlSumAmt": "PnlSumAmt`long", ## 손익합계금액@@
                "CtrctAsm": "CtrctAsm`long", ## 약정누계@@
                "CmsnAmtSumAmt": "CmsnAmtSumAmt`long##수수료합계금액@@"
            },
            "CDPCQ04700OutBlock5": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "MnyinAmt": "MnyinAmt`long", ## 입금금액@@
                "SecinAmt": "SecinAmt`long", ## 입고금액@@
                "MnyoutAmt": "MnyoutAmt`long", ## 출금금액@@
                "SecoutAmt": "SecoutAmt`long", ## 출고금액@@
                "DiffAmt": "DiffAmt`long", ## 차이금액@@
                "DiffAmt0": "DiffAmt0`long", ## 차이금액0@@
                "SellQty": "SellQty`long", ## 매도수량@@
                "SellAmt": "SellAmt`long", ## 매도금액@@
                "SellCmsn": "SellCmsn`long", ## 매도수수료@@
                "EvrTax": "EvrTax`long", ## 제세금@@
                "FcurrSellAdjstAmt": "FcurrSellAdjstAmt`double", ## 외화매도정산금액@@
                "BuyQty": "BuyQty`long", ## 매수수량@@
                "BuyAmt": "BuyAmt`long", ## 매수금액@@
                "BuyCmsn": "BuyCmsn`long", ## 매수수수료@@
                "ExecTax": "ExecTax`long", ## 체결세금@@
                "FcurrBuyAdjstAmt": "FcurrBuyAdjstAmt`double##외화매수정산금액@@"
            }
        }
    },
    "CEXAQ21100": { ## 유렉스 주문체결내역조회
        "input": {
            "CEXAQ21100InBlock1": {
                "RecCnt": "0", ## 레코드갯수@@
                "ChoicInptTpCode": " ", ## 선택입력구분@@
                "AcntNo": " ", ## 지점번호@@
                "Pwd": " ", ## 비밀번호@@
                "PrdtExecTpCode": " ", ## 체결구분@@
                "StnlnSeqTp": " ##정렬순서구분@@"
            }
        },
        "output": {
            "CEXAQ21100OutBlock1": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "ChoicInptTpCode": "ChoicInptTpCode`char", ## 선택입력구분@@
                "AcntNo": "AcntNo`char", ## 지점번호@@
                "Pwd": "Pwd`char", ## 비밀번호@@
                "PrdtExecTpCode": "PrdtExecTpCode`char", ## 체결구분@@
                "StnlnSeqTp": "StnlnSeqTp`char##정렬순서구분@@"
            },
            "CEXAQ21100OutBlock2": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "AcntNm": "AcntNm`char", ## 계좌명@@
                "OrdQty": "OrdQty`long", ## 주문수량@@
                "ExecQty": "ExecQty`long##체결수량@@"
            },
            "CEXAQ21100OutBlock3": {
                "AcntNo1": "AcntNo1`char", ## 계좌번호1@@
                "OrdDt": "OrdDt`char", ## 주문일@@
                "OrdNo": "OrdNo`long", ## 주문번호@@
                "OrgOrdNo": "OrgOrdNo`long", ## 원주문번호@@
                "OrdTime": "OrdTime`char", ## 주문시각@@
                "FnoIsuNo": "FnoIsuNo`char", ## 선물옵션종목번호@@
                "IsuNm": "IsuNm`char", ## 종목명@@
                "BnsTpNm": "BnsTpNm`char", ## 매매구분@@
                "BnsTpCode": "BnsTpCode`char", ## 매매구분@@
                "MrcTpNm": "MrcTpNm`char", ## 정정취소구분명@@
                "ErxPrcCndiTpCode": "ErxPrcCndiTpCode`char", ## 유렉스가격조건구분코드@@
                "FnoOrdprcPtnNm": "FnoOrdprcPtnNm`char", ## 선물옵션호가유형명@@
                "OrdCndiPrc": "OrdCndiPrc`double", ## 주문조건가격@@
                "OrdPrc": "OrdPrc`double", ## 주문가@@
                "OrdQty": "OrdQty`long", ## 주문수량@@
                "OrdTpNm": "OrdTpNm`char", ## 주문구분명@@
                "ExecPrc": "ExecPrc`double", ## 체결가@@
                "ExecQty": "ExecQty`long", ## 체결수량@@
                "UnercQty": "UnercQty`long", ## 미체결수량@@
                "CommdaCode": "CommdaCode`char", ## 통신매체코드@@
                "CommdaNm": "CommdaNm`char##통신매체명@@"
            }
        }
    },
    "CEXAQ21200": { ## 유렉스 주문가능 수량/금액 조회
        "input": {
            "CEXAQ21200InBlock1": {
                "RecCnt": "0", ## 레코드갯수@@
                "AcntNo": " ", ## 계좌번호@@
                "Pwd": " ", ## 비밀번호@@
                "QryTp": " ", ## 조회구분@@
                "OrdAmt": "0", ## 주문금액@@
                "RatVal": "0.0", ## 비율값@@
                "FnoIsuNo": " ", ## 선물옵션종목번호@@
                "BnsTpCode": " ", ## 매매구분@@
                "OrdPrc": "0.0", ## 주문가@@
                "ErxPrcCndiTpCode": " ##유렉스가격조건구분코드@@"
            }
        },
        "output": {
            "CEXAQ21200OutBlock1": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "AcntNo": "AcntNo`char", ## 계좌번호@@
                "Pwd": "Pwd`char", ## 비밀번호@@
                "QryTp": "QryTp`char", ## 조회구분@@
                "OrdAmt": "OrdAmt`long", ## 주문금액@@
                "RatVal": "RatVal`double", ## 비율값@@
                "FnoIsuNo": "FnoIsuNo`char", ## 선물옵션종목번호@@
                "BnsTpCode": "BnsTpCode`char", ## 매매구분@@
                "OrdPrc": "OrdPrc`double", ## 주문가@@
                "ErxPrcCndiTpCode": "ErxPrcCndiTpCode`char##유렉스가격조건구분코드@@"
            },
            "CEXAQ21200OutBlock2": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "AcntNm": "AcntNm`char", ## 계좌명@@
                "QryDt": "QryDt`char", ## 조회일@@
                "NowPrc": "NowPrc`double", ## 현재가@@
                "OrdAbleQty": "OrdAbleQty`long", ## 주문가능수량@@
                "NewOrdAbleQty": "NewOrdAbleQty`long", ## 신규주문가능수량@@
                "LqdtOrdAbleQty": "LqdtOrdAbleQty`long", ## 청산주문가능수량@@
                "UsePreargMgn": "UsePreargMgn`long", ## 사용예정증거금액@@
                "UsePreargMnyMgn": "UsePreargMnyMgn`long", ## 사용예정현금증거금액@@
                "OrdAbleAmt": "OrdAbleAmt`long", ## 주문가능금액@@
                "MnyOrdAbleAmt": "MnyOrdAbleAmt`long##현금주문가능금액@@"
            }
        }
    },
    "CEXAQ31100": { ## 유렉스 야간장잔고및 평가현황
        "input": {
            "CEXAQ31100InBlock1": {
                "RecCnt": "0", ## 레코드갯수@@
                "AcntNo": " ", ## 계좌번호@@
                "InptPwd": " ", ## 입력비밀번호@@
                "IsuCode": " ", ## 종목코드@@
                "BalEvalTp": " ", ## 잔고평가구분@@
                "FutsPrcEvalTp": " ##선물가격평가구분@@"
            }
        },
        "output": {
            "CEXAQ31100OutBlock1": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "AcntNo": "AcntNo`char", ## 계좌번호@@
                "InptPwd": "InptPwd`char", ## 입력비밀번호@@
                "IsuCode": "IsuCode`char", ## 종목코드@@
                "BalEvalTp": "BalEvalTp`char", ## 잔고평가구분@@
                "FutsPrcEvalTp": "FutsPrcEvalTp`char##선물가격평가구분@@"
            },
            "CEXAQ31100OutBlock2": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "AcntNo": "AcntNo`char", ## 계좌번호@@
                "AcntNm": "AcntNm`char", ## 계좌명@@
                "BnsplAmt": "BnsplAmt`long", ## 매매손익금액@@
                "AdjstDfamt": "AdjstDfamt`long", ## 정산차금@@
                "TotEvalAmt": "TotEvalAmt`long", ## 총평가금액@@
                "TotPnlAmt": "TotPnlAmt`long##총손익금액@@"
            },
            "CEXAQ31100OutBlock3": {
                "FnoIsuNo": "FnoIsuNo`char", ## 선물옵션종목번호@@
                "IsuNm": "IsuNm`char", ## 종목명@@
                "BnsTpCode": "BnsTpCode`char", ## 매매구분@@
                "BnsTpNm": "BnsTpNm`char", ## 매매구분@@
                "UnsttQty": "UnsttQty`long", ## 미결제수량@@
                "LqdtAbleQty": "LqdtAbleQty`long", ## 청산가능수량@@
                "FnoAvrPrc": "FnoAvrPrc`double", ## 평균가@@
                "BasePrc": "BasePrc`double", ## 기준가@@
                "NowPrc": "NowPrc`double", ## 현재가@@
                "CmpPrc": "CmpPrc`double", ## 대비가@@
                "EvalAmt": "EvalAmt`long", ## 평가금액@@
                "EvalPnl": "EvalPnl`long", ## 평가손익@@
                "PnlRat": "PnlRat`double", ## 손익률@@
                "UnsttAmt": "UnsttAmt`long", ## 미결제금액@@
                "BnsplAmt": "BnsplAmt`long##매매손익금액@@"
            }
        }
    },
    "CEXAQ31200": { ## 유렉스 예탁금 및 통합잔고조회
        "input": {
            "CEXAQ31200InBlock1": {
                "RecCnt": "0", ## 레코드갯수@@
                "AcntNo": " ", ## 계좌번호@@
                "InptPwd": " ", ## 입력비밀번호@@
                "BalEvalTp": " ", ## 잔고평가구분@@
                "FutsPrcEvalTp": " ##선물가격평가구분@@"
            }
        },
        "output": {
            "CEXAQ31200OutBlock1": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "AcntNo": "AcntNo`char", ## 계좌번호@@
                "InptPwd": "InptPwd`char", ## 입력비밀번호@@
                "BalEvalTp": "BalEvalTp`char", ## 잔고평가구분@@
                "FutsPrcEvalTp": "FutsPrcEvalTp`char##선물가격평가구분@@"
            },
            "CEXAQ31200OutBlock2": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "AcntNo": "AcntNo`char", ## 계좌번호@@
                "AcntNm": "AcntNm`char", ## 계좌명@@
                "EvalDpsamtTotamt": "EvalDpsamtTotamt`long", ## 평가예탁금총액@@
                "MnyEvalDpstgAmt": "MnyEvalDpstgAmt`long", ## 현금평가예탁금액@@
                "DpsamtTotamt": "DpsamtTotamt`long", ## 예탁금총액@@
                "DpstgMny": "DpstgMny`long", ## 예탁현금@@
                "PsnOutAbleTotAmt": "PsnOutAbleTotAmt`long", ## 인출가능총금액@@
                "PsnOutAbleCurAmt": "PsnOutAbleCurAmt`long", ## 인출가능현금액@@
                "OrdAbleTotAmt": "OrdAbleTotAmt`long", ## 주문가능총금액@@
                "MnyOrdAbleAmt": "MnyOrdAbleAmt`long", ## 현금주문가능금액@@
                "CsgnMgnTotamt": "CsgnMgnTotamt`long", ## 위탁증거금총액@@
                "MnyCsgnMgn": "MnyCsgnMgn`long", ## 현금위탁증거금액@@
                "AddMgnTotamt": "AddMgnTotamt`long", ## 추가증거금총액@@
                "MnyAddMgn": "MnyAddMgn`long", ## 현금추가증거금액@@
                "CmsnAmt": "CmsnAmt`long", ## 수수료@@
                "FutsEvalPnlAmt": "FutsEvalPnlAmt`long", ## 선물평가손익금액@@
                "OptEvalPnlAmt": "OptEvalPnlAmt`long", ## 옵션평가손익금액@@
                "OptEvalAmt": "OptEvalAmt`long", ## 옵션평가금액@@
                "OptBnsplAmt": "OptBnsplAmt`long", ## 옵션매매손익금액@@
                "FutsAdjstDfamt": "FutsAdjstDfamt`long", ## 선물정산차금@@
                "TotPnlAmt": "TotPnlAmt`long", ## 총손익금액@@
                "NetPnlAmt": "NetPnlAmt`long", ## 순손익금액@@
                "TotEvalAmt": "TotEvalAmt`long", ## 총평가금액@@
                "MnyinAmt": "MnyinAmt`long", ## 입금금액@@
                "MnyoutAmt": "MnyoutAmt`long", ## 출금금액@@
                "FutsCmsnAmt": "FutsCmsnAmt`long##선물수수료금액@@"
            },
            "CEXAQ31200OutBlock3": {
                "FnoIsuNo": "FnoIsuNo`char", ## 선물옵션종목번호@@
                "IsuNm": "IsuNm`char", ## 종목명@@
                "BnsTpCode": "BnsTpCode`char", ## 매매구분@@
                "BnsTpNm": "BnsTpNm`char", ## 매매구분@@
                "UnsttQty": "UnsttQty`long", ## 미결제수량@@
                "FnoAvrPrc": "FnoAvrPrc`double", ## 평균가@@
                "NowPrc": "NowPrc`double", ## 현재가@@
                "CmpPrc": "CmpPrc`double", ## 대비가@@
                "EvalPnl": "EvalPnl`long", ## 평가손익@@
                "PnlRat": "PnlRat`double", ## 손익률@@
                "EvalAmt": "EvalAmt`long", ## 평가금액@@
                "LqdtAbleQty": "LqdtAbleQty`long##청산가능수량@@"
            }
        }
    },
    "CEXAQ44200": { ## EUREX 야간옵션 기간주문체결조회
        "input": {
            "CEXAQ44200InBlock1": {
                "RecCnt": "0", ## 레코드갯수@@
                "ChoicInptTpCode": " ", ## 선택입력구분@@
                "AcntNo": " ", ## 계좌번호@@
                "Pwd": " ", ## 비밀번호@@
                "QrySrtDt": " ", ## 조회시작일@@
                "QryEndDt": " ", ## 조회종료일@@
                "PrdtExecTpCode": " ", ## 체결구분@@
                "FnoTrdPtnCode": " ", ## 선물옵션거래유형코드@@
                "SrtOrdNo2": "0", ## 시작주문번호2@@
                "StnlnSeqTp": " ##정렬순서구분@@"
            }
        },
        "output": {
            "CEXAQ44200OutBlock1": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "ChoicInptTpCode": "ChoicInptTpCode`char", ## 선택입력구분@@
                "AcntNo": "AcntNo`char", ## 계좌번호@@
                "Pwd": "Pwd`char", ## 비밀번호@@
                "QrySrtDt": "QrySrtDt`char", ## 조회시작일@@
                "QryEndDt": "QryEndDt`char", ## 조회종료일@@
                "PrdtExecTpCode": "PrdtExecTpCode`char", ## 체결구분@@
                "FnoTrdPtnCode": "FnoTrdPtnCode`char", ## 선물옵션거래유형코드@@
                "SrtOrdNo2": "SrtOrdNo2`long", ## 시작주문번호2@@
                "StnlnSeqTp": "StnlnSeqTp`char##정렬순서구분@@"
            },
            "CEXAQ44200OutBlock2": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "OrdQty": "OrdQty`long", ## 주문수량@@
                "ExecQty": "ExecQty`long", ## 체결수량@@
                "UnercQty": "UnercQty`long", ## 미체결수량@@
                "ExecPrc": "ExecPrc`double##체결가@@"
            },
            "CEXAQ44200OutBlock3": {
                "AcntNo1": "AcntNo1`char", ## 계좌번호1@@
                "AcntNm": "AcntNm`char", ## 계좌명@@
                "OrdDt": "OrdDt`char", ## 주문일@@
                "OrdNo": "OrdNo`long", ## 주문번호@@
                "OrgOrdNo": "OrgOrdNo`long", ## 원주문번호@@
                "OrdTime": "OrdTime`char", ## 주문시각@@
                "IsuNo": "IsuNo`char", ## 종목번호@@
                "IsuNm": "IsuNm`char", ## 종목명@@
                "BnsTpNm": "BnsTpNm`char", ## 매매구분@@
                "BnsTpCode": "BnsTpCode`char", ## 매매구분@@
                "ErxOrdprcTpCode": "ErxOrdprcTpCode`char", ## 유렉스호가구분코드@@
                "MrcTpNm": "MrcTpNm`char", ## 정정취소구분명@@
                "ErxPrcCndiTpCode": "ErxPrcCndiTpCode`char", ## 유렉스가격조건구분코드@@
                "CodeNm": "CodeNm`char", ## 코드명@@
                "OrdPrc": "OrdPrc`double", ## 주문가@@
                "OrdQty": "OrdQty`long", ## 주문수량@@
                "FnoRjtRsnCode": "FnoRjtRsnCode`char", ## 선물옵션거부사유코드@@
                "OrdTpNm": "OrdTpNm`char", ## 주문구분명@@
                "ExecTpNm": "ExecTpNm`char", ## 체결구분명@@
                "ExecPrc": "ExecPrc`double", ## 체결가@@
                "ExecQty": "ExecQty`long", ## 체결수량@@
                "ExecTime": "ExecTime`char", ## 체결시각@@
                "ExecNo": "ExecNo`long", ## 체결번호@@
                "UnercQty": "UnercQty`long", ## 미체결수량@@
                "UserId": "UserId`char", ## 사용자ID@@
                "CommdaCode": "CommdaCode`char", ## 통신매체코드@@
                "CommdaCodeNm": "CommdaCodeNm`char", ## 통신매체코드명@@
                "IpAddr": "IpAddr`char", ## IP주소@@
                "TrdPtnTpNm": "TrdPtnTpNm`char", ## 거래유형구분@@
                "ErxOrdStatCode": "ErxOrdStatCode`char", ## 유렉스주문상태코드@@
                "CodeNm0": "CodeNm0`char", ## 코드명0@@
                "ExchRcptTime": "ExchRcptTime`char##거래소접수시각@@"
            }
        }
    },
    "CEXAT11100": { ## 유렉스 매수/매도주문
        "input": {
            "CEXAT11100InBlock1": {
                "AcntNo": " ", ## 계좌번호@@
                "Pwd": " ", ## 비밀번호@@
                "FnoIsuNo": " ", ## 선물옵션종목번호@@
                "BnsTpCode": " ", ## 매매구분@@
                "ErxPrcCndiTpCode": " ", ## 유렉스가격조건구분코드@@
                "OrdPrc": "0.0", ## 주문가격@@
                "OrdQty": "0##주문수량@@"
            }
        },
        "output": {
            "CEXAT11100OutBlock1": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "AcntNo": "AcntNo`char", ## 계좌번호@@
                "Pwd": "Pwd`char", ## 비밀번호@@
                "FnoIsuNo": "FnoIsuNo`char", ## 선물옵션종목번호@@
                "BnsTpCode": "BnsTpCode`char", ## 매매구분@@
                "ErxPrcCndiTpCode": "ErxPrcCndiTpCode`char", ## 유렉스가격조건구분코드@@
                "OrdPrc": "OrdPrc`double", ## 주문가격@@
                "OrdQty": "OrdQty`long", ## 주문수량@@
                "OrdCndiPrc": "OrdCndiPrc`double", ## 주문조건가격@@
                "CommdaCode": "CommdaCode`char##통신매체코드@@"
            },
            "CEXAT11100OutBlock2": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "OrdNo": "OrdNo`long", ## 주문번호@@
                "BrnNm": "BrnNm`char", ## 지점명@@
                "AcntNm": "AcntNm`char", ## 계좌명@@
                "IsuNm": "IsuNm`char", ## 종목명@@
                "OrdAbleAmt": "OrdAbleAmt`long", ## 주문가능금액@@
                "MnyOrdAbleAmt": "MnyOrdAbleAmt`long", ## 현금주문가능금액@@
                "OrdMgn": "OrdMgn`long", ## 주문증거금@@
                "MnyOrdMgn": "MnyOrdMgn`long", ## 현금주문증거금@@
                "OrdAbleQty": "OrdAbleQty`long##주문가능수량@@"
            }
        }
    },
    "CEXAT11200": { ## 유렉스 정정주문
        "input": {
            "CEXAT11200InBlock1": {
                "OrgOrdNo": "0", ## 원주문번호@@
                "AcntNo": " ", ## 계좌번호@@
                "Pwd": " ", ## 비밀번호@@
                "FnoIsuNo": " ", ## 선물옵션종목번호@@
                "OrdPrc": "0.0##주문가격@@"
            }
        },
        "output": {
            "CEXAT11200OutBlock1": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "OrgOrdNo": "OrgOrdNo`long", ## 원주문번호@@
                "AcntNo": "AcntNo`char", ## 계좌번호@@
                "Pwd": "Pwd`char", ## 비밀번호@@
                "FnoIsuNo": "FnoIsuNo`char", ## 선물옵션종목번호@@
                "BnsTpCode": "BnsTpCode`char", ## 매매구분코드@@
                "ErxPrcCndiTpCode": "ErxPrcCndiTpCode`char", ## 유렉스가격조건구분코드@@
                "OrdPrc": "OrdPrc`double", ## 주문가격@@
                "MdfyQty": "MdfyQty`long", ## 정정수량@@
                "OrdCndiPrc": "OrdCndiPrc`double", ## 주문조건가격@@
                "CommdaCode": "CommdaCode`char##통신매체코드@@"
            },
            "CEXAT11200OutBlock2": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "OrdNo": "OrdNo`long", ## 주문번호@@
                "BrnNm": "BrnNm`char", ## 지점명@@
                "AcntNm": "AcntNm`char", ## 계좌명@@
                "IsuNm": "IsuNm`char", ## 종목명@@
                "OrdAbleAmt": "OrdAbleAmt`long", ## 주문가능금액@@
                "MnyOrdAbleAmt": "MnyOrdAbleAmt`long", ## 현금주문가능금액@@
                "OrdMgn": "OrdMgn`long", ## 주문증거금액@@
                "MnyOrdMgn": "MnyOrdMgn`long", ## 현금주문증거금액@@
                "OrdAbleQty": "OrdAbleQty`long##주문가능수량@@"
            }
        }
    },
    "CEXAT11300": { ## 유렉스 취소주문
        "input": {
            "CEXAT11300InBlock1": {
                "OrgOrdNo": "0", ## 원주문번호@@
                "AcntNo": " ", ## 계좌번호@@
                "Pwd": " ", ## 비밀번호@@
                "FnoIsuNo": " ##선물옵션종목번호@@"
            }
        },
        "output": {
            "CEXAT11300OutBlock1": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "OrgOrdNo": "OrgOrdNo`long", ## 원주문번호@@
                "AcntNo": "AcntNo`char", ## 계좌번호@@
                "Pwd": "Pwd`char", ## 비밀번호@@
                "FnoIsuNo": "FnoIsuNo`char", ## 선물옵션종목번호@@
                "CancQty": "CancQty`long", ## 취소수량@@
                "CommdaCode": "CommdaCode`char##통신매체코드@@"
            },
            "CEXAT11300OutBlock2": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "OrdNo": "OrdNo`long", ## 주문번호@@
                "BrnNm": "BrnNm`char", ## 지점명@@
                "AcntNm": "AcntNm`char", ## 계좌명@@
                "IsuNm": "IsuNm`char", ## 종목명@@
                "OrdAbleAmt": "OrdAbleAmt`long", ## 주문가능금액@@
                "MnyOrdAbleAmt": "MnyOrdAbleAmt`long", ## 현금주문가능금액@@
                "OrdMgn": "OrdMgn`long", ## 주문증거금액@@
                "MnyOrdMgn": "MnyOrdMgn`long", ## 현금주문증거금액@@
                "OrdAbleQty": "OrdAbleQty`long##주문가능수량@@"
            }
        }
    },
    "CFOAQ00600": { ## 선물옵션 계좌주문체결내역조회
        "input": {
            "CFOAQ00600InBlock1": {
                "RecCnt": "0", ## 레코드갯수@@
                "AcntNo": " ", ## 계좌번호@@
                "InptPwd": " ", ## 입력비밀번호@@
                "QrySrtDt": " ", ## 조회시작일@@
                "QryEndDt": " ", ## 조회종료일@@
                "FnoClssCode": " ", ## 선물옵션분류코드@@
                "PrdgrpCode": " ", ## 상품군코드@@
                "PrdtExecTpCode": " ", ## 체결구분@@
                "StnlnSeqTp": " ", ## 정렬순서구분@@
                "CommdaCode": " ##통신매체코드@@"
            }
        },
        "output": {
            "CFOAQ00600OutBlock1": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "AcntNo": "AcntNo`char", ## 계좌번호@@
                "InptPwd": "InptPwd`char", ## 입력비밀번호@@
                "QrySrtDt": "QrySrtDt`char", ## 조회시작일@@
                "QryEndDt": "QryEndDt`char", ## 조회종료일@@
                "FnoClssCode": "FnoClssCode`char", ## 선물옵션분류코드@@
                "PrdgrpCode": "PrdgrpCode`char", ## 상품군코드@@
                "PrdtExecTpCode": "PrdtExecTpCode`char", ## 체결구분@@
                "StnlnSeqTp": "StnlnSeqTp`char", ## 정렬순서구분@@
                "CommdaCode": "CommdaCode`char##통신매체코드@@"
            },
            "CFOAQ00600OutBlock2": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "AcntNm": "AcntNm`char", ## 계좌명@@
                "FutsOrdQty": "FutsOrdQty`long", ## 선물주문수량@@
                "FutsExecQty": "FutsExecQty`long", ## 선물체결수량@@
                "OptOrdQty": "OptOrdQty`long", ## 옵션주문수량@@
                "OptExecQty": "OptExecQty`long##옵션체결수량@@"
            },
            "CFOAQ00600OutBlock3": {
                "OrdDt": "OrdDt`char", ## 주문일@@
                "OrdNo": "OrdNo`long", ## 주문번호@@
                "OrgOrdNo": "OrgOrdNo`long", ## 원주문번호@@
                "OrdTime": "OrdTime`char", ## 주문시각@@
                "FnoIsuNo": "FnoIsuNo`char", ## 선물옵션종목번호@@
                "IsuNm": "IsuNm`char", ## 종목명@@
                "BnsTpNm": "BnsTpNm`char", ## 매매구분@@
                "MrcTpNm": "MrcTpNm`char", ## 정정취소구분명@@
                "FnoOrdprcPtnCode": "FnoOrdprcPtnCode`char", ## 선물옵션호가유형코드@@
                "FnoOrdprcPtnNm": "FnoOrdprcPtnNm`char", ## 선물옵션호가유형명@@
                "OrdPrc": "OrdPrc`double", ## 주문가@@
                "OrdQty": "OrdQty`long", ## 주문수량@@
                "OrdTpNm": "OrdTpNm`char", ## 주문구분명@@
                "ExecTpNm": "ExecTpNm`char", ## 체결구분명@@
                "ExecPrc": "ExecPrc`double", ## 체결가@@
                "ExecQty": "ExecQty`long", ## 체결수량@@
                "CtrctTime": "CtrctTime`char", ## 약정시각@@
                "CtrctNo": "CtrctNo`long", ## 약정번호@@
                "ExecNo": "ExecNo`long", ## 체결번호@@
                "BnsplAmt": "BnsplAmt`long", ## 매매손익금액@@
                "UnercQty": "UnercQty`long", ## 미체결수량@@
                "UserId": "UserId`char", ## 사용자ID@@
                "CommdaCode": "CommdaCode`char", ## 통신매체코드@@
                "CommdaCodeNm": "CommdaCodeNm`char##통신매체코드명@@"
            }
        }
    },
    "CFOAQ10100": { ## 선물옵션 주문가능수량조회
        "input": {
            "CFOAQ10100InBlock1": {
                "RecCnt": "0", ## 레코드갯수@@
                "AcntNo": " ", ## 계좌번호@@
                "Pwd": " ", ## 비밀번호@@
                "QryTp": " ", ## 조회구분@@
                "OrdAmt": "0", ## 주문금액@@
                "RatVal": "0.0", ## 비율값@@
                "FnoIsuNo": " ", ## 선물옵션종목번호@@
                "BnsTpCode": " ", ## 매매구분@@
                "OrdPrc": "0.0", ## 주문가@@
                "FnoOrdprcPtnCode": " ##선물옵션호가유형코드@@"
            }
        },
        "output": {
            "CFOAQ10100OutBlock1": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "AcntNo": "AcntNo`char", ## 계좌번호@@
                "Pwd": "Pwd`char", ## 비밀번호@@
                "QryTp": "QryTp`char", ## 조회구분@@
                "OrdAmt": "OrdAmt`long", ## 주문금액@@
                "RatVal": "RatVal`double", ## 비율값@@
                "FnoIsuNo": "FnoIsuNo`char", ## 선물옵션종목번호@@
                "BnsTpCode": "BnsTpCode`char", ## 매매구분@@
                "OrdPrc": "OrdPrc`double", ## 주문가@@
                "FnoOrdprcPtnCode": "FnoOrdprcPtnCode`char##선물옵션호가유형코드@@"
            },
            "CFOAQ10100OutBlock2": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "AcntNm": "AcntNm`char", ## 계좌명@@
                "QryDt": "QryDt`char", ## 조회일@@
                "NowPrc": "NowPrc`double", ## 현재가@@
                "OrdAbleQty": "OrdAbleQty`long", ## 주문가능수량@@
                "NewOrdAbleQty": "NewOrdAbleQty`long", ## 신규주문가능수량@@
                "LqdtOrdAbleQty": "LqdtOrdAbleQty`long", ## 청산주문가능수량@@
                "UsePreargMgn": "UsePreargMgn`long", ## 사용예정증거금액@@
                "UsePreargMnyMgn": "UsePreargMnyMgn`long", ## 사용예정현금증거금액@@
                "OrdAbleAmt": "OrdAbleAmt`long", ## 주문가능금액@@
                "MnyOrdAbleAmt": "MnyOrdAbleAmt`long##현금주문가능금액@@"
            }
        }
    },
    "CFOAT00100": { ## 선물옵션 정상주문
        "input": {
            "CFOAT00100InBlock1": {
                "AcntNo": " ", ## 계좌번호@@
                "Pwd": " ", ## 비밀번호@@
                "FnoIsuNo": " ", ## 선물옵션종목번호@@
                "BnsTpCode": " ", ## 매매구분@@
                "FnoOrdprcPtnCode": " ", ## 선물옵션호가유형코드@@
                "OrdPrc": "0.0", ## 주문가격@@
                "OrdQty": "0##주문수량@@"
            }
        },
        "output": {
            "CFOAT00100OutBlock1": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "OrdMktCode": "OrdMktCode`char", ## 주문시장코드@@
                "AcntNo": "AcntNo`char", ## 계좌번호@@
                "Pwd": "Pwd`char", ## 비밀번호@@
                "FnoIsuNo": "FnoIsuNo`char", ## 선물옵션종목번호@@
                "BnsTpCode": "BnsTpCode`char", ## 매매구분@@
                "FnoOrdPtnCode": "FnoOrdPtnCode`char", ## 선물옵션주문유형코드@@
                "FnoOrdprcPtnCode": "FnoOrdprcPtnCode`char", ## 선물옵션호가유형코드@@
                "FnoTrdPtnCode": "FnoTrdPtnCode`char", ## 선물옵션거래유형코드@@
                "OrdPrc": "OrdPrc`double", ## 주문가격@@
                "OrdQty": "OrdQty`long", ## 주문수량@@
                "CommdaCode": "CommdaCode`char", ## 통신매체코드@@
                "DscusBnsCmpltTime": "DscusBnsCmpltTime`char", ## 협의매매완료시각@@
                "GrpId": "GrpId`char", ## 그룹ID@@
                "OrdSeqno": "OrdSeqno`long", ## 주문일련번호@@
                "PtflNo": "PtflNo`long", ## 포트폴리오번호@@
                "BskNo": "BskNo`long", ## 바스켓번호@@
                "TrchNo": "TrchNo`long", ## 트렌치번호@@
                "ItemNo": "ItemNo`long", ## 항목번호@@
                "OpDrtnNo": "OpDrtnNo`char", ## 운용지시번호@@
                "MgempNo": "MgempNo`char", ## 관리사원번호@@
                "FundId": "FundId`char", ## 펀드ID@@
                "FundOrdNo": "FundOrdNo`long##펀드주문번호@@"
            },
            "CFOAT00100OutBlock2": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "OrdNo": "OrdNo`long", ## 주문번호@@
                "BrnNm": "BrnNm`char", ## 지점명@@
                "AcntNm": "AcntNm`char", ## 계좌명@@
                "IsuNm": "IsuNm`char", ## 종목명@@
                "OrdAbleAmt": "OrdAbleAmt`long", ## 주문가능금액@@
                "MnyOrdAbleAmt": "MnyOrdAbleAmt`long", ## 현금주문가능금액@@
                "OrdMgn": "OrdMgn`long", ## 주문증거금@@
                "MnyOrdMgn": "MnyOrdMgn`long", ## 현금주문증거금@@
                "OrdAbleQty": "OrdAbleQty`long##주문가능수량@@"
            }
        }
    },
    "CFOAT00200": { ## 선물옵션 정정주문
        "input": {
            "CFOAT00200InBlock1": {
                "AcntNo": " ", ## 계좌번호@@
                "Pwd": " ", ## 비밀번호@@
                "FnoIsuNo": " ", ## 선물옵션종목번호@@
                "OrgOrdNo": "0", ## 원주문번호@@
                "FnoOrdprcPtnCode": " ", ## 선물옵션호가유형코드@@
                "OrdPrc": "0.0", ## 주문가격@@
                "MdfyQty": "0##정정수량@@"
            }
        },
        "output": {
            "CFOAT00200OutBlock1": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "OrdMktCode": "OrdMktCode`char", ## 주문시장코드@@
                "AcntNo": "AcntNo`char", ## 계좌번호@@
                "Pwd": "Pwd`char", ## 비밀번호@@
                "FnoIsuNo": "FnoIsuNo`char", ## 선물옵션종목번호@@
                "FnoOrdPtnCode": "FnoOrdPtnCode`char", ## 선물옵션주문유형코드@@
                "OrgOrdNo": "OrgOrdNo`long", ## 원주문번호@@
                "FnoOrdprcPtnCode": "FnoOrdprcPtnCode`char", ## 선물옵션호가유형코드@@
                "OrdPrc": "OrdPrc`double", ## 주문가격@@
                "MdfyQty": "MdfyQty`long", ## 정정수량@@
                "CommdaCode": "CommdaCode`char", ## 통신매체코드@@
                "DscusBnsCmpltTime": "DscusBnsCmpltTime`char", ## 협의매매완료시각@@
                "GrpId": "GrpId`char", ## 그룹ID@@
                "OrdSeqno": "OrdSeqno`long", ## 주문일련번호@@
                "PtflNo": "PtflNo`long", ## 포트폴리오번호@@
                "BskNo": "BskNo`long", ## 바스켓번호@@
                "TrchNo": "TrchNo`long", ## 트렌치번호@@
                "ItemNo": "ItemNo`long", ## 아이템번호@@
                "MgempNo": "MgempNo`char", ## 관리사원번호@@
                "FundId": "FundId`char", ## 펀드ID@@
                "FundOrgOrdNo": "FundOrgOrdNo`long", ## 펀드원주문번호@@
                "FundOrdNo": "FundOrdNo`long##펀드주문번호@@"
            },
            "CFOAT00200OutBlock2": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "OrdNo": "OrdNo`long", ## 주문번호@@
                "BrnNm": "BrnNm`char", ## 지점명@@
                "AcntNm": "AcntNm`char", ## 계좌명@@
                "IsuNm": "IsuNm`char", ## 종목명@@
                "OrdAbleAmt": "OrdAbleAmt`long", ## 주문가능금액@@
                "MnyOrdAbleAmt": "MnyOrdAbleAmt`long", ## 현금주문가능금액@@
                "OrdMgn": "OrdMgn`long", ## 주문증거금액@@
                "MnyOrdMgn": "MnyOrdMgn`long", ## 현금주문증거금액@@
                "OrdAbleQty": "OrdAbleQty`long##주문가능수량@@"
            }
        }
    },
    "CFOAT00300": { ## 선물옵션 취소주문
        "input": {
            "CFOAT00300InBlock1": {
                "AcntNo": " ", ## 계좌번호@@
                "Pwd": " ", ## 비밀번호@@
                "FnoIsuNo": " ", ## 선물옵션종목번호@@
                "OrgOrdNo": "0", ## 원주문번호@@
                "CancQty": "0##취소수량@@"
            }
        },
        "output": {
            "CFOAT00300OutBlock1": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "OrdMktCode": "OrdMktCode`char", ## 주문시장코드@@
                "AcntNo": "AcntNo`char", ## 계좌번호@@
                "Pwd": "Pwd`char", ## 비밀번호@@
                "FnoIsuNo": "FnoIsuNo`char", ## 선물옵션종목번호@@
                "FnoOrdPtnCode": "FnoOrdPtnCode`char", ## 선물옵션주문유형코드@@
                "OrgOrdNo": "OrgOrdNo`long", ## 원주문번호@@
                "CancQty": "CancQty`long", ## 취소수량@@
                "CommdaCode": "CommdaCode`char", ## 통신매체코드@@
                "DscusBnsCmpltTime": "DscusBnsCmpltTime`char", ## 협의매매완료시각@@
                "GrpId": "GrpId`char", ## 그룹ID@@
                "OrdSeqno": "OrdSeqno`long", ## 주문일련번호@@
                "PtflNo": "PtflNo`long", ## 포트폴리오번호@@
                "BskNo": "BskNo`long", ## 바스켓번호@@
                "TrchNo": "TrchNo`long", ## 트렌치번호@@
                "ItemNo": "ItemNo`long", ## 아이템번호@@
                "MgempNo": "MgempNo`char", ## 관리사원번호@@
                "FundId": "FundId`char", ## 펀드ID@@
                "FundOrgOrdNo": "FundOrgOrdNo`long", ## 펀드원주문번호@@
                "FundOrdNo": "FundOrdNo`long##펀드주문번호@@"
            },
            "CFOAT00300OutBlock2": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "OrdNo": "OrdNo`long", ## 주문번호@@
                "BrnNm": "BrnNm`char", ## 지점명@@
                "AcntNm": "AcntNm`char", ## 계좌명@@
                "IsuNm": "IsuNm`char", ## 종목명@@
                "OrdAbleAmt": "OrdAbleAmt`long", ## 주문가능금액@@
                "MnyOrdAbleAmt": "MnyOrdAbleAmt`long", ## 현금주문가능금액@@
                "OrdMgn": "OrdMgn`long", ## 주문증거금액@@
                "MnyOrdMgn": "MnyOrdMgn`long", ## 현금주문증거금액@@
                "OrdAbleQty": "OrdAbleQty`long##주문가능수량@@"
            }
        }
    },
    "CFOBQ10500": { ## 선물옵션 계좌예탁금증거금조회
        "input": {
            "CFOBQ10500InBlock1": {
                "RecCnt": "0", ## 레코드갯수@@
                "AcntNo": " ", ## 계좌번호@@
                "Pwd": " ##비밀번호@@"
            }
        },
        "output": {
            "CFOBQ10500OutBlock1": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "AcntNo": "AcntNo`char", ## 계좌번호@@
                "Pwd": "Pwd`char##비밀번호@@"
            },
            "CFOBQ10500OutBlock2": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "AcntNm": "AcntNm`char", ## 계좌명@@
                "DpsamtTotamt": "DpsamtTotamt`long", ## 예탁금총액@@
                "Dps": "Dps`long", ## 예수금@@
                "SubstAmt": "SubstAmt`long", ## 대용금액@@
                "FilupDpsamtTotamt": "FilupDpsamtTotamt`long", ## 충당예탁금총액@@
                "FilupDps": "FilupDps`long", ## 충당예수금@@
                "FutsPnlAmt": "FutsPnlAmt`long", ## 선물손익금액@@
                "WthdwAbleAmt": "WthdwAbleAmt`long", ## 인출가능금액@@
                "PsnOutAbleCurAmt": "PsnOutAbleCurAmt`long", ## 인출가능현금액@@
                "PsnOutAbleSubstAmt": "PsnOutAbleSubstAmt`long", ## 인출가능대용금액@@
                "Mgn": "Mgn`long", ## 증거금액@@
                "MnyMgn": "MnyMgn`long", ## 현금증거금액@@
                "OrdAbleAmt": "OrdAbleAmt`long", ## 주문가능금액@@
                "MnyOrdAbleAmt": "MnyOrdAbleAmt`long", ## 현금주문가능금액@@
                "AddMgn": "AddMgn`long", ## 추가증거금액@@
                "MnyAddMgn": "MnyAddMgn`long", ## 현금추가증거금액@@
                "AmtPrdayChckInAmt": "AmtPrdayChckInAmt`long", ## 금전일수표입금액@@
                "FnoPrdaySubstSellAmt": "FnoPrdaySubstSellAmt`long", ## 선물옵션전일대용매도금액@@
                "FnoCrdaySubstSellAmt": "FnoCrdaySubstSellAmt`long", ## 선물옵션금일대용매도금액@@
                "FnoPrdayFdamt": "FnoPrdayFdamt`long", ## 선물옵션전일가입금액@@
                "FnoCrdayFdamt": "FnoCrdayFdamt`long", ## 선물옵션금일가입금액@@
                "FcurrSubstAmt": "FcurrSubstAmt`long", ## 외화대용금액@@
                "FnoAcntAfmgnNm": "FnoAcntAfmgnNm`char##선물옵션계좌사후증거금명@@"
            },
            "CFOBQ10500OutBlock3": {
                "PdGrpCodeNm": "PdGrpCodeNm`char", ## 상품군코드명@@
                "NetRiskMgn": "NetRiskMgn`long", ## 순위험증거금액@@
                "PrcMgn": "PrcMgn`long", ## 가격증거금액@@
                "SprdMgn": "SprdMgn`long", ## 스프레드증거금액@@
                "PrcFlctMgn": "PrcFlctMgn`long", ## 가격변동증거금액@@
                "MinMgn": "MinMgn`long", ## 최소증거금액@@
                "OrdMgn": "OrdMgn`long", ## 주문증거금액@@
                "OptNetBuyAmt": "OptNetBuyAmt`long", ## 옵션순매수금액@@
                "CsgnMgn": "CsgnMgn`long", ## 위탁증거금액@@
                "MaintMgn": "MaintMgn`long", ## 유지증거금액@@
                "FutsBuyExecAmt": "FutsBuyExecAmt`long", ## 선물매수체결금액@@
                "FutsSellExecAmt": "FutsSellExecAmt`long", ## 선물매도체결금액@@
                "OptBuyExecAmt": "OptBuyExecAmt`long", ## 옵션매수체결금액@@
                "OptSellExecAmt": "OptSellExecAmt`long", ## 옵션매도체결금액@@
                "FutsPnlAmt": "FutsPnlAmt`long", ## 선물손익금액@@
                "TotRiskCsgnMgn": "TotRiskCsgnMgn`long", ## 총위험위탁증거금@@
                "UndCsgnMgn": "UndCsgnMgn`long", ## 인수도위탁증거금@@
                "MgnRdctAmt": "MgnRdctAmt`long##증거금감면금액@@"
            }
        }
    },
    "CFOBQ10800": { ## 선물옵션 옵션매도시 주문증거금조회
        "input": {
            "CFOBQ10800InBlock1": {
                "RecCnt": "0", ## 레코드갯수@@
                "PrdgrpClssCode": " ", ## 상품군코드@@
                "ClssGrpCode": " ", ## 기초자산코드@@
                "BaseYear": " ", ## 기준연도@@
                "FstmmTpCode": " ##최근월물구분@@"
            }
        },
        "output": {
            "CFOBQ10800OutBlock1": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "PrdgrpClssCode": "PrdgrpClssCode`char", ## 상품군코드@@
                "ClssGrpCode": "ClssGrpCode`char", ## 기초자산코드@@
                "BaseYear": "BaseYear`char", ## 기준연도@@
                "FstmmTpCode": "FstmmTpCode`char##최근월물구분@@"
            },
            "CFOBQ10800OutBlock2": {
                "ElwXrcPrc": "ElwXrcPrc`double", ## 행사가@@
                "FnoIsuNo": "FnoIsuNo`char", ## 선물옵션종목번호@@
                "HanglIsuNm1": "HanglIsuNm1`char", ## 한글종목명1@@
                "TpNm1": "TpNm1`char", ## 구분명1@@
                "UpOptRegulThrprc": "UpOptRegulThrprc`double", ## 상승옵션조정이론가@@
                "Thrprc1": "Thrprc1`double", ## 이론가1@@
                "BasePrc1": "BasePrc1`double", ## 기준가1@@
                "OrdMgn1": "OrdMgn1`long", ## 주문증거금액1@@
                "FnoIsuNo0": "FnoIsuNo0`char", ## 선물옵션종목번호0@@
                "HanglIsuNm2": "HanglIsuNm2`char", ## 한글종목명2@@
                "TpNm2": "TpNm2`char", ## 구분명2@@
                "DownOptRegulThrprc": "DownOptRegulThrprc`double", ## 하락옵션조정이론가@@
                "Thrprc2": "Thrprc2`double", ## 이론가2@@
                "BasePrc2": "BasePrc2`double", ## 기준가2@@
                "OrdMgn2": "OrdMgn2`long##주문증거금액2@@"
            }
        }
    },
    "CFOEQ11100": { ## 선물옵션가정산예탁금상세
        "input": {
            "CFOEQ11100InBlock1": {
                "RecCnt": "0", ## 레코드갯수@@
                "AcntNo": " ", ## 계좌번호@@
                "Pwd": " ", ## 비밀번호@@
                "BnsDt": " ##매매일@@"
            }
        },
        "output": {
            "CFOEQ11100OutBlock1": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "AcntNo": "AcntNo`char", ## 계좌번호@@
                "Pwd": "Pwd`char", ## 비밀번호@@
                "BnsDt": "BnsDt`char##매매일@@"
            },
            "CFOEQ11100OutBlock2": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "AcntNm": "AcntNm`char", ## 계좌명@@
                "OpnmkDpsamtTotamt": "OpnmkDpsamtTotamt`long", ## 개장시예탁금총액@@
                "OpnmkDps": "OpnmkDps`long", ## 개장시예수금@@
                "OpnmkMnyrclAmt": "OpnmkMnyrclAmt`long", ## 개장시현금미수금@@
                "OpnmkSubstAmt": "OpnmkSubstAmt`long", ## 개장시대용금액@@
                "TotAmt": "TotAmt`long", ## 총금액@@
                "Dps": "Dps`long", ## 예수금@@
                "MnyrclAmt": "MnyrclAmt`long", ## 현금미수금액@@
                "SubstDsgnAmt": "SubstDsgnAmt`long", ## 대용지정금액@@
                "CsgnMgn": "CsgnMgn`long", ## 위탁증거금액@@
                "MnyCsgnMgn": "MnyCsgnMgn`long", ## 현금위탁증거금액@@
                "MaintMgn": "MaintMgn`long", ## 유지증거금액@@
                "MnyMaintMgn": "MnyMaintMgn`long", ## 현금유지증거금액@@
                "OutAbleAmt": "OutAbleAmt`long", ## 출금가능총액@@
                "MnyoutAbleAmt": "MnyoutAbleAmt`long", ## 출금가능금액@@
                "SubstOutAbleAmt": "SubstOutAbleAmt`long", ## 출금가능대용@@
                "OrdAbleAmt": "OrdAbleAmt`long", ## 주문가능금액@@
                "MnyOrdAbleAmt": "MnyOrdAbleAmt`long", ## 현금주문가능금액@@
                "AddMgnOcrTpCode": "AddMgnOcrTpCode`char", ## 추가증거금구분@@
                "AddMgn": "AddMgn`long", ## 추가증거금액@@
                "MnyAddMgn": "MnyAddMgn`long", ## 현금추가증거금액@@
                "NtdayTotAmt": "NtdayTotAmt`long", ## 익일예탁총액@@
                "NtdayDps": "NtdayDps`long", ## 익일예탁현금@@
                "NtdayMnyrclAmt": "NtdayMnyrclAmt`long", ## 익일미수금@@
                "NtdaySubstAmt": "NtdaySubstAmt`long", ## 익일예탁대용@@
                "NtdayCsgnMgn": "NtdayCsgnMgn`long", ## 익일위탁증거금@@
                "NtdayMnyCsgnMgn": "NtdayMnyCsgnMgn`long", ## 익일위탁증거금현금@@
                "NtdayMaintMgn": "NtdayMaintMgn`long", ## 익일유지증거금@@
                "NtdayMnyMaintMgn": "NtdayMnyMaintMgn`long", ## 익일유지증거금현금@@
                "NtdayOutAbleAmt": "NtdayOutAbleAmt`long", ## 익일인출가능금액@@
                "NtdayMnyoutAbleAmt": "NtdayMnyoutAbleAmt`long", ## 익일인출가능금액@@
                "NtdaySubstOutAbleAmt": "NtdaySubstOutAbleAmt`long", ## 익일인출가능대용@@
                "NtdayOrdAbleAmt": "NtdayOrdAbleAmt`long", ## 익일주문가능금액@@
                "NtdayMnyOrdAbleAmt": "NtdayMnyOrdAbleAmt`long", ## 익일주문가능현금@@
                "NtdayAddMgnTp": "NtdayAddMgnTp`char", ## 익일추가증거금구분@@
                "NtdayAddMgn": "NtdayAddMgn`long", ## 익일추가증거금@@
                "NtdayMnyAddMgn": "NtdayMnyAddMgn`long", ## 익일추가증거금현금@@
                "NtdaySettAmt": "NtdaySettAmt`long", ## 익일결제금액@@
                "EvalDpsamtTotamt": "EvalDpsamtTotamt`long", ## 평가예탁금총액@@
                "MnyEvalDpstgAmt": "MnyEvalDpstgAmt`long", ## 현금평가예탁금액@@
                "DpsamtUtlfeeGivPrergAmt": "DpsamtUtlfeeGivPrergAmt`long", ## 예탁금이용료지급예정금액@@
                "TaxAmt": "TaxAmt`long", ## 세금@@
                "CsgnMgnrat": "CsgnMgnrat`double", ## 위탁증거금 비율@@
                "CsgnMnyMgnrat": "CsgnMnyMgnrat`double", ## 위탁증거금현금비율@@
                "DpstgTotamtLackAmt": "DpstgTotamtLackAmt`long", ## 예탁총액부족금액(위탁증거금기준)@@
                "DpstgMnyLackAmt": "DpstgMnyLackAmt`long", ## 예탁현금부족금액(위탁증거금기준)@@
                "RealInAmt": "RealInAmt`long", ## 실입금액@@
                "InAmt": "InAmt`long", ## 입금액@@
                "OutAmt": "OutAmt`long", ## 출금액@@
                "FutsAdjstDfamt": "FutsAdjstDfamt`long", ## 선물정산차금@@
                "FutsThdayDfamt": "FutsThdayDfamt`long", ## 선물당일차금@@
                "FutsUpdtDfamt": "FutsUpdtDfamt`long", ## 선물갱신차금@@
                "FutsLastSettDfamt": "FutsLastSettDfamt`long", ## 선물최종결제차금@@
                "OptSettDfamt": "OptSettDfamt`long", ## 옵션결제차금@@
                "OptBuyAmt": "OptBuyAmt`long", ## 옵션매수금액@@
                "OptSellAmt": "OptSellAmt`long", ## 옵션매도금액@@
                "OptXrcDfamt": "OptXrcDfamt`long", ## 옵션행사차금@@
                "OptAsgnDfamt": "OptAsgnDfamt`long", ## 옵션배정차금@@
                "RealGdsUndAmt": "RealGdsUndAmt`long", ## 실물인수도금액@@
                "RealGdsUndAsgnAmt": "RealGdsUndAsgnAmt`long", ## 실물인수도배정대금@@
                "RealGdsUndXrcAmt": "RealGdsUndXrcAmt`long", ## 실물인수도행사대금@@
                "CmsnAmt": "CmsnAmt`long", ## 수수료@@
                "FutsCmsn": "FutsCmsn`long", ## 선물수수료@@
                "OptCmsn": "OptCmsn`long", ## 옵션수수료@@
                "FutsCtrctQty": "FutsCtrctQty`long", ## 선물약정수량@@
                "FutsCtrctAmt": "FutsCtrctAmt`long", ## 선물약정금액@@
                "OptCtrctQty": "OptCtrctQty`long", ## 옵션약정수량@@
                "OptCtrctAmt": "OptCtrctAmt`long", ## 옵션약정금액@@
                "FutsUnsttQty": "FutsUnsttQty`long", ## 선물미결제수량@@
                "FutsUnsttAmt": "FutsUnsttAmt`long", ## 선물미결제금액@@
                "OptUnsttQty": "OptUnsttQty`long", ## 옵션미결제수량@@
                "OptUnsttAmt": "OptUnsttAmt`long", ## 옵션미결제금액@@
                "FutsBuyUnsttQty": "FutsBuyUnsttQty`long", ## 선물매수미결제수량@@
                "FutsBuyUnsttAmt": "FutsBuyUnsttAmt`long", ## 선물매수미결제금액@@
                "FutsSellUnsttQty": "FutsSellUnsttQty`long", ## 선물매도미결제수량@@
                "FutsSellUnsttAmt": "FutsSellUnsttAmt`long", ## 선물매도미결제금액@@
                "OptBuyUnsttQty": "OptBuyUnsttQty`long", ## 옵션매수미결제수량@@
                "OptBuyUnsttAmt": "OptBuyUnsttAmt`long", ## 옵션매수미결제금액@@
                "OptSellUnsttQty": "OptSellUnsttQty`long", ## 옵션매도미결제수량@@
                "OptSellUnsttAmt": "OptSellUnsttAmt`long", ## 옵션매도미결제금액@@
                "FutsBuyctrQty": "FutsBuyctrQty`long", ## 선물매수약정수량@@
                "FutsBuyctrAmt": "FutsBuyctrAmt`long", ## 선물매수약정금액@@
                "FutsSlctrQty": "FutsSlctrQty`long", ## 선물매도약정수량@@
                "FutsSlctrAmt": "FutsSlctrAmt`long", ## 선물매도약정금액@@
                "OptBuyctrQty": "OptBuyctrQty`long", ## 옵션매수약정수량@@
                "OptBuyctrAmt": "OptBuyctrAmt`long", ## 옵션매수약정금액@@
                "OptSlctrQty": "OptSlctrQty`long", ## 옵션매도약정수량@@
                "OptSlctrAmt": "OptSlctrAmt`long", ## 옵션매도약정금액@@
                "FutsBnsplAmt": "FutsBnsplAmt`long", ## 선물매매손익금액@@
                "OptBnsplAmt": "OptBnsplAmt`long", ## 옵션매매손익금액@@
                "FutsEvalPnlAmt": "FutsEvalPnlAmt`long", ## 선물평가손익금액@@
                "OptEvalPnlAmt": "OptEvalPnlAmt`long", ## 옵션평가손익금액@@
                "FutsEvalAmt": "FutsEvalAmt`long", ## 선물평가금액@@
                "OptEvalAmt": "OptEvalAmt`long", ## 옵션평가금액@@
                "MktEndAfMnyInAmt": "MktEndAfMnyInAmt`long", ## 장종료후현금입금금액@@
                "MktEndAfMnyOutAmt": "MktEndAfMnyOutAmt`long", ## 장종료후현금출금금액@@
                "MktEndAfSubstDsgnAmt": "MktEndAfSubstDsgnAmt`long", ## 장종료후대용지정금액@@
                "MktEndAfSubstAbndAmt": "MktEndAfSubstAbndAmt`long##장종료후대용해지금액@@"
            }
        }
    },
    "CFOEQ82600": { ## 선물옵션 일별 계좌손익내역
        "input": {
            "CFOEQ82600InBlock1": {
                "RecCnt": "0", ## 레코드갯수@@
                "AcntNo": " ", ## 계좌번호@@
                "Pwd": " ", ## 비밀번호@@
                "QrySrtDt": " ", ## 조회시작일@@
                "QryEndDt": " ", ## 조회종료일@@
                "QryTp": " ", ## 조회구분@@
                "StnlnSeqTp": " ", ## 정렬순서구분@@
                "FnoBalEvalTpCode": " ##선물옵션잔고평가구분코드@@"
            }
        },
        "output": {
            "CFOEQ82600OutBlock1": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "AcntNo": "AcntNo`char", ## 계좌번호@@
                "Pwd": "Pwd`char", ## 비밀번호@@
                "QrySrtDt": "QrySrtDt`char", ## 조회시작일@@
                "QryEndDt": "QryEndDt`char", ## 조회종료일@@
                "QryTp": "QryTp`char", ## 조회구분@@
                "StnlnSeqTp": "StnlnSeqTp`char", ## 정렬순서구분@@
                "FnoBalEvalTpCode": "FnoBalEvalTpCode`char##선물옵션잔고평가구분코드@@"
            },
            "CFOEQ82600OutBlock2": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "FutsAdjstDfamt": "FutsAdjstDfamt`long", ## 선물정산차금@@
                "OptBnsplAmt": "OptBnsplAmt`long", ## 옵션매매손익금액@@
                "FnoCmsnAmt": "FnoCmsnAmt`long", ## 선물옵션수수료@@
                "PnlSumAmt": "PnlSumAmt`long", ## 손익합계금액@@
                "MnyinSumAmt": "MnyinSumAmt`long", ## 입금합계금액@@
                "MnyoutSumAmt": "MnyoutSumAmt`long", ## 출금합계금액@@
                "AcntNm": "AcntNm`char##계좌명@@"
            },
            "CFOEQ82600OutBlock3": {
                "QryDt": "QryDt`char", ## 조회일@@
                "DpstgTotamt": "DpstgTotamt`long", ## 예탁총액@@
                "DpstgMny": "DpstgMny`long", ## 예탁현금@@
                "FnoMgn": "FnoMgn`long", ## 선물옵션증거금액@@
                "FutsPnlAmt": "FutsPnlAmt`long", ## 선물손익금액@@
                "OptBsnPnlAmt": "OptBsnPnlAmt`long", ## 옵션매매손익금액@@
                "OptEvalPnlAmt": "OptEvalPnlAmt`long", ## 옵션평가손익금액@@
                "CmsnAmt": "CmsnAmt`long", ## 수수료@@
                "SumAmt1": "SumAmt1`long", ## 합계금액1@@
                "SumAmt2": "SumAmt2`long", ## 합계금액@@
                "PnlSumAmt": "PnlSumAmt`long", ## 손익합계금액@@
                "FutsBuyAmt": "FutsBuyAmt`long", ## 선물매수금액@@
                "FutsSellAmt": "FutsSellAmt`long", ## 선물매도금액@@
                "OptBuyAmt": "OptBuyAmt`long", ## 옵션매수금액@@
                "OptSellAmt": "OptSellAmt`long", ## 옵션매도금액@@
                "InAmt": "InAmt`long", ## 입금액@@
                "OutAmt": "OutAmt`long", ## 출금액@@
                "EvalAmt": "EvalAmt`long", ## 평가금액@@
                "AddupEvalAmt": "AddupEvalAmt`long", ## 합산평가금액@@
                "Amt2": "Amt2`long##금액2@@"
            }
        }
    },
    "CFOFQ02400": { ## 계좌 미결제 약정현황(평균가)
        "input": {
            "CFOFQ02400InBlock1": {
                "RecCnt": "0", ## 레코드갯수@@
                "AcntNo": " ", ## 계좌번호@@
                "Pwd": " ", ## 비밀번호@@
                "RegMktCode": " ", ## 등록시장코드@@
                "BuyDt": " ##매수일자@@"
            }
        },
        "output": {
            "CFOFQ02400OutBlock1": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "AcntNo": "AcntNo`char", ## 계좌번호@@
                "Pwd": "Pwd`char", ## 비밀번호@@
                "RegMktCode": "RegMktCode`char", ## 등록시장코드@@
                "BuyDt": "BuyDt`char##매수일자@@"
            },
            "CFOFQ02400OutBlock2": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "AcntNm": "AcntNm`char", ## 계좌명@@
                "FutsCtrctQty": "FutsCtrctQty`long", ## 선물약정수량@@
                "OptCtrctQty": "OptCtrctQty`long", ## 옵션약정수량@@
                "CtrctQty": "CtrctQty`long", ## 약정수량@@
                "FutsCtrctAmt": "FutsCtrctAmt`long", ## 선물약정금액@@
                "FutsBuyctrAmt": "FutsBuyctrAmt`long", ## 선물매수약정금액@@
                "FutsSlctrAmt": "FutsSlctrAmt`long", ## 선물매도약정금액@@
                "CalloptCtrctAmt": "CalloptCtrctAmt`long", ## 콜옵션약정금액@@
                "CallBuyAmt": "CallBuyAmt`long", ## 콜매수금액@@
                "CallSellAmt": "CallSellAmt`long", ## 콜매도금액@@
                "PutoptCtrctAmt": "PutoptCtrctAmt`long", ## 풋옵션약정금액@@
                "PutBuyAmt": "PutBuyAmt`long", ## 풋매수금액@@
                "PutSellAmt": "PutSellAmt`long", ## 풋매도금액@@
                "AllCtrctAmt": "AllCtrctAmt`long", ## 전체약정금액@@
                "BuyctrAsmAmt": "BuyctrAsmAmt`long", ## 매수약정누계금액@@
                "SlctrAsmAmt": "SlctrAsmAmt`long", ## 매도약정누계금액@@
                "FutsPnlSum": "FutsPnlSum`long", ## 선물손익합계@@
                "OptPnlSum": "OptPnlSum`long", ## 옵션손익합계@@
                "AllPnlSum": "AllPnlSum`long##전체손익합계@@"
            },
            "CFOFQ02400OutBlock3": {
                "FnoClssCode": "FnoClssCode`char", ## 선물옵션품목구분@@
                "FutsSellQty": "FutsSellQty`long", ## 선물매도수량@@
                "FutsSellPnl": "FutsSellPnl`long", ## 선물매도손익@@
                "FutsBuyQty": "FutsBuyQty`long", ## 선물매수수량@@
                "FutsBuyPnl": "FutsBuyPnl`long", ## 선물매수손익@@
                "CallSellQty": "CallSellQty`long", ## 콜매도수량@@
                "CallSellPnl": "CallSellPnl`long", ## 콜매도손익@@
                "CallBuyQty": "CallBuyQty`long", ## 콜매수수량@@
                "CallBuyPnl": "CallBuyPnl`long", ## 콜매수손익@@
                "PutSellQty": "PutSellQty`long", ## 풋매도수량@@
                "PutSellPnl": "PutSellPnl`long", ## 풋매도손익@@
                "PutBuyQty": "PutBuyQty`long", ## 풋매수수량@@
                "PutBuyPnl": "PutBuyPnl`long##풋매수손익@@"
            },
            "CFOFQ02400OutBlock4": {
                "IsuNo": "IsuNo`char", ## 종목번호@@
                "IsuNm": "IsuNm`char", ## 종목명@@
                "BnsTpCode": "BnsTpCode`char", ## 매매구분@@
                "BnsTpNm": "BnsTpNm`char", ## 매매구분@@
                "BalQty": "BalQty`long", ## 잔고수량@@
                "FnoAvrPrc": "FnoAvrPrc`double", ## 평균가@@
                "BgnAmt": "BgnAmt`long", ## 당초금액@@
                "ThdayLqdtQty": "ThdayLqdtQty`long", ## 당일청산수량@@
                "Curprc": "Curprc`double", ## 현재가@@
                "EvalAmt": "EvalAmt`long", ## 평가금액@@
                "EvalPnlAmt": "EvalPnlAmt`long", ## 평가손익금액@@
                "EvalErnrat": "EvalErnrat`double##평가수익률@@"
            }
        }
    },
    "ChartExcel": { ## 챠트엑셀데이터조회
        "input": {
            "ChartExcelInBlock": {
                "indexid": "0", ## 지표ID@@
                "indexname": " ", ## 지표명@@
                "indexparam": " ", ## 지표조건설정@@
                "indexouttype": " ", ## 결과데이터 구분@@
                "market": " ", ## 시장구분@@
                "period": " ", ## 주기구분@@
                "shcode": " ", ## 단축코드@@
                "isexcelout": " ", ## 결과 지표데이터 엑셀표시 여부@@
                "excelfilename": " ", ## 엑셀데이터 파일명@@
                "IsReal": " ##실시간 데이터수신 자동등록 여부@@"
            }
        },
        "output": {
            "ChartExcelOutBlock": {
                "indexid": "indexid`long", ## 지표ID@@
                "rec_cnt": "rec_cnt`long", ## 레코드갯수@@
                "validdata_cnt": "validdata_cnt`long##유효 데이터 컬럼 갯수@@"
            },
            "ChartExcelOutBlock1": {
                "date": "date`char", ## 일자@@
                "time": "time`char", ## 시간@@
                "open": "open`float", ## 시가@@
                "high": "high`float", ## 고가@@
                "low": "low`float", ## 저가@@
                "close": "close`float", ## 종가@@
                "volume": "volume`float", ## 거래량@@
                "value1": "value1`float", ## 지표값1@@
                "value2": "value2`float", ## 지표값2@@
                "value3": "value3`float", ## 지표값3@@
                "value4": "value4`float", ## 지표값4@@
                "value5": "value5`float", ## 지표값5@@
                "pos": "pos`long##위치@@"
            }
        }
    },
    "ChartIndex": { ## 챠트지표데이터조회
        "input": {
            "ChartIndexInBlock": {
                "indexid": "0", ## 지표ID@@
                "indexname": " ", ## 지표명@@
                "indexparam": " ", ## 지표조건설정@@
                "market": " ", ## 시장구분@@
                "period": " ", ## 주기구분@@
                "shcode": " ", ## 단축코드@@
                "qrycnt": "2000", ## 요청건수(최대 500개)@@
                "ncnt": "1", ## 단위(n틱/n분)@@
                "sdate": " ", ## 시작일자@@
                "edate": " ", ## 종료일자@@
                "Isamend": " ", ## 수정주가 반영 여부@@
                "Isgab": " ", ## 갭보정 여부@@
                "IsReal": " ##실시간 데이터수신 자동등록 여부@@"
            }
        },
        "output": {
            "ChartIndexOutBlock": {
                "indexid": "indexid`long", ## 지표ID@@
                "rec_cnt": "rec_cnt`long", ## 레코드갯수@@
                "validdata_cnt": "validdata_cnt`long##유효 데이터 컬럼 갯수@@"
            },
            "ChartIndexOutBlock1": {
                "date": "date`char", ## 일자@@
                "time": "time`char", ## 시간@@
                "open": "open`float", ## 시가@@
                "high": "high`float", ## 고가@@
                "low": "low`float", ## 저가@@
                "close": "close`float", ## 종가@@
                "volume": "volume`float", ## 거래량@@
                "value1": "value1`float", ## 지표값1@@
                "value2": "value2`float", ## 지표값2@@
                "value3": "value3`float", ## 지표값3@@
                "value4": "value4`float", ## 지표값4@@
                "value5": "value5`float", ## 지표값5@@
                "pos": "pos`long##위치@@"
            }
        }
    },
    "CIDBQ01400": { ## 해외선물 체결내역개별 조회
        "input": {
            "CIDBQ01400InBlock1": {
                "RecCnt": "0", ## 레코드갯수@@
                "QryTpCode": " ", ## 조회구분코드@@
                "AcntNo": " ", ## 계좌번호@@
                "IsuCodeVal": " ", ## 종목코드값@@
                "BnsTpCode": " ", ## 매매구분코드@@
                "OvrsDrvtOrdPrc": "0.0", ## 해외파생주문가격@@
                "AbrdFutsOrdPtnCode": " ##해외선물주문유형코드@@"
            }
        },
        "output": {
            "CIDBQ01400OutBlock1": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "QryTpCode": "QryTpCode`char", ## 조회구분코드@@
                "AcntNo": "AcntNo`char", ## 계좌번호@@
                "IsuCodeVal": "IsuCodeVal`char", ## 종목코드값@@
                "BnsTpCode": "BnsTpCode`char", ## 매매구분코드@@
                "OvrsDrvtOrdPrc": "OvrsDrvtOrdPrc`double", ## 해외파생주문가격@@
                "AbrdFutsOrdPtnCode": "AbrdFutsOrdPtnCode`char##해외선물주문유형코드@@"
            },
            "CIDBQ01400OutBlock2": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "OrdAbleQty": "OrdAbleQty`long##주문가능수량@@"
            }
        }
    },
    "CIDBQ01500": { ## 해외선물 미결제 잔고내역
        "input": {
            "CIDBQ01500InBlock1": {
                "RecCnt": "0", ## 레코드갯수@@
                "AcntTpCode": " ", ## 계좌구분코드@@
                "AcntNo": " ", ## 계좌번호@@
                "FcmAcntNo": " ", ## FCM계좌번호@@
                "Pwd": " ", ## 비밀번호@@
                "QryDt": " ", ## 조회일자@@
                "BalTpCode": " ##잔고구분코드@@"
            }
        },
        "output": {
            "CIDBQ01500OutBlock1": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "AcntTpCode": "AcntTpCode`char", ## 계좌구분코드@@
                "AcntNo": "AcntNo`char", ## 계좌번호@@
                "FcmAcntNo": "FcmAcntNo`char", ## FCM계좌번호@@
                "Pwd": "Pwd`char", ## 비밀번호@@
                "QryDt": "QryDt`char", ## 조회일자@@
                "BalTpCode": "BalTpCode`char##잔고구분코드@@"
            },
            "CIDBQ01500OutBlock2": {
                "BaseDt": "BaseDt`char", ## 기준일자@@
                "Dps": "Dps`long", ## 예수금@@
                "LpnlAmt": "LpnlAmt`double", ## 청산손익금액@@
                "FutsDueBfLpnlAmt": "FutsDueBfLpnlAmt`double", ## 선물만기전청산손익금액@@
                "FutsDueBfCmsn": "FutsDueBfCmsn`double", ## 선물만기전수수료@@
                "CsgnMgn": "CsgnMgn`long", ## 위탁증거금액@@
                "MaintMgn": "MaintMgn`long", ## 유지증거금@@
                "CtlmtAmt": "CtlmtAmt`double", ## 신용한도금액@@
                "AddMgn": "AddMgn`long", ## 추가증거금액@@
                "MgnclRat": "MgnclRat`double", ## 마진콜율@@
                "OrdAbleAmt": "OrdAbleAmt`long", ## 주문가능금액@@
                "WthdwAbleAmt": "WthdwAbleAmt`long", ## 인출가능금액@@
                "AcntNo": "AcntNo`char", ## 계좌번호@@
                "IsuCodeVal": "IsuCodeVal`char", ## 종목코드값@@
                "IsuNm": "IsuNm`char", ## 종목명@@
                "CrcyCodeVal": "CrcyCodeVal`char", ## 통화코드값@@
                "OvrsDrvtPrdtCode": "OvrsDrvtPrdtCode`char", ## 해외파생상품코드@@
                "OvrsDrvtOptTpCode": "OvrsDrvtOptTpCode`char", ## 해외파생옵션구분코드@@
                "DueDt": "DueDt`char", ## 만기일자@@
                "OvrsDrvtXrcPrc": "OvrsDrvtXrcPrc`double", ## 해외파생행사가격@@
                "BnsTpCode": "BnsTpCode`char", ## 매매구분코드@@
                "CmnCodeNm": "CmnCodeNm`char", ## 공통코드명@@
                "TpCodeNm": "TpCodeNm`char", ## 구분코드명@@
                "BalQty": "BalQty`long", ## 잔고수량@@
                "PchsPrc": "PchsPrc`double", ## 매입가격@@
                "OvrsDrvtNowPrc": "OvrsDrvtNowPrc`double", ## 해외파생현재가@@
                "AbrdFutsEvalPnlAmt": "AbrdFutsEvalPnlAmt`double", ## 해외선물평가손익금액@@
                "CsgnCmsn": "CsgnCmsn`double", ## 위탁수수료@@
                "PosNo": "PosNo`char", ## 포지션번호@@
                "EufOneCmsnAmt": "EufOneCmsnAmt`double", ## 거래소비용1수수료금액@@
                "EufTwoCmsnAmt": "EufTwoCmsnAmt`double##거래소비용2수수료금액@@"
            }
        }
    },
    "CIDBQ01800": { ## 해외선물 주문체결내역 조회
        "input": {
            "CIDBQ01800InBlock1": {
                "RecCnt": "0", ## 레코드갯수@@
                "AcntNo": " ", ## 계좌번호@@
                "Pwd": " ", ## 비밀번호@@
                "IsuCodeVal": " ", ## 종목코드값@@
                "OrdDt": " ", ## 주문일자@@
                "ThdayTpCode": " ", ## 당일구분코드@@
                "OrdStatCode": " ", ## 주문상태코드@@
                "BnsTpCode": " ", ## 매매구분코드@@
                "QryTpCode": " ", ## 조회구분코드@@
                "OrdPtnCode": " ", ## 주문유형코드@@
                "OvrsDrvtFnoTpCode": " ##해외파생선물옵션구분코드@@"
            }
        },
        "output": {
            "CIDBQ01800OutBlock1": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "AcntNo": "AcntNo`char", ## 계좌번호@@
                "Pwd": "Pwd`char", ## 비밀번호@@
                "IsuCodeVal": "IsuCodeVal`char", ## 종목코드값@@
                "OrdDt": "OrdDt`char", ## 주문일자@@
                "ThdayTpCode": "ThdayTpCode`char", ## 당일구분코드@@
                "OrdStatCode": "OrdStatCode`char", ## 주문상태코드@@
                "BnsTpCode": "BnsTpCode`char", ## 매매구분코드@@
                "QryTpCode": "QryTpCode`char", ## 조회구분코드@@
                "OrdPtnCode": "OrdPtnCode`char", ## 주문유형코드@@
                "OvrsDrvtFnoTpCode": "OvrsDrvtFnoTpCode`char##해외파생선물옵션구분코드@@"
            },
            "CIDBQ01800OutBlock2": {
                "OvrsFutsOrdNo": "OvrsFutsOrdNo`char", ## 해외선물주문번호@@
                "OvrsFutsOrgOrdNo": "OvrsFutsOrgOrdNo`char", ## 해외선물원주문번호@@
                "FcmOrdNo": "FcmOrdNo`char", ## FCM주문번호@@
                "IsuCodeVal": "IsuCodeVal`char", ## 종목코드값@@
                "IsuNm": "IsuNm`char", ## 종목명@@
                "AbrdFutsXrcPrc": "AbrdFutsXrcPrc`double", ## 해외선물행사가격@@
                "FcmAcntNo": "FcmAcntNo`char", ## FCM계좌번호@@
                "BnsTpCode": "BnsTpCode`char", ## 매매구분코드@@
                "BnsTpNm": "BnsTpNm`char", ## 매매구분명@@
                "FutsOrdStatCode": "FutsOrdStatCode`char", ## 선물주문상태코드@@
                "TpCodeNm": "TpCodeNm`char", ## 구분코드명@@
                "FutsOrdTpCode": "FutsOrdTpCode`char", ## 선물주문구분코드@@
                "TrdTpNm": "TrdTpNm`char", ## 거래구분명@@
                "AbrdFutsOrdPtnCode": "AbrdFutsOrdPtnCode`char", ## 해외선물주문유형코드@@
                "OrdPtnNm": "OrdPtnNm`char", ## 주문유형명@@
                "OrdPtnTermTpCode": "OrdPtnTermTpCode`char", ## 주문유형기간구분코드@@
                "CmnCodeNm": "CmnCodeNm`char", ## 공통코드명@@
                "AppSrtDt": "AppSrtDt`char", ## 적용시작일자@@
                "AppEndDt": "AppEndDt`char", ## 적용종료일자@@
                "OvrsDrvtOrdPrc": "OvrsDrvtOrdPrc`double", ## 해외파생주문가격@@
                "OrdQty": "OrdQty`long", ## 주문수량@@
                "OvrsDrvtExecIsuCode": "OvrsDrvtExecIsuCode`char", ## 해외파생체결종목코드@@
                "ExecIsuNm": "ExecIsuNm`char", ## 체결종목명@@
                "ExecBnsTpCode": "ExecBnsTpCode`char", ## 체결매매구분코드@@
                "ExecBnsTpNm": "ExecBnsTpNm`char", ## 체결매매구분명@@
                "AbrdFutsExecPrc": "AbrdFutsExecPrc`double", ## 해외선물체결가격@@
                "ExecQty": "ExecQty`long", ## 체결수량@@
                "OrdCndiPrc": "OrdCndiPrc`double", ## 주문조건가격@@
                "OvrsDrvtNowPrc": "OvrsDrvtNowPrc`double", ## 해외파생현재가@@
                "MdfyQty": "MdfyQty`long", ## 정정수량@@
                "CancQty": "CancQty`long", ## 취소수량@@
                "RjtQty": "RjtQty`long", ## 거부수량@@
                "CnfQty": "CnfQty`long", ## 확인수량@@
                "UnercQty": "UnercQty`long", ## 미체결수량@@
                "CvrgYn": "CvrgYn`char", ## 반대매매여부@@
                "RegTmnlNo": "RegTmnlNo`char", ## 등록단말번호@@
                "RegBrnNo": "RegBrnNo`char", ## 등록지점번호@@
                "RegUserId": "RegUserId`char", ## 등록사용자ID@@
                "OrdDt": "OrdDt`char", ## 주문일자@@
                "OrdTime": "OrdTime`char", ## 주문시각@@
                "OvrsOptXrcRsvTpCode": "OvrsOptXrcRsvTpCode`char", ## 해외옵션행사예약구분코드@@
                "OvrsDrvtOptTpCode": "OvrsDrvtOptTpCode`char", ## 해외파생옵션구분코드@@
                "SprdBaseIsuYn": "SprdBaseIsuYn`char", ## 스프레드기준종목여부@@
                "OvrsFutsOrdDt": "OvrsFutsOrdDt`char", ## 해외선물주문일자@@
                "OvrsFutsOrdNo2": "OvrsFutsOrdNo2`char", ## 해외선물주문번호2@@
                "OvrsFutsOrgOrdNo2": "OvrsFutsOrgOrdNo2`char", ## 해외선물원주문번호2@@
                "OvrsDrvtIsuCode2": "OvrsDrvtIsuCode2`char##해외파생종목코드2@@"
            }
        }
    },
    "CIDBQ02400": { ## 해외선물 주문체결내역 상세 조회
        "input": {
            "CIDBQ02400InBlock1": {
                "RecCnt": "0", ## 레코드갯수@@
                "AcntNo": " ", ## 계좌번호@@
                "Pwd": " ", ## 비밀번호@@
                "IsuCodeVal": " ", ## 종목코드값@@
                "QrySrtDt": " ", ## 조회시작일자@@
                "QryEndDt": " ", ## 조회종료일자@@
                "ThdayTpCode": " ", ## 당일구분코드@@
                "OrdStatCode": " ", ## 주문상태코드@@
                "BnsTpCode": " ", ## 매매구분코드@@
                "QryTpCode": " ", ## 조회구분코드@@
                "OrdPtnCode": " ", ## 주문유형코드@@
                "OvrsDrvtFnoTpCode": " ##해외파생선물옵션구분코드@@"
            }
        },
        "output": {
            "CIDBQ02400OutBlock1": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "AcntNo": "AcntNo`char", ## 계좌번호@@
                "Pwd": "Pwd`char", ## 비밀번호@@
                "IsuCodeVal": "IsuCodeVal`char", ## 종목코드값@@
                "QrySrtDt": "QrySrtDt`char", ## 조회시작일자@@
                "QryEndDt": "QryEndDt`char", ## 조회종료일자@@
                "ThdayTpCode": "ThdayTpCode`char", ## 당일구분코드@@
                "OrdStatCode": "OrdStatCode`char", ## 주문상태코드@@
                "BnsTpCode": "BnsTpCode`char", ## 매매구분코드@@
                "QryTpCode": "QryTpCode`char", ## 조회구분코드@@
                "OrdPtnCode": "OrdPtnCode`char", ## 주문유형코드@@
                "OvrsDrvtFnoTpCode": "OvrsDrvtFnoTpCode`char##해외파생선물옵션구분코드@@"
            },
            "CIDBQ02400OutBlock2": {
                "OrdDt": "OrdDt`char", ## 주문일자@@
                "OvrsFutsOrdNo": "OvrsFutsOrdNo`char", ## 해외선물주문번호@@
                "OvrsFutsOrgOrdNo": "OvrsFutsOrgOrdNo`char", ## 해외선물원주문번호@@
                "FcmOrdNo": "FcmOrdNo`char", ## FCM주문번호@@
                "ExecDt": "ExecDt`char", ## 체결일자@@
                "OvrsFutsExecNo": "OvrsFutsExecNo`char", ## 해외선물체결번호@@
                "FcmAcntNo": "FcmAcntNo`char", ## FCM계좌번호@@
                "IsuCodeVal": "IsuCodeVal`char", ## 종목코드값@@
                "IsuNm": "IsuNm`char", ## 종목명@@
                "AbrdFutsXrcPrc": "AbrdFutsXrcPrc`double", ## 해외선물행사가격@@
                "BnsTpCode": "BnsTpCode`char", ## 매매구분코드@@
                "BnsTpNm": "BnsTpNm`char", ## 매매구분명@@
                "FutsOrdStatCode": "FutsOrdStatCode`char", ## 선물주문상태코드@@
                "TpCodeNm": "TpCodeNm`char", ## 구분코드명@@
                "FutsOrdTpCode": "FutsOrdTpCode`char", ## 선물주문구분코드@@
                "TrdTpNm": "TrdTpNm`char", ## 거래구분명@@
                "AbrdFutsOrdPtnCode": "AbrdFutsOrdPtnCode`char", ## 해외선물주문유형코드@@
                "OrdPtnNm": "OrdPtnNm`char", ## 주문유형명@@
                "OrdPtnTermTpCode": "OrdPtnTermTpCode`char", ## 주문유형기간구분코드@@
                "CmnCodeNm": "CmnCodeNm`char", ## 공통코드명@@
                "AppSrtDt": "AppSrtDt`char", ## 적용시작일자@@
                "AppEndDt": "AppEndDt`char", ## 적용종료일자@@
                "OrdQty": "OrdQty`long", ## 주문수량@@
                "OvrsDrvtOrdPrc": "OvrsDrvtOrdPrc`double", ## 해외파생주문가격@@
                "OvrsDrvtExecIsuCode": "OvrsDrvtExecIsuCode`char", ## 해외파생체결종목코드@@
                "ExecIsuNm": "ExecIsuNm`char", ## 체결종목명@@
                "ExecBnsTpCode": "ExecBnsTpCode`char", ## 체결매매구분코드@@
                "ExecBnsTpNm": "ExecBnsTpNm`char", ## 체결매매구분명@@
                "ExecQty": "ExecQty`long", ## 체결수량@@
                "AbrdFutsExecPrc": "AbrdFutsExecPrc`double", ## 해외선물체결가격@@
                "OrdCndiPrc": "OrdCndiPrc`double", ## 주문조건가격@@
                "OvrsDrvtNowPrc": "OvrsDrvtNowPrc`double", ## 해외파생현재가@@
                "UnercQty": "UnercQty`long", ## 미체결수량@@
                "TrxStatCode": "TrxStatCode`char", ## 처리상태코드@@
                "TrxStatCodeNm": "TrxStatCodeNm`char", ## 처리상태코드명@@
                "CsgnCmsn": "CsgnCmsn`double", ## 위탁수수료@@
                "FcmCmsn": "FcmCmsn`double", ## FCM수수료@@
                "ThcoCmsn": "ThcoCmsn`double", ## 당사수수료@@
                "MdaCode": "MdaCode`char", ## 매체코드@@
                "MdaCodeNm": "MdaCodeNm`char", ## 매체코드명@@
                "RegTmnlNo": "RegTmnlNo`char", ## 등록단말번호@@
                "RegUserId": "RegUserId`char", ## 등록사용자ID@@
                "OrdSndDttm": "OrdSndDttm`char", ## 주문발송일시@@
                "ExecDttm": "ExecDttm`char", ## 체결일시@@
                "EufOneCmsnAmt": "EufOneCmsnAmt`double", ## 거래소비용1수수료금액@@
                "EufTwoCmsnAmt": "EufTwoCmsnAmt`double", ## 거래소비용2수수료금액@@
                "LchOneCmsnAmt": "LchOneCmsnAmt`double", ## 런던청산소1수수료금액@@
                "LchTwoCmsnAmt": "LchTwoCmsnAmt`double", ## 런던청산소2수수료금액@@
                "TrdOneCmsnAmt": "TrdOneCmsnAmt`double", ## 거래1수수료금액@@
                "TrdTwoCmsnAmt": "TrdTwoCmsnAmt`double", ## 거래2수수료금액@@
                "TrdThreeCmsnAmt": "TrdThreeCmsnAmt`double", ## 거래3수수료금액@@
                "StrmOneCmsnAmt": "StrmOneCmsnAmt`double", ## 단기1수수료금액@@
                "StrmTwoCmsnAmt": "StrmTwoCmsnAmt`double", ## 단기2수수료금액@@
                "StrmThreeCmsnAmt": "StrmThreeCmsnAmt`double", ## 단기3수수료금액@@
                "TransOneCmsnAmt": "TransOneCmsnAmt`double", ## 전달1수수료금액@@
                "TransTwoCmsnAmt": "TransTwoCmsnAmt`double", ## 전달2수수료금액@@
                "TransThreeCmsnAmt": "TransThreeCmsnAmt`double", ## 전달3수수료금액@@
                "TransFourCmsnAmt": "TransFourCmsnAmt`double", ## 전달4수수료금액@@
                "OvrsOptXrcRsvTpCode": "OvrsOptXrcRsvTpCode`char", ## 해외옵션행사예약구분코드@@
                "OvrsDrvtOptTpCode": "OvrsDrvtOptTpCode`char", ## 해외파생옵션구분코드@@
                "SprdBaseIsuYn": "SprdBaseIsuYn`char", ## 스프레드기준종목여부@@
                "OvrsDrvtIsuCode2": "OvrsDrvtIsuCode2`char##해외파생종목코드2@@"
            }
        }
    },
    "CIDBQ03000": { ## 해외선물 예수금/잔고현황
        "input": {
            "CIDBQ03000InBlock1": {
                "RecCnt": "0", ## 레코드갯수@@
                "AcntTpCode": " ", ## 계좌구분코드@@
                "AcntNo": " ", ## 계좌번호@@
                "AcntPwd": " ", ## 계좌비밀번호@@
                "TrdDt": " ##거래일자@@"
            }
        },
        "output": {
            "CIDBQ03000OutBlock1": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "AcntTpCode": "AcntTpCode`char", ## 계좌구분코드@@
                "AcntNo": "AcntNo`char", ## 계좌번호@@
                "AcntPwd": "AcntPwd`char", ## 계좌비밀번호@@
                "TrdDt": "TrdDt`char##거래일자@@"
            },
            "CIDBQ03000OutBlock2": {
                "AcntNo": "AcntNo`char", ## 계좌번호@@
                "TrdDt": "TrdDt`char", ## 거래일자@@
                "CrcyObjCode": "CrcyObjCode`char", ## 통화대상코드@@
                "OvrsFutsDps": "OvrsFutsDps`double", ## 해외선물예수금@@
                "CustmMnyioAmt": "CustmMnyioAmt`double", ## 고객입출금금액@@
                "AbrdFutsLqdtPnlAmt": "AbrdFutsLqdtPnlAmt`double", ## 해외선물청산손익금액@@
                "AbrdFutsCmsnAmt": "AbrdFutsCmsnAmt`double", ## 해외선물수수료금액@@
                "PrexchDps": "PrexchDps`double", ## 가환전예수금@@
                "EvalAssetAmt": "EvalAssetAmt`double", ## 평가자산금액@@
                "AbrdFutsCsgnMgn": "AbrdFutsCsgnMgn`double", ## 해외선물위탁증거금액@@
                "AbrdFutsAddMgn": "AbrdFutsAddMgn`double", ## 해외선물추가증거금액@@
                "AbrdFutsWthdwAbleAmt": "AbrdFutsWthdwAbleAmt`double", ## 해외선물인출가능금액@@
                "AbrdFutsOrdAbleAmt": "AbrdFutsOrdAbleAmt`double", ## 해외선물주문가능금액@@
                "AbrdFutsEvalPnlAmt": "AbrdFutsEvalPnlAmt`double", ## 해외선물평가손익금액@@
                "LastSettPnlAmt": "LastSettPnlAmt`double", ## 최종결제손익금액@@
                "OvrsOptSettAmt": "OvrsOptSettAmt`double", ## 해외옵션결제금액@@
                "OvrsOptBalEvalAmt": "OvrsOptBalEvalAmt`double##해외옵션잔고평가금액@@"
            }
        }
    },
    "CIDBQ05300": { ## 해외선물 계좌예탁자산조회
        "input": {
            "CIDBQ05300InBlock1": {
                "RecCnt": "0", ## 레코드갯수@@
                "OvrsAcntTpCode": " ", ## 해외계좌구분코드@@
                "FcmAcntNo": " ", ## FCM계좌번호@@
                "AcntNo": " ", ## 계좌번호@@
                "AcntPwd": " ", ## 계좌비밀번호@@
                "CrcyCode": " ##통화코드@@"
            }
        },
        "output": {
            "CIDBQ05300OutBlock1": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "OvrsAcntTpCode": "OvrsAcntTpCode`char", ## 해외계좌구분코드@@
                "FcmAcntNo": "FcmAcntNo`char", ## FCM계좌번호@@
                "AcntNo": "AcntNo`char", ## 계좌번호@@
                "AcntPwd": "AcntPwd`char", ## 계좌비밀번호@@
                "CrcyCode": "CrcyCode`char##통화코드@@"
            },
            "CIDBQ05300OutBlock2": {
                "AcntNo": "AcntNo`char", ## 계좌번호@@
                "CrcyCode": "CrcyCode`char", ## 통화코드@@
                "OvrsFutsDps": "OvrsFutsDps`double", ## 해외선물예수금@@
                "AbrdFutsCsgnMgn": "AbrdFutsCsgnMgn`double", ## 해외선물위탁증거금액@@
                "OvrsFutsSplmMgn": "OvrsFutsSplmMgn`double", ## 해외선물추가증거금@@
                "CustmLpnlAmt": "CustmLpnlAmt`double", ## 고객청산손익금액@@
                "AbrdFutsEvalPnlAmt": "AbrdFutsEvalPnlAmt`double", ## 해외선물평가손익금액@@
                "AbrdFutsCmsnAmt": "AbrdFutsCmsnAmt`double", ## 해외선물수수료금액@@
                "AbrdFutsEvalDpstgTotAmt": "AbrdFutsEvalDpstgTotAmt`double", ## 해외선물평가예탁총금액@@
                "Xchrat": "Xchrat`double", ## 환율@@
                "FcurrRealMxchgAmt": "FcurrRealMxchgAmt`double", ## 외화실환전금액@@
                "AbrdFutsWthdwAbleAmt": "AbrdFutsWthdwAbleAmt`double", ## 해외선물인출가능금액@@
                "AbrdFutsOrdAbleAmt": "AbrdFutsOrdAbleAmt`double", ## 해외선물주문가능금액@@
                "FutsDueNarrvLqdtPnlAmt": "FutsDueNarrvLqdtPnlAmt`double", ## 선물만기미도래청산손익금액@@
                "FutsDueNarrvCmsn": "FutsDueNarrvCmsn`double", ## 선물만기미도래수수료@@
                "AbrdFutsLqdtPnlAmt": "AbrdFutsLqdtPnlAmt`double", ## 해외선물청산손익금액@@
                "OvrsFutsDueCmsn": "OvrsFutsDueCmsn`double", ## 해외선물만기수수료@@
                "OvrsFutsOptBuyAmt": "OvrsFutsOptBuyAmt`double", ## 해외선물옵션매수금액@@
                "OvrsFutsOptSellAmt": "OvrsFutsOptSellAmt`double", ## 해외선물옵션매도금액@@
                "OptBuyMktWrthAmt": "OptBuyMktWrthAmt`double", ## 옵션매수시장가치금액@@
                "OptSellMktWrthAmt": "OptSellMktWrthAmt`double##옵션매도시장가치금액@@"
            },
            "CIDBQ05300OutBlock3": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "OvrsFutsDps": "OvrsFutsDps`double", ## 해외선물예수금@@
                "AbrdFutsLqdtPnlAmt": "AbrdFutsLqdtPnlAmt`double", ## 해외선물청산손익금액@@
                "FutsDueNarrvLqdtPnlAmt": "FutsDueNarrvLqdtPnlAmt`double", ## 선물만기미도래청산손익금액@@
                "AbrdFutsEvalPnlAmt": "AbrdFutsEvalPnlAmt`double", ## 해외선물평가손익금액@@
                "AbrdFutsEvalDpstgTotAmt": "AbrdFutsEvalDpstgTotAmt`double", ## 해외선물평가예탁총금액@@
                "CustmLpnlAmt": "CustmLpnlAmt`double", ## 고객청산손익금액@@
                "OvrsFutsDueCmsn": "OvrsFutsDueCmsn`double", ## 해외선물만기수수료@@
                "FcurrRealMxchgAmt": "FcurrRealMxchgAmt`double", ## 외화실환전금액@@
                "AbrdFutsCmsnAmt": "AbrdFutsCmsnAmt`double", ## 해외선물수수료금액@@
                "FutsDueNarrvCmsn": "FutsDueNarrvCmsn`double", ## 선물만기미도래수수료@@
                "AbrdFutsCsgnMgn": "AbrdFutsCsgnMgn`double", ## 해외선물위탁증거금액@@
                "OvrsFutsMaintMgn": "OvrsFutsMaintMgn`double", ## 해외선물유지증거금@@
                "OvrsFutsOptBuyAmt": "OvrsFutsOptBuyAmt`double", ## 해외선물옵션매수금액@@
                "OvrsFutsOptSellAmt": "OvrsFutsOptSellAmt`double", ## 해외선물옵션매도금액@@
                "CtlmtAmt": "CtlmtAmt`double", ## 신용한도금액@@
                "OvrsFutsSplmMgn": "OvrsFutsSplmMgn`double", ## 해외선물추가증거금@@
                "MgnclRat": "MgnclRat`double", ## 마진콜율@@
                "AbrdFutsOrdAbleAmt": "AbrdFutsOrdAbleAmt`double", ## 해외선물주문가능금액@@
                "AbrdFutsWthdwAbleAmt": "AbrdFutsWthdwAbleAmt`double", ## 해외선물인출가능금액@@
                "OptBuyMktWrthAmt": "OptBuyMktWrthAmt`double", ## 옵션매수시장가치금액@@
                "OptSellMktWrthAmt": "OptSellMktWrthAmt`double", ## 옵션매도시장가치금액@@
                "OvrsOptSettAmt": "OvrsOptSettAmt`double", ## 해외옵션결제금액@@
                "OvrsOptBalEvalAmt": "OvrsOptBalEvalAmt`double##해외옵션잔고평가금액@@"
            }
        }
    },
    "CIDBT00100": { ## 해외선물신규주문
        "input": {
            "CIDBT00100InBlock1": {
                "RecCnt": "0", ## 레코드갯수@@
                "OrdDt": " ", ## 주문일자@@
                "BrnCode": " ", ## 지점코드@@
                "AcntNo": " ", ## 계좌번호@@
                "Pwd": " ", ## 비밀번호@@
                "IsuCodeVal": " ", ## 종목코드값@@
                "FutsOrdTpCode": " ", ## 선물주문구분코드@@
                "BnsTpCode": " ", ## 매매구분코드@@
                "AbrdFutsOrdPtnCode": " ", ## 해외선물주문유형코드@@
                "CrcyCode": " ", ## 통화코드@@
                "OvrsDrvtOrdPrc": "0.0", ## 해외파생주문가격@@
                "CndiOrdPrc": "0.0", ## 조건주문가격@@
                "OrdQty": "0", ## 주문수량@@
                "PrdtCode": " ", ## 상품코드@@
                "DueYymm": " ", ## 만기년월@@
                "ExchCode": " ##거래소코드@@"
            }
        },
        "output": {
            "CIDBT00100OutBlock1": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "OrdDt": "OrdDt`char", ## 주문일자@@
                "BrnCode": "BrnCode`char", ## 지점코드@@
                "AcntNo": "AcntNo`char", ## 계좌번호@@
                "Pwd": "Pwd`char", ## 비밀번호@@
                "IsuCodeVal": "IsuCodeVal`char", ## 종목코드값@@
                "FutsOrdTpCode": "FutsOrdTpCode`char", ## 선물주문구분코드@@
                "BnsTpCode": "BnsTpCode`char", ## 매매구분코드@@
                "AbrdFutsOrdPtnCode": "AbrdFutsOrdPtnCode`char", ## 해외선물주문유형코드@@
                "CrcyCode": "CrcyCode`char", ## 통화코드@@
                "OvrsDrvtOrdPrc": "OvrsDrvtOrdPrc`double", ## 해외파생주문가격@@
                "CndiOrdPrc": "CndiOrdPrc`double", ## 조건주문가격@@
                "OrdQty": "OrdQty`long", ## 주문수량@@
                "PrdtCode": "PrdtCode`char", ## 상품코드@@
                "DueYymm": "DueYymm`char", ## 만기년월@@
                "ExchCode": "ExchCode`char##거래소코드@@"
            },
            "CIDBT00100OutBlock2": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "AcntNo": "AcntNo`char", ## 계좌번호@@
                "OvrsFutsOrdNo": "OvrsFutsOrdNo`char##해외선물주문번호@@"
            }
        }
    },
    "CIDBT00900": { ## 해외선물정정주문
        "input": {
            "CIDBT00900InBlock1": {
                "RecCnt": "0", ## 레코드갯수@@
                "OrdDt": " ", ## 주문일자@@
                "RegBrnNo": " ", ## 등록지점번호@@
                "AcntNo": " ", ## 계좌번호@@
                "Pwd": " ", ## 비밀번호@@
                "OvrsFutsOrgOrdNo": " ", ## 해외선물원주문번호@@
                "IsuCodeVal": " ", ## 종목코드값@@
                "FutsOrdTpCode": " ", ## 선물주문구분코드@@
                "BnsTpCode": " ", ## 매매구분코드@@
                "FutsOrdPtnCode": " ", ## 선물주문유형코드@@
                "CrcyCodeVal": " ", ## 통화코드값@@
                "OvrsDrvtOrdPrc": "0.0", ## 해외파생주문가격@@
                "CndiOrdPrc": "0.0", ## 조건주문가격@@
                "OrdQty": "0", ## 주문수량@@
                "OvrsDrvtPrdtCode": " ", ## 해외파생상품코드@@
                "DueYymm": " ", ## 만기년월@@
                "ExchCode": " ##거래소코드@@"
            }
        },
        "output": {
            "CIDBT00900OutBlock1": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "OrdDt": "OrdDt`char", ## 주문일자@@
                "RegBrnNo": "RegBrnNo`char", ## 등록지점번호@@
                "AcntNo": "AcntNo`char", ## 계좌번호@@
                "Pwd": "Pwd`char", ## 비밀번호@@
                "OvrsFutsOrgOrdNo": "OvrsFutsOrgOrdNo`char", ## 해외선물원주문번호@@
                "IsuCodeVal": "IsuCodeVal`char", ## 종목코드값@@
                "FutsOrdTpCode": "FutsOrdTpCode`char", ## 선물주문구분코드@@
                "BnsTpCode": "BnsTpCode`char", ## 매매구분코드@@
                "FutsOrdPtnCode": "FutsOrdPtnCode`char", ## 선물주문유형코드@@
                "CrcyCodeVal": "CrcyCodeVal`char", ## 통화코드값@@
                "OvrsDrvtOrdPrc": "OvrsDrvtOrdPrc`double", ## 해외파생주문가격@@
                "CndiOrdPrc": "CndiOrdPrc`double", ## 조건주문가격@@
                "OrdQty": "OrdQty`long", ## 주문수량@@
                "OvrsDrvtPrdtCode": "OvrsDrvtPrdtCode`char", ## 해외파생상품코드@@
                "DueYymm": "DueYymm`char", ## 만기년월@@
                "ExchCode": "ExchCode`char##거래소코드@@"
            },
            "CIDBT00900OutBlock2": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "AcntNo": "AcntNo`char", ## 계좌번호@@
                "OvrsFutsOrdNo": "OvrsFutsOrdNo`char", ## 해외선물주문번호@@
                "InnerMsgCnts": "InnerMsgCnts`char##내부메시지내용@@"
            }
        }
    },
    "CIDBT01000": { ## 해외선물취소주문
        "input": {
            "CIDBT01000InBlock1": {
                "RecCnt": "0", ## 레코드갯수@@
                "OrdDt": " ", ## 주문일자@@
                "BrnNo": " ", ## 지점번호@@
                "AcntNo": " ", ## 계좌번호@@
                "Pwd": " ", ## 비밀번호@@
                "IsuCodeVal": " ", ## 종목코드값@@
                "OvrsFutsOrgOrdNo": " ", ## 해외선물원주문번호@@
                "FutsOrdTpCode": " ", ## 선물주문구분코드@@
                "PrdtTpCode": " ", ## 상품구분코드@@
                "ExchCode": " ##거래소코드@@"
            }
        },
        "output": {
            "CIDBT01000OutBlock1": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "OrdDt": "OrdDt`char", ## 주문일자@@
                "BrnNo": "BrnNo`char", ## 지점번호@@
                "AcntNo": "AcntNo`char", ## 계좌번호@@
                "Pwd": "Pwd`char", ## 비밀번호@@
                "IsuCodeVal": "IsuCodeVal`char", ## 종목코드값@@
                "OvrsFutsOrgOrdNo": "OvrsFutsOrgOrdNo`char", ## 해외선물원주문번호@@
                "FutsOrdTpCode": "FutsOrdTpCode`char", ## 선물주문구분코드@@
                "PrdtTpCode": "PrdtTpCode`char", ## 상품구분코드@@
                "ExchCode": "ExchCode`char##거래소코드@@"
            },
            "CIDBT01000OutBlock2": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "AcntNo": "AcntNo`char", ## 계좌번호@@
                "OvrsFutsOrdNo": "OvrsFutsOrdNo`char", ## 해외선물주문번호@@
                "InnerMsgCnts": "InnerMsgCnts`char##내부메시지내용@@"
            }
        }
    },
    "CIDEQ00800": { ## 일자별 미결제 잔고내역
        "input": {
            "CIDEQ00800InBlock1": {
                "RecCnt": "0", ## 레코드갯수@@
                "AcntNo": " ", ## 계좌번호@@
                "AcntPwd": " ", ## 계좌비밀번호@@
                "TrdDt": " ##거래일자@@"
            }
        },
        "output": {
            "CIDEQ00800OutBlock1": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "AcntNo": "AcntNo`char", ## 계좌번호@@
                "AcntPwd": "AcntPwd`char", ## 계좌비밀번호@@
                "TrdDt": "TrdDt`char##거래일자@@"
            },
            "CIDEQ00800OutBlock2": {
                "AcntNo": "AcntNo`char", ## 계좌번호@@
                "TrdDt": "TrdDt`char", ## 거래일자@@
                "IsuCodeVal": "IsuCodeVal`char", ## 종목코드값@@
                "BnsTpNm": "BnsTpNm`char", ## 매매구분명@@
                "BalQty": "BalQty`long", ## 잔고수량@@
                "LqdtAbleQty": "LqdtAbleQty`long", ## 청산가능수량@@
                "PchsPrc": "PchsPrc`double", ## 매입가격@@
                "OvrsDrvtNowPrc": "OvrsDrvtNowPrc`double", ## 해외파생현재가@@
                "AbrdFutsEvalPnlAmt": "AbrdFutsEvalPnlAmt`double", ## 해외선물평가손익금액@@
                "CustmBalAmt": "CustmBalAmt`double", ## 고객잔고금액@@
                "FcurrEvalAmt": "FcurrEvalAmt`double", ## 외화평가금액@@
                "IsuNm": "IsuNm`char", ## 종목명@@
                "CrcyCodeVal": "CrcyCodeVal`char", ## 통화코드값@@
                "OvrsDrvtPrdtCode": "OvrsDrvtPrdtCode`char", ## 해외파생상품코드@@
                "DueDt": "DueDt`char", ## 만기일자@@
                "PrcntrAmt": "PrcntrAmt`double", ## 계약당금액@@
                "FcurrEvalPnlAmt": "FcurrEvalPnlAmt`double##외화평가손익금액@@"
            }
        }
    },
    "CLNAQ00100": { ## 예탁담보융자가능종목현황조회
        "input": {
            "CLNAQ00100InBlock1": {
                "RecCnt": "0", ## 레코드갯수@@
                "QryTp": " ", ## 조회구분@@
                "IsuNo": " ", ## 종목번호@@
                "SecTpCode": " ", ## 유가증권구분@@
                "LoanIntrstGrdCode": " ", ## 대출이자등급코드@@
                "LoanTp": " ##대출구분@@"
            }
        },
        "output": {
            "CLNAQ00100OutBlock1": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "QryTp": "QryTp`char", ## 조회구분@@
                "IsuNo": "IsuNo`char", ## 종목번호@@
                "SecTpCode": "SecTpCode`char", ## 유가증권구분@@
                "LoanIntrstGrdCode": "LoanIntrstGrdCode`char", ## 대출이자등급코드@@
                "LoanTp": "LoanTp`char##대출구분@@"
            },
            "CLNAQ00100OutBlock2": {
                "IsuNo": "IsuNo`char", ## 종목번호@@
                "IsuNm": "IsuNm`char", ## 종목명@@
                "Parprc": "Parprc`double", ## 액면가@@
                "PrdayCprc": "PrdayCprc`double", ## 전일종가@@
                "RatVal": "RatVal`double", ## 비율값@@
                "SubstPrc": "SubstPrc`double", ## 대용가@@
                "RegTpNm": "RegTpNm`char", ## 등록구분@@
                "SpotMgnLevyClssNm": "SpotMgnLevyClssNm`char", ## 현물증거금징수분류명@@
                "FnoTrdStopRsnCnts": "FnoTrdStopRsnCnts`char", ## 거래정지사유@@
                "DgrsPtnNm": "DgrsPtnNm`char", ## 요주의유형명@@
                "AcdPtnNm": "AcdPtnNm`char", ## 사고유형@@
                "MktTpNm": "MktTpNm`char", ## 시장구분@@
                "LmtVal": "LmtVal`long", ## 한도값@@
                "AcntLmtVal": "AcntLmtVal`long", ## 계좌한도값@@
                "LoanGrdCode": "LoanGrdCode`char", ## 대출등급코드@@
                "LoanAmt": "LoanAmt`long", ## 대출금액@@
                "LoanAbleRat": "LoanAbleRat`double", ## 대출가능율@@
                "LoanIntrat1": "LoanIntrat1`double", ## 대출이율1@@
                "RegPsnId": "RegPsnId`char", ## 등록자ID@@
                "Rat01": "Rat01`double", ## 비율값@@
                "Rat02": "Rat02`double##비율값@@"
            },
            "CLNAQ00100OutBlock3": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "LrgMnyoutSumAmt": "LrgMnyoutSumAmt`long##대출금합계금액@@"
            }
        }
    },
    "CSPAQ00600": { ## 계좌별신용한도조회
        "input": {
            "CSPAQ00600InBlock1": {
                "RecCnt": "0", ## 레코드갯수@@
                "AcntNo": " ", ## 계좌번호@@
                "InptPwd": " ", ## 입력비밀번호@@
                "LoanDtlClssCode": " ", ## 대출상세분류코드@@
                "IsuNo": " ", ## 종목번호@@
                "OrdPrc": "0.0", ## 주문가@@
                "CommdaCode": " ##통신매체코드@@"
            }
        },
        "output": {
            "CSPAQ00600OutBlock1": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "AcntNo": "AcntNo`char", ## 계좌번호@@
                "InptPwd": "InptPwd`char", ## 입력비밀번호@@
                "LoanDtlClssCode": "LoanDtlClssCode`char", ## 대출상세분류코드@@
                "IsuNo": "IsuNo`char", ## 종목번호@@
                "OrdPrc": "OrdPrc`double", ## 주문가@@
                "CommdaCode": "CommdaCode`char##통신매체코드@@"
            },
            "CSPAQ00600OutBlock2": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "AcntNm": "AcntNm`char", ## 계좌명@@
                "OrdPrc": "OrdPrc`double", ## 주문가@@
                "SloanLmtAmt": "SloanLmtAmt`long", ## 대주한도@@
                "SloanAmtSum": "SloanAmtSum`long", ## 대주금액합계@@
                "SloanNewAmt": "SloanNewAmt`long", ## 대주신규금액@@
                "SloanRfundAmt": "SloanRfundAmt`long", ## 대주상환금액@@
                "MktcplMloanLmtAmt": "MktcplMloanLmtAmt`long", ## 유통융자한도금액@@
                "MktcplMloanAmtSum": "MktcplMloanAmtSum`long", ## 유통융자금액합계@@
                "MktcplMloanNewAmt": "MktcplMloanNewAmt`long", ## 유통융자신규금액@@
                "MktcplMloanRfundAmt": "MktcplMloanRfundAmt`long", ## 유통융자상환금액@@
                "SfaccMloanLmtAmt": "SfaccMloanLmtAmt`long", ## 자기융자한도금액@@
                "SfaccMloanAmtSum": "SfaccMloanAmtSum`long", ## 자기융자금액합계@@
                "SfaccMloanNewAmt": "SfaccMloanNewAmt`long", ## 자기융자신규금액@@
                "SfaccMloanRfundAmt": "SfaccMloanRfundAmt`long", ## 자기융자상환금액@@
                "BrnMktcplMloanLmtAmt": "BrnMktcplMloanLmtAmt`long", ## 지점유통융자한도금액@@
                "BrnMktcplMloanNewAmt": "BrnMktcplMloanNewAmt`long", ## 지점유통융자신규금액@@
                "BrnMktcplMloanRfundAmt": "BrnMktcplMloanRfundAmt`long", ## 지점유통융자상환금액@@
                "BrnMktcplMloanUseAmt": "BrnMktcplMloanUseAmt`long", ## 지점유통융자사용금액@@
                "BrnSfaccMloanLmtAmt": "BrnSfaccMloanLmtAmt`long", ## 지점자기융자한도금액@@
                "BrnSfaccMloanNewAmt": "BrnSfaccMloanNewAmt`long", ## 지점자기융자신규금액@@
                "BrnSfaccMloanRfundAmt": "BrnSfaccMloanRfundAmt`long", ## 지점자기융자상환금액@@
                "BrnSfaccMloanUseAmt": "BrnSfaccMloanUseAmt`long", ## 지점자기융자사용금액@@
                "FirmMloanLmtMgmtYn": "FirmMloanLmtMgmtYn`char", ## 이용사융자한도관리여부@@
                "FirmCrdtIsuRestrcTp": "FirmCrdtIsuRestrcTp`char", ## 이용사신용종목제한구분@@
                "PldgMaintRat": "PldgMaintRat`double", ## 담보유지비율@@
                "FirmNm": "FirmNm`char", ## 이용사명@@
                "PldgRat": "PldgRat`double", ## 담보비율@@
                "DpsastSum": "DpsastSum`long", ## 예탁자산합계@@
                "LmtChgAbleAmt": "LmtChgAbleAmt`long", ## 한도변경가능금액@@
                "OrdAbleAmt": "OrdAbleAmt`long", ## 주문가능금액@@
                "OrdAbleQty": "OrdAbleQty`long", ## 주문가능수량@@
                "RcvblUablOrdAbleQty": "RcvblUablOrdAbleQty`long##미수불가주문가능수량@@"
            }
        }
    },
    "CSPAQ12200": { ## 현물계좌예수금 주문가능금액 총평가 조회
        "input": {
            "CSPAQ12200InBlock1": {
                "RecCnt": "0", ## 레코드갯수@@
                "MgmtBrnNo": " ", ## 관리지점번호@@
                "AcntNo": " ", ## 계좌번호@@
                "Pwd": " ", ## 비밀번호@@
                "BalCreTp": " ##잔고생성구분@@"
            }
        },
        "output": {
            "CSPAQ12200OutBlock1": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "MgmtBrnNo": "MgmtBrnNo`char", ## 관리지점번호@@
                "AcntNo": "AcntNo`char", ## 계좌번호@@
                "Pwd": "Pwd`char", ## 비밀번호@@
                "BalCreTp": "BalCreTp`char##잔고생성구분@@"
            },
            "CSPAQ12200OutBlock2": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "BrnNm": "BrnNm`char", ## 지점명@@
                "AcntNm": "AcntNm`char", ## 계좌명@@
                "MnyOrdAbleAmt": "MnyOrdAbleAmt`long", ## 현금주문가능금액@@
                "MnyoutAbleAmt": "MnyoutAbleAmt`long", ## 출금가능금액@@
                "SeOrdAbleAmt": "SeOrdAbleAmt`long", ## 거래소금액@@
                "KdqOrdAbleAmt": "KdqOrdAbleAmt`long", ## 코스닥금액@@
                "BalEvalAmt": "BalEvalAmt`long", ## 잔고평가금액@@
                "RcvblAmt": "RcvblAmt`long", ## 미수금액@@
                "DpsastTotamt": "DpsastTotamt`long", ## 예탁자산총액@@
                "PnlRat": "PnlRat`double", ## 손익율@@
                "InvstOrgAmt": "InvstOrgAmt`long", ## 투자원금@@
                "InvstPlAmt": "InvstPlAmt`long", ## 투자손익금액@@
                "CrdtPldgOrdAmt": "CrdtPldgOrdAmt`long", ## 신용담보주문금액@@
                "Dps": "Dps`long", ## 예수금@@
                "SubstAmt": "SubstAmt`long", ## 대용금액@@
                "D1Dps": "D1Dps`long", ## D1예수금@@
                "D2Dps": "D2Dps`long", ## D2예수금@@
                "MnyrclAmt": "MnyrclAmt`long", ## 현금미수금액@@
                "MgnMny": "MgnMny`long", ## 증거금현금@@
                "MgnSubst": "MgnSubst`long", ## 증거금대용@@
                "ChckAmt": "ChckAmt`long", ## 수표금액@@
                "SubstOrdAbleAmt": "SubstOrdAbleAmt`long", ## 대용주문가능금액@@
                "MgnRat100pctOrdAbleAmt": "MgnRat100pctOrdAbleAmt`long", ## 증거금률100퍼센트주문가능금액@@
                "MgnRat35ordAbleAmt": "MgnRat35ordAbleAmt`long", ## 증거금률35%주문가능금액@@
                "MgnRat50ordAbleAmt": "MgnRat50ordAbleAmt`long", ## 증거금률50%주문가능금액@@
                "PrdaySellAdjstAmt": "PrdaySellAdjstAmt`long", ## 전일매도정산금액@@
                "PrdayBuyAdjstAmt": "PrdayBuyAdjstAmt`long", ## 전일매수정산금액@@
                "CrdaySellAdjstAmt": "CrdaySellAdjstAmt`long", ## 금일매도정산금액@@
                "CrdayBuyAdjstAmt": "CrdayBuyAdjstAmt`long", ## 금일매수정산금액@@
                "D1ovdRepayRqrdAmt": "D1ovdRepayRqrdAmt`long", ## D1연체변제소요금액@@
                "D2ovdRepayRqrdAmt": "D2ovdRepayRqrdAmt`long", ## D2연체변제소요금액@@
                "D1PrsmptWthdwAbleAmt": "D1PrsmptWthdwAbleAmt`long", ## D1추정인출가능금액@@
                "D2PrsmptWthdwAbleAmt": "D2PrsmptWthdwAbleAmt`long", ## D2추정인출가능금액@@
                "DpspdgLoanAmt": "DpspdgLoanAmt`long", ## 예탁담보대출금액@@
                "Imreq": "Imreq`long", ## 신용설정보증금@@
                "MloanAmt": "MloanAmt`long", ## 융자금액@@
                "ChgAfPldgRat": "ChgAfPldgRat`double", ## 변경후담보비율@@
                "OrgPldgAmt": "OrgPldgAmt`long", ## 원담보금액@@
                "SubPldgAmt": "SubPldgAmt`long", ## 부담보금액@@
                "RqrdPldgAmt": "RqrdPldgAmt`long", ## 소요담보금액@@
                "OrgPdlckAmt": "OrgPdlckAmt`long", ## 원담보부족금액@@
                "PdlckAmt": "PdlckAmt`long", ## 담보부족금액@@
                "AddPldgMny": "AddPldgMny`long", ## 추가담보현금@@
                "D1OrdAbleAmt": "D1OrdAbleAmt`long", ## D1주문가능금액@@
                "CrdtIntdltAmt": "CrdtIntdltAmt`long", ## 신용이자미납금액@@
                "EtclndAmt": "EtclndAmt`long", ## 기타대여금액@@
                "NtdayPrsmptCvrgAmt": "NtdayPrsmptCvrgAmt`long", ## 익일추정반대매매금액@@
                "OrgPldgSumAmt": "OrgPldgSumAmt`long", ## 원담보합계금액@@
                "CrdtOrdAbleAmt": "CrdtOrdAbleAmt`long", ## 신용주문가능금액@@
                "SubPldgSumAmt": "SubPldgSumAmt`long", ## 부담보합계금액@@
                "CrdtPldgAmtMny": "CrdtPldgAmtMny`long", ## 신용담보금현금@@
                "CrdtPldgSubstAmt": "CrdtPldgSubstAmt`long", ## 신용담보대용금액@@
                "AddCrdtPldgMny": "AddCrdtPldgMny`long", ## 추가신용담보현금@@
                "CrdtPldgRuseAmt": "CrdtPldgRuseAmt`long", ## 신용담보재사용금액@@
                "AddCrdtPldgSubst": "AddCrdtPldgSubst`long", ## 추가신용담보대용@@
                "CslLoanAmtdt1": "CslLoanAmtdt1`long", ## 매도대금담보대출금액@@
                "DpslRestrcAmt": "DpslRestrcAmt`long##처분제한금액@@"
            }
        }
    },
    "CSPAQ12300": { ## BEP단가조회
        "input": {
            "CSPAQ12300InBlock1": {
                "RecCnt": "0", ## 레코드갯수@@
                "AcntNo": " ", ## 계좌번호@@
                "Pwd": " ", ## 비밀번호@@
                "BalCreTp": " ", ## 잔고생성구분@@
                "CmsnAppTpCode": " ", ## 수수료적용구분@@
                "D2balBaseQryTp": " ", ## D2잔고기준조회구분@@
                "UprcTpCode": " ##단가구분@@"
            }
        },
        "output": {
            "CSPAQ12300OutBlock1": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "AcntNo": "AcntNo`char", ## 계좌번호@@
                "Pwd": "Pwd`char", ## 비밀번호@@
                "BalCreTp": "BalCreTp`char", ## 잔고생성구분@@
                "CmsnAppTpCode": "CmsnAppTpCode`char", ## 수수료적용구분@@
                "D2balBaseQryTp": "D2balBaseQryTp`char", ## D2잔고기준조회구분@@
                "UprcTpCode": "UprcTpCode`char##단가구분@@"
            },
            "CSPAQ12300OutBlock2": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "BrnNm": "BrnNm`char", ## 지점명@@
                "AcntNm": "AcntNm`char", ## 계좌명@@
                "MnyOrdAbleAmt": "MnyOrdAbleAmt`long", ## 현금주문가능금액@@
                "MnyoutAbleAmt": "MnyoutAbleAmt`long", ## 출금가능금액@@
                "SeOrdAbleAmt": "SeOrdAbleAmt`long", ## 거래소금액@@
                "KdqOrdAbleAmt": "KdqOrdAbleAmt`long", ## 코스닥금액@@
                "HtsOrdAbleAmt": "HtsOrdAbleAmt`long", ## HTS주문가능금액@@
                "MgnRat100pctOrdAbleAmt": "MgnRat100pctOrdAbleAmt`long", ## 증거금률100퍼센트주문가능금액@@
                "BalEvalAmt": "BalEvalAmt`long", ## 잔고평가금액@@
                "PchsAmt": "PchsAmt`long", ## 매입금액@@
                "RcvblAmt": "RcvblAmt`long", ## 미수금액@@
                "PnlRat": "PnlRat`double", ## 손익율@@
                "InvstOrgAmt": "InvstOrgAmt`long", ## 투자원금@@
                "InvstPlAmt": "InvstPlAmt`long", ## 투자손익금액@@
                "CrdtPldgOrdAmt": "CrdtPldgOrdAmt`long", ## 신용담보주문금액@@
                "Dps": "Dps`long", ## 예수금@@
                "D1Dps": "D1Dps`long", ## D1예수금@@
                "D2Dps": "D2Dps`long", ## D2예수금@@
                "OrdDt": "OrdDt`char", ## 주문일@@
                "MnyMgn": "MnyMgn`long", ## 현금증거금액@@
                "SubstMgn": "SubstMgn`long", ## 대용증거금액@@
                "SubstAmt": "SubstAmt`long", ## 대용금액@@
                "PrdayBuyExecAmt": "PrdayBuyExecAmt`long", ## 전일매수체결금액@@
                "PrdaySellExecAmt": "PrdaySellExecAmt`long", ## 전일매도체결금액@@
                "CrdayBuyExecAmt": "CrdayBuyExecAmt`long", ## 금일매수체결금액@@
                "CrdaySellExecAmt": "CrdaySellExecAmt`long", ## 금일매도체결금액@@
                "EvalPnlSum": "EvalPnlSum`long", ## 평가손익합계@@
                "DpsastTotamt": "DpsastTotamt`long", ## 예탁자산총액@@
                "Evrprc": "Evrprc`long", ## 제비용@@
                "RuseAmt": "RuseAmt`long", ## 재사용금액@@
                "EtclndAmt": "EtclndAmt`long", ## 기타대여금액@@
                "PrcAdjstAmt": "PrcAdjstAmt`long", ## 가정산금액@@
                "D1CmsnAmt": "D1CmsnAmt`long", ## D1수수료@@
                "D2CmsnAmt": "D2CmsnAmt`long", ## D2수수료@@
                "D1EvrTax": "D1EvrTax`long", ## D1제세금@@
                "D2EvrTax": "D2EvrTax`long", ## D2제세금@@
                "D1SettPrergAmt": "D1SettPrergAmt`long", ## D1결제예정금액@@
                "D2SettPrergAmt": "D2SettPrergAmt`long", ## D2결제예정금액@@
                "PrdayKseMnyMgn": "PrdayKseMnyMgn`long", ## 전일KSE현금증거금@@
                "PrdayKseSubstMgn": "PrdayKseSubstMgn`long", ## 전일KSE대용증거금@@
                "PrdayKseCrdtMnyMgn": "PrdayKseCrdtMnyMgn`long", ## 전일KSE신용현금증거금@@
                "PrdayKseCrdtSubstMgn": "PrdayKseCrdtSubstMgn`long", ## 전일KSE신용대용증거금@@
                "CrdayKseMnyMgn": "CrdayKseMnyMgn`long", ## 금일KSE현금증거금@@
                "CrdayKseSubstMgn": "CrdayKseSubstMgn`long", ## 금일KSE대용증거금@@
                "CrdayKseCrdtMnyMgn": "CrdayKseCrdtMnyMgn`long", ## 금일KSE신용현금증거금@@
                "CrdayKseCrdtSubstMgn": "CrdayKseCrdtSubstMgn`long", ## 금일KSE신용대용증거금@@
                "PrdayKdqMnyMgn": "PrdayKdqMnyMgn`long", ## 전일코스닥현금증거금@@
                "PrdayKdqSubstMgn": "PrdayKdqSubstMgn`long", ## 전일코스닥대용증거금@@
                "PrdayKdqCrdtMnyMgn": "PrdayKdqCrdtMnyMgn`long", ## 전일코스닥신용현금증거금@@
                "PrdayKdqCrdtSubstMgn": "PrdayKdqCrdtSubstMgn`long", ## 전일코스닥신용대용증거금@@
                "CrdayKdqMnyMgn": "CrdayKdqMnyMgn`long", ## 금일코스닥현금증거금@@
                "CrdayKdqSubstMgn": "CrdayKdqSubstMgn`long", ## 금일코스닥대용증거금@@
                "CrdayKdqCrdtMnyMgn": "CrdayKdqCrdtMnyMgn`long", ## 금일코스닥신용현금증거금@@
                "CrdayKdqCrdtSubstMgn": "CrdayKdqCrdtSubstMgn`long", ## 금일코스닥신용대용증거금@@
                "PrdayFrbrdMnyMgn": "PrdayFrbrdMnyMgn`long", ## 전일프리보드현금증거금@@
                "PrdayFrbrdSubstMgn": "PrdayFrbrdSubstMgn`long", ## 전일프리보드대용증거금@@
                "CrdayFrbrdMnyMgn": "CrdayFrbrdMnyMgn`long", ## 금일프리보드현금증거금@@
                "CrdayFrbrdSubstMgn": "CrdayFrbrdSubstMgn`long", ## 금일프리보드대용증거금@@
                "PrdayCrbmkMnyMgn": "PrdayCrbmkMnyMgn`long", ## 전일장외현금증거금@@
                "PrdayCrbmkSubstMgn": "PrdayCrbmkSubstMgn`long", ## 전일장외대용증거금@@
                "CrdayCrbmkMnyMgn": "CrdayCrbmkMnyMgn`long", ## 금일장외현금증거금@@
                "CrdayCrbmkSubstMgn": "CrdayCrbmkSubstMgn`long", ## 금일장외대용증거금@@
                "DpspdgQty": "DpspdgQty`long", ## 예탁담보수량@@
                "BuyAdjstAmtD2": "BuyAdjstAmtD2`long", ## 매수정산금(D+2)@@
                "SellAdjstAmtD2": "SellAdjstAmtD2`long", ## 매도정산금(D+2)@@
                "RepayRqrdAmtD1": "RepayRqrdAmtD1`long", ## 변제소요금(D+1)@@
                "RepayRqrdAmtD2": "RepayRqrdAmtD2`long", ## 변제소요금(D+2)@@
                "LoanAmt": "LoanAmt`long##대출금액@@"
            },
            "CSPAQ12300OutBlock3": {
                "IsuNo": "IsuNo`char", ## 종목번호@@
                "IsuNm": "IsuNm`char", ## 종목명@@
                "SecBalPtnCode": "SecBalPtnCode`char", ## 유가증권잔고유형코드@@
                "SecBalPtnNm": "SecBalPtnNm`char", ## 유가증권잔고유형명@@
                "BalQty": "BalQty`long", ## 잔고수량@@
                "BnsBaseBalQty": "BnsBaseBalQty`long", ## 매매기준잔고수량@@
                "CrdayBuyExecQty": "CrdayBuyExecQty`long", ## 금일매수체결수량@@
                "CrdaySellExecQty": "CrdaySellExecQty`long", ## 금일매도체결수량@@
                "SellPrc": "SellPrc`double", ## 매도가@@
                "BuyPrc": "BuyPrc`double", ## 매수가@@
                "SellPnlAmt": "SellPnlAmt`long", ## 매도손익금액@@
                "PnlRat": "PnlRat`double", ## 손익율@@
                "NowPrc": "NowPrc`double", ## 현재가@@
                "CrdtAmt": "CrdtAmt`long", ## 신용금액@@
                "DueDt": "DueDt`char", ## 만기일@@
                "PrdaySellExecPrc": "PrdaySellExecPrc`double", ## 전일매도체결가@@
                "PrdaySellQty": "PrdaySellQty`long", ## 전일매도수량@@
                "PrdayBuyExecPrc": "PrdayBuyExecPrc`double", ## 전일매수체결가@@
                "PrdayBuyQty": "PrdayBuyQty`long", ## 전일매수수량@@
                "LoanDt": "LoanDt`char", ## 대출일@@
                "AvrUprc": "AvrUprc`double", ## 평균단가@@
                "SellAbleQty": "SellAbleQty`long", ## 매도가능수량@@
                "SellOrdQty": "SellOrdQty`long", ## 매도주문수량@@
                "CrdayBuyExecAmt": "CrdayBuyExecAmt`long", ## 금일매수체결금액@@
                "CrdaySellExecAmt": "CrdaySellExecAmt`long", ## 금일매도체결금액@@
                "PrdayBuyExecAmt": "PrdayBuyExecAmt`long", ## 전일매수체결금액@@
                "PrdaySellExecAmt": "PrdaySellExecAmt`long", ## 전일매도체결금액@@
                "BalEvalAmt": "BalEvalAmt`long", ## 잔고평가금액@@
                "EvalPnl": "EvalPnl`long", ## 평가손익@@
                "MnyOrdAbleAmt": "MnyOrdAbleAmt`long", ## 현금주문가능금액@@
                "OrdAbleAmt": "OrdAbleAmt`long", ## 주문가능금액@@
                "SellUnercQty": "SellUnercQty`long", ## 매도미체결수량@@
                "SellUnsttQty": "SellUnsttQty`long", ## 매도미결제수량@@
                "BuyUnercQty": "BuyUnercQty`long", ## 매수미체결수량@@
                "BuyUnsttQty": "BuyUnsttQty`long", ## 매수미결제수량@@
                "UnsttQty": "UnsttQty`long", ## 미결제수량@@
                "UnercQty": "UnercQty`long", ## 미체결수량@@
                "PrdayCprc": "PrdayCprc`double", ## 전일종가@@
                "PchsAmt": "PchsAmt`long", ## 매입금액@@
                "RegMktCode": "RegMktCode`char", ## 등록시장코드@@
                "LoanDtlClssCode": "LoanDtlClssCode`char", ## 대출상세분류코드@@
                "DpspdgLoanQty": "DpspdgLoanQty`long##예탁담보대출수량@@"
            }
        }
    },
    "CSPAQ13700": { ## 현물계좌주문체결내역조회
        "input": {
            "CSPAQ13700InBlock1": {
                "RecCnt": "0", ## 레코드갯수@@
                "AcntNo": " ", ## 계좌번호@@
                "InptPwd": " ", ## 입력비밀번호@@
                "OrdMktCode": " ", ## 주문시장코드@@
                "BnsTpCode": " ", ## 매매구분@@
                "IsuNo": " ", ## 종목번호@@
                "ExecYn": " ", ## 체결여부@@
                "OrdDt": " ", ## 주문일@@
                "SrtOrdNo2": "0", ## 시작주문번호2@@
                "BkseqTpCode": " ", ## 역순구분@@
                "OrdPtnCode": " ##주문유형코드@@"
            }
        },
        "output": {
            "CSPAQ13700OutBlock1": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "AcntNo": "AcntNo`char", ## 계좌번호@@
                "InptPwd": "InptPwd`char", ## 입력비밀번호@@
                "OrdMktCode": "OrdMktCode`char", ## 주문시장코드@@
                "BnsTpCode": "BnsTpCode`char", ## 매매구분@@
                "IsuNo": "IsuNo`char", ## 종목번호@@
                "ExecYn": "ExecYn`char", ## 체결여부@@
                "OrdDt": "OrdDt`char", ## 주문일@@
                "SrtOrdNo2": "SrtOrdNo2`long", ## 시작주문번호2@@
                "BkseqTpCode": "BkseqTpCode`char", ## 역순구분@@
                "OrdPtnCode": "OrdPtnCode`char##주문유형코드@@"
            },
            "CSPAQ13700OutBlock2": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "SellExecAmt": "SellExecAmt`long", ## 매도체결금액@@
                "BuyExecAmt": "BuyExecAmt`long", ## 매수체결금액@@
                "SellExecQty": "SellExecQty`long", ## 매도체결수량@@
                "BuyExecQty": "BuyExecQty`long", ## 매수체결수량@@
                "SellOrdQty": "SellOrdQty`long", ## 매도주문수량@@
                "BuyOrdQty": "BuyOrdQty`long##매수주문수량@@"
            },
            "CSPAQ13700OutBlock3": {
                "OrdDt": "OrdDt`char", ## 주문일@@
                "MgmtBrnNo": "MgmtBrnNo`char", ## 관리지점번호@@
                "OrdMktCode": "OrdMktCode`char", ## 주문시장코드@@
                "OrdNo": "OrdNo`long", ## 주문번호@@
                "OrgOrdNo": "OrgOrdNo`long", ## 원주문번호@@
                "IsuNo": "IsuNo`char", ## 종목번호@@
                "IsuNm": "IsuNm`char", ## 종목명@@
                "BnsTpCode": "BnsTpCode`char", ## 매매구분@@
                "BnsTpNm": "BnsTpNm`char", ## 매매구분@@
                "OrdPtnCode": "OrdPtnCode`char", ## 주문유형코드@@
                "OrdPtnNm": "OrdPtnNm`char", ## 주문유형명@@
                "OrdTrxPtnCode": "OrdTrxPtnCode`long", ## 주문처리유형코드@@
                "OrdTrxPtnNm": "OrdTrxPtnNm`char", ## 주문처리유형명@@
                "MrcTpCode": "MrcTpCode`char", ## 정정취소구분@@
                "MrcTpNm": "MrcTpNm`char", ## 정정취소구분명@@
                "MrcQty": "MrcQty`long", ## 정정취소수량@@
                "MrcAbleQty": "MrcAbleQty`long", ## 정정취소가능수량@@
                "OrdQty": "OrdQty`long", ## 주문수량@@
                "OrdPrc": "OrdPrc`double", ## 주문가격@@
                "ExecQty": "ExecQty`long", ## 체결수량@@
                "ExecPrc": "ExecPrc`double", ## 체결가@@
                "ExecTrxTime": "ExecTrxTime`char", ## 체결처리시각@@
                "LastExecTime": "LastExecTime`char", ## 최종체결시각@@
                "OrdprcPtnCode": "OrdprcPtnCode`char", ## 호가유형코드@@
                "OrdprcPtnNm": "OrdprcPtnNm`char", ## 호가유형명@@
                "OrdCndiTpCode": "OrdCndiTpCode`char", ## 주문조건구분@@
                "AllExecQty": "AllExecQty`long", ## 전체체결수량@@
                "RegCommdaCode": "RegCommdaCode`char", ## 통신매체코드@@
                "CommdaNm": "CommdaNm`char", ## 통신매체명@@
                "MbrNo": "MbrNo`char", ## 회원번호@@
                "RsvOrdYn": "RsvOrdYn`char", ## 예약주문여부@@
                "LoanDt": "LoanDt`char", ## 대출일@@
                "OrdTime": "OrdTime`char", ## 주문시각@@
                "OpDrtnNo": "OpDrtnNo`char", ## 운용지시번호@@
                "OdrrId": "OdrrId`char##주문자ID@@"
            }
        }
    },
    "CSPAQ22200": { ## 현물계좌예수금 주문가능금액 총평가2
        "input": {
            "CSPAQ22200InBlock1": {
                "RecCnt": "0", ## 레코드갯수@@
                "MgmtBrnNo": " ", ## 관리지점번호@@
                "AcntNo": " ", ## 계좌번호@@
                "Pwd": " ", ## 비밀번호@@
                "BalCreTp": " ##잔고생성구분@@"
            }
        },
        "output": {
            "CSPAQ22200OutBlock1": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "MgmtBrnNo": "MgmtBrnNo`char", ## 관리지점번호@@
                "AcntNo": "AcntNo`char", ## 계좌번호@@
                "Pwd": "Pwd`char", ## 비밀번호@@
                "BalCreTp": "BalCreTp`char##잔고생성구분@@"
            },
            "CSPAQ22200OutBlock2": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "BrnNm": "BrnNm`char", ## 지점명@@
                "AcntNm": "AcntNm`char", ## 계좌명@@
                "MnyOrdAbleAmt": "MnyOrdAbleAmt`long", ## 현금주문가능금액@@
                "SubstOrdAbleAmt": "SubstOrdAbleAmt`long", ## 대용주문가능금액@@
                "SeOrdAbleAmt": "SeOrdAbleAmt`long", ## 거래소금액@@
                "KdqOrdAbleAmt": "KdqOrdAbleAmt`long", ## 코스닥금액@@
                "CrdtPldgOrdAmt": "CrdtPldgOrdAmt`long", ## 신용담보주문금액@@
                "MgnRat100pctOrdAbleAmt": "MgnRat100pctOrdAbleAmt`long", ## 증거금률100퍼센트주문가능금액@@
                "MgnRat35ordAbleAmt": "MgnRat35ordAbleAmt`long", ## 증거금률35%주문가능금액@@
                "MgnRat50ordAbleAmt": "MgnRat50ordAbleAmt`long", ## 증거금률50%주문가능금액@@
                "CrdtOrdAbleAmt": "CrdtOrdAbleAmt`long", ## 신용주문가능금액@@
                "Dps": "Dps`long", ## 예수금@@
                "SubstAmt": "SubstAmt`long", ## 대용금액@@
                "MgnMny": "MgnMny`long", ## 증거금현금@@
                "MgnSubst": "MgnSubst`long", ## 증거금대용@@
                "D1Dps": "D1Dps`long", ## D1예수금@@
                "D2Dps": "D2Dps`long", ## D2예수금@@
                "RcvblAmt": "RcvblAmt`long", ## 미수금액@@
                "D1ovdRepayRqrdAmt": "D1ovdRepayRqrdAmt`long", ## D1연체변제소요금액@@
                "D2ovdRepayRqrdAmt": "D2ovdRepayRqrdAmt`long", ## D2연체변제소요금액@@
                "MloanAmt": "MloanAmt`long", ## 융자금액@@
                "ChgAfPldgRat": "ChgAfPldgRat`double", ## 변경후담보비율@@
                "RqrdPldgAmt": "RqrdPldgAmt`long", ## 소요담보금액@@
                "PdlckAmt": "PdlckAmt`long", ## 담보부족금액@@
                "OrgPldgSumAmt": "OrgPldgSumAmt`long", ## 원담보합계금액@@
                "SubPldgSumAmt": "SubPldgSumAmt`long", ## 부담보합계금액@@
                "CrdtPldgAmtMny": "CrdtPldgAmtMny`long", ## 신용담보금현금@@
                "CrdtPldgSubstAmt": "CrdtPldgSubstAmt`long", ## 신용담보대용금액@@
                "Imreq": "Imreq`long", ## 신용설정보증금@@
                "CrdtPldgRuseAmt": "CrdtPldgRuseAmt`long", ## 신용담보재사용금액@@
                "DpslRestrcAmt": "DpslRestrcAmt`long", ## 처분제한금액@@
                "PrdaySellAdjstAmt": "PrdaySellAdjstAmt`long", ## 전일매도정산금액@@
                "PrdayBuyAdjstAmt": "PrdayBuyAdjstAmt`long", ## 전일매수정산금액@@
                "CrdaySellAdjstAmt": "CrdaySellAdjstAmt`long", ## 금일매도정산금액@@
                "CrdayBuyAdjstAmt": "CrdayBuyAdjstAmt`long", ## 금일매수정산금액@@
                "CslLoanAmtdt1": "CslLoanAmtdt1`long##매도대금담보대출금액@@"
            }
        }
    },
    "CSPAT00600": { ## 현물주문
        "input": {
            "CSPAT00600InBlock1": {
                "AcntNo": " ", ## 계좌번호@@
                "InptPwd": " ", ## 입력비밀번호@@
                "IsuNo": " ", ## 종목번호@@
                "OrdQty": "0", ## 주문수량@@
                "OrdPrc": "0.0", ## 주문가@@
                "BnsTpCode": " ", ## 매매구분@@
                "OrdprcPtnCode": " ", ## 호가유형코드@@
                "MgntrnCode": " ", ## 신용거래코드@@
                "LoanDt": " ", ## 대출일@@
                "OrdCndiTpCode": " ##주문조건구분@@"
            }
        },
        "output": {
            "CSPAT00600OutBlock1": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "AcntNo": "AcntNo`char", ## 계좌번호@@
                "InptPwd": "InptPwd`char", ## 입력비밀번호@@
                "IsuNo": "IsuNo`char", ## 종목번호@@
                "OrdQty": "OrdQty`long", ## 주문수량@@
                "OrdPrc": "OrdPrc`double", ## 주문가@@
                "BnsTpCode": "BnsTpCode`char", ## 매매구분@@
                "OrdprcPtnCode": "OrdprcPtnCode`char", ## 호가유형코드@@
                "PrgmOrdprcPtnCode": "PrgmOrdprcPtnCode`char", ## 프로그램호가유형코드@@
                "StslAbleYn": "StslAbleYn`char", ## 공매도가능여부@@
                "StslOrdprcTpCode": "StslOrdprcTpCode`char", ## 공매도호가구분@@
                "CommdaCode": "CommdaCode`char", ## 통신매체코드@@
                "MgntrnCode": "MgntrnCode`char", ## 신용거래코드@@
                "LoanDt": "LoanDt`char", ## 대출일@@
                "MbrNo": "MbrNo`char", ## 회원번호@@
                "OrdCndiTpCode": "OrdCndiTpCode`char", ## 주문조건구분@@
                "StrtgCode": "StrtgCode`char", ## 전략코드@@
                "GrpId": "GrpId`char", ## 그룹ID@@
                "OrdSeqNo": "OrdSeqNo`long", ## 주문회차@@
                "PtflNo": "PtflNo`long", ## 포트폴리오번호@@
                "BskNo": "BskNo`long", ## 바스켓번호@@
                "TrchNo": "TrchNo`long", ## 트렌치번호@@
                "ItemNo": "ItemNo`long", ## 아이템번호@@
                "OpDrtnNo": "OpDrtnNo`char", ## 운용지시번호@@
                "LpYn": "LpYn`char", ## 유동성공급자여부@@
                "CvrgTpCode": "CvrgTpCode`char##반대매매구분@@"
            },
            "CSPAT00600OutBlock2": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "OrdNo": "OrdNo`long", ## 주문번호@@
                "OrdTime": "OrdTime`char", ## 주문시각@@
                "OrdMktCode": "OrdMktCode`char", ## 주문시장코드@@
                "OrdPtnCode": "OrdPtnCode`char", ## 주문유형코드@@
                "ShtnIsuNo": "ShtnIsuNo`char", ## 단축종목번호@@
                "MgempNo": "MgempNo`char", ## 관리사원번호@@
                "OrdAmt": "OrdAmt`long", ## 주문금액@@
                "SpareOrdNo": "SpareOrdNo`long", ## 예비주문번호@@
                "CvrgSeqno": "CvrgSeqno`long", ## 반대매매일련번호@@
                "RsvOrdNo": "RsvOrdNo`long", ## 예약주문번호@@
                "SpotOrdQty": "SpotOrdQty`long", ## 실물주문수량@@
                "RuseOrdQty": "RuseOrdQty`long", ## 재사용주문수량@@
                "MnyOrdAmt": "MnyOrdAmt`long", ## 현금주문금액@@
                "SubstOrdAmt": "SubstOrdAmt`long", ## 대용주문금액@@
                "RuseOrdAmt": "RuseOrdAmt`long", ## 재사용주문금액@@
                "AcntNm": "AcntNm`char", ## 계좌명@@
                "IsuNm": "IsuNm`char##종목명@@"
            }
        }
    },
    "CSPAT00700": { ## 현물정정주문
        "input": {
            "CSPAT00700InBlock1": {
                "OrgOrdNo": "0", ## 원주문번호@@
                "AcntNo": " ", ## 계좌번호@@
                "InptPwd": " ", ## 입력비밀번호@@
                "IsuNo": " ", ## 종목번호@@
                "OrdQty": "0", ## 주문수량@@
                "OrdprcPtnCode": " ", ## 호가유형코드@@
                "OrdCndiTpCode": " ", ## 주문조건구분@@
                "OrdPrc": "0.0##주문가@@"
            }
        },
        "output": {
            "CSPAT00700OutBlock1": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "OrgOrdNo": "OrgOrdNo`long", ## 원주문번호@@
                "AcntNo": "AcntNo`char", ## 계좌번호@@
                "InptPwd": "InptPwd`char", ## 입력비밀번호@@
                "IsuNo": "IsuNo`char", ## 종목번호@@
                "OrdQty": "OrdQty`long", ## 주문수량@@
                "OrdprcPtnCode": "OrdprcPtnCode`char", ## 호가유형코드@@
                "OrdCndiTpCode": "OrdCndiTpCode`char", ## 주문조건구분@@
                "OrdPrc": "OrdPrc`double", ## 주문가@@
                "CommdaCode": "CommdaCode`char", ## 통신매체코드@@
                "StrtgCode": "StrtgCode`char", ## 전략코드@@
                "GrpId": "GrpId`char", ## 그룹ID@@
                "OrdSeqNo": "OrdSeqNo`long", ## 주문회차@@
                "PtflNo": "PtflNo`long", ## 포트폴리오번호@@
                "BskNo": "BskNo`long", ## 바스켓번호@@
                "TrchNo": "TrchNo`long", ## 트렌치번호@@
                "ItemNo": "ItemNo`long##아이템번호@@"
            },
            "CSPAT00700OutBlock2": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "OrdNo": "OrdNo`long", ## 주문번호@@
                "PrntOrdNo": "PrntOrdNo`long", ## 모주문번호@@
                "OrdTime": "OrdTime`char", ## 주문시각@@
                "OrdMktCode": "OrdMktCode`char", ## 주문시장코드@@
                "OrdPtnCode": "OrdPtnCode`char", ## 주문유형코드@@
                "ShtnIsuNo": "ShtnIsuNo`char", ## 단축종목번호@@
                "PrgmOrdprcPtnCode": "PrgmOrdprcPtnCode`char", ## 프로그램호가유형코드@@
                "StslOrdprcTpCode": "StslOrdprcTpCode`char", ## 공매도호가구분@@
                "StslAbleYn": "StslAbleYn`char", ## 공매도가능여부@@
                "MgntrnCode": "MgntrnCode`char", ## 신용거래코드@@
                "LoanDt": "LoanDt`char", ## 대출일@@
                "CvrgOrdTp": "CvrgOrdTp`char", ## 반대매매주문구분@@
                "LpYn": "LpYn`char", ## 유동성공급자여부@@
                "MgempNo": "MgempNo`char", ## 관리사원번호@@
                "OrdAmt": "OrdAmt`long", ## 주문금액@@
                "BnsTpCode": "BnsTpCode`char", ## 매매구분@@
                "SpareOrdNo": "SpareOrdNo`long", ## 예비주문번호@@
                "CvrgSeqno": "CvrgSeqno`long", ## 반대매매일련번호@@
                "RsvOrdNo": "RsvOrdNo`long", ## 예약주문번호@@
                "MnyOrdAmt": "MnyOrdAmt`long", ## 현금주문금액@@
                "SubstOrdAmt": "SubstOrdAmt`long", ## 대용주문금액@@
                "RuseOrdAmt": "RuseOrdAmt`long", ## 재사용주문금액@@
                "AcntNm": "AcntNm`char", ## 계좌명@@
                "IsuNm": "IsuNm`char##종목명@@"
            }
        }
    },
    "CSPAT00800": { ## 현물취소주문
        "input": {
            "CSPAT00800InBlock1": {
                "OrgOrdNo": "0", ## 원주문번호@@
                "AcntNo": " ", ## 계좌번호@@
                "InptPwd": " ", ## 입력비밀번호@@
                "IsuNo": " ", ## 종목번호@@
                "OrdQty": "0##주문수량@@"
            }
        },
        "output": {
            "CSPAT00800OutBlock1": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "OrgOrdNo": "OrgOrdNo`long", ## 원주문번호@@
                "AcntNo": "AcntNo`char", ## 계좌번호@@
                "InptPwd": "InptPwd`char", ## 입력비밀번호@@
                "IsuNo": "IsuNo`char", ## 종목번호@@
                "OrdQty": "OrdQty`long", ## 주문수량@@
                "CommdaCode": "CommdaCode`char", ## 통신매체코드@@
                "GrpId": "GrpId`char", ## 그룹ID@@
                "StrtgCode": "StrtgCode`char", ## 전략코드@@
                "OrdSeqNo": "OrdSeqNo`long", ## 주문회차@@
                "PtflNo": "PtflNo`long", ## 포트폴리오번호@@
                "BskNo": "BskNo`long", ## 바스켓번호@@
                "TrchNo": "TrchNo`long", ## 트렌치번호@@
                "ItemNo": "ItemNo`long##아이템번호@@"
            },
            "CSPAT00800OutBlock2": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "OrdNo": "OrdNo`long", ## 주문번호@@
                "PrntOrdNo": "PrntOrdNo`long", ## 모주문번호@@
                "OrdTime": "OrdTime`char", ## 주문시각@@
                "OrdMktCode": "OrdMktCode`char", ## 주문시장코드@@
                "OrdPtnCode": "OrdPtnCode`char", ## 주문유형코드@@
                "ShtnIsuNo": "ShtnIsuNo`char", ## 단축종목번호@@
                "PrgmOrdprcPtnCode": "PrgmOrdprcPtnCode`char", ## 프로그램호가유형코드@@
                "StslOrdprcTpCode": "StslOrdprcTpCode`char", ## 공매도호가구분@@
                "StslAbleYn": "StslAbleYn`char", ## 공매도가능여부@@
                "MgntrnCode": "MgntrnCode`char", ## 신용거래코드@@
                "LoanDt": "LoanDt`char", ## 대출일@@
                "CvrgOrdTp": "CvrgOrdTp`char", ## 반대매매주문구분@@
                "LpYn": "LpYn`char", ## 유동성공급자여부@@
                "MgempNo": "MgempNo`char", ## 관리사원번호@@
                "BnsTpCode": "BnsTpCode`char", ## 매매구분@@
                "SpareOrdNo": "SpareOrdNo`long", ## 예비주문번호@@
                "CvrgSeqno": "CvrgSeqno`long", ## 반대매매일련번호@@
                "RsvOrdNo": "RsvOrdNo`long", ## 예약주문번호@@
                "AcntNm": "AcntNm`char", ## 계좌명@@
                "IsuNm": "IsuNm`char##종목명@@"
            }
        }
    },
    "CSPBQ00200": { ## 현물계좌증거금률별주문가능수량조회
        "input": {
            "CSPBQ00200InBlock1": {
                "RecCnt": "0", ## 레코드갯수@@
                "BnsTpCode": " ", ## 매매구분@@
                "AcntNo": " ", ## 계좌번호@@
                "InptPwd": " ", ## 입력비밀번호@@
                "IsuNo": " ", ## 종목번호@@
                "OrdPrc": "0.0", ## 주문가격@@
                "RegCommdaCode": " ##통신매체코드@@"
            }
        },
        "output": {
            "CSPBQ00200OutBlock1": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "BnsTpCode": "BnsTpCode`char", ## 매매구분@@
                "AcntNo": "AcntNo`char", ## 계좌번호@@
                "InptPwd": "InptPwd`char", ## 입력비밀번호@@
                "IsuNo": "IsuNo`char", ## 종목번호@@
                "OrdPrc": "OrdPrc`double", ## 주문가격@@
                "RegCommdaCode": "RegCommdaCode`char##통신매체코드@@"
            },
            "CSPBQ00200OutBlock2": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "AcntNm": "AcntNm`char", ## 계좌명@@
                "IsuNm": "IsuNm`char", ## 종목명@@
                "Dps": "Dps`long", ## 예수금@@
                "SubstAmt": "SubstAmt`long", ## 대용금액@@
                "CrdtPldgRuseAmt": "CrdtPldgRuseAmt`long", ## 신용담보재사용금액@@
                "MnyOrdAbleAmt": "MnyOrdAbleAmt`long", ## 현금주문가능금액@@
                "SubstOrdAbleAmt": "SubstOrdAbleAmt`long", ## 대용주문가능금액@@
                "MnyMgn": "MnyMgn`long", ## 현금증거금액@@
                "SubstMgn": "SubstMgn`long", ## 대용증거금액@@
                "SeOrdAbleAmt": "SeOrdAbleAmt`long", ## 거래소금액@@
                "KdqOrdAbleAmt": "KdqOrdAbleAmt`long", ## 코스닥금액@@
                "PrsmptDpsD1": "PrsmptDpsD1`long", ## 추정예수금(D+1)@@
                "PrsmptDpsD2": "PrsmptDpsD2`long", ## 추정예수금(D+2)@@
                "MnyoutAbleAmt": "MnyoutAbleAmt`long", ## 출금가능금액@@
                "RcvblAmt": "RcvblAmt`long", ## 미수금액@@
                "CmsnRat": "CmsnRat`double", ## 수수료율@@
                "AddLevyAmt": "AddLevyAmt`long", ## 추가징수금액@@
                "RuseObjAmt": "RuseObjAmt`long", ## 재사용대상금액@@
                "MnyRuseObjAmt": "MnyRuseObjAmt`long", ## 현금재사용대상금액@@
                "FirmMgnRat": "FirmMgnRat`double", ## 이용사증거금률@@
                "SubstRuseObjAmt": "SubstRuseObjAmt`long", ## 대용재사용대상금액@@
                "IsuMgnRat": "IsuMgnRat`double", ## 종목증거금률@@
                "AcntMgnRat": "AcntMgnRat`double", ## 계좌증거금률@@
                "TrdMgnrt": "TrdMgnrt`double", ## 거래증거금률@@
                "Cmsn": "Cmsn`long", ## 수수료@@
                "MgnRat20pctOrdAbleAmt": "MgnRat20pctOrdAbleAmt`long", ## 증거금률20퍼센트주문가능금액@@
                "MgnRat20OrdAbleQty": "MgnRat20OrdAbleQty`long", ## 증거금률100퍼센트현금주문가능수량?@@
                "MgnRat30pctOrdAbleAmt": "MgnRat30pctOrdAbleAmt`long", ## 증거금률30퍼센트주문가능금액@@
                "MgnRat30OrdAbleQty": "MgnRat30OrdAbleQty`long", ## 증거금률30퍼센트주문가능수량??@@
                "MgnRat40pctOrdAbleAmt": "MgnRat40pctOrdAbleAmt`long", ## 증거금률40퍼센트주문가능금액@@
                "MgnRat40OrdAbleQty": "MgnRat40OrdAbleQty`long", ## 증거금률40퍼센트주문가능수량??@@
                "MgnRat100pctOrdAbleAmt": "MgnRat100pctOrdAbleAmt`long", ## 증거금률100퍼센트주문가능금액@@
                "MgnRat100OrdAbleQty": "MgnRat100OrdAbleQty`long", ## 증거금률100퍼센트주문가능수량??@@
                "MgnRat100MnyOrdAbleAmt": "MgnRat100MnyOrdAbleAmt`long", ## 증거금률100퍼센트현금주문가능금액?@@
                "MgnRat100MnyOrdAbleQty": "MgnRat100MnyOrdAbleQty`long", ## 증거금률100퍼센트현금주문가능수량@@
                "MgnRat20pctRuseAbleAmt": "MgnRat20pctRuseAbleAmt`long", ## 증거금률20퍼센트재사용가능금액@@
                "MgnRat30pctRuseAbleAmt": "MgnRat30pctRuseAbleAmt`long", ## 증거금률30퍼센트재사용가능금액@@
                "MgnRat40pctRuseAbleAmt": "MgnRat40pctRuseAbleAmt`long", ## 증거금률40퍼센트재사용가능금액@@
                "MgnRat100pctRuseAbleAmt": "MgnRat100pctRuseAbleAmt`long", ## 증거금률100퍼센트재사용가능금액@@
                "OrdAbleQty": "OrdAbleQty`long", ## 주문가능수량@@
                "OrdAbleAmt": "OrdAbleAmt`long##주문가능금액@@"
            }
        }
    },
    "CUR": { ## 현물정보 USD 실시간(CUR)
        "input": {
            "InBlock": {
                "base_id": " ##기초자산ID@@"
            }
        },
        "output": {
            "OutBlock": {
                "time": "time`char", ## 전송시간@@
                "offer": "offer`float", ## 매도호가@@
                "bid": "bid`float", ## 매수호가@@
                "open": "open`float", ## 시가@@
                "high": "high`float", ## 고가@@
                "low": "low`float", ## 저가@@
                "price": "price`float", ## 체결가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`float", ## 전일대비@@
                "drate": "drate`float", ## 등락율@@
                "ctime": "ctime`char", ## 데이타 발생시간@@
                "base_id": "base_id`char##기초자산ID@@"
            }
        }
    },
    "DH1": { ## KOSPI시간외단일가호가잔량(DH1)
        "input": {
            "InBlock": {
                "shcode": " ##단축코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "dan_hotime": "dan_hotime`char", ## 시간외단일가호가시간@@
                "dan_hstatus": "dan_hstatus`char", ## 시간외단일가장구분@@
                "dan_offerho1": "dan_offerho1`long", ## 시간외단일가매도호가1@@
                "dan_bidho1": "dan_bidho1`long", ## 시간외단일가매수호가1@@
                "dan_offerrem1": "dan_offerrem1`long", ## 시간외단일가매도호가잔량1@@
                "dan_bidrem1": "dan_bidrem1`long", ## 시간외단일가매수호가잔량1@@
                "dan_preoffercha1": "dan_preoffercha1`long", ## 시간외단일가직전매도대비수량1@@
                "dan_prebidcha1": "dan_prebidcha1`long", ## 시간외단일가직전매수대비수량1@@
                "dan_offerho2": "dan_offerho2`long", ## 시간외단일가매도호가2@@
                "dan_bidho2": "dan_bidho2`long", ## 시간외단일가매수호가2@@
                "dan_offerrem2": "dan_offerrem2`long", ## 시간외단일가매도호가잔량2@@
                "dan_bidrem2": "dan_bidrem2`long", ## 시간외단일가매수호가잔량2@@
                "dan_preoffercha2": "dan_preoffercha2`long", ## 시간외단일가직전매도대비수량2@@
                "dan_prebidcha2": "dan_prebidcha2`long", ## 시간외단일가직전매수대비수량2@@
                "dan_offerho3": "dan_offerho3`long", ## 시간외단일가매도호가3@@
                "dan_bidho3": "dan_bidho3`long", ## 시간외단일가매수호가3@@
                "dan_offerrem3": "dan_offerrem3`long", ## 시간외단일가매도호가잔량3@@
                "dan_bidrem3": "dan_bidrem3`long", ## 시간외단일가매수호가잔량3@@
                "dan_preoffercha3": "dan_preoffercha3`long", ## 시간외단일가직전매도대비수량3@@
                "dan_prebidcha3": "dan_prebidcha3`long", ## 시간외단일가직전매수대비수량3@@
                "dan_offerho4": "dan_offerho4`long", ## 시간외단일가매도호가4@@
                "dan_bidho4": "dan_bidho4`long", ## 시간외단일가매수호가4@@
                "dan_offerrem4": "dan_offerrem4`long", ## 시간외단일가매도호가잔량4@@
                "dan_bidrem4": "dan_bidrem4`long", ## 시간외단일가매수호가잔량4@@
                "dan_preoffercha4": "dan_preoffercha4`long", ## 시간외단일가직전매도대비수량4@@
                "dan_prebidcha4": "dan_prebidcha4`long", ## 시간외단일가직전매수대비수량4@@
                "dan_offerho5": "dan_offerho5`long", ## 시간외단일가매도호가5@@
                "dan_bidho5": "dan_bidho5`long", ## 시간외단일가매수호가5@@
                "dan_offerrem5": "dan_offerrem5`long", ## 시간외단일가매도호가잔량5@@
                "dan_bidrem5": "dan_bidrem5`long", ## 시간외단일가매수호가잔량5@@
                "dan_preoffercha5": "dan_preoffercha5`long", ## 시간외단일가직전매도대비수량5@@
                "dan_prebidcha5": "dan_prebidcha5`long", ## 시간외단일가직전매수대비수량5@@
                "dan_totofferrem": "dan_totofferrem`long", ## 시간외단일가총매도호가잔량@@
                "dan_totbidrem": "dan_totbidrem`long", ## 시간외단일가총매수호가잔량@@
                "dan_preoffercha": "dan_preoffercha`long", ## 시간외단일가직전매도호가총대비수량@@
                "dan_prebidcha": "dan_prebidcha`long", ## 시간외단일가직전매수호가총대비수량@@
                "dan_yeprice": "dan_yeprice`long", ## 시간외단일가예상체결가격@@
                "dan_yevolume": "dan_yevolume`long", ## 시간외단일가예상체결수량@@
                "dan_preysign": "dan_preysign`char", ## 시간외단일가예상가직전가대비구분@@
                "dan_preychange": "dan_preychange`long", ## 시간외단일가예상가직전가대비@@
                "dan_jnilysign": "dan_jnilysign`char", ## 시간외단일가예상가전일가대비구분@@
                "dan_jnilychange": "dan_jnilychange`long", ## 시간외단일가예상가전일가대비@@
                "shcode": "shcode`char##단축코드@@"
            }
        }
    },
    "DHA": { ## KOSDAQ시간외단일가호가잔량(DHA)
        "input": {
            "InBlock": {
                "shcode": " ##단축코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "dan_hotime": "dan_hotime`char", ## 시간외단일가호가시간@@
                "dan_hstatus": "dan_hstatus`char", ## 시간외단일가장구분@@
                "dan_offerho1": "dan_offerho1`long", ## 시간외단일가매도호가1@@
                "dan_bidho1": "dan_bidho1`long", ## 시간외단일가매수호가1@@
                "dan_offerrem1": "dan_offerrem1`long", ## 시간외단일가매도호가잔량1@@
                "dan_bidrem1": "dan_bidrem1`long", ## 시간외단일가매수호가잔량1@@
                "dan_preoffercha1": "dan_preoffercha1`long", ## 시간외단일가직전매도대비수량1@@
                "dan_prebidcha1": "dan_prebidcha1`long", ## 시간외단일가직전매수대비수량1@@
                "dan_offerho2": "dan_offerho2`long", ## 시간외단일가매도호가2@@
                "dan_bidho2": "dan_bidho2`long", ## 시간외단일가매수호가2@@
                "dan_offerrem2": "dan_offerrem2`long", ## 시간외단일가매도호가잔량2@@
                "dan_bidrem2": "dan_bidrem2`long", ## 시간외단일가매수호가잔량2@@
                "dan_preoffercha2": "dan_preoffercha2`long", ## 시간외단일가직전매도대비수량2@@
                "dan_prebidcha2": "dan_prebidcha2`long", ## 시간외단일가직전매수대비수량2@@
                "dan_offerho3": "dan_offerho3`long", ## 시간외단일가매도호가3@@
                "dan_bidho3": "dan_bidho3`long", ## 시간외단일가매수호가3@@
                "dan_offerrem3": "dan_offerrem3`long", ## 시간외단일가매도호가잔량3@@
                "dan_bidrem3": "dan_bidrem3`long", ## 시간외단일가매수호가잔량3@@
                "dan_preoffercha3": "dan_preoffercha3`long", ## 시간외단일가직전매도대비수량3@@
                "dan_prebidcha3": "dan_prebidcha3`long", ## 시간외단일가직전매수대비수량3@@
                "dan_offerho4": "dan_offerho4`long", ## 시간외단일가매도호가4@@
                "dan_bidho4": "dan_bidho4`long", ## 시간외단일가매수호가4@@
                "dan_offerrem4": "dan_offerrem4`long", ## 시간외단일가매도호가잔량4@@
                "dan_bidrem4": "dan_bidrem4`long", ## 시간외단일가매수호가잔량4@@
                "dan_preoffercha4": "dan_preoffercha4`long", ## 시간외단일가직전매도대비수량4@@
                "dan_prebidcha4": "dan_prebidcha4`long", ## 시간외단일가직전매수대비수량4@@
                "dan_offerho5": "dan_offerho5`long", ## 시간외단일가매도호가5@@
                "dan_bidho5": "dan_bidho5`long", ## 시간외단일가매수호가5@@
                "dan_offerrem5": "dan_offerrem5`long", ## 시간외단일가매도호가잔량5@@
                "dan_bidrem5": "dan_bidrem5`long", ## 시간외단일가매수호가잔량5@@
                "dan_preoffercha5": "dan_preoffercha5`long", ## 시간외단일가직전매도대비수량5@@
                "dan_prebidcha5": "dan_prebidcha5`long", ## 시간외단일가직전매수대비수량5@@
                "dan_totofferrem": "dan_totofferrem`long", ## 시간외단일가총매도호가잔량@@
                "dan_totbidrem": "dan_totbidrem`long", ## 시간외단일가총매수호가잔량@@
                "dan_preoffercha": "dan_preoffercha`long", ## 시간외단일가직전매도호가총대비수량@@
                "dan_prebidcha": "dan_prebidcha`long", ## 시간외단일가직전매수호가총대비수량@@
                "dan_yeprice": "dan_yeprice`long", ## 시간외단일가예상체결가격@@
                "dan_yevolume": "dan_yevolume`long", ## 시간외단일가예상체결수량@@
                "dan_preysign": "dan_preysign`char", ## 시간외단일가예상가직전가대비구분@@
                "dan_preychange": "dan_preychange`long", ## 시간외단일가예상가직전가대비@@
                "dan_jnilysign": "dan_jnilysign`char", ## 시간외단일가예상가전일가대비구분@@
                "dan_jnilychange": "dan_jnilychange`long", ## 시간외단일가예상가전일가대비@@
                "shcode": "shcode`char##단축코드@@"
            }
        }
    },
    "DK3": { ## KOSDAQ시간외단일가체결(DK3)
        "input": {
            "InBlock": {
                "shcode": " ##단축코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "dan_chetime": "dan_chetime`char", ## 시간외단일가체결시간@@
                "dan_sign": "dan_sign`char", ## 시간외단일가전일대비구분@@
                "dan_change": "dan_change`long", ## 시간외단일가전일대비@@
                "dan_drate": "dan_drate`float", ## 시간외단일가등락율@@
                "dan_price": "dan_price`long", ## 시간외단일가현재가@@
                "dan_opentime": "dan_opentime`char", ## 시간외단일가시가시간@@
                "dan_open": "dan_open`long", ## 시간외단일가시가@@
                "dan_hightime": "dan_hightime`char", ## 시간외단일가고가시간@@
                "dan_high": "dan_high`long", ## 시간외단일가고가@@
                "dan_lowtime": "dan_lowtime`char", ## 시간외단일가저가시간@@
                "dan_low": "dan_low`long", ## 시간외단일가저가@@
                "dan_cgubun": "dan_cgubun`char", ## 시간외단일가체결구분@@
                "dan_cvolume": "dan_cvolume`long", ## 시간외단일가체결량@@
                "dan_volume": "dan_volume`long", ## 시간외단일가누적거래량@@
                "dan_value": "dan_value`long", ## 시간외단일가누적거래대금@@
                "dan_mdvolume": "dan_mdvolume`long", ## 시간외단일가매도누적체결량@@
                "dan_mdchecnt": "dan_mdchecnt`long", ## 시간외단일가매도누적체결건수@@
                "dan_msvolume": "dan_msvolume`long", ## 시간외단일가매수누적체결량@@
                "dan_mschecnt": "dan_mschecnt`long", ## 시간외단일가매수누적체결건수@@
                "dan_prevolume": "dan_prevolume`long", ## 시간외단일가직전거래량@@
                "dan_precvolume": "dan_precvolume`long", ## 시간외단일가직전체결수량@@
                "dan_cpower": "dan_cpower`float", ## 시간외단일가체결강도@@
                "dan_status": "dan_status`char", ## 시간외단일가장정보@@
                "shcode": "shcode`char##단축코드@@"
            }
        }
    },
    "DS3": { ## KOSPI시간외단일가체결(DS3)
        "input": {
            "InBlock": {
                "shcode": " ##단축코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "dan_chetime": "dan_chetime`char", ## 시간외단일가체결시간@@
                "dan_sign": "dan_sign`char", ## 시간외단일가전일대비구분@@
                "dan_change": "dan_change`long", ## 시간외단일가전일대비@@
                "dan_drate": "dan_drate`float", ## 시간외단일가등락율@@
                "dan_price": "dan_price`long", ## 시간외단일가현재가@@
                "dan_opentime": "dan_opentime`char", ## 시간외단일가시가시간@@
                "dan_open": "dan_open`long", ## 시간외단일가시가@@
                "dan_hightime": "dan_hightime`char", ## 시간외단일가고가시간@@
                "dan_high": "dan_high`long", ## 시간외단일가고가@@
                "dan_lowtime": "dan_lowtime`char", ## 시간외단일가저가시간@@
                "dan_low": "dan_low`long", ## 시간외단일가저가@@
                "dan_cgubun": "dan_cgubun`char", ## 시간외단일가체결구분@@
                "dan_cvolume": "dan_cvolume`long", ## 시간외단일가체결량@@
                "dan_volume": "dan_volume`long", ## 시간외단일가누적거래량@@
                "dan_value": "dan_value`long", ## 시간외단일가누적거래대금@@
                "dan_mdvolume": "dan_mdvolume`long", ## 시간외단일가매도누적체결량@@
                "dan_mdchecnt": "dan_mdchecnt`long", ## 시간외단일가매도누적체결건수@@
                "dan_msvolume": "dan_msvolume`long", ## 시간외단일가매수누적체결량@@
                "dan_mschecnt": "dan_mschecnt`long", ## 시간외단일가매수누적체결건수@@
                "dan_prevolume": "dan_prevolume`long", ## 시간외단일가직전거래량@@
                "dan_precvolume": "dan_precvolume`long", ## 시간외단일가직전체결수량@@
                "dan_cpower": "dan_cpower`float", ## 시간외단일가체결강도@@
                "dan_status": "dan_status`char", ## 시간외단일가장정보@@
                "shcode": "shcode`char##단축코드@@"
            }
        }
    },
    "DVI": { ## 시간외단일가VI발동해제(DVI)
        "input": {
            "InBlock": {
                "shcode": " ##단축코드(KEY)@@"
            }
        },
        "output": {
            "OutBlock": {
                "vi_gubun": "vi_gubun`char", ## 구분@@0:해제 1:정적발동 2:동적발동 3:정적&동적
                "svi_recprice": "svi_recprice`long", ## 정적VI발동기준가격@@
                "dvi_recprice": "dvi_recprice`long", ## 동적VI발동기준가격@@
                "vi_trgprice": "vi_trgprice`long", ## VI발동가격@@
                "shcode": "shcode`char", ## 단축코드(KEY)@@
                "ref_shcode": "ref_shcode`char", ## 참조코드(미사용)@@
                "time": "time`char##시간@@"
            }
        }
    },
    "EC0": { ## EUREX연계KP200지수옵션선물체결(EC0)
        "input": {
            "InBlock": {
                "optcode": " ##단축코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "chetime": "chetime`char", ## 체결시간(24시간)@@
                "chetime1": "chetime1`char", ## 체결시간(36시간)@@
                "sign": "sign`char", ## 정규장종가대비구분@@
                "change": "change`float", ## 정규장종가대비@@
                "drate": "drate`float", ## 정규장종가기준등락율@@
                "price": "price`float", ## 현재가@@
                "open": "open`float", ## 시가@@
                "high": "high`float", ## 고가@@
                "low": "low`float", ## 저가@@
                "cgubun": "cgubun`char", ## 체결구분@@
                "cvolume": "cvolume`long", ## 체결량@@
                "volume": "volume`long", ## 누적거래량@@
                "value": "value`long", ## 누적거래대금(미제공)@@
                "mdvolume": "mdvolume`long", ## 매도누적체결량@@
                "mdchecnt": "mdchecnt`long", ## 매도누적체결건수(미제공)@@
                "msvolume": "msvolume`long", ## 매수누적체결량@@
                "mschecnt": "mschecnt`long", ## 매수누적체결건수(미제공)@@
                "cpower": "cpower`float", ## 체결강도@@
                "offerho1": "offerho1`float", ## 매도호가1@@
                "bidho1": "bidho1`float", ## 매수호가1@@
                "openyak": "openyak`long", ## 미결제약정수량@@
                "k200jisu": "k200jisu`float", ## KOSPI200지수@@
                "eqva": "eqva`float", ## KOSPI등가@@
                "theoryprice": "theoryprice`float", ## 이론가@@
                "impv": "impv`float", ## 내재변동성@@
                "openyakcha": "openyakcha`long", ## 미결제약정증감@@
                "timevalue": "timevalue`float", ## 시간가치@@
                "jgubun": "jgubun`char", ## 장운영정보@@
                "jnilvolume": "jnilvolume`long", ## 전일동시간대거래량@@
                "optcode": "optcode`char##단축코드@@"
            }
        }
    },
    "EH0": { ## EUREX연계KP200지수옵션선물호가(EH0)
        "input": {
            "InBlock": {
                "optcode": " ##단축코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "hotime": "hotime`char", ## 호가시간(24시간)@@
                "hotime1": "hotime1`char", ## 호가시간(36시간)@@
                "offerho1": "offerho1`double", ## 매도호가1@@
                "bidho1": "bidho1`double", ## 매수호가1@@
                "offerrem1": "offerrem1`long", ## 매도호가수량1@@
                "bidrem1": "bidrem1`long", ## 매수호가수량1@@
                "offercnt1": "offercnt1`long", ## 매도호가건수1(미제공)@@
                "bidcnt1": "bidcnt1`long", ## 매수호가건수1(미제공)@@
                "offerho2": "offerho2`double", ## 매도호가2@@
                "bidho2": "bidho2`double", ## 매수호가2@@
                "offerrem2": "offerrem2`long", ## 매도호가수량2@@
                "bidrem2": "bidrem2`long", ## 매수호가수량2@@
                "offercnt2": "offercnt2`long", ## 매도호가건수2(미제공)@@
                "bidcnt2": "bidcnt2`long", ## 매수호가건수2(미제공)@@
                "offerho3": "offerho3`double", ## 매도호가3@@
                "bidho3": "bidho3`double", ## 매수호가3@@
                "offerrem3": "offerrem3`long", ## 매도호가수량3@@
                "bidrem3": "bidrem3`long", ## 매수호가수량3@@
                "offercnt3": "offercnt3`long", ## 매도호가건수3(미제공)@@
                "bidcnt3": "bidcnt3`long", ## 매수호가건수3(미제공)@@
                "offerho4": "offerho4`double", ## 매도호가4(미제공)@@
                "bidho4": "bidho4`double", ## 매수호가4(미제공)@@
                "offerrem4": "offerrem4`long", ## 매도호가수량4(미제공)@@
                "bidrem4": "bidrem4`long", ## 매수호가수량4(미제공)@@
                "offercnt4": "offercnt4`long", ## 매도호가건수4(미제공)@@
                "bidcnt4": "bidcnt4`long", ## 매수호가건수4(미제공)@@
                "offerho5": "offerho5`double", ## 매도호가5(미제공)@@
                "bidho5": "bidho5`double", ## 매수호가5(미제공)@@
                "offerrem5": "offerrem5`long", ## 매도호가수량5(미제공)@@
                "bidrem5": "bidrem5`long", ## 매수호가수량5(미제공)@@
                "offercnt5": "offercnt5`long", ## 매도호가건수5(미제공)@@
                "bidcnt5": "bidcnt5`long", ## 매수호가건수5(미제공)@@
                "totofferrem": "totofferrem`long", ## 매도호가총수량@@
                "totbidrem": "totbidrem`long", ## 매수호가총수량@@
                "totoffercnt": "totoffercnt`long", ## 매도호가총건수@@
                "totbidcnt": "totbidcnt`long", ## 매수호가총건수@@
                "optcode": "optcode`char", ## 단축코드@@
                "danhochk": "danhochk`char##단일가호가여부@@"
            }
        }
    },
    "ESN": { ## 뉴ELW투자지표민감도(ESN)
        "input": {
            "InBlock": {
                "shcode": " ##단축코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "time": "time`char", ## 시간@@
                "theoryprice": "theoryprice`float", ## 장중이론가@@
                "delt": "delt`float", ## 델타@@
                "gama": "gama`float", ## 감마@@
                "ceta": "ceta`float", ## 세타@@
                "vega": "vega`float", ## 베가@@
                "rhox": "rhox`float", ## 로우@@
                "impv": "impv`float", ## 내재변동성@@
                "egearing": "egearing`float", ## E.기어링@@
                "shcode": "shcode`char", ## 단축코드@@
                "elwclose": "elwclose`long", ## ELW현재가@@
                "sign": "sign`char", ## ELW전일대비구분@@
                "change": "change`long", ## ELW전일대비@@
                "date": "date`char", ## 일자@@
                "tickvalue": "tickvalue`float", ## 틱환산@@
                "lp_impv": "lp_impv`float##LP내재변동성@@"
            }
        }
    },
    "EU0": { ## EUX접수
        "input": {
            "InBlock": {}
        },
        "output": {
            "OutBlock": {
                "lineseq": "lineseq`long", ## 라인일련번호@@
                "accno": "accno`char", ## 계좌번호@@
                "user": "user`char", ## 조작자ID@@
                "len": "len`long", ## 헤더길이@@
                "gubun": "gubun`char", ## 헤더구분@@
                "compress": "compress`char", ## 압축구분@@
                "encrypt": "encrypt`char", ## 암호구분@@
                "offset": "offset`long", ## 공통시작지점@@
                "trcode": "trcode`char", ## TRCODE@@
                "comid": "comid`char", ## 이용사번호@@
                "userid": "userid`char", ## 사용자ID@@
                "media": "media`char", ## 접속매체@@
                "ifid": "ifid`char", ## I/F일련번호@@
                "seq": "seq`char", ## 전문일련번호@@
                "trid": "trid`char", ## TR추적ID@@
                "pubip": "pubip`char", ## 공인IP@@
                "prvip": "prvip`char", ## 사설IP@@
                "pcbpno": "pcbpno`char", ## 처리지점번호@@
                "bpno": "bpno`char", ## 지점번호@@
                "termno": "termno`char", ## 단말번호@@
                "lang": "lang`char", ## 언어구분@@
                "proctm": "proctm`long", ## AP처리시간@@
                "msgcode": "msgcode`char", ## 메세지코드@@
                "outgu": "outgu`char", ## 메세지출력구분@@
                "compreq": "compreq`char", ## 압축요청구분@@
                "funckey": "funckey`char", ## 기능키@@
                "reqcnt": "reqcnt`long", ## 요청레코드개수@@
                "filler": "filler`char", ## 예비영역@@
                "cont": "cont`char", ## 연속구분@@
                "contkey": "contkey`char", ## 연속키값@@
                "varlen": "varlen`long", ## 가변시스템길이@@
                "varhdlen": "varhdlen`long", ## 가변해더길이@@
                "varmsglen": "varmsglen`long", ## 가변메시지길이@@
                "trsrc": "trsrc`char", ## 조회발원지@@
                "eventid": "eventid`char", ## I/F이벤트ID@@
                "ifinfo": "ifinfo`char", ## I/F정보@@
                "filler1": "filler1`char", ## 예비영역@@
                "trcode1": "trcode1`char", ## tr코드@@
                "firmno": "firmno`char", ## 회사번호@@
                "acntno": "acntno`char", ## 계좌번호@@
                "acntno1": "acntno1`char", ## 계좌번호@@
                "acntnm": "acntnm`char", ## 계좌명@@
                "brnno": "brnno`char", ## 지점번호@@
                "ordmktcode": "ordmktcode`char", ## 주문시장코드@@
                "ordno1": "ordno1`char", ## 주문번호@@
                "ordno": "ordno`long", ## 주문번호@@
                "orgordno1": "orgordno1`char", ## 원주문번호@@
                "orgordno": "orgordno`long", ## 원주문번호@@
                "prntordno": "prntordno`char", ## 모주문번호@@
                "prntordno1": "prntordno1`long", ## 모주문번호@@
                "isuno": "isuno`char", ## 종목번호@@
                "fnoIsuno": "fnoIsuno`char", ## 선물옵션종목번호@@
                "fnoIsunm": "fnoIsunm`char", ## 선물옵션종목명@@
                "pdgrpcode": "pdgrpcode`char", ## 상품군분류코드@@
                "fnoIsuptntp": "fnoIsuptntp`char", ## 선물옵션종목유형구분@@
                "bnstp": "bnstp`char", ## 매매구분@@
                "mrctp": "mrctp`char", ## 정정취소구분@@
                "ordqty": "ordqty`long", ## 주문수량@@
                "hogatype": "hogatype`char", ## 호가유형코드@@
                "mmgb": "mmgb`char", ## 거래유형코드@@
                "ordprc": "ordprc`double", ## 주문가격@@
                "unercqty": "unercqty`long", ## 미체결수량@@
                "commdacode": "commdacode`char", ## 통신매체@@
                "peeamtcode": "peeamtcode`char", ## 수수료합산코드@@
                "mgempno": "mgempno`char", ## 관리사원@@
                "fnotrdunitamt": "fnotrdunitamt`double", ## 선물옵션거래단위금액@@
                "trxtime": "trxtime`char", ## 처리시각@@
                "strtgcode": "strtgcode`char", ## 전략코드@@
                "grpId": "grpId`char", ## 그룹Id@@
                "ordseqno": "ordseqno`char", ## 주문회차@@
                "ptflno": "ptflno`char", ## 포트폴리오 번호@@
                "bskno": "bskno`char", ## 바스켓번호@@
                "trchno": "trchno`char", ## 트렌치번호@@
                "Itemno": "Itemno`char", ## 아이템번호@@
                "OrderID": "OrderID`char", ## 주문자Id@@
                "opdrtnno": "opdrtnno`char", ## 운영지시번호@@
                "rjtcode": "rjtcode`char", ## 부적격코드@@
                "mrccnfqty": "mrccnfqty`long", ## 정정취소확인수량@@
                "orgordunercqty": "orgordunercqty`long", ## 원주문미체결수량@@
                "orgordmrcqty": "orgordmrcqty`long", ## 원주문정정취소수량@@
                "ctrcttime": "ctrcttime`char", ## 약정시각(체결시각)@@
                "ctrctno": "ctrctno`char", ## 약정번호@@
                "execprc": "execprc`double", ## 체결가격@@
                "execqty": "execqty`long", ## 체결수량@@
                "newqty": "newqty`long", ## 신규체결수량@@
                "qdtqty": "qdtqty`long", ## 청산체결수량@@
                "lastqty": "lastqty`long", ## 최종결제수량@@
                "lallexecqty": "lallexecqty`long", ## 전체체결수량@@
                "allexecamt": "allexecamt`long", ## 전체체결금액@@
                "fnobalevaltp": "fnobalevaltp`char", ## 잔고평가구분@@
                "bnsplamt": "bnsplamt`long", ## 매매손익금액@@
                "fnoIsuno1": "fnoIsuno1`char", ## 선물옵션종목번호1@@
                "bnstp1": "bnstp1`char", ## 매매구분1@@
                "execprc1": "execprc1`double", ## 체결가1@@
                "newqty1": "newqty1`long", ## 신규체결수량1@@
                "qdtqty1": "qdtqty1`long", ## 청산체결수량1@@
                "allexecamt1": "allexecamt1`long", ## 전체체결금액1@@
                "fnoIsuno2": "fnoIsuno2`char", ## 선물옵션종목번호2@@
                "bnstp2": "bnstp2`char", ## 매매구분2@@
                "execprc2": "execprc2`double", ## 체결가2@@
                "newqty2": "newqty2`long", ## 신규체결수량2@@
                "lqdtqty2": "lqdtqty2`long", ## 청산체결수량2@@
                "allexecamt2": "allexecamt2`long", ## 전체체결금액2@@
                "dps": "dps`long", ## 예수금@@
                "ftsubtdsgnamt": "ftsubtdsgnamt`long", ## 선물대용지정금액@@
                "mgn": "mgn`long", ## 증거금@@
                "mnymgn": "mnymgn`long", ## 증거금현금@@
                "ordableamt": "ordableamt`long", ## 주문가능금액@@
                "mnyordableamt": "mnyordableamt`long", ## 주문가능현금액@@
                "fnoIsuno_1": "fnoIsuno_1`char", ## 잔고 종목번호1@@
                "bnstp_1": "bnstp_1`char", ## 잔고 매매구분1@@
                "unsttqty_1": "unsttqty_1`long", ## 미결제수량1@@
                "lqdtableqty_1": "lqdtableqty_1`long", ## 주문가능수량1@@
                "avrprc_1": "avrprc_1`double", ## 평균가1@@
                "fnoIsuno_2": "fnoIsuno_2`char", ## 잔고 종목번호2@@
                "bnstp_2": "bnstp_2`char", ## 잔고 매매구분2@@
                "unsttqty_2": "unsttqty_2`long", ## 미결제수량2@@
                "lqdtableqty_2": "lqdtableqty_2`long", ## 주문가능수량2@@
                "avrprc_2": "avrprc_2`double##평균가2@@"
            }
        }
    },
    "EU1": { ## EUX체결
        "input": {
            "InBlock": {}
        },
        "output": {
            "OutBlock": {
                "lineseq": "lineseq`long", ## 라인일련번호@@
                "accno": "accno`char", ## 계좌번호@@
                "user": "user`char", ## 조작자ID@@
                "len": "len`long", ## 헤더길이@@
                "gubun": "gubun`char", ## 헤더구분@@
                "compress": "compress`char", ## 압축구분@@
                "encrypt": "encrypt`char", ## 암호구분@@
                "offset": "offset`long", ## 공통시작지점@@
                "trcode": "trcode`char", ## TRCODE@@
                "comid": "comid`char", ## 이용사번호@@
                "userid": "userid`char", ## 사용자ID@@
                "media": "media`char", ## 접속매체@@
                "ifid": "ifid`char", ## I/F일련번호@@
                "seq": "seq`char", ## 전문일련번호@@
                "trid": "trid`char", ## TR추적ID@@
                "pubip": "pubip`char", ## 공인IP@@
                "prvip": "prvip`char", ## 사설IP@@
                "pcbpno": "pcbpno`char", ## 처리지점번호@@
                "bpno": "bpno`char", ## 지점번호@@
                "termno": "termno`char", ## 단말번호@@
                "lang": "lang`char", ## 언어구분@@
                "proctm": "proctm`long", ## AP처리시간@@
                "msgcode": "msgcode`char", ## 메세지코드@@
                "outgu": "outgu`char", ## 메세지출력구분@@
                "compreq": "compreq`char", ## 압축요청구분@@
                "funckey": "funckey`char", ## 기능키@@
                "reqcnt": "reqcnt`long", ## 요청레코드개수@@
                "filler": "filler`char", ## 예비영역@@
                "cont": "cont`char", ## 연속구분@@
                "contkey": "contkey`char", ## 연속키값@@
                "varlen": "varlen`long", ## 가변시스템길이@@
                "varhdlen": "varhdlen`long", ## 가변해더길이@@
                "varmsglen": "varmsglen`long", ## 가변메시지길이@@
                "trsrc": "trsrc`char", ## 조회발원지@@
                "eventid": "eventid`char", ## I/F이벤트ID@@
                "ifinfo": "ifinfo`char", ## I/F정보@@
                "filler1": "filler1`char", ## 예비영역@@
                "trcode1": "trcode1`char", ## tr코드@@
                "firmno": "firmno`char", ## 회사번호@@
                "acntno": "acntno`char", ## 계좌번호@@
                "acntno1": "acntno1`char", ## 계좌번호@@
                "acntnm": "acntnm`char", ## 계좌명@@
                "brnno": "brnno`char", ## 지점번호@@
                "ordmktcode": "ordmktcode`char", ## 주문시장코드@@
                "ordno1": "ordno1`char", ## 주문번호@@
                "ordno": "ordno`long", ## 주문번호@@
                "orgordno1": "orgordno1`char", ## 원주문번호@@
                "orgordno": "orgordno`long", ## 원주문번호@@
                "prntordno": "prntordno`char", ## 모주문번호@@
                "prntordno1": "prntordno1`long", ## 모주문번호@@
                "isuno": "isuno`char", ## 종목번호@@
                "fnoIsuno": "fnoIsuno`char", ## 선물옵션종목번호@@
                "fnoIsunm": "fnoIsunm`char", ## 선물옵션종목명@@
                "pdgrpcode": "pdgrpcode`char", ## 상품군분류코드@@
                "fnoIsuptntp": "fnoIsuptntp`char", ## 선물옵션종목유형구분@@
                "bnstp": "bnstp`char", ## 매매구분@@
                "mrctp": "mrctp`char", ## 정정취소구분@@
                "ordqty": "ordqty`long", ## 주문수량@@
                "hogatype": "hogatype`char", ## 호가유형코드@@
                "mmgb": "mmgb`char", ## 거래유형코드@@
                "ordprc": "ordprc`double", ## 주문가격@@
                "unercqty": "unercqty`long", ## 미체결수량@@
                "commdacode": "commdacode`char", ## 통신매체@@
                "peeamtcode": "peeamtcode`char", ## 수수료합산코드@@
                "mgempno": "mgempno`char", ## 관리사원@@
                "fnotrdunitamt": "fnotrdunitamt`double", ## 선물옵션거래단위금액@@
                "trxtime": "trxtime`char", ## 처리시각@@
                "strtgcode": "strtgcode`char", ## 전략코드@@
                "grpId": "grpId`char", ## 그룹Id@@
                "ordseqno": "ordseqno`char", ## 주문회차@@
                "ptflno": "ptflno`char", ## 포트폴리오 번호@@
                "bskno": "bskno`char", ## 바스켓번호@@
                "trchno": "trchno`char", ## 트렌치번호@@
                "Itemno": "Itemno`char", ## 아이템번호@@
                "OrderID": "OrderID`char", ## 주문자Id@@
                "opdrtnno": "opdrtnno`char", ## 운영지시번호@@
                "rjtcode": "rjtcode`char", ## 부적격코드@@
                "mrccnfqty": "mrccnfqty`long", ## 정정취소확인수량@@
                "orgordunercqty": "orgordunercqty`long", ## 원주문미체결수량@@
                "orgordmrcqty": "orgordmrcqty`long", ## 원주문정정취소수량@@
                "ctrcttime": "ctrcttime`char", ## 약정시각(체결시각)@@
                "ctrctno": "ctrctno`char", ## 약정번호@@
                "execprc": "execprc`double", ## 체결가격@@
                "execqty": "execqty`long", ## 체결수량@@
                "newqty": "newqty`long", ## 신규체결수량@@
                "qdtqty": "qdtqty`long", ## 청산체결수량@@
                "lastqty": "lastqty`long", ## 최종결제수량@@
                "lallexecqty": "lallexecqty`long", ## 전체체결수량@@
                "allexecamt": "allexecamt`long", ## 전체체결금액@@
                "fnobalevaltp": "fnobalevaltp`char", ## 잔고평가구분@@
                "bnsplamt": "bnsplamt`long", ## 매매손익금액@@
                "fnoIsuno1": "fnoIsuno1`char", ## 선물옵션종목번호1@@
                "bnstp1": "bnstp1`char", ## 매매구분1@@
                "execprc1": "execprc1`double", ## 체결가1@@
                "newqty1": "newqty1`long", ## 신규체결수량1@@
                "qdtqty1": "qdtqty1`long", ## 청산체결수량1@@
                "allexecamt1": "allexecamt1`long", ## 전체체결금액1@@
                "fnoIsuno2": "fnoIsuno2`char", ## 선물옵션종목번호2@@
                "bnstp2": "bnstp2`char", ## 매매구분2@@
                "execprc2": "execprc2`double", ## 체결가2@@
                "newqty2": "newqty2`long", ## 신규체결수량2@@
                "lqdtqty2": "lqdtqty2`long", ## 청산체결수량2@@
                "allexecamt2": "allexecamt2`long", ## 전체체결금액2@@
                "dps": "dps`long", ## 예수금@@
                "ftsubtdsgnamt": "ftsubtdsgnamt`long", ## 선물대용지정금액@@
                "mgn": "mgn`long", ## 증거금@@
                "mnymgn": "mnymgn`long", ## 증거금현금@@
                "ordableamt": "ordableamt`long", ## 주문가능금액@@
                "mnyordableamt": "mnyordableamt`long", ## 주문가능현금액@@
                "fnoIsuno_1": "fnoIsuno_1`char", ## 잔고 종목번호1@@
                "bnstp_1": "bnstp_1`char", ## 잔고 매매구분1@@
                "unsttqty_1": "unsttqty_1`long", ## 미결제수량1@@
                "lqdtableqty_1": "lqdtableqty_1`long", ## 주문가능수량1@@
                "avrprc_1": "avrprc_1`double", ## 평균가1@@
                "fnoIsuno_2": "fnoIsuno_2`char", ## 잔고 종목번호2@@
                "bnstp_2": "bnstp_2`char", ## 잔고 매매구분2@@
                "unsttqty_2": "unsttqty_2`long", ## 미결제수량2@@
                "lqdtableqty_2": "lqdtableqty_2`long", ## 주문가능수량2@@
                "avrprc_2": "avrprc_2`double##평균가2@@"
            }
        }
    },
    "EU2": { ## EUX확인
        "input": {
            "InBlock": {}
        },
        "output": {
            "OutBlock": {
                "lineseq": "lineseq`long", ## 라인일련번호@@
                "accno": "accno`char", ## 계좌번호@@
                "user": "user`char", ## 조작자ID@@
                "len": "len`long", ## 헤더길이@@
                "gubun": "gubun`char", ## 헤더구분@@
                "compress": "compress`char", ## 압축구분@@
                "encrypt": "encrypt`char", ## 암호구분@@
                "offset": "offset`long", ## 공통시작지점@@
                "trcode": "trcode`char", ## TRCODE@@
                "comid": "comid`char", ## 이용사번호@@
                "userid": "userid`char", ## 사용자ID@@
                "media": "media`char", ## 접속매체@@
                "ifid": "ifid`char", ## I/F일련번호@@
                "seq": "seq`char", ## 전문일련번호@@
                "trid": "trid`char", ## TR추적ID@@
                "pubip": "pubip`char", ## 공인IP@@
                "prvip": "prvip`char", ## 사설IP@@
                "pcbpno": "pcbpno`char", ## 처리지점번호@@
                "bpno": "bpno`char", ## 지점번호@@
                "termno": "termno`char", ## 단말번호@@
                "lang": "lang`char", ## 언어구분@@
                "proctm": "proctm`long", ## AP처리시간@@
                "msgcode": "msgcode`char", ## 메세지코드@@
                "outgu": "outgu`char", ## 메세지출력구분@@
                "compreq": "compreq`char", ## 압축요청구분@@
                "funckey": "funckey`char", ## 기능키@@
                "reqcnt": "reqcnt`long", ## 요청레코드개수@@
                "filler": "filler`char", ## 예비영역@@
                "cont": "cont`char", ## 연속구분@@
                "contkey": "contkey`char", ## 연속키값@@
                "varlen": "varlen`long", ## 가변시스템길이@@
                "varhdlen": "varhdlen`long", ## 가변해더길이@@
                "varmsglen": "varmsglen`long", ## 가변메시지길이@@
                "trsrc": "trsrc`char", ## 조회발원지@@
                "eventid": "eventid`char", ## I/F이벤트ID@@
                "ifinfo": "ifinfo`char", ## I/F정보@@
                "filler1": "filler1`char", ## 예비영역@@
                "trcode1": "trcode1`char", ## tr코드@@
                "firmno": "firmno`char", ## 회사번호@@
                "acntno": "acntno`char", ## 계좌번호@@
                "acntno1": "acntno1`char", ## 계좌번호@@
                "acntnm": "acntnm`char", ## 계좌명@@
                "brnno": "brnno`char", ## 지점번호@@
                "ordmktcode": "ordmktcode`char", ## 주문시장코드@@
                "ordno1": "ordno1`char", ## 주문번호@@
                "ordno": "ordno`long", ## 주문번호@@
                "orgordno1": "orgordno1`char", ## 원주문번호@@
                "orgordno": "orgordno`long", ## 원주문번호@@
                "prntordno": "prntordno`char", ## 모주문번호@@
                "prntordno1": "prntordno1`long", ## 모주문번호@@
                "isuno": "isuno`char", ## 종목번호@@
                "fnoIsuno": "fnoIsuno`char", ## 선물옵션종목번호@@
                "fnoIsunm": "fnoIsunm`char", ## 선물옵션종목명@@
                "pdgrpcode": "pdgrpcode`char", ## 상품군분류코드@@
                "fnoIsuptntp": "fnoIsuptntp`char", ## 선물옵션종목유형구분@@
                "bnstp": "bnstp`char", ## 매매구분@@
                "mrctp": "mrctp`char", ## 정정취소구분@@
                "ordqty": "ordqty`long", ## 주문수량@@
                "hogatype": "hogatype`char", ## 호가유형코드@@
                "mmgb": "mmgb`char", ## 거래유형코드@@
                "ordprc": "ordprc`double", ## 주문가격@@
                "unercqty": "unercqty`long", ## 미체결수량@@
                "commdacode": "commdacode`char", ## 통신매체@@
                "peeamtcode": "peeamtcode`char", ## 수수료합산코드@@
                "mgempno": "mgempno`char", ## 관리사원@@
                "fnotrdunitamt": "fnotrdunitamt`double", ## 선물옵션거래단위금액@@
                "trxtime": "trxtime`char", ## 처리시각@@
                "strtgcode": "strtgcode`char", ## 전략코드@@
                "grpId": "grpId`char", ## 그룹Id@@
                "ordseqno": "ordseqno`char", ## 주문회차@@
                "ptflno": "ptflno`char", ## 포트폴리오 번호@@
                "bskno": "bskno`char", ## 바스켓번호@@
                "trchno": "trchno`char", ## 트렌치번호@@
                "Itemno": "Itemno`char", ## 아이템번호@@
                "OrderID": "OrderID`char", ## 주문자Id@@
                "opdrtnno": "opdrtnno`char", ## 운영지시번호@@
                "rjtcode": "rjtcode`char", ## 부적격코드@@
                "mrccnfqty": "mrccnfqty`long", ## 정정취소확인수량@@
                "orgordunercqty": "orgordunercqty`long", ## 원주문미체결수량@@
                "orgordmrcqty": "orgordmrcqty`long", ## 원주문정정취소수량@@
                "ctrcttime": "ctrcttime`char", ## 약정시각(체결시각)@@
                "ctrctno": "ctrctno`char", ## 약정번호@@
                "execprc": "execprc`double", ## 체결가격@@
                "execqty": "execqty`long", ## 체결수량@@
                "newqty": "newqty`long", ## 신규체결수량@@
                "qdtqty": "qdtqty`long", ## 청산체결수량@@
                "lastqty": "lastqty`long", ## 최종결제수량@@
                "lallexecqty": "lallexecqty`long", ## 전체체결수량@@
                "allexecamt": "allexecamt`long", ## 전체체결금액@@
                "fnobalevaltp": "fnobalevaltp`char", ## 잔고평가구분@@
                "bnsplamt": "bnsplamt`long", ## 매매손익금액@@
                "fnoIsuno1": "fnoIsuno1`char", ## 선물옵션종목번호1@@
                "bnstp1": "bnstp1`char", ## 매매구분1@@
                "execprc1": "execprc1`double", ## 체결가1@@
                "newqty1": "newqty1`long", ## 신규체결수량1@@
                "qdtqty1": "qdtqty1`long", ## 청산체결수량1@@
                "allexecamt1": "allexecamt1`long", ## 전체체결금액1@@
                "fnoIsuno2": "fnoIsuno2`char", ## 선물옵션종목번호2@@
                "bnstp2": "bnstp2`char", ## 매매구분2@@
                "execprc2": "execprc2`double", ## 체결가2@@
                "newqty2": "newqty2`long", ## 신규체결수량2@@
                "lqdtqty2": "lqdtqty2`long", ## 청산체결수량2@@
                "allexecamt2": "allexecamt2`long", ## 전체체결금액2@@
                "dps": "dps`long", ## 예수금@@
                "ftsubtdsgnamt": "ftsubtdsgnamt`long", ## 선물대용지정금액@@
                "mgn": "mgn`long", ## 증거금@@
                "mnymgn": "mnymgn`long", ## 증거금현금@@
                "ordableamt": "ordableamt`long", ## 주문가능금액@@
                "mnyordableamt": "mnyordableamt`long", ## 주문가능현금액@@
                "fnoIsuno_1": "fnoIsuno_1`char", ## 잔고 종목번호1@@
                "bnstp_1": "bnstp_1`char", ## 잔고 매매구분1@@
                "unsttqty_1": "unsttqty_1`long", ## 미결제수량1@@
                "lqdtableqty_1": "lqdtableqty_1`long", ## 주문가능수량1@@
                "avrprc_1": "avrprc_1`double", ## 평균가1@@
                "fnoIsuno_2": "fnoIsuno_2`char", ## 잔고 종목번호2@@
                "bnstp_2": "bnstp_2`char", ## 잔고 매매구분2@@
                "unsttqty_2": "unsttqty_2`long", ## 미결제수량2@@
                "lqdtableqty_2": "lqdtableqty_2`long", ## 주문가능수량2@@
                "avrprc_2": "avrprc_2`double##평균가2@@"
            }
        }
    },
    "FC0": { ## KOSPI200선물체결(C0)
        "input": {
            "InBlock": {
                "futcode": " ##단축코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "chetime": "chetime`char", ## 체결시간@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`float", ## 전일대비@@
                "drate": "drate`float", ## 등락율@@
                "price": "price`float", ## 현재가@@
                "open": "open`float", ## 시가@@
                "high": "high`float", ## 고가@@
                "low": "low`float", ## 저가@@
                "cgubun": "cgubun`char", ## 체결구분@@
                "cvolume": "cvolume`long", ## 체결량@@
                "volume": "volume`long", ## 누적거래량@@
                "value": "value`long", ## 누적거래대금@@
                "mdvolume": "mdvolume`long", ## 매도누적체결량@@
                "mdchecnt": "mdchecnt`long", ## 매도누적체결건수@@
                "msvolume": "msvolume`long", ## 매수누적체결량@@
                "mschecnt": "mschecnt`long", ## 매수누적체결건수@@
                "cpower": "cpower`float", ## 체결강도@@
                "offerho1": "offerho1`float", ## 매도호가1@@
                "bidho1": "bidho1`float", ## 매수호가1@@
                "openyak": "openyak`long", ## 미결제약정수량@@
                "k200jisu": "k200jisu`float", ## KOSPI200지수@@
                "theoryprice": "theoryprice`float", ## 이론가@@
                "kasis": "kasis`float", ## 괴리율@@
                "sbasis": "sbasis`float", ## 시장BASIS@@
                "ibasis": "ibasis`float", ## 이론BASIS@@
                "openyakcha": "openyakcha`long", ## 미결제약정증감@@
                "jgubun": "jgubun`char", ## 장운영정보@@
                "jnilvolume": "jnilvolume`long", ## 전일동시간대거래량@@
                "futcode": "futcode`char##단축코드@@"
            }
        }
    },
    "FD0": { ## KOSPI200선물실시간상하한가(D0)
        "input": {
            "InBlock": {
                "futcode": " ##단축코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "gubun": "gubun`char", ## 접속매매여부@@
                "dy_gubun": "dy_gubun`char", ## 실시간가격제한여부@@
                "dy_uplmtprice": "dy_uplmtprice`float", ## 실시간상한가@@
                "dy_dnlmtprice": "dy_dnlmtprice`float", ## 실시간하한가@@
                "futcode": "futcode`char##단축코드@@"
            }
        }
    },
    "FH0": { ## KOSPI200선물호가(H0)
        "input": {
            "InBlock": {
                "futcode": " ##단축코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "hotime": "hotime`char", ## 호가시간@@
                "offerho1": "offerho1`double", ## 매도호가1@@
                "bidho1": "bidho1`double", ## 매수호가1@@
                "offerrem1": "offerrem1`long", ## 매도호가수량1@@
                "bidrem1": "bidrem1`long", ## 매수호가수량1@@
                "offercnt1": "offercnt1`long", ## 매도호가건수1@@
                "bidcnt1": "bidcnt1`long", ## 매수호가건수1@@
                "offerho2": "offerho2`double", ## 매도호가2@@
                "bidho2": "bidho2`double", ## 매수호가2@@
                "offerrem2": "offerrem2`long", ## 매도호가수량2@@
                "bidrem2": "bidrem2`long", ## 매수호가수량2@@
                "offercnt2": "offercnt2`long", ## 매도호가건수2@@
                "bidcnt2": "bidcnt2`long", ## 매수호가건수2@@
                "offerho3": "offerho3`double", ## 매도호가3@@
                "bidho3": "bidho3`double", ## 매수호가3@@
                "offerrem3": "offerrem3`long", ## 매도호가수량3@@
                "bidrem3": "bidrem3`long", ## 매수호가수량3@@
                "offercnt3": "offercnt3`long", ## 매도호가건수3@@
                "bidcnt3": "bidcnt3`long", ## 매수호가건수3@@
                "offerho4": "offerho4`double", ## 매도호가4@@
                "bidho4": "bidho4`double", ## 매수호가4@@
                "offerrem4": "offerrem4`long", ## 매도호가수량4@@
                "bidrem4": "bidrem4`long", ## 매수호가수량4@@
                "offercnt4": "offercnt4`long", ## 매도호가건수4@@
                "bidcnt4": "bidcnt4`long", ## 매수호가건수4@@
                "offerho5": "offerho5`double", ## 매도호가5@@
                "bidho5": "bidho5`double", ## 매수호가5@@
                "offerrem5": "offerrem5`long", ## 매도호가수량5@@
                "bidrem5": "bidrem5`long", ## 매수호가수량5@@
                "offercnt5": "offercnt5`long", ## 매도호가건수5@@
                "bidcnt5": "bidcnt5`long", ## 매수호가건수5@@
                "totofferrem": "totofferrem`long", ## 매도호가총수량@@
                "totbidrem": "totbidrem`long", ## 매수호가총수량@@
                "totoffercnt": "totoffercnt`long", ## 매도호가총건수@@
                "totbidcnt": "totbidcnt`long", ## 매수호가총건수@@
                "futcode": "futcode`char", ## 단축코드@@
                "danhochk": "danhochk`char", ## 단일가호가여부@@
                "alloc_gubun": "alloc_gubun`char##배분적용구분@@"
            }
        }
    },
    "FOCCQ33600": { ## 주식계좌 기간별수익률 상세
        "input": {
            "FOCCQ33600InBlock1": {
                "RecCnt": "0", ## 레코드갯수@@
                "AcntNo": " ", ## 계좌번호@@
                "Pwd": " ", ## 비밀번호@@
                "QrySrtDt": " ", ## 조회시작일@@
                "QryEndDt": " ", ## 조회종료일@@
                "TermTp": " ##기간구분@@"
            }
        },
        "output": {
            "FOCCQ33600OutBlock1": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "AcntNo": "AcntNo`char", ## 계좌번호@@
                "Pwd": "Pwd`char", ## 비밀번호@@
                "QrySrtDt": "QrySrtDt`char", ## 조회시작일@@
                "QryEndDt": "QryEndDt`char", ## 조회종료일@@
                "TermTp": "TermTp`char##기간구분@@"
            },
            "FOCCQ33600OutBlock2": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "AcntNm": "AcntNm`char", ## 계좌명@@
                "BnsctrAmt": "BnsctrAmt`long", ## 매매약정금액@@
                "MnyinAmt": "MnyinAmt`long", ## 입금금액@@
                "MnyoutAmt": "MnyoutAmt`long", ## 출금금액@@
                "InvstAvrbalPramt": "InvstAvrbalPramt`long", ## 투자원금평잔금액@@
                "InvstPlAmt": "InvstPlAmt`long", ## 투자손익금액@@
                "InvstErnrat": "InvstErnrat`double##투자수익률@@"
            },
            "FOCCQ33600OutBlock3": {
                "BaseDt": "BaseDt`char", ## 기준일@@
                "FdEvalAmt": "FdEvalAmt`long", ## 기초평가금액@@
                "EotEvalAmt": "EotEvalAmt`long", ## 기말평가금액@@
                "InvstAvrbalPramt": "InvstAvrbalPramt`long", ## 투자원금평잔금액@@
                "BnsctrAmt": "BnsctrAmt`long", ## 매매약정금액@@
                "MnyinSecinAmt": "MnyinSecinAmt`long", ## 입금고액@@
                "MnyoutSecoutAmt": "MnyoutSecoutAmt`long", ## 출금고액@@
                "EvalPnlAmt": "EvalPnlAmt`long", ## 평가손익금액@@
                "TermErnrat": "TermErnrat`double", ## 기간수익률@@
                "Idx": "Idx`double##지수@@"
            }
        }
    }
}
