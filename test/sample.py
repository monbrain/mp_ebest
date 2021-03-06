EBEST_API_SPECS = {
    "B7_": { ## ETF호가잔량(B7)
        "input": {
            "InBlock": {
                "shcode": " ##단축코드@@"
            }
        },
        "output": {
            "OutBlock": {
                # "hotime": "hotime`char", ## 호가시간@@
                # "lp_offerho1": "lp_offerho1`long", ## LP매도호가수량1@@
                # "lp_bidho1": "lp_bidho1`long", ## LP매수호가수량1@@
                "lp_offerho2": "lp_offerho2`long", ## LP매도호가수량2@@
                "lp_bidho2": "lp_bidho2`long", ## LP매수호가수량2@@
                "lp_offerho3": "lp_offerho3`long", ## LP매도호가수량3@@
                "lp_bidho3": "lp_bidho3`long", ## LP매수호가수량3@@
                "lp_offerho4": "lp_offerho4`long", ## LP매도호가수량4@@
                "lp_bidho4": "lp_bidho4`long", ## LP매수호가수량4@@
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
    },
    "FOCCQ33700": { ## 선물옵션 기간별 계좌 수익률 현황
        "input": {
            "FOCCQ33700InBlock1": {
                "RecCnt": "0", ## 레코드갯수@@
                "AcntNo": " ", ## 계좌번호@@
                "Pwd": " ", ## 비밀번호@@
                "QrySrtDt": " ", ## 조회시작일@@
                "QryEndDt": " ", ## 조회종료일@@
                "QryTp": " ", ## 조회구분@@
                "BaseAmtTp": " ", ## 기준금액구분@@
                "QryTermTp": " ", ## 조회기간구분@@
                "PnlCalcTpCode": " ##손익산출구분코드@@"
            }
        },
        "output": {
            "FOCCQ33700OutBlock1": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "AcntNo": "AcntNo`char", ## 계좌번호@@
                "Pwd": "Pwd`char", ## 비밀번호@@
                "QrySrtDt": "QrySrtDt`char", ## 조회시작일@@
                "QryEndDt": "QryEndDt`char", ## 조회종료일@@
                "QryTp": "QryTp`char", ## 조회구분@@
                "BaseAmtTp": "BaseAmtTp`char", ## 기준금액구분@@
                "QryTermTp": "QryTermTp`char", ## 조회기간구분@@
                "PnlCalcTpCode": "PnlCalcTpCode`char##손익산출구분코드@@"
            },
            "FOCCQ33700OutBlock2": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "AcntNm": "AcntNm`char", ## 계좌명@@
                "InAmt": "InAmt`long", ## 입금액@@
                "OutAmt": "OutAmt`long", ## 출금액@@
                "FnoCtrctAmt": "FnoCtrctAmt`long", ## 선물옵션약정금액@@
                "InvstPramtAvrbalAmt": "InvstPramtAvrbalAmt`long", ## 투자원금평잔금액@@
                "FutsAdjstDfamt": "FutsAdjstDfamt`long", ## 선물정산차금@@
                "OptBsnPnlAmt": "OptBsnPnlAmt`long", ## 옵션매매손익금액@@
                "OptEvalPnlAmt": "OptEvalPnlAmt`long", ## 옵션평가손익금액@@
                "InvstPlAmt": "InvstPlAmt`long", ## 투자손익금액@@
                "ErnRat": "ErnRat`double##수익률@@"
            },
            "FOCCQ33700OutBlock3": {
                "TrdDt": "TrdDt`char", ## 거래일@@
                "FdDpsastAmt": "FdDpsastAmt`long", ## 기초예탁자산금액@@
                "EotDpsastAmt": "EotDpsastAmt`long", ## 기말예탁자산금액@@
                "InAmt": "InAmt`long", ## 입금액@@
                "OutAmt": "OutAmt`long", ## 출금액@@
                "InvstAvrbalPramt": "InvstAvrbalPramt`long", ## 투자원금평잔금액@@
                "InvstPlAmt": "InvstPlAmt`long", ## 투자손익금액@@
                "Ernrat": "Ernrat`double", ## 수익률@@
                "FnoCtrctAmt": "FnoCtrctAmt`long", ## 선물옵션약정금액@@
                "Trnrat": "Trnrat`double", ## 회전율@@
                "FutsAdjstDfamt": "FutsAdjstDfamt`long", ## 선물정산차금@@
                "OptBsnPnlAmt": "OptBsnPnlAmt`long", ## 옵션매매손익금액@@
                "OptEvalPnlAmt": "OptEvalPnlAmt`long##옵션평가손익금액@@"
            }
        }
    },
    "FX0": { ## KOSPI200선물가격제한폭확대(X0)
        "input": {
            "InBlock": {
                "futcode": " ##단축코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "upstep": "upstep`char", ## 적용 상한단계@@
                "dnstep": "dnstep`char", ## 적용 하한단계@@
                "uplmtprice": "uplmtprice`float", ## 적용 상한가@@
                "dnlmtprice": "dnlmtprice`float", ## 적용 하한가@@
                "futcode": "futcode`char##단축코드@@"
            }
        }
    },
    "H01": { ## 선물주문정정취소
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
                "dosugb": "dosugb`char", ## 매도수구분@@
                "mocagb": "mocagb`char", ## 정정취소구분@@
                "accno1": "accno1`char", ## 계좌번호1@@
                "qty2": "qty2`long", ## 호가수량@@
                "price": "price`float", ## 호가가격@@
                "ordgb": "ordgb`char", ## 주문유형@@
                "hogagb": "hogagb`char", ## 호가구분@@
                "sihogagb": "sihogagb`char", ## 시장조성호가구분@@
                "treaid": "treaid`char", ## 자사주신고서ID@@
                "treacode": "treacode`char", ## 자사주매매방법@@
                "askcode": "askcode`char", ## 매도유형코드@@
                "creditcode": "creditcode`char", ## 신용구분코드@@
                "jakigb": "jakigb`char", ## 위탁자기구분@@
                "trustnum": "trustnum`char", ## 위탁사번호@@
                "ptgb": "ptgb`char", ## 프로그램구분@@
                "substocnum": "substocnum`char", ## 대용주권계좌번호@@
                "accgb": "accgb`char", ## 계좌구분코드@@
                "accmarggb": "accmarggb`char", ## 계좌증거금코드@@
                "nationcode": "nationcode`char", ## 국가코드@@
                "investgb": "investgb`char", ## 투자자구분@@
                "forecode": "forecode`char", ## 외국인코드@@
                "medcode": "medcode`char", ## 주문매체구분@@
                "ordid": "ordid`char", ## 주문식별자번호@@
                "macid": "macid`char", ## MAC주소@@
                "orddate": "orddate`char", ## 호가일자@@
                "rcvtime": "rcvtime`char", ## 회원사주문시각@@
                "mem_filler": "mem_filler`char", ## mem_filler1@@
                "mem_accno": "mem_accno`char", ## mem_accno@@
                "ordacpttm": "ordacpttm`char", ## 매칭접수시간@@
                "qty": "qty`long", ## 실정정취소수량@@
                "autogb": "autogb`char", ## 자동취소구분@@
                "rejcode": "rejcode`char", ## 거부사유@@
                "prgordde": "prgordde`char##프로그램호가신고@@"
            }
        }
    },
    "H1_": { ## KOSPI호가잔량(H1)
        "input": {
            "InBlock": {
                "shcode": " ##단축코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "hotime": "hotime`char", ## 호가시간@@
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
                "shcode": "shcode`char", ## 단축코드@@
                "alloc_gubun": "alloc_gubun`char##배분적용구분@@"
            }
        }
    },
    "H2_": { ## KOSPI장전시간외호가잔량(H2)
        "input": {
            "InBlock": {
                "shcode": " ##단축코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "hotime": "hotime`char", ## 호가시간@@
                "tmofferrem": "tmofferrem`long", ## 시간외매도잔량@@
                "tmbidrem": "tmbidrem`long", ## 시간외매수잔량@@
                "pretmoffercha": "pretmoffercha`long", ## 시간외매도수량직전대비@@
                "pretmbidcha": "pretmbidcha`long", ## 시간외매수수량직전대비@@
                "shcode": "shcode`char##단축코드@@"
            }
        }
    },
    "h2_4ELW": { ## ELW장전시간외호가잔량(h2)
        "input": {
            "InBlock": {
                "shcode": " ##단축코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "hotime": "hotime`char", ## 호가시간@@
                "tmofferrem": "tmofferrem`long", ## 시간외매도잔량@@
                "tmbidrem": "tmbidrem`long", ## 시간외매수잔량@@
                "pretmoffercha": "pretmoffercha`long", ## 시간외매도수량직전대비@@
                "pretmbidcha": "pretmbidcha`long", ## 시간외매수수량직전대비@@
                "shcode": "shcode`char##단축코드@@"
            }
        }
    },
    "h3_4ELW": { ## ELW호가잔량(h3)
        "input": {
            "InBlock": {
                "shcode": " ##단축코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "hotime": "hotime`char", ## 호가시간@@
                "offerho1": "offerho1`long", ## 매도호가1@@
                "bidho1": "bidho1`long", ## 매수호가1@@
                "offerrem1": "offerrem1`long", ## 매도호가잔량1@@
                "bidrem1": "bidrem1`long", ## 매수호가잔량1@@
                "lp_offerho1": "lp_offerho1`long", ## LP매도호가수량1@@
                "lp_bidho1": "lp_bidho1`long", ## LP매수호가수량1@@
                "offerho2": "offerho2`long", ## 매도호가2@@
                "bidho2": "bidho2`long", ## 매수호가2@@
                "offerrem2": "offerrem2`long", ## 매도호가잔량2@@
                "bidrem2": "bidrem2`long", ## 매수호가잔량2@@
                "lp_offerho2": "lp_offerho2`long", ## LP매도호가수량2@@
                "lp_bidho2": "lp_bidho2`long", ## LP매수호가수량2@@
                "offerho3": "offerho3`long", ## 매도호가3@@
                "bidho3": "bidho3`long", ## 매수호가3@@
                "offerrem3": "offerrem3`long", ## 매도호가잔량3@@
                "bidrem3": "bidrem3`long", ## 매수호가잔량3@@
                "lp_offerho3": "lp_offerho3`long", ## LP매도호가수량3@@
                "lp_bidho3": "lp_bidho3`long", ## LP매수호가수량3@@
                "offerho4": "offerho4`long", ## 매도호가4@@
                "bidho4": "bidho4`long", ## 매수호가4@@
                "offerrem4": "offerrem4`long", ## 매도호가잔량4@@
                "bidrem4": "bidrem4`long", ## 매수호가잔량4@@
                "lp_offerho4": "lp_offerho4`long", ## LP매도호가수량4@@
                "lp_bidho4": "lp_bidho4`long", ## LP매수호가수량4@@
                "offerho5": "offerho5`long", ## 매도호가5@@
                "bidho5": "bidho5`long", ## 매수호가5@@
                "offerrem5": "offerrem5`long", ## 매도호가잔량5@@
                "bidrem5": "bidrem5`long", ## 매수호가잔량5@@
                "lp_offerho5": "lp_offerho5`long", ## LP매도호가수량5@@
                "lp_bidho5": "lp_bidho5`long", ## LP매수호가수량5@@
                "offerho6": "offerho6`long", ## 매도호가6@@
                "bidho6": "bidho6`long", ## 매수호가6@@
                "offerrem6": "offerrem6`long", ## 매도호가잔량6@@
                "bidrem6": "bidrem6`long", ## 매수호가잔량6@@
                "lp_offerho6": "lp_offerho6`long", ## LP매도호가수량6@@
                "lp_bidho6": "lp_bidho6`long", ## LP매수호가수량6@@
                "offerho7": "offerho7`long", ## 매도호가7@@
                "bidho7": "bidho7`long", ## 매수호가7@@
                "offerrem7": "offerrem7`long", ## 매도호가잔량7@@
                "bidrem7": "bidrem7`long", ## 매수호가잔량7@@
                "lp_offerho7": "lp_offerho7`long", ## LP매도호가수량7@@
                "lp_bidho7": "lp_bidho7`long", ## LP매수호가수량7@@
                "offerho8": "offerho8`long", ## 매도호가8@@
                "bidho8": "bidho8`long", ## 매수호가8@@
                "offerrem8": "offerrem8`long", ## 매도호가잔량8@@
                "bidrem8": "bidrem8`long", ## 매수호가잔량8@@
                "lp_offerho8": "lp_offerho8`long", ## LP매도호가수량8@@
                "lp_bidho8": "lp_bidho8`long", ## LP매수호가수량8@@
                "offerho9": "offerho9`long", ## 매도호가9@@
                "bidho9": "bidho9`long", ## 매수호가9@@
                "offerrem9": "offerrem9`long", ## 매도호가잔량9@@
                "bidrem9": "bidrem9`long", ## 매수호가잔량9@@
                "lp_offerho9": "lp_offerho9`long", ## LP매도호가수량9@@
                "lp_bidho9": "lp_bidho9`long", ## LP매수호가수량9@@
                "offerho10": "offerho10`long", ## 매도호가10@@
                "bidho10": "bidho10`long", ## 매수호가10@@
                "offerrem10": "offerrem10`long", ## 매도호가잔량10@@
                "bidrem10": "bidrem10`long", ## 매수호가잔량10@@
                "lp_offerho10": "lp_offerho10`long", ## LP매도호가수량10@@
                "lp_bidho10": "lp_bidho10`long", ## LP매수호가수량10@@
                "totofferrem": "totofferrem`long", ## 총매도호가잔량@@
                "totbidrem": "totbidrem`long", ## 총매수호가잔량@@
                "donsigubun": "donsigubun`char", ## 동시호가구분@@
                "spread": "spread`float", ## 스프레드@@
                "shcode": "shcode`char##단축코드@@"
            }
        }
    },
    "HA_": { ## KOSDAQ호가잔량(HA)
        "input": {
            "InBlock": {
                "shcode": " ##단축코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "hotime": "hotime`char", ## 호가시간@@
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
                "shcode": "shcode`char", ## 단축코드@@
                "alloc_gubun": "alloc_gubun`char##배분적용구분@@"
            }
        }
    },
    "HB_": { ## KOSDAQ장전시간외호가잔량(HB)
        "input": {
            "InBlock": {
                "shcode": " ##단축코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "hotime": "hotime`char", ## 호가시간@@
                "tmofferrem": "tmofferrem`long", ## 시간외매도잔량@@
                "tmbidrem": "tmbidrem`long", ## 시간외매수잔량@@
                "pretmoffercha": "pretmoffercha`long", ## 시간외매도수량직전대비@@
                "pretmbidcha": "pretmbidcha`long", ## 시간외매수수량직전대비@@
                "shcode": "shcode`char##단축코드@@"
            }
        }
    },
    "I5_": { ## 코스피ETF종목실시간NAV(I5)
        "input": {
            "InBlock": {
                "shcode": " ##단축코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "time": "time`char", ## 시간@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "volume": "volume`float", ## 누적거래량@@
                "navdiff": "navdiff`float", ## NAV대비@@
                "nav": "nav`float", ## NAV@@
                "navchange": "navchange`float", ## 전일대비@@
                "crate": "crate`float", ## 추적오차@@
                "grate": "grate`float", ## 괴리@@
                "jisu": "jisu`float", ## 지수@@
                "jichange": "jichange`float", ## 전일대비@@
                "jirate": "jirate`float", ## 전일대비율@@
                "shcode": "shcode`char##단축코드@@"
            }
        }
    },
    "IJ_": { ## 지수(IJ)
        "input": {
            "InBlock": {
                "upcode": " ##업종코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "time": "time`char", ## 시간@@
                "jisu": "jisu`float", ## 지수@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`float", ## 전일비@@
                "drate": "drate`float", ## 등락율@@
                "cvolume": "cvolume`long", ## 체결량@@
                "volume": "volume`long", ## 거래량@@
                "value": "value`long", ## 거래대금@@
                "upjo": "upjo`long", ## 상한종목수@@
                "highjo": "highjo`long", ## 상승종목수@@
                "unchgjo": "unchgjo`long", ## 보합종목수@@
                "lowjo": "lowjo`long", ## 하락종목수@@
                "downjo": "downjo`long", ## 하한종목수@@
                "upjrate": "upjrate`float", ## 상승종목비율@@
                "openjisu": "openjisu`float", ## 시가지수@@
                "opentime": "opentime`char", ## 시가시간@@
                "highjisu": "highjisu`float", ## 고가지수@@
                "hightime": "hightime`char", ## 고가시간@@
                "lowjisu": "lowjisu`float", ## 저가지수@@
                "lowtime": "lowtime`char", ## 저가시간@@
                "frgsvolume": "frgsvolume`long", ## 외인순매수수량@@
                "orgsvolume": "orgsvolume`long", ## 기관순매수수량@@
                "frgsvalue": "frgsvalue`long", ## 외인순매수금액@@
                "orgsvalue": "orgsvalue`long", ## 기관순매수금액@@
                "upcode": "upcode`char##업종코드@@"
            }
        }
    },
    "JC0": { ## 주식선물체결(JC0)
        "input": {
            "InBlock": {
                "futcode": " ##단축코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "futcode": "futcode`char", ## 단축코드@@
                "chetime": "chetime`char", ## 체결시간@@
                "sign": "sign`char", ## 대비기호@@
                "change": "change`long", ## 전일대비@@
                "drate": "drate`double", ## 등락율@@
                "price": "price`long", ## 현재가@@
                "open": "open`long", ## 시가@@
                "high": "high`long", ## 고가@@
                "low": "low`long", ## 저가@@
                "cgubun": "cgubun`char", ## 체결구분@@
                "cvolume": "cvolume`long", ## 체결량@@
                "volume": "volume`long", ## 누적거래량@@
                "value": "value`long", ## 누적거래대금@@
                "mdvolume": "mdvolume`long", ## 매도누적체결량@@
                "mdchecnt": "mdchecnt`long", ## 매도누적체결건수@@
                "msvolume": "msvolume`long", ## 매수누적체결량@@
                "mschecnt": "mschecnt`long", ## 매수누적체결건수@@
                "cpower": "cpower`double", ## 체결강도@@
                "offerho1": "offerho1`long", ## 매도호가1@@
                "bidho1": "bidho1`long", ## 매수호가1@@
                "openyak": "openyak`long", ## 미결제약정수량@@
                "k200jisu": "k200jisu`double", ## KOSPI200지수@@
                "theoryprice": "theoryprice`long", ## 이론가@@
                "kasis": "kasis`double", ## 괴리율@@
                "sbasis": "sbasis`long", ## 시장BASIS@@
                "ibasis": "ibasis`long", ## 이론BASIS@@
                "openyakcha": "openyakcha`long", ## 미결제약정증감@@
                "jgubun": "jgubun`char", ## 장운영정보@@
                "jnilvolume": "jnilvolume`long", ## 전일동시간대거래량@@
                "basprice": "basprice`long##기초자산현재가@@"
            }
        }
    },
    "JD0": { ## 주식선물실시간상하한가(JD0)
        "input": {
            "InBlock": {
                "futcode": " ##단축코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "gubun": "gubun`char", ## 접속매매여부@@
                "dy_gubun": "dy_gubun`char", ## 실시간가격제한여부@@
                "dy_uplmtprice": "dy_uplmtprice`long", ## 실시간상한가@@
                "dy_dnlmtprice": "dy_dnlmtprice`long", ## 실시간하한가@@
                "futcode": "futcode`char##단축코드@@"
            }
        }
    },
    "JH0": { ## 주식선물호가(JH0)
        "input": {
            "InBlock": {
                "futcode": " ##단축코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "futcode": "futcode`char", ## 단축코드@@
                "hotime": "hotime`char", ## 호가시간@@
                "offerho1": "offerho1`long", ## 매도호가1@@
                "bidho1": "bidho1`long", ## 매수호가1@@
                "offerrem1": "offerrem1`long", ## 매도호가수량1@@
                "bidrem1": "bidrem1`long", ## 매수호가수량1@@
                "offercnt1": "offercnt1`long", ## 매도호가건수1@@
                "bidcnt1": "bidcnt1`long", ## 매수호가건수1@@
                "offerho2": "offerho2`long", ## 매도호가2@@
                "bidho2": "bidho2`long", ## 매수호가2@@
                "offerrem2": "offerrem2`long", ## 매도호가수량2@@
                "bidrem2": "bidrem2`long", ## 매수호가수량2@@
                "offercnt2": "offercnt2`long", ## 매도호가건수2@@
                "bidcnt2": "bidcnt2`long", ## 매수호가건수2@@
                "offerho3": "offerho3`long", ## 매도호가3@@
                "bidho3": "bidho3`long", ## 매수호가3@@
                "offerrem3": "offerrem3`long", ## 매도호가수량3@@
                "bidrem3": "bidrem3`long", ## 매수호가수량3@@
                "offercnt3": "offercnt3`long", ## 매도호가건수3@@
                "bidcnt3": "bidcnt3`long", ## 매수호가건수3@@
                "offerho4": "offerho4`long", ## 매도호가4@@
                "bidho4": "bidho4`long", ## 매수호가4@@
                "offerrem4": "offerrem4`long", ## 매도호가수량4@@
                "bidrem4": "bidrem4`long", ## 매수호가수량4@@
                "offercnt4": "offercnt4`long", ## 매도호가건수4@@
                "bidcnt4": "bidcnt4`long", ## 매수호가건수4@@
                "offerho5": "offerho5`long", ## 매도호가5@@
                "bidho5": "bidho5`long", ## 매수호가5@@
                "offerrem5": "offerrem5`long", ## 매도호가수량5@@
                "bidrem5": "bidrem5`long", ## 매수호가수량5@@
                "offercnt5": "offercnt5`long", ## 매도호가건수5@@
                "bidcnt5": "bidcnt5`long", ## 매수호가건수5@@
                "offerho6": "offerho6`long", ## 매도호가6@@
                "bidho6": "bidho6`long", ## 매수호가6@@
                "offerrem6": "offerrem6`long", ## 매도호가수량6@@
                "bidrem6": "bidrem6`long", ## 매수호가수량6@@
                "offercnt6": "offercnt6`long", ## 매도호가건수6@@
                "bidcnt6": "bidcnt6`long", ## 매수호가건수6@@
                "offerho7": "offerho7`long", ## 매도호가7@@
                "bidho7": "bidho7`long", ## 매수호가7@@
                "offerrem7": "offerrem7`long", ## 매도호가수량7@@
                "bidrem7": "bidrem7`long", ## 매수호가수량7@@
                "offercnt7": "offercnt7`long", ## 매도호가건수7@@
                "bidcnt7": "bidcnt7`long", ## 매수호가건수7@@
                "offerho8": "offerho8`long", ## 매도호가8@@
                "bidho8": "bidho8`long", ## 매수호가8@@
                "offerrem8": "offerrem8`long", ## 매도호가수량8@@
                "bidrem8": "bidrem8`long", ## 매수호가수량8@@
                "offercnt8": "offercnt8`long", ## 매도호가건수8@@
                "bidcnt8": "bidcnt8`long", ## 매수호가건수8@@
                "offerho9": "offerho9`long", ## 매도호가9@@
                "bidho9": "bidho9`long", ## 매수호가9@@
                "offerrem9": "offerrem9`long", ## 매도호가수량9@@
                "bidrem9": "bidrem9`long", ## 매수호가수량9@@
                "offercnt9": "offercnt9`long", ## 매도호가건수9@@
                "bidcnt9": "bidcnt9`long", ## 매수호가건수9@@
                "offerho10": "offerho10`long", ## 매도호가10@@
                "bidho10": "bidho10`long", ## 매수호가10@@
                "offerrem10": "offerrem10`long", ## 매도호가수량10@@
                "bidrem10": "bidrem10`long", ## 매수호가수량10@@
                "offercnt10": "offercnt10`long", ## 매도호가건수10@@
                "bidcnt10": "bidcnt10`long", ## 매수호가건수10@@
                "totofferrem": "totofferrem`long", ## 매도호가총수량@@
                "totbidrem": "totbidrem`long", ## 매수호가총수량@@
                "totoffercnt": "totoffercnt`long", ## 매도호가총건수@@
                "totbidcnt": "totbidcnt`long", ## 매수호가총건수@@
                "danhochk": "danhochk`char", ## 단일가호가여부@@
                "alloc_gubun": "alloc_gubun`char##배분적용구분@@"
            }
        }
    },
    "JIF": { ## 장운영정보(JIF)
        "input": {
            "InBlock": {
                "jangubun": " ##장구분@@"
            }
        },
        "output": {
            "OutBlock": {
                "jangubun": "jangubun`char", ## 장구분@@
                "jstatus": "jstatus`char##장상태@@"
            }
        }
    },
    "JX0": { ## 주식선물가격제한폭확대(JX0)
        "input": {
            "InBlock": {
                "futcode": " ##단축코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "upstep": "upstep`char", ## 적용 상한단계@@
                "dnstep": "dnstep`char", ## 적용 하한단계@@
                "uplmtprice": "uplmtprice`long", ## 적용 상한가@@
                "dnlmtprice": "dnlmtprice`long", ## 적용 하한가@@
                "futcode": "futcode`char##단축코드@@"
            }
        }
    },
    "K1_": { ## KOSPI거래원(K1)
        "input": {
            "InBlock": {
                "shcode": " ##단축코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "offerno1": "offerno1`char", ## 매도증권사코드1@@
                "bidno1": "bidno1`char", ## 매수증권사코드1@@
                "offertrad1": "offertrad1`char", ## 매도회원사명1@@
                "bidtrad1": "bidtrad1`char", ## 매수회원사명1@@
                "tradmdvol1": "tradmdvol1`long", ## 매도거래량1@@
                "tradmsvol1": "tradmsvol1`long", ## 매수거래량1@@
                "tradmdrate1": "tradmdrate1`float", ## 매도거래량비중1@@
                "tradmsrate1": "tradmsrate1`float", ## 매도거래량비중1@@
                "tradmdcha1": "tradmdcha1`long", ## 매도거래량직전대비1@@
                "tradmscha1": "tradmscha1`long", ## 매수거래량직전대비1@@
                "offerno2": "offerno2`char", ## 매도증권사코드2@@
                "bidno2": "bidno2`char", ## 매수증권사코드2@@
                "offertrad2": "offertrad2`char", ## 매도회원사명2@@
                "bidtrad2": "bidtrad2`char", ## 매수회원사명2@@
                "tradmdvol2": "tradmdvol2`long", ## 매도거래량2@@
                "tradmsvol2": "tradmsvol2`long", ## 매수거래량2@@
                "tradmdrate2": "tradmdrate2`float", ## 매도거래량비중2@@
                "tradmsrate2": "tradmsrate2`float", ## 매수거래량비중2@@
                "tradmdcha2": "tradmdcha2`long", ## 매도거래량직전대비2@@
                "tradmscha2": "tradmscha2`long", ## 매수거래량직전대비2@@
                "offerno3": "offerno3`char", ## 매도증권사코드3@@
                "bidno3": "bidno3`char", ## 매수증권사코드3@@
                "offertrad3": "offertrad3`char", ## 매도회원사명3@@
                "bidtrad3": "bidtrad3`char", ## 매수회원사명3@@
                "tradmdvol3": "tradmdvol3`long", ## 매도거래량3@@
                "tradmsvol3": "tradmsvol3`long", ## 매수거래량3@@
                "tradmdrate3": "tradmdrate3`float", ## 매도거래량비중3@@
                "tradmsrate3": "tradmsrate3`float", ## 매수거래량비중3@@
                "tradmdcha3": "tradmdcha3`long", ## 매도거래량직전대비3@@
                "tradmscha3": "tradmscha3`long", ## 매수거래량직전대비3@@
                "offerno4": "offerno4`char", ## 매도증권사코드4@@
                "bidno4": "bidno4`char", ## 매수증권사코드4@@
                "offertrad4": "offertrad4`char", ## 매도회원사명4@@
                "bidtrad4": "bidtrad4`char", ## 매수회원사명4@@
                "tradmdvol4": "tradmdvol4`long", ## 매도거래량4@@
                "tradmsvol4": "tradmsvol4`long", ## 매수거래량4@@
                "tradmdrate4": "tradmdrate4`float", ## 매도거래량비중4@@
                "tradmsrate4": "tradmsrate4`float", ## 매수거래량비중4@@
                "tradmdcha4": "tradmdcha4`long", ## 매도거래량직전대비4@@
                "tradmscha4": "tradmscha4`long", ## 매수거래량직전대비4@@
                "offerno5": "offerno5`char", ## 매도증권사코드5@@
                "bidno5": "bidno5`char", ## 매수증권사코드5@@
                "offertrad5": "offertrad5`char", ## 매도회원사명5@@
                "bidtrad5": "bidtrad5`char", ## 매수회원사명5@@
                "tradmdvol5": "tradmdvol5`long", ## 매도거래량5@@
                "tradmsvol5": "tradmsvol5`long", ## 매수거래량5@@
                "tradmdrate5": "tradmdrate5`float", ## 매도거래량비중5@@
                "tradmsrate5": "tradmsrate5`float", ## 매수거래량비중5@@
                "tradmdcha5": "tradmdcha5`long", ## 매도거래량직전대비5@@
                "tradmscha5": "tradmscha5`long", ## 매수거래량직전대비5@@
                "ftradmdvol": "ftradmdvol`char", ## 외국계증권사매도합계@@
                "ftradmsvol": "ftradmsvol`char", ## 외국계증권사매수합계@@
                "ftradmdrate": "ftradmdrate`float", ## 외국계증권사매도거래량비중@@
                "ftradmsrate": "ftradmsrate`float", ## 외국계증권사매수거래량비중@@
                "ftradmdcha": "ftradmdcha`char", ## 외국계증권사매도거래량직전대비@@
                "ftradmscha": "ftradmscha`char", ## 외국계증권사매수거래량직전대비@@
                "shcode": "shcode`char", ## 단축코드@@
                "tradmdval1": "tradmdval1`long", ## 매도거래대금1@@
                "tradmsval1": "tradmsval1`long", ## 매수거래대금1@@
                "tradmdavg1": "tradmdavg1`long", ## 매도평균단가1@@
                "tradmsavg1": "tradmsavg1`long", ## 매수평균단가1@@
                "tradmdval2": "tradmdval2`long", ## 매도거래대금2@@
                "tradmsval2": "tradmsval2`long", ## 매수거래대금2@@
                "tradmdavg2": "tradmdavg2`long", ## 매도평균단가2@@
                "tradmsavg2": "tradmsavg2`long", ## 매수평균단가2@@
                "tradmdval3": "tradmdval3`long", ## 매도거래대금3@@
                "tradmsval3": "tradmsval3`long", ## 매수거래대금3@@
                "tradmdavg3": "tradmdavg3`long", ## 매도평균단가3@@
                "tradmsavg3": "tradmsavg3`long", ## 매수평균단가3@@
                "tradmdval4": "tradmdval4`long", ## 매도거래대금4@@
                "tradmsval4": "tradmsval4`long", ## 매수거래대금4@@
                "tradmdavg4": "tradmdavg4`long", ## 매도평균단가4@@
                "tradmsavg4": "tradmsavg4`long", ## 매수평균단가4@@
                "tradmdval5": "tradmdval5`long", ## 매도거래대금5@@
                "tradmsval5": "tradmsval5`long", ## 매수거래대금5@@
                "tradmdavg5": "tradmdavg5`long", ## 매도평균단가5@@
                "tradmsavg5": "tradmsavg5`long", ## 매수평균단가5@@
                "ftradmdval": "ftradmdval`long", ## 외국계증권사매도거래대금@@
                "ftradmsval": "ftradmsval`long", ## 외국계증권사매수거래대금@@
                "ftradmdavg": "ftradmdavg`long", ## 외국계증권사매도평균단가@@
                "ftradmsavg": "ftradmsavg`long##외국계증권사매수평균단가@@"
            }
        }
    },
    "k1_4ELW": { ## ELW거래원(k1)
        "input": {
            "InBlock": {
                "shcode": " ##단축코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "offerno1": "offerno1`char", ## 매도증권사코드1@@
                "bidno1": "bidno1`char", ## 매수증권사코드1@@
                "offertrad1": "offertrad1`char", ## 매도회원사명1@@
                "bidtrad1": "bidtrad1`char", ## 매수회원사명1@@
                "tradmdvol1": "tradmdvol1`long", ## 매도거래량1@@
                "tradmsvol1": "tradmsvol1`long", ## 매수거래량1@@
                "tradmdrate1": "tradmdrate1`float", ## 매도거래량비중1@@
                "tradmsrate1": "tradmsrate1`float", ## 매도거래량비중1@@
                "tradmdcha1": "tradmdcha1`long", ## 매도거래량직전대비1@@
                "tradmscha1": "tradmscha1`long", ## 매수거래량직전대비1@@
                "offerno2": "offerno2`char", ## 매도증권사코드2@@
                "bidno2": "bidno2`char", ## 매수증권사코드2@@
                "offertrad2": "offertrad2`char", ## 매도회원사명2@@
                "bidtrad2": "bidtrad2`char", ## 매수회원사명2@@
                "tradmdvol2": "tradmdvol2`long", ## 매도거래량2@@
                "tradmsvol2": "tradmsvol2`long", ## 매수거래량2@@
                "tradmdrate2": "tradmdrate2`float", ## 매도거래량비중2@@
                "tradmsrate2": "tradmsrate2`float", ## 매수거래량비중2@@
                "tradmdcha2": "tradmdcha2`long", ## 매도거래량직전대비2@@
                "tradmscha2": "tradmscha2`long", ## 매수거래량직전대비2@@
                "offerno3": "offerno3`char", ## 매도증권사코드3@@
                "bidno3": "bidno3`char", ## 매수증권사코드3@@
                "offertrad3": "offertrad3`char", ## 매도회원사명3@@
                "bidtrad3": "bidtrad3`char", ## 매수회원사명3@@
                "tradmdvol3": "tradmdvol3`long", ## 매도거래량3@@
                "tradmsvol3": "tradmsvol3`long", ## 매수거래량3@@
                "tradmdrate3": "tradmdrate3`float", ## 매도거래량비중3@@
                "tradmsrate3": "tradmsrate3`float", ## 매수거래량비중3@@
                "tradmdcha3": "tradmdcha3`long", ## 매도거래량직전대비3@@
                "tradmscha3": "tradmscha3`long", ## 매수거래량직전대비3@@
                "offerno4": "offerno4`char", ## 매도증권사코드4@@
                "bidno4": "bidno4`char", ## 매수증권사코드4@@
                "offertrad4": "offertrad4`char", ## 매도회원사명4@@
                "bidtrad4": "bidtrad4`char", ## 매수회원사명4@@
                "tradmdvol4": "tradmdvol4`long", ## 매도거래량4@@
                "tradmsvol4": "tradmsvol4`long", ## 매수거래량4@@
                "tradmdrate4": "tradmdrate4`float", ## 매도거래량비중4@@
                "tradmsrate4": "tradmsrate4`float", ## 매수거래량비중4@@
                "tradmdcha4": "tradmdcha4`long", ## 매도거래량직전대비4@@
                "tradmscha4": "tradmscha4`long", ## 매수거래량직전대비4@@
                "offerno5": "offerno5`char", ## 매도증권사코드5@@
                "bidno5": "bidno5`char", ## 매수증권사코드5@@
                "offertrad5": "offertrad5`char", ## 매도회원사명5@@
                "bidtrad5": "bidtrad5`char", ## 매수회원사명5@@
                "tradmdvol5": "tradmdvol5`long", ## 매도거래량5@@
                "tradmsvol5": "tradmsvol5`long", ## 매수거래량5@@
                "tradmdrate5": "tradmdrate5`float", ## 매도거래량비중5@@
                "tradmsrate5": "tradmsrate5`float", ## 매수거래량비중5@@
                "tradmdcha5": "tradmdcha5`long", ## 매도거래량직전대비5@@
                "tradmscha5": "tradmscha5`long", ## 매수거래량직전대비5@@
                "ftradmdvol": "ftradmdvol`char", ## 외국계증권사매도합계@@
                "ftradmsvol": "ftradmsvol`char", ## 외국계증권사매수합계@@
                "ftradmdrate": "ftradmdrate`float", ## 외국계증권사매도거래량비중@@
                "ftradmsrate": "ftradmsrate`float", ## 외국계증권사매수거래량비중@@
                "ftradmdcha": "ftradmdcha`char", ## 외국계증권사매도거래량직전대비@@
                "ftradmscha": "ftradmscha`char", ## 외국계증권사매수거래량직전대비@@
                "shcode": "shcode`char##단축코드@@"
            }
        }
    },
    "K3_": { ## KOSDAQ체결(K3)
        "input": {
            "InBlock": {
                "shcode": " ##단축코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "chetime": "chetime`char", ## 체결시간@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "drate": "drate`float", ## 등락율@@
                "price": "price`long", ## 현재가@@
                "opentime": "opentime`char", ## 시가시간@@
                "open": "open`long", ## 시가@@
                "hightime": "hightime`char", ## 고가시간@@
                "high": "high`long", ## 고가@@
                "lowtime": "lowtime`char", ## 저가시간@@
                "low": "low`long", ## 저가@@
                "cgubun": "cgubun`char", ## 체결구분@@
                "cvolume": "cvolume`long", ## 체결량@@
                "volume": "volume`long", ## 누적거래량@@
                "value": "value`long", ## 누적거래대금@@
                "mdvolume": "mdvolume`long", ## 매도누적체결량@@
                "mdchecnt": "mdchecnt`long", ## 매도누적체결건수@@
                "msvolume": "msvolume`long", ## 매수누적체결량@@
                "mschecnt": "mschecnt`long", ## 매수누적체결건수@@
                "cpower": "cpower`float", ## 체결강도@@
                "w_avrg": "w_avrg`long", ## 가중평균가@@
                "offerho": "offerho`long", ## 매도호가@@
                "bidho": "bidho`long", ## 매수호가@@
                "status": "status`char", ## 장정보@@
                "jnilvolume": "jnilvolume`long", ## 전일동시간대거래량@@
                "shcode": "shcode`char##단축코드@@"
            }
        }
    },
    "KH_": { ## KOSDAQ프로그램매매종목별(KH)
        "input": {
            "InBlock": {
                "shcode": " ##종목코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "time": "time`char", ## 수신시간@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`long", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "volume": "volume`long", ## 누적거래량@@
                "drate": "drate`float", ## 등락율@@
                "cdhrem": "cdhrem`long", ## 차익매도호가 잔량@@
                "cshrem": "cshrem`long", ## 차익매수호가 잔량@@
                "bdhrem": "bdhrem`long", ## 비차익매도호가 잔량@@
                "bshrem": "bshrem`long", ## 비차익매수호가 잔량@@
                "cdhvolume": "cdhvolume`long", ## 차익매도호가 수량@@
                "cshvolume": "cshvolume`long", ## 차익매수호가 수량@@
                "bdhvolume": "bdhvolume`long", ## 비차익매도호가 수량@@
                "bshvolume": "bshvolume`long", ## 비차익매수호가 수량@@
                "dwcvolume": "dwcvolume`long", ## 전체매도위탁체결수량@@
                "swcvolume": "swcvolume`long", ## 전체매수위탁체결수량@@
                "djcvolume": "djcvolume`long", ## 전체매도자기체결수량@@
                "sjcvolume": "sjcvolume`long", ## 전체매수자기체결수량@@
                "tdvolume": "tdvolume`long", ## 전체매도체결수량@@
                "tsvolume": "tsvolume`long", ## 전체매수체결수량@@
                "tvol": "tvol`long", ## 전체순매수 수량@@
                "dwcvalue": "dwcvalue`long", ## 전체매도위탁체결금액@@
                "swcvalue": "swcvalue`long", ## 전체매수위탁체결금액@@
                "djcvalue": "djcvalue`long", ## 전체매도자기체결금액@@
                "sjcvalue": "sjcvalue`long", ## 전체매수자기체결금액@@
                "tdvalue": "tdvalue`long", ## 전체매도체결금액@@
                "tsvalue": "tsvalue`long", ## 전체매수체결금액@@
                "tval": "tval`long", ## 전체순매수 금액@@
                "pdgvolume": "pdgvolume`long", ## 매도 사전공시수량@@
                "psgvolume": "psgvolume`long", ## 매수 사전공시수량@@
                "shcode": "shcode`char##종목코드@@"
            }
        }
    },
    "KM_": { ## KOSDAQ프로그램매매전체집계(KM)
        "input": {
            "InBlock": {
                "gubun": " ##구분값@@"
            }
        },
        "output": {
            "OutBlock": {
                "time": "time`char", ## 수신시간@@
                "cdhrem": "cdhrem`long", ## 차익매도호가 잔량@@
                "cshrem": "cshrem`long", ## 차익매수호가 잔량@@
                "bdhrem": "bdhrem`long", ## 비차익매도호가 잔량@@
                "bshrem": "bshrem`long", ## 비차익매수호가 잔량@@
                "cdhvolume": "cdhvolume`long", ## 차익매도호가 수량@@
                "cshvolume": "cshvolume`long", ## 차익매수호가 수량@@
                "bdhvolume": "bdhvolume`long", ## 비차익매도호가 수량@@
                "bshvolume": "bshvolume`long", ## 비차익매수호가 수량@@
                "cdwvolume": "cdwvolume`long", ## 차익매도위탁체결수량@@
                "cdjvolume": "cdjvolume`long", ## 차익매도자기체결수량@@
                "cswvolume": "cswvolume`long", ## 차익매수위탁체결수량@@
                "csjvolume": "csjvolume`long", ## 차익매수자기체결수량@@
                "cwvol": "cwvol`long", ## 차익위탁순매수 수량@@
                "cjvol": "cjvol`long", ## 차익자기순매수 수량@@
                "bdwvolume": "bdwvolume`long", ## 비차익매도위탁체결수량@@
                "bdjvolume": "bdjvolume`long", ## 비차익매도자기체결수량@@
                "bswvolume": "bswvolume`long", ## 비차익매수위탁체결수량@@
                "bsjvolume": "bsjvolume`long", ## 비차익매수자기체결수량@@
                "bwvol": "bwvol`long", ## 비차익위탁순매수 수량@@
                "bjvol": "bjvol`long", ## 비차익자기순매수 수량@@
                "dwvolume": "dwvolume`long", ## 전체매도위탁체결수량@@
                "swvolume": "swvolume`long", ## 전체매수위탁체결수량@@
                "wvol": "wvol`long", ## 전체위탁순매수 수량@@
                "djvolume": "djvolume`long", ## 전체매도자기체결수량@@
                "sjvolume": "sjvolume`long", ## 전체매수자기체결수량@@
                "jvol": "jvol`long", ## 전체자기순매수 수량@@
                "cdwvalue": "cdwvalue`long", ## 차익매도위탁체결금액@@
                "cdjvalue": "cdjvalue`long", ## 차익매도자기체결금액@@
                "cswvalue": "cswvalue`long", ## 차익매수위탁체결금액@@
                "csjvalue": "csjvalue`long", ## 차익매수자기체결금액@@
                "cwval": "cwval`long", ## 차익위탁순매수 금액@@
                "cjval": "cjval`long", ## 차익자기순매수 금액@@
                "bdwvalue": "bdwvalue`long", ## 비차익매도위탁체결금액@@
                "bdjvalue": "bdjvalue`long", ## 비차익매도자기체결금액@@
                "bswvalue": "bswvalue`long", ## 비차익매수위탁체결금액@@
                "bsjvalue": "bsjvalue`long", ## 비차익매수자기체결금액@@
                "bwval": "bwval`long", ## 비차익위탁순매수 금액@@
                "bjval": "bjval`long", ## 비차익자기순매수 금액@@
                "dwvalue": "dwvalue`long", ## 전체매도위탁체결금액@@
                "swvalue": "swvalue`long", ## 전체매수위탁체결금액@@
                "wval": "wval`long", ## 전체위탁순매수 금액@@
                "djvalue": "djvalue`long", ## 전체매도자기체결금액@@
                "sjvalue": "sjvalue`long", ## 전체매수자기체결금액@@
                "jval": "jval`long", ## 전체자기순매수 금액@@
                "k50jisu": "k50jisu`float", ## KOSDAQ50 지수@@
                "k50sign": "k50sign`char", ## KOSDAQ50 전일대비구분@@
                "change": "change`float", ## KOSDAQ50 전일대비@@
                "k50basis": "k50basis`float", ## KOSDAQ50 베이시스@@
                "cdvolume": "cdvolume`long", ## 차익매도체결수량합계@@
                "csvolume": "csvolume`long", ## 차익매수체결수량합계@@
                "cvol": "cvol`long", ## 차익순매수 수량합계@@
                "bdvolume": "bdvolume`long", ## 비차익매도체결수량합계@@
                "bsvolume": "bsvolume`long", ## 비차익매수체결수량합계@@
                "bvol": "bvol`long", ## 비차익순매수 수량합계@@
                "tdvolume": "tdvolume`long", ## 전체매도체결수량합계@@
                "tsvolume": "tsvolume`long", ## 전체매수체결수량합계@@
                "tvol": "tvol`long", ## 전체순매수 수량합계@@
                "cdvalue": "cdvalue`long", ## 차익매도체결금액합계@@
                "csvalue": "csvalue`long", ## 차익매수체결금액합계@@
                "cval": "cval`long", ## 차익순매수 금액합계@@
                "bdvalue": "bdvalue`long", ## 비차익매도체결금액합계@@
                "bsvalue": "bsvalue`long", ## 비차익매수체결금액합계@@
                "bval": "bval`long", ## 비차익순매수 금액합계@@
                "tdvalue": "tdvalue`long", ## 전체매도체결금액합계@@
                "tsvalue": "tsvalue`long", ## 전체매수체결금액합계@@
                "tval": "tval`long", ## 전체순매수 금액합계@@
                "p_cdvolcha": "p_cdvolcha`long", ## 차익매도체결수량직전대비@@
                "p_csvolcha": "p_csvolcha`long", ## 차익매수체결수량직전대비@@
                "p_cvolcha": "p_cvolcha`long", ## 차익순매수 수량직전대비@@
                "p_bdvolcha": "p_bdvolcha`long", ## 비차익매도체결수량직전대비@@
                "p_bsvolcha": "p_bsvolcha`long", ## 비차익매수체결수량직전대비@@
                "p_bvolcha": "p_bvolcha`long", ## 비차익순매수 수량직전대비@@
                "p_tdvolcha": "p_tdvolcha`long", ## 전체매도체결수량직전대비@@
                "p_tsvolcha": "p_tsvolcha`long", ## 전체매수체결수량직전대비@@
                "p_tvolcha": "p_tvolcha`long", ## 전체순매수 수량직전대비@@
                "p_cdvalcha": "p_cdvalcha`long", ## 차익매도체결금액직전대비@@
                "p_csvalcha": "p_csvalcha`long", ## 차익매수체결금액직전대비@@
                "p_cvalcha": "p_cvalcha`long", ## 차익순매수 금액직전대비@@
                "p_bdvalcha": "p_bdvalcha`long", ## 비차익매도체결금액직전대비@@
                "p_bsvalcha": "p_bsvalcha`long", ## 비차익매수체결금액직전대비@@
                "p_bvalcha": "p_bvalcha`long", ## 비차익순매수 금액직전대비@@
                "p_tdvalcha": "p_tdvalcha`long", ## 전체매도체결금액직전대비@@
                "p_tsvalcha": "p_tsvalcha`long", ## 전체매수체결금액직전대비@@
                "p_tvalcha": "p_tvalcha`long", ## 전체순매수 금액직전대비@@
                "gubun": "gubun`char##구분값@@"
            }
        }
    },
    "KS_": { ## KOSDAQ우선호가(KS)
        "input": {
            "InBlock": {
                "shcode": " ##단축코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "offerho": "offerho`long", ## 매도호가@@
                "bidho": "bidho`long", ## 매수호가@@
                "shcode": "shcode`char##단축코드@@"
            }
        }
    },
    "MK2": { ## US지수(MK2)
        "input": {
            "InBlock": {
                "symbol": " ##심볼코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "date": "date`char", ## 일자@@
                "time": "time`char", ## 시간@@
                "kodate": "kodate`char", ## 한국일자@@
                "kotime": "kotime`char", ## 한국시간@@
                "open": "open`float", ## 시가@@
                "high": "high`float", ## 고가@@
                "low": "low`float", ## 저가@@
                "price": "price`float", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`float", ## 전일대비@@
                "uprate": "uprate`float", ## 등락율@@
                "bidho": "bidho`float", ## 매수호가@@
                "bidrem": "bidrem`long", ## 매수잔량@@
                "offerho": "offerho`float", ## 매도호가@@
                "offerrem": "offerrem`long", ## 매도잔량@@
                "volume": "volume`float", ## 누적거래량@@
                "xsymbol": "xsymbol`char", ## 심벌@@
                "cvolume": "cvolume`float##체결거래량@@"
            }
        }
    },
    "MMDAQ91200": { ## 파생상품증거금율조회
        "input": {
            "MMDAQ91200InBlock1": {
                "RecCnt": "0", ## 레코드갯수@@
                "IsuLgclssCode": " ", ## 종목대분류코드@@
                "IsuMdclssCode": " ##종목중분류코드@@"
            }
        },
        "output": {
            "MMDAQ91200OutBlock1": {
                "RecCnt": "RecCnt`long", ## 레코드갯수@@
                "IsuLgclssCode": "IsuLgclssCode`char", ## 종목대분류코드@@
                "IsuMdclssCode": "IsuMdclssCode`char##종목중분류코드@@"
            },
            "MMDAQ91200OutBlock2": {
                "IsuSmclssCode": "IsuSmclssCode`char", ## 종목소분류코드@@
                "IsuMdclssCode": "IsuMdclssCode`char", ## 종목중분류코드@@
                "IsuLrgMdclssNm": "IsuLrgMdclssNm`char", ## 종목대중분류명@@
                "IsuLrgMidSmclssNm": "IsuLrgMidSmclssNm`char", ## 종목대중소분류명@@
                "ShtnHanglIsuNm": "ShtnHanglIsuNm`char", ## 단축한글종목명@@
                "CsgnMgnrt": "CsgnMgnrt`double", ## 위탁증거금율@@
                "MaintMgnrt": "MaintMgnrt`double", ## 유지증거금율@@
                "MnyMgnrt": "MnyMgnrt`double", ## 현금증거금율@@
                "RmndDays": "RmndDays`long##잔여일수@@"
            }
        }
    },
    "NWS": { ## 실시간 뉴스 제목 패킷(NWS)
        "input": {
            "InBlock": {
                "nwcode": " ##뉴스코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "date": "date`char", ## 날짜@@
                "time": "time`char", ## 시간@@
                "id": "id`char", ## 뉴스구분자@@
                "realkey": "realkey`char", ## 키값@@
                "title": "title`char", ## 제목@@
                "code": "code`char", ## 단축종목코드@@
                "bodysize": "bodysize`long##BODY길이@@"
            }
        }
    },
    "O01": { ## 선물접수
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
                "userId": "userId`char", ## 주문자Id@@
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
    "o3101": { ## 해외선물마스터조회(o3101)-API용
        "input": {
            "o3101InBlock": {
                "gubun": " ##입력구분(예비)@@"
            }
        },
        "output": {
            "o3101OutBlock": {
                "Symbol": "Symbol`char", ## 종목코드@@
                "SymbolNm": "SymbolNm`char", ## 종목명@@
                "ApplDate": "ApplDate`char", ## 종목배치수신일(한국일자)@@
                "BscGdsCd": "BscGdsCd`char", ## 기초상품코드@@
                "BscGdsNm": "BscGdsNm`char", ## 기초상품명@@
                "ExchCd": "ExchCd`char", ## 거래소코드@@
                "ExchNm": "ExchNm`char", ## 거래소명@@
                "CrncyCd": "CrncyCd`char", ## 기준통화코드@@
                "NotaCd": "NotaCd`char", ## 진법구분코드@@
                "UntPrc": "UntPrc`double", ## 호가단위가격@@
                "MnChgAmt": "MnChgAmt`double", ## 최소가격변동금액@@
                "RgltFctr": "RgltFctr`double", ## 가격조정계수@@
                "CtrtPrAmt": "CtrtPrAmt`double", ## 계약당금액@@
                "GdsCd": "GdsCd`char", ## 상품구분코드@@
                "LstngYr": "LstngYr`char", ## 월물(년)@@
                "LstngM": "LstngM`char", ## 월물(월)@@
                "EcPrc": "EcPrc`double", ## 정산가격@@
                "DlStrtTm": "DlStrtTm`char", ## 거래시작시간@@
                "DlEndTm": "DlEndTm`char", ## 거래종료시간@@
                "DlPsblCd": "DlPsblCd`char", ## 거래가능구분코드@@
                "MgnCltCd": "MgnCltCd`char", ## 증거금징수구분코드@@
                "OpngMgn": "OpngMgn`double", ## 개시증거금@@
                "MntncMgn": "MntncMgn`double", ## 유지증거금@@
                "OpngMgnR": "OpngMgnR`double", ## 개시증거금율@@
                "MntncMgnR": "MntncMgnR`double", ## 유지증거금율@@
                "DotGb": "DotGb`long##유효소수점자리수@@"
            }
        }
    },
    "o3103": { ## 해외선물차트(분)(o3103)-API용
        "input": {
            "o3103InBlock": {
                "shcode": " ", ## 단축코드@@
                "ncnt": "1", ## N분주기@@
                "readcnt": "0", ## 조회건수@@
                "cts_date": " ", ## 연속일자@@
                "cts_time": " ##연속시간@@"
            }
        },
        "output": {
            "o3103OutBlock": {
                "shcode": "shcode`char", ## 단축코드@@
                "timediff": "timediff`long", ## 시차@@
                "readcnt": "readcnt`long", ## 조회건수@@
                "cts_date": "cts_date`char", ## 연속일자@@
                "cts_time": "cts_time`char##연속시간@@"
            },
            "o3103OutBlock1": {
                "date": "date`char", ## 날짜@@
                "time": "time`char", ## 현지시간@@
                "open": "open`double", ## 시가@@
                "high": "high`double", ## 고가@@
                "low": "low`double", ## 저가@@
                "close": "close`double", ## 종가@@
                "volume": "volume`long##거래량@@"
            }
        }
    },
    "o3104": { ## 해외선물일별체결조회(o3104)-API용
        "input": {
            "o3104InBlock": {
                "gubun": " ", ## 조회구분@@
                "shcode": " ", ## 단축코드@@
                "date": " ##조회일자@@"
            }
        },
        "output": {
            "o3104OutBlock1": {
                "chedate": "chedate`char", ## 일자@@
                "price": "price`double", ## 현재가@@
                "sign": "sign`char", ## 대비구분@@
                "change": "change`double", ## 대비@@
                "diff": "diff`float", ## 등락율@@
                "open": "open`double", ## 시가@@
                "high": "high`double", ## 고가@@
                "low": "low`double", ## 저가@@
                "cgubun": "cgubun`char", ## 체결구분@@
                "volume": "volume`long##누적거래량@@"
            }
        }
    },
    "o3105": { ## 해외선물현재가(종목정보)조회(o3105)-API용
        "input": {
            "o3105InBlock": {
                "symbol": " ##종목코드@@"
            }
        },
        "output": {
            "o3105OutBlock": {
                "Symbol": "Symbol`char", ## 종목코드@@
                "SymbolNm": "SymbolNm`char", ## 종목명@@
                "ApplDate": "ApplDate`char", ## 종목배치수신일@@
                "BscGdsCd": "BscGdsCd`char", ## 기초상품코드@@
                "BscGdsNm": "BscGdsNm`char", ## 기초상품명@@
                "ExchCd": "ExchCd`char", ## 거래소코드@@
                "ExchNm": "ExchNm`char", ## 거래소명@@
                "EcCd": "EcCd`char", ## 정산구분코드@@
                "CrncyCd": "CrncyCd`char", ## 기준통화코드@@
                "NotaCd": "NotaCd`char", ## 진법구분코드@@
                "UntPrc": "UntPrc`double", ## 호가단위가격@@
                "MnChgAmt": "MnChgAmt`double", ## 최소가격변동금액@@
                "RgltFctr": "RgltFctr`double", ## 가격조정계수@@
                "CtrtPrAmt": "CtrtPrAmt`double", ## 계약당금액@@
                "LstngMCnt": "LstngMCnt`long", ## 상장개월수@@
                "GdsCd": "GdsCd`char", ## 상품구분코드@@
                "MrktCd": "MrktCd`char", ## 시장구분코드@@
                "EminiCd": "EminiCd`char", ## Emini구분코드@@
                "LstngYr": "LstngYr`char", ## 상장년@@
                "LstngM": "LstngM`char", ## 상장월@@
                "SeqNo": "SeqNo`long", ## 월물순서@@
                "LstngDt": "LstngDt`char", ## 상장일자@@
                "MtrtDt": "MtrtDt`char", ## 만기일자@@
                "FnlDlDt": "FnlDlDt`char", ## 최종거래일@@
                "FstTrsfrDt": "FstTrsfrDt`char", ## 최초인도통지일자@@
                "EcPrc": "EcPrc`double", ## 정산가격@@
                "DlDt": "DlDt`char", ## 거래시작일자(한국)@@
                "DlStrtTm": "DlStrtTm`char", ## 거래시작시간(한국)@@
                "DlEndTm": "DlEndTm`char", ## 거래종료시간(한국)@@
                "OvsStrDay": "OvsStrDay`char", ## 거래시작일자(현지)@@
                "OvsStrTm": "OvsStrTm`char", ## 거래시작시간(현지)@@
                "OvsEndDay": "OvsEndDay`char", ## 거래종료일자(현지)@@
                "OvsEndTm": "OvsEndTm`char", ## 거래종료시간(현지)@@
                "DlPsblCd": "DlPsblCd`char", ## 거래가능구분코드@@
                "MgnCltCd": "MgnCltCd`char", ## 증거금징수구분코드@@
                "OpngMgn": "OpngMgn`double", ## 개시증거금@@
                "MntncMgn": "MntncMgn`double", ## 유지증거금@@
                "OpngMgnR": "OpngMgnR`double", ## 개시증거금율@@
                "MntncMgnR": "MntncMgnR`double", ## 유지증거금율@@
                "DotGb": "DotGb`long", ## 유효소수점자리수@@
                "TimeDiff": "TimeDiff`long", ## 시차@@
                "OvsDate": "OvsDate`char", ## 현지체결일자@@
                "KorDate": "KorDate`char", ## 한국체결일자@@
                "TrdTm": "TrdTm`char", ## 현지체결시간@@
                "RcvTm": "RcvTm`char", ## 한국체결시각@@
                "TrdP": "TrdP`double", ## 체결가격@@
                "TrdQ": "TrdQ`long", ## 체결수량@@
                "TotQ": "TotQ`long", ## 누적거래량@@
                "TrdAmt": "TrdAmt`double", ## 체결거래대금@@
                "TotAmt": "TotAmt`double", ## 누적거래대금@@
                "OpenP": "OpenP`double", ## 시가@@
                "HighP": "HighP`double", ## 고가@@
                "LowP": "LowP`double", ## 저가@@
                "CloseP": "CloseP`double", ## 전일종가@@
                "YdiffP": "YdiffP`double", ## 전일대비@@
                "YdiffSign": "YdiffSign`char", ## 전일대비구분@@
                "Cgubun": "Cgubun`char", ## 체결구분@@
                "Diff": "Diff`double##등락율@@"
            }
        }
    },
    "o3106": { ## 해외선물현재가호가조회(o3106)-API용
        "input": {
            "o3106InBlock": {
                "symbol": " ##단축코드@@"
            }
        },
        "output": {
            "o3106OutBlock": {
                "symbol": "symbol`char", ## 종목코드@@
                "symbolname": "symbolname`char", ## 종목명@@
                "price": "price`double", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`double", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 누적거래량@@
                "jnilclose": "jnilclose`double", ## 전일종가@@
                "open": "open`double", ## 시가@@
                "high": "high`double", ## 고가@@
                "low": "low`double", ## 저가@@
                "hotime": "hotime`char", ## 호가수신시간@@
                "offerho1": "offerho1`double", ## 매도호가1@@
                "bidho1": "bidho1`double", ## 매수호가1@@
                "offercnt1": "offercnt1`long", ## 매도호가건수1@@
                "bidcnt1": "bidcnt1`long", ## 매수호가건수1@@
                "offerrem1": "offerrem1`long", ## 매도호가수량1@@
                "bidrem1": "bidrem1`long", ## 매수호가수량1@@
                "offerho2": "offerho2`double", ## 매도호가2@@
                "bidho2": "bidho2`double", ## 매수호가2@@
                "offercnt2": "offercnt2`long", ## 매도호가건수2@@
                "bidcnt2": "bidcnt2`long", ## 매수호가건수2@@
                "offerrem2": "offerrem2`long", ## 매도호가수량2@@
                "bidrem2": "bidrem2`long", ## 매수호가수량2@@
                "offerho3": "offerho3`double", ## 매도호가3@@
                "bidho3": "bidho3`double", ## 매수호가3@@
                "offercnt3": "offercnt3`long", ## 매도호가건수3@@
                "bidcnt3": "bidcnt3`long", ## 매수호가건수3@@
                "offerrem3": "offerrem3`long", ## 매도호가수량3@@
                "bidrem3": "bidrem3`long", ## 매수호가수량3@@
                "offerho4": "offerho4`double", ## 매도호가4@@
                "bidho4": "bidho4`double", ## 매수호가4@@
                "offercnt4": "offercnt4`long", ## 매도호가건수4@@
                "bidcnt4": "bidcnt4`long", ## 매수호가건수4@@
                "offerrem4": "offerrem4`long", ## 매도호가수량4@@
                "bidrem4": "bidrem4`long", ## 매수호가수량4@@
                "offerho5": "offerho5`double", ## 매도호가5@@
                "bidho5": "bidho5`double", ## 매수호가5@@
                "offercnt5": "offercnt5`long", ## 매도호가건수5@@
                "bidcnt5": "bidcnt5`long", ## 매수호가건수5@@
                "offerrem5": "offerrem5`long", ## 매도호가수량5@@
                "bidrem5": "bidrem5`long", ## 매수호가수량5@@
                "offercnt": "offercnt`long", ## 매도호가건수합@@
                "bidcnt": "bidcnt`long", ## 매수호가건수합@@
                "offer": "offer`long", ## 매도호가수량합@@
                "bid": "bid`long##매수호가수량합@@"
            }
        }
    },
    "o3107": { ## 해외선물관심종목조회(o3107)-API용
        "input": {
            "o3107InBlock": {
                "symbol": " ##종목심볼@@"
            }
        },
        "output": {
            "o3107OutBlock": {
                "symbol": "symbol`char", ## 종목코드@@
                "symbolname": "symbolname`char", ## 종목명@@
                "price": "price`double", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`double", ## 전일대비@@
                "diff": "diff`double", ## 등락율@@
                "volume": "volume`long", ## 누적거래량@@
                "jnilclose": "jnilclose`double", ## 전일종가@@
                "open": "open`double", ## 시가@@
                "high": "high`double", ## 고가@@
                "low": "low`double", ## 저가@@
                "offerho1": "offerho1`double", ## 매도호가1@@
                "bidho1": "bidho1`double", ## 매수호가1@@
                "offercnt1": "offercnt1`long", ## 매도호가건수1@@
                "bidcnt1": "bidcnt1`long", ## 매수호가건수1@@
                "offerrem1": "offerrem1`long", ## 매도호가수량1@@
                "bidrem1": "bidrem1`long", ## 매수호가수량1@@
                "offercnt": "offercnt`long", ## 매도호가건수합@@
                "bidcnt": "bidcnt`long", ## 매수호가건수합@@
                "offer": "offer`long", ## 매도호가수량합@@
                "bid": "bid`long##매수호가수량합@@"
            }
        }
    },
    "o3108": { ## 해외선물차트(일주월)(o3108)-API용
        "input": {
            "o3108InBlock": {
                "shcode": " ", ## 단축코드@@
                "gubun": " ", ## 주기구분@@
                "qrycnt": "2000", ## 요청건수@@
                "sdate": " ", ## 시작일자@@
                "edate": " ", ## 종료일자@@
                "cts_date": " ##연속일자@@"
            }
        },
        "output": {
            "o3108OutBlock": {
                "shcode": "shcode`char", ## 단축코드@@
                "jisiga": "jisiga`double", ## 전일시가@@
                "jihigh": "jihigh`double", ## 전일고가@@
                "jilow": "jilow`double", ## 전일저가@@
                "jiclose": "jiclose`double", ## 전일종가@@
                "jivolume": "jivolume`long", ## 전일거래량@@
                "disiga": "disiga`double", ## 당일시가@@
                "dihigh": "dihigh`double", ## 당일고가@@
                "dilow": "dilow`double", ## 당일저가@@
                "diclose": "diclose`double", ## 당일종가@@
                "mk_stime": "mk_stime`char", ## 장시작시간@@
                "mk_etime": "mk_etime`char", ## 장마감시간@@
                "cts_date": "cts_date`char", ## 연속일자@@
                "rec_count": "rec_count`long##레코드카운트@@"
            },
            "o3108OutBlock1": {
                "date": "date`char", ## 날짜@@
                "open": "open`double", ## 시가@@
                "high": "high`double", ## 고가@@
                "low": "low`double", ## 저가@@
                "close": "close`double", ## 종가@@
                "volume": "volume`long##거래량@@"
            }
        }
    },
    "o3116": { ## 해외선물시간대별(Tick)체결(o3116)-API용
        "input": {
            "o3116InBlock": {
                "gubun": " ", ## 조회구분@@0:당일1:전일
                "shcode": " ", ## 단축코드@@
                "readcnt": "0", ## 조회갯수@@
                "cts_seq": "0##순번CTS@@"
            }
        },
        "output": {
            "o3116OutBlock": {
                "cts_seq": "cts_seq`long##순번CTS@@"
            },
            "o3116OutBlock1": {
                "ovsdate": "ovsdate`char", ## 현지일자@@
                "ovstime": "ovstime`char", ## 현지시간@@
                "price": "price`double", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`double", ## 전일대비@@
                "diff": "diff`double", ## 등락율@@
                "cvolume": "cvolume`long", ## 체결수량@@
                "volume": "volume`long##누적거래량@@"
            }
        }
    },
    "o3117": { ## 해외선물차트용NTick(o3117)-API용
        "input": {
            "o3117InBlock": {
                "shcode": " ", ## 단축코드@@
                "ncnt": "1", ## 단위@@
                "qrycnt": "2000", ## 건수@@
                "cts_seq": " ", ## 연속시간@@
                "cts_daygb": " ##연속당일구분@@"
            }
        },
        "output": {
            "o3117OutBlock": {
                "shcode": "shcode`char", ## 단축코드@@
                "rec_count": "rec_count`long", ## 레코드카운트@@
                "cts_seq": "cts_seq`char", ## 연속시간@@
                "cts_daygb": "cts_daygb`char##연속당일구분@@"
            },
            "o3117OutBlock1": {
                "date": "date`char", ## 날짜@@
                "time": "time`char", ## 시간@@
                "open": "open`double", ## 시가@@
                "high": "high`double", ## 고가@@
                "low": "low`double", ## 저가@@
                "close": "close`double", ## 종가@@
                "volume": "volume`long##거래량@@"
            }
        }
    },
    "o3121": { ## 해외선물옵션마스터조회(o3121)-API용
        "input": {
            "o3121InBlock": {
                "MktGb": " ", ## 시장구분@@
                "BscGdsCd": " ##옵션기초상품코드@@"
            }
        },
        "output": {
            "o3121OutBlock": {
                "Symbol": "Symbol`char", ## 종목코드@@
                "SymbolNm": "SymbolNm`char", ## 종목명@@
                "ApplDate": "ApplDate`char", ## 종목배치수신일(한국일자)@@
                "BscGdsCd": "BscGdsCd`char", ## 기초상품코드@@
                "BscGdsNm": "BscGdsNm`char", ## 기초상품명@@
                "ExchCd": "ExchCd`char", ## 거래소코드@@
                "ExchNm": "ExchNm`char", ## 거래소명@@
                "CrncyCd": "CrncyCd`char", ## 기준통화코드@@
                "NotaCd": "NotaCd`char", ## 진법구분코드@@
                "UntPrc": "UntPrc`double", ## 호가단위가격@@
                "MnChgAmt": "MnChgAmt`double", ## 최소가격변동금액@@
                "RgltFctr": "RgltFctr`double", ## 가격조정계수@@
                "CtrtPrAmt": "CtrtPrAmt`double", ## 계약당금액@@
                "GdsCd": "GdsCd`char", ## 상품구분코드@@
                "LstngYr": "LstngYr`char", ## 월물(년)@@
                "LstngM": "LstngM`char", ## 월물(월)@@
                "EcPrc": "EcPrc`double", ## 정산가격@@
                "DlStrtTm": "DlStrtTm`char", ## 거래시작시간@@
                "DlEndTm": "DlEndTm`char", ## 거래종료시간@@
                "DlPsblCd": "DlPsblCd`char", ## 거래가능구분코드@@
                "MgnCltCd": "MgnCltCd`char", ## 증거금징수구분코드@@
                "OpngMgn": "OpngMgn`double", ## 개시증거금@@
                "MntncMgn": "MntncMgn`double", ## 유지증거금@@
                "OpngMgnR": "OpngMgnR`double", ## 개시증거금율@@
                "MntncMgnR": "MntncMgnR`double", ## 유지증거금율@@
                "DotGb": "DotGb`long", ## 유효소수점자리수@@
                "XrcPrc": "XrcPrc`char", ## 옵션행사가@@
                "FdasBasePrc": "FdasBasePrc`char", ## 기초자산기준가격@@
                "OptTpCode": "OptTpCode`char", ## 옵션콜풋구분@@
                "RgtXrcPtnCode": "RgtXrcPtnCode`char", ## 권리행사구분코드@@
                "Moneyness": "Moneyness`char", ## ATM구분@@
                "LastSettPtnCode": "LastSettPtnCode`char", ## 해외파생기초자산종목코드@@
                "OptMinOrcPrc": "OptMinOrcPrc`char", ## 해외옵션최소호가@@
                "OptMinBaseOrcPrc": "OptMinBaseOrcPrc`char##해외옵션최소기준호가@@"
            }
        }
    },
    "o3123": { ## 해외선물옵션차트(분)(o3123)-API용
        "input": {
            "o3123InBlock": {
                "mktgb": " ", ## 시장구분@@
                "shcode": " ", ## 단축코드@@
                "ncnt": "1", ## N분주기@@
                "readcnt": "0", ## 조회건수@@
                "cts_date": " ", ## 연속일자@@
                "cts_time": " ##연속시간@@"
            }
        },
        "output": {
            "o3123OutBlock": {
                "shcode": "shcode`char", ## 단축코드@@
                "timediff": "timediff`long", ## 시차@@
                "readcnt": "readcnt`long", ## 조회건수@@
                "cts_date": "cts_date`char", ## 연속일자@@
                "cts_time": "cts_time`char##연속시간@@"
            },
            "o3123OutBlock1": {
                "date": "date`char", ## 날짜@@
                "time": "time`char", ## 현지시간@@
                "open": "open`double", ## 시가@@
                "high": "high`double", ## 고가@@
                "low": "low`double", ## 저가@@
                "close": "close`double", ## 종가@@
                "volume": "volume`long##거래량@@"
            }
        }
    },
    "o3125": { ## 해외선물옵션현재가(종목정보)조회(o3125)-API용
        "input": {
            "o3125InBlock": {
                "mktgb": " ", ## 시장구분@@
                "symbol": " ##종목코드@@"
            }
        },
        "output": {
            "o3125OutBlock": {
                "Symbol": "Symbol`char", ## 종목코드@@
                "SymbolNm": "SymbolNm`char", ## 종목명@@
                "ApplDate": "ApplDate`char", ## 종목배치수신일@@
                "BscGdsCd": "BscGdsCd`char", ## 기초상품코드@@
                "BscGdsNm": "BscGdsNm`char", ## 기초상품명@@
                "ExchCd": "ExchCd`char", ## 거래소코드@@
                "ExchNm": "ExchNm`char", ## 거래소명@@
                "EcCd": "EcCd`char", ## 정산구분코드@@
                "CrncyCd": "CrncyCd`char", ## 기준통화코드@@
                "NotaCd": "NotaCd`char", ## 진법구분코드@@
                "UntPrc": "UntPrc`double", ## 호가단위가격@@
                "MnChgAmt": "MnChgAmt`double", ## 최소가격변동금액@@
                "RgltFctr": "RgltFctr`double", ## 가격조정계수@@
                "CtrtPrAmt": "CtrtPrAmt`double", ## 계약당금액@@
                "LstngMCnt": "LstngMCnt`long", ## 상장개월수@@
                "GdsCd": "GdsCd`char", ## 상품구분코드@@
                "MrktCd": "MrktCd`char", ## 시장구분코드@@
                "EminiCd": "EminiCd`char", ## Emini구분코드@@
                "LstngYr": "LstngYr`char", ## 상장년@@
                "LstngM": "LstngM`char", ## 상장월@@
                "SeqNo": "SeqNo`long", ## 월물순서@@
                "LstngDt": "LstngDt`char", ## 상장일자@@
                "MtrtDt": "MtrtDt`char", ## 만기일자@@
                "FnlDlDt": "FnlDlDt`char", ## 최종거래일@@
                "FstTrsfrDt": "FstTrsfrDt`char", ## 최초인도통지일자@@
                "EcPrc": "EcPrc`double", ## 정산가격@@
                "DlDt": "DlDt`char", ## 거래시작일자(한국)@@
                "DlStrtTm": "DlStrtTm`char", ## 거래시작시간(한국)@@
                "DlEndTm": "DlEndTm`char", ## 거래종료시간(한국)@@
                "OvsStrDay": "OvsStrDay`char", ## 거래시작일자(현지)@@
                "OvsStrTm": "OvsStrTm`char", ## 거래시작시간(현지)@@
                "OvsEndDay": "OvsEndDay`char", ## 거래종료일자(현지)@@
                "OvsEndTm": "OvsEndTm`char", ## 거래종료시간(현지)@@
                "DlPsblCd": "DlPsblCd`char", ## 거래가능구분코드@@
                "MgnCltCd": "MgnCltCd`char", ## 증거금징수구분코드@@
                "OpngMgn": "OpngMgn`double", ## 개시증거금@@
                "MntncMgn": "MntncMgn`double", ## 유지증거금@@
                "OpngMgnR": "OpngMgnR`double", ## 개시증거금율@@
                "MntncMgnR": "MntncMgnR`double", ## 유지증거금율@@
                "DotGb": "DotGb`long", ## 유효소수점자리수@@
                "TimeDiff": "TimeDiff`long", ## 시차@@
                "OvsDate": "OvsDate`char", ## 현지체결일자@@
                "KorDate": "KorDate`char", ## 한국체결일자@@
                "TrdTm": "TrdTm`char", ## 현지체결시간@@
                "RcvTm": "RcvTm`char", ## 한국체결시각@@
                "TrdP": "TrdP`double", ## 체결가격@@
                "TrdQ": "TrdQ`long", ## 체결수량@@
                "TotQ": "TotQ`long", ## 누적거래량@@
                "TrdAmt": "TrdAmt`double", ## 체결거래대금@@
                "TotAmt": "TotAmt`double", ## 누적거래대금@@
                "OpenP": "OpenP`double", ## 시가@@
                "HighP": "HighP`double", ## 고가@@
                "LowP": "LowP`double", ## 저가@@
                "CloseP": "CloseP`double", ## 전일종가@@
                "YdiffP": "YdiffP`double", ## 전일대비@@
                "YdiffSign": "YdiffSign`char", ## 전일대비구분@@
                "Cgubun": "Cgubun`char", ## 체결구분@@
                "Diff": "Diff`double", ## 등락율@@
                "MinOrcPrc": "MinOrcPrc`double", ## 최소호가@@
                "MinBaseOrcPrc": "MinBaseOrcPrc`double##최소기준호가@@"
            }
        }
    },
    "o3126": { ## 해외선물옵션현재가호가조회(o3126)-API용
        "input": {
            "o3126InBlock": {
                "mktgb": " ", ## 시장구분@@
                "symbol": " ##단축코드@@"
            }
        },
        "output": {
            "o3126OutBlock": {
                "symbol": "symbol`char", ## 종목코드@@
                "symbolname": "symbolname`char", ## 종목명@@
                "price": "price`double", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`double", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 누적거래량@@
                "jnilclose": "jnilclose`double", ## 전일종가@@
                "open": "open`double", ## 시가@@
                "high": "high`double", ## 고가@@
                "low": "low`double", ## 저가@@
                "hotime": "hotime`char", ## 호가수신시간@@
                "offerho1": "offerho1`double", ## 매도호가1@@
                "bidho1": "bidho1`double", ## 매수호가1@@
                "offercnt1": "offercnt1`long", ## 매도호가건수1@@
                "bidcnt1": "bidcnt1`long", ## 매수호가건수1@@
                "offerrem1": "offerrem1`long", ## 매도호가수량1@@
                "bidrem1": "bidrem1`long", ## 매수호가수량1@@
                "offerho2": "offerho2`double", ## 매도호가2@@
                "bidho2": "bidho2`double", ## 매수호가2@@
                "offercnt2": "offercnt2`long", ## 매도호가건수2@@
                "bidcnt2": "bidcnt2`long", ## 매수호가건수2@@
                "offerrem2": "offerrem2`long", ## 매도호가수량2@@
                "bidrem2": "bidrem2`long", ## 매수호가수량2@@
                "offerho3": "offerho3`double", ## 매도호가3@@
                "bidho3": "bidho3`double", ## 매수호가3@@
                "offercnt3": "offercnt3`long", ## 매도호가건수3@@
                "bidcnt3": "bidcnt3`long", ## 매수호가건수3@@
                "offerrem3": "offerrem3`long", ## 매도호가수량3@@
                "bidrem3": "bidrem3`long", ## 매수호가수량3@@
                "offerho4": "offerho4`double", ## 매도호가4@@
                "bidho4": "bidho4`double", ## 매수호가4@@
                "offercnt4": "offercnt4`long", ## 매도호가건수4@@
                "bidcnt4": "bidcnt4`long", ## 매수호가건수4@@
                "offerrem4": "offerrem4`long", ## 매도호가수량4@@
                "bidrem4": "bidrem4`long", ## 매수호가수량4@@
                "offerho5": "offerho5`double", ## 매도호가5@@
                "bidho5": "bidho5`double", ## 매수호가5@@
                "offercnt5": "offercnt5`long", ## 매도호가건수5@@
                "bidcnt5": "bidcnt5`long", ## 매수호가건수5@@
                "offerrem5": "offerrem5`long", ## 매도호가수량5@@
                "bidrem5": "bidrem5`long", ## 매수호가수량5@@
                "offercnt": "offercnt`long", ## 매도호가건수합@@
                "bidcnt": "bidcnt`long", ## 매수호가건수합@@
                "offer": "offer`long", ## 매도호가수량합@@
                "bid": "bid`long##매수호가수량합@@"
            }
        }
    },
    "o3127": { ## 해외선물옵션관심종목조회(o3127)-API용
        "input": {
            "o3127InBlock": {
                "nrec": "0##건수@@"
            },
            "o3127InBlock1": {
                "mktgb": " ", ## 시장구분@@
                "symbol": " ##종목심볼@@"
            }
        },
        "output": {
            "o3127OutBlock": {
                "symbol": "symbol`char", ## 종목코드@@
                "symbolname": "symbolname`char", ## 종목명@@
                "price": "price`double", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`double", ## 전일대비@@
                "diff": "diff`double", ## 등락율@@
                "volume": "volume`long", ## 누적거래량@@
                "jnilclose": "jnilclose`double", ## 전일종가@@
                "open": "open`double", ## 시가@@
                "high": "high`double", ## 고가@@
                "low": "low`double", ## 저가@@
                "offerho1": "offerho1`double", ## 매도호가1@@
                "bidho1": "bidho1`double", ## 매수호가1@@
                "offercnt1": "offercnt1`long", ## 매도호가건수1@@
                "bidcnt1": "bidcnt1`long", ## 매수호가건수1@@
                "offerrem1": "offerrem1`long", ## 매도호가수량1@@
                "bidrem1": "bidrem1`long", ## 매수호가수량1@@
                "offercnt": "offercnt`long", ## 매도호가건수합@@
                "bidcnt": "bidcnt`long", ## 매수호가건수합@@
                "offer": "offer`long", ## 매도호가수량합@@
                "bid": "bid`long##매수호가수량합@@"
            }
        }
    },
    "o3128": { ## 해외선물옵션차트일주월(o3128)-API용
        "input": {
            "o3128InBlock": {
                "mktgb": " ", ## 시장구분@@
                "shcode": " ", ## 단축코드@@
                "gubun": " ", ## 주기구분@@
                "qrycnt": "2000", ## 요청건수@@
                "sdate": " ", ## 시작일자@@
                "edate": " ", ## 종료일자@@
                "cts_date": " ##연속일자@@"
            }
        },
        "output": {
            "o3128OutBlock": {
                "shcode": "shcode`char", ## 단축코드@@
                "jisiga": "jisiga`double", ## 전일시가@@
                "jihigh": "jihigh`double", ## 전일고가@@
                "jilow": "jilow`double", ## 전일저가@@
                "jiclose": "jiclose`double", ## 전일종가@@
                "jivolume": "jivolume`long", ## 전일거래량@@
                "disiga": "disiga`double", ## 당일시가@@
                "dihigh": "dihigh`double", ## 당일고가@@
                "dilow": "dilow`double", ## 당일저가@@
                "diclose": "diclose`double", ## 당일종가@@
                "mk_stime": "mk_stime`char", ## 장시작시간@@
                "mk_etime": "mk_etime`char", ## 장마감시간@@
                "cts_date": "cts_date`char", ## 연속일자@@
                "rec_count": "rec_count`long##레코드카운트@@"
            },
            "o3128OutBlock1": {
                "date": "date`char", ## 날짜@@
                "open": "open`double", ## 시가@@
                "high": "high`double", ## 고가@@
                "low": "low`double", ## 저가@@
                "close": "close`double", ## 종가@@
                "volume": "volume`long##거래량@@"
            }
        }
    },
    "o3136": { ## 해외선물옵션시간대별(Tick)체결(o3136)-API용
        "input": {
            "o3136InBlock": {
                "gubun": " ", ## 조회구분@@0:당일1:전일
                "mktgb": " ", ## 시장구분@@
                "shcode": " ", ## 단축코드@@
                "readcnt": "0", ## 조회갯수@@
                "cts_seq": "0##순번CTS@@"
            }
        },
        "output": {
            "o3136OutBlock": {
                "cts_seq": "cts_seq`long##순번CTS@@"
            },
            "o3136OutBlock1": {
                "ovsdate": "ovsdate`char", ## 현지일자@@
                "ovstime": "ovstime`char", ## 현지시간@@
                "price": "price`double", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`double", ## 전일대비@@
                "diff": "diff`double", ## 등락율@@
                "cvolume": "cvolume`long", ## 체결수량@@
                "volume": "volume`long##누적거래량@@"
            }
        }
    },
    "o3137": { ## 해외선물옵션차트용NTick(o3137)-API용
        "input": {
            "o3137InBlock": {
                "mktgb": " ", ## 시장구분@@
                "shcode": " ", ## 단축코드@@
                "ncnt": "1", ## 단위@@
                "qrycnt": "2000", ## 건수@@
                "cts_seq": " ", ## 연속시간@@
                "cts_daygb": " ##연속당일구분@@"
            }
        },
        "output": {
            "o3137OutBlock": {
                "shcode": "shcode`char", ## 단축코드@@
                "rec_count": "rec_count`long", ## 레코드카운트@@
                "cts_seq": "cts_seq`char", ## 연속시간@@
                "cts_daygb": "cts_daygb`char##연속당일구분@@"
            },
            "o3137OutBlock1": {
                "date": "date`char", ## 날짜@@
                "time": "time`char", ## 시간@@
                "open": "open`double", ## 시가@@
                "high": "high`double", ## 고가@@
                "low": "low`double", ## 저가@@
                "close": "close`double", ## 종가@@
                "volume": "volume`long##거래량@@"
            }
        }
    },
    "o3139": { ## 해외선물옵션차트용NTick(고정형)(o3139)-API용
        "input": {
            "o3139InBlock": {
                "mktgb": " ", ## 시장구분@@
                "shcode": " ", ## 단축코드@@
                "ncnt": "1", ## 단위@@
                "qrycnt": "2000", ## 건수@@
                "cts_seq": " ", ## 연속시간@@
                "cts_daygb": " ##연속당일구분@@"
            }
        },
        "output": {
            "o3139OutBlock": {
                "shcode": "shcode`char", ## 단축코드@@
                "rec_count": "rec_count`long", ## 레코드카운트@@
                "cts_seq": "cts_seq`char", ## 연속시간@@
                "cts_daygb": "cts_daygb`char", ## 연속당일구분@@
                "last_count": "last_count`long##마지막Tick건수@@"
            },
            "o3139OutBlock1": {
                "date": "date`char", ## 날짜@@
                "time": "time`char", ## 시간@@
                "open": "open`double", ## 시가@@
                "high": "high`double", ## 고가@@
                "low": "low`double", ## 저가@@
                "close": "close`double", ## 종가@@
                "volume": "volume`long##거래량@@"
            }
        }
    },
    "OC0": { ## KOSPI200옵션체결(C0)
        "input": {
            "InBlock": {
                "optcode": " ##단축코드@@"
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
    "OD0": { ## KOSPI200옵션실시간상하한가(D0)
        "input": {
            "InBlock": {
                "optcode": " ##단축코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "gubun": "gubun`char", ## 접속매매여부@@
                "dy_gubun": "dy_gubun`char", ## 실시간가격제한여부@@
                "dy_uplmtprice": "dy_uplmtprice`float", ## 실시간상한가@@
                "dy_dnlmtprice": "dy_dnlmtprice`float", ## 실시간하한가@@
                "opttcode": "opttcode`char##단축코드@@"
            }
        }
    },
    "OH0": { ## KOSPI200옵션호가(H0)
        "input": {
            "InBlock": {
                "optcode": " ##단축코드@@"
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
                "optcode": "optcode`char", ## 단축코드@@
                "danhochk": "danhochk`char", ## 단일가호가여부@@
                "alloc_gubun": "alloc_gubun`char##배분적용구분@@"
            }
        }
    },
    "OK_": { ## KOSDAQ거래원(OK)
        "input": {
            "InBlock": {
                "shcode": " ##단축코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "offerno1": "offerno1`char", ## 매도증권사코드1@@
                "bidno1": "bidno1`char", ## 매수증권사코드1@@
                "offertrad1": "offertrad1`char", ## 매도회원사명1@@
                "bidtrad1": "bidtrad1`char", ## 매수회원사명1@@
                "tradmdvol1": "tradmdvol1`long", ## 매도거래량1@@
                "tradmsvol1": "tradmsvol1`long", ## 매수거래량1@@
                "tradmdrate1": "tradmdrate1`float", ## 매도거래량비중1@@
                "tradmsrate1": "tradmsrate1`float", ## 매도거래량비중1@@
                "tradmdcha1": "tradmdcha1`long", ## 매도거래량직전대비1@@
                "tradmscha1": "tradmscha1`long", ## 매수거래량직전대비1@@
                "offerno2": "offerno2`char", ## 매도증권사코드2@@
                "bidno2": "bidno2`char", ## 매수증권사코드2@@
                "offertrad2": "offertrad2`char", ## 매도회원사명2@@
                "bidtrad2": "bidtrad2`char", ## 매수회원사명2@@
                "tradmdvol2": "tradmdvol2`long", ## 매도거래량2@@
                "tradmsvol2": "tradmsvol2`long", ## 매수거래량2@@
                "tradmdrate2": "tradmdrate2`float", ## 매도거래량비중2@@
                "tradmsrate2": "tradmsrate2`float", ## 매수거래량비중2@@
                "tradmdcha2": "tradmdcha2`long", ## 매도거래량직전대비2@@
                "tradmscha2": "tradmscha2`long", ## 매수거래량직전대비2@@
                "offerno3": "offerno3`char", ## 매도증권사코드3@@
                "bidno3": "bidno3`char", ## 매수증권사코드3@@
                "offertrad3": "offertrad3`char", ## 매도회원사명3@@
                "bidtrad3": "bidtrad3`char", ## 매수회원사명3@@
                "tradmdvol3": "tradmdvol3`long", ## 매도거래량3@@
                "tradmsvol3": "tradmsvol3`long", ## 매수거래량3@@
                "tradmdrate3": "tradmdrate3`float", ## 매도거래량비중3@@
                "tradmsrate3": "tradmsrate3`float", ## 매수거래량비중3@@
                "tradmdcha3": "tradmdcha3`long", ## 매도거래량직전대비3@@
                "tradmscha3": "tradmscha3`long", ## 매수거래량직전대비3@@
                "offerno4": "offerno4`char", ## 매도증권사코드4@@
                "bidno4": "bidno4`char", ## 매수증권사코드4@@
                "offertrad4": "offertrad4`char", ## 매도회원사명4@@
                "bidtrad4": "bidtrad4`char", ## 매수회원사명4@@
                "tradmdvol4": "tradmdvol4`long", ## 매도거래량4@@
                "tradmsvol4": "tradmsvol4`long", ## 매수거래량4@@
                "tradmdrate4": "tradmdrate4`float", ## 매도거래량비중4@@
                "tradmsrate4": "tradmsrate4`float", ## 매수거래량비중4@@
                "tradmdcha4": "tradmdcha4`long", ## 매도거래량직전대비4@@
                "tradmscha4": "tradmscha4`long", ## 매수거래량직전대비4@@
                "offerno5": "offerno5`char", ## 매도증권사코드5@@
                "bidno5": "bidno5`char", ## 매수증권사코드5@@
                "offertrad5": "offertrad5`char", ## 매도회원사명5@@
                "bidtrad5": "bidtrad5`char", ## 매수회원사명5@@
                "tradmdvol5": "tradmdvol5`long", ## 매도거래량5@@
                "tradmsvol5": "tradmsvol5`long", ## 매수거래량5@@
                "tradmdrate5": "tradmdrate5`float", ## 매도거래량비중5@@
                "tradmsrate5": "tradmsrate5`float", ## 매수거래량비중5@@
                "tradmdcha5": "tradmdcha5`long", ## 매도거래량직전대비5@@
                "tradmscha5": "tradmscha5`long", ## 매수거래량직전대비5@@
                "ftradmdvol": "ftradmdvol`char", ## 외국계증권사매도합계@@
                "ftradmsvol": "ftradmsvol`char", ## 외국계증권사매수합계@@
                "ftradmdrate": "ftradmdrate`float", ## 외국계증권사매도거래량비중@@
                "ftradmsrate": "ftradmsrate`float", ## 외국계증권사매수거래량비중@@
                "ftradmdcha": "ftradmdcha`char", ## 외국계증권사매도거래량직전대비@@
                "ftradmscha": "ftradmscha`char", ## 외국계증권사매수거래량직전대비@@
                "shcode": "shcode`char", ## 단축코드@@
                "tradmdval1": "tradmdval1`long", ## 매도거래대금1@@
                "tradmsval1": "tradmsval1`long", ## 매수거래대금1@@
                "tradmdavg1": "tradmdavg1`long", ## 매도평균단가1@@
                "tradmsavg1": "tradmsavg1`long", ## 매수평균단가1@@
                "tradmdval2": "tradmdval2`long", ## 매도거래대금2@@
                "tradmsval2": "tradmsval2`long", ## 매수거래대금2@@
                "tradmdavg2": "tradmdavg2`long", ## 매도평균단가2@@
                "tradmsavg2": "tradmsavg2`long", ## 매수평균단가2@@
                "tradmdval3": "tradmdval3`long", ## 매도거래대금3@@
                "tradmsval3": "tradmsval3`long", ## 매수거래대금3@@
                "tradmdavg3": "tradmdavg3`long", ## 매도평균단가3@@
                "tradmsavg3": "tradmsavg3`long", ## 매수평균단가3@@
                "tradmdval4": "tradmdval4`long", ## 매도거래대금4@@
                "tradmsval4": "tradmsval4`long", ## 매수거래대금4@@
                "tradmdavg4": "tradmdavg4`long", ## 매도평균단가4@@
                "tradmsavg4": "tradmsavg4`long", ## 매수평균단가4@@
                "tradmdval5": "tradmdval5`long", ## 매도거래대금5@@
                "tradmsval5": "tradmsval5`long", ## 매수거래대금5@@
                "tradmdavg5": "tradmdavg5`long", ## 매도평균단가5@@
                "tradmsavg5": "tradmsavg5`long", ## 매수평균단가5@@
                "ftradmdval": "ftradmdval`long", ## 외국계증권사매도거래대금@@
                "ftradmsval": "ftradmsval`long", ## 외국계증권사매수거래대금@@
                "ftradmdavg": "ftradmdavg`long", ## 외국계증권사매도평균단가@@
                "ftradmsavg": "ftradmsavg`long##외국계증권사매수평균단가@@"
            }
        }
    },
    "OMG": { ## KOSPI200옵션민감도(MG)
        "input": {
            "InBlock": {
                "optcode": " ##옵션코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "chetime": "chetime`char", ## 체결시간@@
                "actprice": "actprice`float", ## 행사가@@
                "k200jisu": "k200jisu`float", ## KOSPI200지수@@
                "fut200jisu": "fut200jisu`float", ## 선물가격@@
                "price": "price`float", ## 현재가@@
                "capimpv": "capimpv`float", ## 대표내재변동성@@
                "impv": "impv`float", ## 내재변동성@@
                "delt": "delt`float", ## 델타(블랙숄즈)@@
                "gama": "gama`float", ## 감마(블랙숄즈)@@
                "ceta": "ceta`float", ## 세타(블랙숄즈)@@
                "vega": "vega`float", ## 베가(블랙숄즈)@@
                "rhox": "rhox`float", ## 로우(블랙숄즈)@@
                "theoryprice": "theoryprice`float", ## 이론가(블랙숄즈)@@
                "bimpv": "bimpv`float", ## 전일가내재변동성@@
                "offerimpv": "offerimpv`float", ## 매도가내재변동성@@
                "bidimpv": "bidimpv`float", ## 매수가내재변동성@@
                "optcode": "optcode`char##옵션코드@@"
            }
        }
    },
    "OVC": { ## 해외선물 현재가체결(OVC)
        "input": {
            "InBlock": {
                "symbol": " ##종목코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "symbol": "symbol`char", ## 종목코드@@
                "ovsdate": "ovsdate`char", ## 체결일자(현지)@@
                "kordate": "kordate`char", ## 체결일자(한국)@@
                "trdtm": "trdtm`char", ## 체결시간(현지)@@
                "kortm": "kortm`char", ## 체결시간(한국)@@
                "curpr": "curpr`double", ## 체결가격@@
                "ydiffpr": "ydiffpr`double", ## 전일대비@@
                "ydiffSign": "ydiffSign`char", ## 전일대비기호@@
                "open": "open`double", ## 시가@@
                "high": "high`double", ## 고가@@
                "low": "low`double", ## 저가@@
                "chgrate": "chgrate`float", ## 등락율@@
                "trdq": "trdq`long", ## 건별체결수량@@
                "totq": "totq`char", ## 누적체결수량@@
                "cgubun": "cgubun`char", ## 체결구분@@
                "mdvolume": "mdvolume`char", ## 매도누적체결수량@@
                "msvolume": "msvolume`char", ## 매수누적체결수량@@
                "ovsmkend": "ovsmkend`char##장마감일@@"
            }
        }
    },
    "OVH": { ## 해외선물 호가(OVH)
        "input": {
            "InBlock": {
                "symbol": " ##종목코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "symbol": "symbol`char", ## 종목코드@@
                "hotime": "hotime`char", ## 호가시간@@
                "offerho1": "offerho1`double", ## 매도호가 1@@
                "bidho1": "bidho1`double", ## 매수호가 1@@
                "offerrem1": "offerrem1`long", ## 매도호가 잔량 1@@
                "bidrem1": "bidrem1`long", ## 매수호가 잔량 1@@
                "offerno1": "offerno1`long", ## 매도호가 건수 1@@
                "bidno1": "bidno1`long", ## 매수호가 건수 1@@
                "offerho2": "offerho2`double", ## 매도호가 2@@
                "bidho2": "bidho2`double", ## 매수호가 2@@
                "offerrem2": "offerrem2`long", ## 매도호가 잔량 2@@
                "bidrem2": "bidrem2`long", ## 매수호가 잔량 2@@
                "offerno2": "offerno2`long", ## 매도호가 건수 2@@
                "bidno2": "bidno2`long", ## 매수호가 건수 2@@
                "offerho3": "offerho3`double", ## 매도호가 3@@
                "bidho3": "bidho3`double", ## 매수호가 3@@
                "offerrem3": "offerrem3`long", ## 매도호가 잔량 3@@
                "bidrem3": "bidrem3`long", ## 매수호가 잔량 3@@
                "offerno3": "offerno3`long", ## 매도호가 건수 3@@
                "bidno3": "bidno3`long", ## 매수호가 건수 3@@
                "offerho4": "offerho4`double", ## 매도호가 4@@
                "bidho4": "bidho4`double", ## 매수호가 4@@
                "offerrem4": "offerrem4`long", ## 매도호가 잔량 4@@
                "bidrem4": "bidrem4`long", ## 매수호가 잔량 4@@
                "offerno4": "offerno4`long", ## 매도호가 건수 4@@
                "bidno4": "bidno4`long", ## 매수호가 건수 4@@
                "offerho5": "offerho5`double", ## 매도호가 5@@
                "bidho5": "bidho5`double", ## 매수호가 5@@
                "offerrem5": "offerrem5`long", ## 매도호가 잔량 5@@
                "bidrem5": "bidrem5`long", ## 매수호가 잔량 5@@
                "offerno5": "offerno5`long", ## 매도호가 건수 5@@
                "bidno5": "bidno5`long", ## 매수호가 건수 5@@
                "totoffercnt": "totoffercnt`long", ## 매도호가총건수@@
                "totbidcnt": "totbidcnt`long", ## 매수호가총건수@@
                "totofferrem": "totofferrem`long", ## 매도호가총수량@@
                "totbidrem": "totbidrem`long##매수호가총수량@@"
            }
        }
    },
    "OX0": { ## KOSPI200옵션가격제한폭확대(X0)
        "input": {
            "InBlock": {
                "optcode": " ##단축코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "upstep": "upstep`char", ## 적용 상한단계@@
                "dnstep": "dnstep`char", ## 적용 하한단계@@
                "uplmtprice": "uplmtprice`float", ## 적용 상한가@@
                "dnlmtprice": "dnlmtprice`float", ## 적용 하한가@@
                "opttcode": "opttcode`char##단축코드@@"
            }
        }
    },
    "PH_": { ## KOSPI프로그램매매종목별(PH)
        "input": {
            "InBlock": {
                "shcode": " ##종목코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "time": "time`char", ## 수신시간@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`long", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "volume": "volume`long", ## 누적거래량@@
                "drate": "drate`float", ## 등락율@@
                "cdhrem": "cdhrem`long", ## 차익매도호가 잔량@@
                "cshrem": "cshrem`long", ## 차익매수호가 잔량@@
                "bdhrem": "bdhrem`long", ## 비차익매도호가 잔량@@
                "bshrem": "bshrem`long", ## 비차익매수호가 잔량@@
                "cdhvolume": "cdhvolume`long", ## 차익매도호가 수량@@
                "cshvolume": "cshvolume`long", ## 차익매수호가 수량@@
                "bdhvolume": "bdhvolume`long", ## 비차익매도호가 수량@@
                "bshvolume": "bshvolume`long", ## 비차익매수호가 수량@@
                "dwcvolume": "dwcvolume`long", ## 전체매도위탁체결수량@@
                "swcvolume": "swcvolume`long", ## 전체매수위탁체결수량@@
                "djcvolume": "djcvolume`long", ## 전체매도자기체결수량@@
                "sjcvolume": "sjcvolume`long", ## 전체매수자기체결수량@@
                "tdvolume": "tdvolume`long", ## 전체매도체결수량@@
                "tsvolume": "tsvolume`long", ## 전체매수체결수량@@
                "tvol": "tvol`long", ## 전체순매수 수량@@
                "dwcvalue": "dwcvalue`long", ## 전체매도위탁체결금액@@
                "swcvalue": "swcvalue`long", ## 전체매수위탁체결금액@@
                "djcvalue": "djcvalue`long", ## 전체매도자기체결금액@@
                "sjcvalue": "sjcvalue`long", ## 전체매수자기체결금액@@
                "tdvalue": "tdvalue`long", ## 전체매도체결금액@@
                "tsvalue": "tsvalue`long", ## 전체매수체결금액@@
                "tval": "tval`long", ## 전체순매수 금액@@
                "pdgvolume": "pdgvolume`long", ## 매도 사전공시수량@@
                "psgvolume": "psgvolume`long", ## 매수 사전공시수량@@
                "shcode": "shcode`char##종목코드@@"
            }
        }
    },
    "PM_": { ## KOSPI프로그램매매전체집계(PM)
        "input": {
            "InBlock": {
                "gubun": " ##구분값@@"
            }
        },
        "output": {
            "OutBlock": {
                "time": "time`char", ## 수신시간@@
                "cdhrem": "cdhrem`long", ## 차익매도호가 잔량@@
                "cshrem": "cshrem`long", ## 차익매수호가 잔량@@
                "bdhrem": "bdhrem`long", ## 비차익매도호가 잔량@@
                "bshrem": "bshrem`long", ## 비차익매수호가 잔량@@
                "cdhvolume": "cdhvolume`long", ## 차익매도호가 수량@@
                "cshvolume": "cshvolume`long", ## 차익매수호가 수량@@
                "bdhvolume": "bdhvolume`long", ## 비차익매도호가 수량@@
                "bshvolume": "bshvolume`long", ## 비차익매수호가 수량@@
                "cdwvolume": "cdwvolume`long", ## 차익매도위탁체결수량@@
                "cdjvolume": "cdjvolume`long", ## 차익매도자기체결수량@@
                "cswvolume": "cswvolume`long", ## 차익매수위탁체결수량@@
                "csjvolume": "csjvolume`long", ## 차익매수자기체결수량@@
                "cwvol": "cwvol`long", ## 차익위탁순매수 수량@@
                "cjvol": "cjvol`long", ## 차익자기순매수 수량@@
                "bdwvolume": "bdwvolume`long", ## 비차익매도위탁체결수량@@
                "bdjvolume": "bdjvolume`long", ## 비차익매도자기체결수량@@
                "bswvolume": "bswvolume`long", ## 비차익매수위탁체결수량@@
                "bsjvolume": "bsjvolume`long", ## 비차익매수자기체결수량@@
                "bwvol": "bwvol`long", ## 비차익위탁순매수 수량@@
                "bjvol": "bjvol`long", ## 비차익자기순매수 수량@@
                "dwvolume": "dwvolume`long", ## 전체매도위탁체결수량@@
                "swvolume": "swvolume`long", ## 전체매수위탁체결수량@@
                "wvol": "wvol`long", ## 전체위탁순매수 수량@@
                "djvolume": "djvolume`long", ## 전체매도자기체결수량@@
                "sjvolume": "sjvolume`long", ## 전체매수자기체결수량@@
                "jvol": "jvol`long", ## 전체자기순매수 수량@@
                "cdwvalue": "cdwvalue`long", ## 차익매도위탁체결금액@@
                "cdjvalue": "cdjvalue`long", ## 차익매도자기체결금액@@
                "cswvalue": "cswvalue`long", ## 차익매수위탁체결금액@@
                "csjvalue": "csjvalue`long", ## 차익매수자기체결금액@@
                "cwval": "cwval`long", ## 차익위탁순매수 금액@@
                "cjval": "cjval`long", ## 차익자기순매수 금액@@
                "bdwvalue": "bdwvalue`long", ## 비차익매도위탁체결금액@@
                "bdjvalue": "bdjvalue`long", ## 비차익매도자기체결금액@@
                "bswvalue": "bswvalue`long", ## 비차익매수위탁체결금액@@
                "bsjvalue": "bsjvalue`long", ## 비차익매수자기체결금액@@
                "bwval": "bwval`long", ## 비차익위탁순매수 금액@@
                "bjval": "bjval`long", ## 비차익자기순매수 금액@@
                "dwvalue": "dwvalue`long", ## 전체매도위탁체결금액@@
                "swvalue": "swvalue`long", ## 전체매수위탁체결금액@@
                "wval": "wval`long", ## 전체위탁순매수 금액@@
                "djvalue": "djvalue`long", ## 전체매도자기체결금액@@
                "sjvalue": "sjvalue`long", ## 전체매수자기체결금액@@
                "jval": "jval`long", ## 전체자기순매수 금액@@
                "k200jisu": "k200jisu`float", ## KOSPI200 지수@@
                "k200sign": "k200sign`char", ## KOSPI200 전일대비구분@@
                "change": "change`float", ## KOSPI200 전일대비@@
                "k200basis": "k200basis`float", ## KOSPI200 베이시스@@
                "cdvolume": "cdvolume`long", ## 차익매도체결수량합계@@
                "csvolume": "csvolume`long", ## 차익매수체결수량합계@@
                "cvol": "cvol`long", ## 차익순매수 수량합계@@
                "bdvolume": "bdvolume`long", ## 비차익매도체결수량합계@@
                "bsvolume": "bsvolume`long", ## 비차익매수체결수량합계@@
                "bvol": "bvol`long", ## 비차익순매수 수량합계@@
                "tdvolume": "tdvolume`long", ## 전체매도체결수량합계@@
                "tsvolume": "tsvolume`long", ## 전체매수체결수량합계@@
                "tvol": "tvol`long", ## 전체순매수 수량합계@@
                "cdvalue": "cdvalue`long", ## 차익매도체결금액합계@@
                "csvalue": "csvalue`long", ## 차익매수체결금액합계@@
                "cval": "cval`long", ## 차익순매수 금액합계@@
                "bdvalue": "bdvalue`long", ## 비차익매도체결금액합계@@
                "bsvalue": "bsvalue`long", ## 비차익매수체결금액합계@@
                "bval": "bval`long", ## 비차익순매수 금액합계@@
                "tdvalue": "tdvalue`long", ## 전체매도체결금액합계@@
                "tsvalue": "tsvalue`long", ## 전체매수체결금액합계@@
                "tval": "tval`long", ## 전체순매수 금액합계@@
                "p_cdvolcha": "p_cdvolcha`long", ## 차익매도체결수량직전대비@@
                "p_csvolcha": "p_csvolcha`long", ## 차익매수체결수량직전대비@@
                "p_cvolcha": "p_cvolcha`long", ## 차익순매수 수량직전대비@@
                "p_bdvolcha": "p_bdvolcha`long", ## 비차익매도체결수량직전대비@@
                "p_bsvolcha": "p_bsvolcha`long", ## 비차익매수체결수량직전대비@@
                "p_bvolcha": "p_bvolcha`long", ## 비차익순매수 수량직전대비@@
                "p_tdvolcha": "p_tdvolcha`long", ## 전체매도체결수량직전대비@@
                "p_tsvolcha": "p_tsvolcha`long", ## 전체매수체결수량직전대비@@
                "p_tvolcha": "p_tvolcha`long", ## 전체순매수 수량직전대비@@
                "p_cdvalcha": "p_cdvalcha`long", ## 차익매도체결금액직전대비@@
                "p_csvalcha": "p_csvalcha`long", ## 차익매수체결금액직전대비@@
                "p_cvalcha": "p_cvalcha`long", ## 차익순매수 금액직전대비@@
                "p_bdvalcha": "p_bdvalcha`long", ## 비차익매도체결금액직전대비@@
                "p_bsvalcha": "p_bsvalcha`long", ## 비차익매수체결금액직전대비@@
                "p_bvalcha": "p_bvalcha`long", ## 비차익순매수 금액직전대비@@
                "p_tdvalcha": "p_tdvalcha`long", ## 전체매도체결금액직전대비@@
                "p_tsvalcha": "p_tsvalcha`long", ## 전체매수체결금액직전대비@@
                "p_tvalcha": "p_tvalcha`long", ## 전체순매수 금액직전대비@@
                "gubun": "gubun`char##구분값@@"
            }
        }
    },
    "S2_": { ## KOSPI우선호가(S2)
        "input": {
            "InBlock": {
                "shcode": " ##단축코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "offerho": "offerho`long", ## 매도호가@@
                "bidho": "bidho`long", ## 매수호가@@
                "shcode": "shcode`char##단축코드@@"
            }
        }
    },
    "s2_4ELW": { ## ELW우선호가(s2)
        "input": {
            "InBlock": {
                "shcode": " ##단축코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "offerho": "offerho`long", ## 매도호가@@
                "bidho": "bidho`long", ## 매수호가@@
                "shcode": "shcode`char##단축코드@@"
            }
        }
    },
    "S3_": { ## KOSPI체결(S3)
        "input": {
            "InBlock": {
                "shcode": " ##단축코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "chetime": "chetime`char", ## 체결시간@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "drate": "drate`float", ## 등락율@@
                "price": "price`long", ## 현재가@@
                "opentime": "opentime`char", ## 시가시간@@
                "open": "open`long", ## 시가@@
                "hightime": "hightime`char", ## 고가시간@@
                "high": "high`long", ## 고가@@
                "lowtime": "lowtime`char", ## 저가시간@@
                "low": "low`long", ## 저가@@
                "cgubun": "cgubun`char", ## 체결구분@@
                "cvolume": "cvolume`long", ## 체결량@@
                "volume": "volume`long", ## 누적거래량@@
                "value": "value`long", ## 누적거래대금@@
                "mdvolume": "mdvolume`long", ## 매도누적체결량@@
                "mdchecnt": "mdchecnt`long", ## 매도누적체결건수@@
                "msvolume": "msvolume`long", ## 매수누적체결량@@
                "mschecnt": "mschecnt`long", ## 매수누적체결건수@@
                "cpower": "cpower`float", ## 체결강도@@
                "w_avrg": "w_avrg`long", ## 가중평균가@@
                "offerho": "offerho`long", ## 매도호가@@
                "bidho": "bidho`long", ## 매수호가@@
                "status": "status`char", ## 장정보@@
                "jnilvolume": "jnilvolume`long", ## 전일동시간대거래량@@
                "shcode": "shcode`char##단축코드@@"
            }
        }
    },
    "s3_4ELW": { ## ELW체결(s3)
        "input": {
            "InBlock": {
                "shcode": " ##단축코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "chetime": "chetime`char", ## 체결시간@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "drate": "drate`float", ## 등락율@@
                "price": "price`long", ## 현재가@@
                "opentime": "opentime`char", ## 시가시간@@
                "open": "open`long", ## 시가@@
                "hightime": "hightime`char", ## 고가시간@@
                "high": "high`long", ## 고가@@
                "lowtime": "lowtime`char", ## 저가시간@@
                "low": "low`long", ## 저가@@
                "cgubun": "cgubun`char", ## 체결구분@@
                "cvolume": "cvolume`long", ## 체결량@@
                "volume": "volume`long", ## 누적거래량@@
                "value": "value`long", ## 누적거래대금@@
                "mdvolume": "mdvolume`long", ## 매도누적체결량@@
                "mdchecnt": "mdchecnt`long", ## 매도누적체결건수@@
                "msvolume": "msvolume`long", ## 매수누적체결량@@
                "mschecnt": "mschecnt`long", ## 매수누적체결건수@@
                "cpower": "cpower`float", ## 체결강도@@
                "w_avrg": "w_avrg`long", ## 가중평균가@@
                "offerho": "offerho`long", ## 매도호가@@
                "bidho": "bidho`long", ## 매수호가@@
                "status": "status`char", ## 장정보@@
                "jnilvolume": "jnilvolume`long", ## 전일동시간대거래량@@
                "premium": "premium`float", ## 프리미엄@@
                "moneyness": "moneyness`char", ## ATM구분@@
                "shcode": "shcode`char", ## 단축코드@@
                "lpvolume": "lpvolume`long##LP보유수량@@"
            }
        }
    },
    "S4_": { ## KOSPI기세(S4)
        "input": {
            "InBlock": {
                "shcode": " ##단축코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "drate": "drate`float", ## 등락율@@
                "price": "price`long", ## 현재가@@
                "opentime": "opentime`char", ## 시가시간@@
                "open": "open`long", ## 시가@@
                "hightime": "hightime`char", ## 고가시간@@
                "high": "high`long", ## 고가@@
                "lowtime": "lowtime`char", ## 저가시간@@
                "low": "low`long", ## 저가@@
                "shcode": "shcode`char##단축코드@@"
            }
        }
    },
    "s4_ELW": { ## ELW기세(s4)
        "input": {
            "InBlock": {
                "shcode": " ##단축코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "drate": "drate`float", ## 등락율@@
                "price": "price`long", ## 현재가@@
                "opentime": "opentime`char", ## 시가시간@@
                "open": "open`long", ## 시가@@
                "hightime": "hightime`char", ## 고가시간@@
                "high": "high`long", ## 고가@@
                "lowtime": "lowtime`char", ## 저가시간@@
                "low": "low`long", ## 저가@@
                "shcode": "shcode`char##단축코드@@"
            }
        }
    },
    "SC0": { ## 주식주문접수
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
                "ordchegb": "ordchegb`char", ## 주문체결구분@@
                "marketgb": "marketgb`char", ## 시장구분@@
                "ordgb": "ordgb`char", ## 주문구분@@
                "orgordno": "orgordno`long", ## 원주문번호@@
                "accno1": "accno1`char", ## 계좌번호@@
                "accno2": "accno2`char", ## 계좌번호@@
                "passwd": "passwd`char", ## 비밀번호@@
                "expcode": "expcode`char", ## 종목번호@@
                "shtcode": "shtcode`char", ## 단축종목번호@@
                "hname": "hname`char", ## 종목명@@
                "ordqty": "ordqty`long", ## 주문수량@@
                "ordprice": "ordprice`long", ## 주문가격@@
                "hogagb": "hogagb`char", ## 주문조건@@
                "etfhogagb": "etfhogagb`char", ## 호가유형코드@@
                "pgmtype": "pgmtype`long", ## 프로그램호가구분@@
                "gmhogagb": "gmhogagb`long", ## 공매도호가구분@@
                "gmhogayn": "gmhogayn`long", ## 공매도가능여부@@
                "singb": "singb`char", ## 신용구분@@
                "loandt": "loandt`char", ## 대출일@@
                "cvrgordtp": "cvrgordtp`char", ## 반대매매주문구분@@
                "strtgcode": "strtgcode`char", ## 전략코드@@
                "groupid": "groupid`char", ## 그룹ID@@
                "ordseqno": "ordseqno`long", ## 주문회차@@
                "prtno": "prtno`long", ## 포트폴리오번호@@
                "basketno": "basketno`long", ## 바스켓번호@@
                "trchno": "trchno`long", ## 트렌치번호@@
                "itemno": "itemno`long", ## 아아템번호@@
                "brwmgmyn": "brwmgmyn`long", ## 차입구분@@
                "mbrno": "mbrno`long", ## 회원사번호@@
                "procgb": "procgb`char", ## 처리구분@@
                "admbrchno": "admbrchno`char", ## 관리지점번호@@
                "futaccno": "futaccno`char", ## 선물계좌번호@@
                "futmarketgb": "futmarketgb`char", ## 선물상품구분@@
                "tongsingb": "tongsingb`char", ## 통신매체구분@@
                "lpgb": "lpgb`char", ## 유동성공급자구분@@
                "dummy": "dummy`char", ## DUMMY@@
                "ordno": "ordno`long", ## 주문번호@@
                "ordtm": "ordtm`char", ## 주문시각@@
                "prntordno": "prntordno`long", ## 모주문번호@@
                "mgempno": "mgempno`char", ## 관리사원번호@@
                "orgordundrqty": "orgordundrqty`long", ## 원주문미체결수량@@
                "orgordmdfyqty": "orgordmdfyqty`long", ## 원주문정정수량@@
                "ordordcancelqty": "ordordcancelqty`long", ## 원주문취소수량@@
                "nmcpysndno": "nmcpysndno`long", ## 비회원사송신번호@@
                "ordamt": "ordamt`long", ## 주문금액@@
                "bnstp": "bnstp`char", ## 매매구분@@
                "spareordno": "spareordno`long", ## 예비주문번호@@
                "cvrgseqno": "cvrgseqno`long", ## 반대매매일련번호@@
                "rsvordno": "rsvordno`long", ## 예약주문번호@@
                "mtordseqno": "mtordseqno`long", ## 복수주문일련번호@@
                "spareordqty": "spareordqty`long", ## 예비주문수량@@
                "orduserid": "orduserid`char", ## 주문사원번호@@
                "spotordqty": "spotordqty`long", ## 실물주문수량@@
                "ordruseqty": "ordruseqty`long", ## 재사용주문수량@@
                "mnyordamt": "mnyordamt`long", ## 현금주문금액@@
                "ordsubstamt": "ordsubstamt`long", ## 주문대용금액@@
                "ruseordamt": "ruseordamt`long", ## 재사용주문금액@@
                "ordcmsnamt": "ordcmsnamt`long", ## 수수료주문금액@@
                "crdtuseamt": "crdtuseamt`long", ## 사용신용담보재사용금@@
                "secbalqty": "secbalqty`long", ## 잔고수량@@
                "spotordableqty": "spotordableqty`long", ## 실물가능수량@@
                "ordableruseqty": "ordableruseqty`long", ## 재사용가능수량(매도)@@
                "flctqty": "flctqty`long", ## 변동수량@@
                "secbalqtyd2": "secbalqtyd2`long", ## 잔고수량(D2)@@
                "sellableqty": "sellableqty`long", ## 매도주문가능수량@@
                "unercsellordqty": "unercsellordqty`long", ## 미체결매도주문수량@@
                "avrpchsprc": "avrpchsprc`long", ## 평균매입가@@
                "pchsamt": "pchsamt`long", ## 매입금액@@
                "deposit": "deposit`long", ## 예수금@@
                "substamt": "substamt`long", ## 대용금@@
                "csgnmnymgn": "csgnmnymgn`long", ## 위탁증거금현금@@
                "csgnsubstmgn": "csgnsubstmgn`long", ## 위탁증거금대용@@
                "crdtpldgruseamt": "crdtpldgruseamt`long", ## 신용담보재사용금@@
                "ordablemny": "ordablemny`long", ## 주문가능현금@@
                "ordablesubstamt": "ordablesubstamt`long", ## 주문가능대용@@
                "ruseableamt": "ruseableamt`long##재사용가능금액@@"
            }
        }
    },
    "SC1": { ## 주식주문체결
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
                "ordxctptncode": "ordxctptncode`char", ## 주문체결유형코드@@
                "ordmktcode": "ordmktcode`char", ## 주문시장코드@@
                "ordptncode": "ordptncode`char", ## 주문유형코드@@
                "mgmtbrnno": "mgmtbrnno`char", ## 관리지점번호@@
                "accno1": "accno1`char", ## 계좌번호@@
                "accno2": "accno2`char", ## 계좌번호@@
                "acntnm": "acntnm`char", ## 계좌명@@
                "Isuno": "Isuno`char", ## 종목번호@@
                "Isunm": "Isunm`char", ## 종목명@@
                "ordno": "ordno`long", ## 주문번호@@
                "orgordno": "orgordno`long", ## 원주문번호@@
                "execno": "execno`long", ## 체결번호@@
                "ordqty": "ordqty`long", ## 주문수량@@
                "ordprc": "ordprc`long", ## 주문가격@@
                "execqty": "execqty`long", ## 체결수량@@
                "execprc": "execprc`long", ## 체결가격@@
                "mdfycnfqty": "mdfycnfqty`long", ## 정정확인수량@@
                "mdfycnfprc": "mdfycnfprc`long", ## 정정확인가격@@
                "canccnfqty": "canccnfqty`long", ## 취소확인수량@@
                "rjtqty": "rjtqty`long", ## 거부수량@@
                "ordtrxptncode": "ordtrxptncode`long", ## 주문처리유형코드@@
                "mtiordseqno": "mtiordseqno`long", ## 복수주문일련번호@@
                "ordcndi": "ordcndi`char", ## 주문조건@@
                "ordprcptncode": "ordprcptncode`char", ## 호가유형코드@@
                "nsavtrdqty": "nsavtrdqty`long", ## 비저축체결수량@@
                "shtnIsuno": "shtnIsuno`char", ## 단축종목번호@@
                "opdrtnno": "opdrtnno`char", ## 운용지시번호@@
                "cvrgordtp": "cvrgordtp`char", ## 반대매매주문구분@@
                "unercqty": "unercqty`long", ## 미체결수량(주문)@@
                "orgordunercqty": "orgordunercqty`long", ## 원주문미체결수량@@
                "orgordmdfyqty": "orgordmdfyqty`long", ## 원주문정정수량@@
                "orgordcancqty": "orgordcancqty`long", ## 원주문취소수량@@
                "ordavrexecprc": "ordavrexecprc`long", ## 주문평균체결가격@@
                "ordamt": "ordamt`long", ## 주문금액@@
                "stdIsuno": "stdIsuno`char", ## 표준종목번호@@
                "bfstdIsuno": "bfstdIsuno`char", ## 전표준종목번호@@
                "bnstp": "bnstp`char", ## 매매구분@@
                "ordtrdptncode": "ordtrdptncode`char", ## 주문거래유형코드@@
                "mgntrncode": "mgntrncode`char", ## 신용거래코드@@
                "adduptp": "adduptp`char", ## 수수료합산코드@@
                "commdacode": "commdacode`char", ## 통신매체코드@@
                "Loandt": "Loandt`char", ## 대출일@@
                "mbrnmbrno": "mbrnmbrno`long", ## 회원/비회원사번호@@
                "ordacntno": "ordacntno`char", ## 주문계좌번호@@
                "agrgbrnno": "agrgbrnno`char", ## 집계지점번호@@
                "mgempno": "mgempno`char", ## 관리사원번호@@
                "futsLnkbrnno": "futsLnkbrnno`char", ## 선물연계지점번호@@
                "futsLnkacntno": "futsLnkacntno`char", ## 선물연계계좌번호@@
                "futsmkttp": "futsmkttp`char", ## 선물시장구분@@
                "regmktcode": "regmktcode`char", ## 등록시장코드@@
                "mnymgnrat": "mnymgnrat`long", ## 현금증거금률@@
                "substmgnrat": "substmgnrat`long", ## 대용증거금률@@
                "mnyexecamt": "mnyexecamt`long", ## 현금체결금액@@
                "ubstexecamt": "ubstexecamt`long", ## 대용체결금액@@
                "cmsnamtexecamt": "cmsnamtexecamt`long", ## 수수료체결금액@@
                "crdtpldgexecamt": "crdtpldgexecamt`long", ## 신용담보체결금액@@
                "crdtexecamt": "crdtexecamt`long", ## 신용체결금액@@
                "prdayruseexecval": "prdayruseexecval`long", ## 전일재사용체결금액@@
                "crdayruseexecval": "crdayruseexecval`long", ## 금일재사용체결금액@@
                "spotexecqty": "spotexecqty`long", ## 실물체결수량@@
                "stslexecqty": "stslexecqty`long", ## 공매도체결수량@@
                "strtgcode": "strtgcode`char", ## 전략코드@@
                "grpId": "grpId`char", ## 그룹Id@@
                "ordseqno": "ordseqno`long", ## 주문회차@@
                "ptflno": "ptflno`long", ## 포트폴리오번호@@
                "bskno": "bskno`long", ## 바스켓번호@@
                "trchno": "trchno`long", ## 트렌치번호@@
                "itemno": "itemno`long", ## 아이템번호@@
                "orduserId": "orduserId`char", ## 주문자Id@@
                "brwmgmtYn": "brwmgmtYn`long", ## 차입관리여부@@
                "frgrunqno": "frgrunqno`char", ## 외국인고유번호@@
                "trtzxLevytp": "trtzxLevytp`char", ## 거래세징수구분@@
                "lptp": "lptp`char", ## 유동성공급자구분@@
                "exectime": "exectime`char", ## 체결시각@@
                "rcptexectime": "rcptexectime`char", ## 거래소수신체결시각@@
                "rmndLoanamt": "rmndLoanamt`long", ## 잔여대출금액@@
                "secbalqty": "secbalqty`long", ## 잔고수량@@
                "spotordableqty": "spotordableqty`long", ## 실물가능수량@@
                "ordableruseqty": "ordableruseqty`long", ## 재사용가능수량(매도)@@
                "flctqty": "flctqty`long", ## 변동수량@@
                "secbalqtyd2": "secbalqtyd2`long", ## 잔고수량(d2)@@
                "sellableqty": "sellableqty`long", ## 매도주문가능수량@@
                "unercsellordqty": "unercsellordqty`long", ## 미체결매도주문수량@@
                "avrpchsprc": "avrpchsprc`long", ## 평균매입가@@
                "pchsant": "pchsant`long", ## 매입금액@@
                "deposit": "deposit`long", ## 예수금@@
                "substamt": "substamt`long", ## 대용금@@
                "csgnmnymgn": "csgnmnymgn`long", ## 위탁증거금현금@@
                "csgnsubstmgn": "csgnsubstmgn`long", ## 위탁증거금대용@@
                "crdtpldgruseamt": "crdtpldgruseamt`long", ## 신용담보재사용금@@
                "ordablemny": "ordablemny`long", ## 주문가능현금@@
                "ordablesubstamt": "ordablesubstamt`long", ## 주문가능대용@@
                "ruseableamt": "ruseableamt`long##재사용가능금액@@"
            }
        }
    },
    "SC2": { ## 주식주문정정
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
                "ordxctptncode": "ordxctptncode`char", ## 주문체결유형코드@@
                "ordmktcode": "ordmktcode`char", ## 주문시장코드@@
                "ordptncode": "ordptncode`char", ## 주문유형코드@@
                "mgmtbrnno": "mgmtbrnno`char", ## 관리지점번호@@
                "accno1": "accno1`char", ## 계좌번호@@
                "accno2": "accno2`char", ## 계좌번호@@
                "acntnm": "acntnm`char", ## 계좌명@@
                "Isuno": "Isuno`char", ## 종목번호@@
                "Isunm": "Isunm`char", ## 종목명@@
                "ordno": "ordno`long", ## 주문번호@@
                "orgordno": "orgordno`long", ## 원주문번호@@
                "execno": "execno`long", ## 체결번호@@
                "ordqty": "ordqty`long", ## 주문수량@@
                "ordprc": "ordprc`long", ## 주문가격@@
                "execqty": "execqty`long", ## 체결수량@@
                "execprc": "execprc`long", ## 체결가격@@
                "mdfycnfqty": "mdfycnfqty`long", ## 정정확인수량@@
                "mdfycnfprc": "mdfycnfprc`long", ## 정정확인가격@@
                "canccnfqty": "canccnfqty`long", ## 취소확인수량@@
                "rjtqty": "rjtqty`long", ## 거부수량@@
                "ordtrxptncode": "ordtrxptncode`long", ## 주문처리유형코드@@
                "mtiordseqno": "mtiordseqno`long", ## 복수주문일련번호@@
                "ordcndi": "ordcndi`char", ## 주문조건@@
                "ordprcptncode": "ordprcptncode`char", ## 호가유형코드@@
                "nsavtrdqty": "nsavtrdqty`long", ## 비저축체결수량@@
                "shtnIsuno": "shtnIsuno`char", ## 단축종목번호@@
                "opdrtnno": "opdrtnno`char", ## 운용지시번호@@
                "cvrgordtp": "cvrgordtp`char", ## 반대매매주문구분@@
                "unercqty": "unercqty`long", ## 미체결수량(주문)@@
                "orgordunercqty": "orgordunercqty`long", ## 원주문미체결수량@@
                "orgordmdfyqty": "orgordmdfyqty`long", ## 원주문정정수량@@
                "orgordcancqty": "orgordcancqty`long", ## 원주문취소수량@@
                "ordavrexecprc": "ordavrexecprc`long", ## 주문평균체결가격@@
                "ordamt": "ordamt`long", ## 주문금액@@
                "stdIsuno": "stdIsuno`char", ## 표준종목번호@@
                "bfstdIsuno": "bfstdIsuno`char", ## 전표준종목번호@@
                "bnstp": "bnstp`char", ## 매매구분@@
                "ordtrdptncode": "ordtrdptncode`char", ## 주문거래유형코드@@
                "mgntrncode": "mgntrncode`char", ## 신용거래코드@@
                "adduptp": "adduptp`char", ## 수수료합산코드@@
                "commdacode": "commdacode`char", ## 통신매체코드@@
                "Loandt": "Loandt`char", ## 대출일@@
                "mbrnmbrno": "mbrnmbrno`long", ## 회원/비회원사번호@@
                "ordacntno": "ordacntno`char", ## 주문계좌번호@@
                "agrgbrnno": "agrgbrnno`char", ## 집계지점번호@@
                "mgempno": "mgempno`char", ## 관리사원번호@@
                "futsLnkbrnno": "futsLnkbrnno`char", ## 선물연계지점번호@@
                "futsLnkacntno": "futsLnkacntno`char", ## 선물연계계좌번호@@
                "futsmkttp": "futsmkttp`char", ## 선물시장구분@@
                "regmktcode": "regmktcode`char", ## 등록시장코드@@
                "mnymgnrat": "mnymgnrat`long", ## 현금증거금률@@
                "substmgnrat": "substmgnrat`long", ## 대용증거금률@@
                "mnyexecamt": "mnyexecamt`long", ## 현금체결금액@@
                "ubstexecamt": "ubstexecamt`long", ## 대용체결금액@@
                "cmsnamtexecamt": "cmsnamtexecamt`long", ## 수수료체결금액@@
                "crdtpldgexecamt": "crdtpldgexecamt`long", ## 신용담보체결금액@@
                "crdtexecamt": "crdtexecamt`long", ## 신용체결금액@@
                "prdayruseexecval": "prdayruseexecval`long", ## 전일재사용체결금액@@
                "crdayruseexecval": "crdayruseexecval`long", ## 금일재사용체결금액@@
                "spotexecqty": "spotexecqty`long", ## 실물체결수량@@
                "stslexecqty": "stslexecqty`long", ## 공매도체결수량@@
                "strtgcode": "strtgcode`char", ## 전략코드@@
                "grpId": "grpId`char", ## 그룹Id@@
                "ordseqno": "ordseqno`long", ## 주문회차@@
                "ptflno": "ptflno`long", ## 포트폴리오번호@@
                "bskno": "bskno`long", ## 바스켓번호@@
                "trchno": "trchno`long", ## 트렌치번호@@
                "itemno": "itemno`long", ## 아이템번호@@
                "orduserId": "orduserId`char", ## 주문자Id@@
                "brwmgmtYn": "brwmgmtYn`long", ## 차입관리여부@@
                "frgrunqno": "frgrunqno`char", ## 외국인고유번호@@
                "trtzxLevytp": "trtzxLevytp`char", ## 거래세징수구분@@
                "lptp": "lptp`char", ## 유동성공급자구분@@
                "exectime": "exectime`char", ## 체결시각@@
                "rcptexectime": "rcptexectime`char", ## 거래소수신체결시각@@
                "rmndLoanamt": "rmndLoanamt`long", ## 잔여대출금액@@
                "secbalqty": "secbalqty`long", ## 잔고수량@@
                "spotordableqty": "spotordableqty`long", ## 실물가능수량@@
                "ordableruseqty": "ordableruseqty`long", ## 재사용가능수량(매도)@@
                "flctqty": "flctqty`long", ## 변동수량@@
                "secbalqtyd2": "secbalqtyd2`long", ## 잔고수량(d2)@@
                "sellableqty": "sellableqty`long", ## 매도주문가능수량@@
                "unercsellordqty": "unercsellordqty`long", ## 미체결매도주문수량@@
                "avrpchsprc": "avrpchsprc`long", ## 평균매입가@@
                "pchsant": "pchsant`long", ## 매입금액@@
                "deposit": "deposit`long", ## 예수금@@
                "substamt": "substamt`long", ## 대용금@@
                "csgnmnymgn": "csgnmnymgn`long", ## 위탁증거금현금@@
                "csgnsubstmgn": "csgnsubstmgn`long", ## 위탁증거금대용@@
                "crdtpldgruseamt": "crdtpldgruseamt`long", ## 신용담보재사용금@@
                "ordablemny": "ordablemny`long", ## 주문가능현금@@
                "ordablesubstamt": "ordablesubstamt`long", ## 주문가능대용@@
                "ruseableamt": "ruseableamt`long##재사용가능금액@@"
            }
        }
    },
    "SC3": { ## 주식주문취소
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
                "ordxctptncode": "ordxctptncode`char", ## 주문체결유형코드@@
                "ordmktcode": "ordmktcode`char", ## 주문시장코드@@
                "ordptncode": "ordptncode`char", ## 주문유형코드@@
                "mgmtbrnno": "mgmtbrnno`char", ## 관리지점번호@@
                "accno1": "accno1`char", ## 계좌번호@@
                "accno2": "accno2`char", ## 계좌번호@@
                "acntnm": "acntnm`char", ## 계좌명@@
                "Isuno": "Isuno`char", ## 종목번호@@
                "Isunm": "Isunm`char", ## 종목명@@
                "ordno": "ordno`long", ## 주문번호@@
                "orgordno": "orgordno`long", ## 원주문번호@@
                "execno": "execno`long", ## 체결번호@@
                "ordqty": "ordqty`long", ## 주문수량@@
                "ordprc": "ordprc`long", ## 주문가격@@
                "execqty": "execqty`long", ## 체결수량@@
                "execprc": "execprc`long", ## 체결가격@@
                "mdfycnfqty": "mdfycnfqty`long", ## 정정확인수량@@
                "mdfycnfprc": "mdfycnfprc`long", ## 정정확인가격@@
                "canccnfqty": "canccnfqty`long", ## 취소확인수량@@
                "rjtqty": "rjtqty`long", ## 거부수량@@
                "ordtrxptncode": "ordtrxptncode`long", ## 주문처리유형코드@@
                "mtiordseqno": "mtiordseqno`long", ## 복수주문일련번호@@
                "ordcndi": "ordcndi`char", ## 주문조건@@
                "ordprcptncode": "ordprcptncode`char", ## 호가유형코드@@
                "nsavtrdqty": "nsavtrdqty`long", ## 비저축체결수량@@
                "shtnIsuno": "shtnIsuno`char", ## 단축종목번호@@
                "opdrtnno": "opdrtnno`char", ## 운용지시번호@@
                "cvrgordtp": "cvrgordtp`char", ## 반대매매주문구분@@
                "unercqty": "unercqty`long", ## 미체결수량(주문)@@
                "orgordunercqty": "orgordunercqty`long", ## 원주문미체결수량@@
                "orgordmdfyqty": "orgordmdfyqty`long", ## 원주문정정수량@@
                "orgordcancqty": "orgordcancqty`long", ## 원주문취소수량@@
                "ordavrexecprc": "ordavrexecprc`long", ## 주문평균체결가격@@
                "ordamt": "ordamt`long", ## 주문금액@@
                "stdIsuno": "stdIsuno`char", ## 표준종목번호@@
                "bfstdIsuno": "bfstdIsuno`char", ## 전표준종목번호@@
                "bnstp": "bnstp`char", ## 매매구분@@
                "ordtrdptncode": "ordtrdptncode`char", ## 주문거래유형코드@@
                "mgntrncode": "mgntrncode`char", ## 신용거래코드@@
                "adduptp": "adduptp`char", ## 수수료합산코드@@
                "commdacode": "commdacode`char", ## 통신매체코드@@
                "Loandt": "Loandt`char", ## 대출일@@
                "mbrnmbrno": "mbrnmbrno`long", ## 회원/비회원사번호@@
                "ordacntno": "ordacntno`char", ## 주문계좌번호@@
                "agrgbrnno": "agrgbrnno`char", ## 집계지점번호@@
                "mgempno": "mgempno`char", ## 관리사원번호@@
                "futsLnkbrnno": "futsLnkbrnno`char", ## 선물연계지점번호@@
                "futsLnkacntno": "futsLnkacntno`char", ## 선물연계계좌번호@@
                "futsmkttp": "futsmkttp`char", ## 선물시장구분@@
                "regmktcode": "regmktcode`char", ## 등록시장코드@@
                "mnymgnrat": "mnymgnrat`long", ## 현금증거금률@@
                "substmgnrat": "substmgnrat`long", ## 대용증거금률@@
                "mnyexecamt": "mnyexecamt`long", ## 현금체결금액@@
                "ubstexecamt": "ubstexecamt`long", ## 대용체결금액@@
                "cmsnamtexecamt": "cmsnamtexecamt`long", ## 수수료체결금액@@
                "crdtpldgexecamt": "crdtpldgexecamt`long", ## 신용담보체결금액@@
                "crdtexecamt": "crdtexecamt`long", ## 신용체결금액@@
                "prdayruseexecval": "prdayruseexecval`long", ## 전일재사용체결금액@@
                "crdayruseexecval": "crdayruseexecval`long", ## 금일재사용체결금액@@
                "spotexecqty": "spotexecqty`long", ## 실물체결수량@@
                "stslexecqty": "stslexecqty`long", ## 공매도체결수량@@
                "strtgcode": "strtgcode`char", ## 전략코드@@
                "grpId": "grpId`char", ## 그룹Id@@
                "ordseqno": "ordseqno`long", ## 주문회차@@
                "ptflno": "ptflno`long", ## 포트폴리오번호@@
                "bskno": "bskno`long", ## 바스켓번호@@
                "trchno": "trchno`long", ## 트렌치번호@@
                "itemno": "itemno`long", ## 아이템번호@@
                "orduserId": "orduserId`char", ## 주문자Id@@
                "brwmgmtYn": "brwmgmtYn`long", ## 차입관리여부@@
                "frgrunqno": "frgrunqno`char", ## 외국인고유번호@@
                "trtzxLevytp": "trtzxLevytp`char", ## 거래세징수구분@@
                "lptp": "lptp`char", ## 유동성공급자구분@@
                "exectime": "exectime`char", ## 체결시각@@
                "rcptexectime": "rcptexectime`char", ## 거래소수신체결시각@@
                "rmndLoanamt": "rmndLoanamt`long", ## 잔여대출금액@@
                "secbalqty": "secbalqty`long", ## 잔고수량@@
                "spotordableqty": "spotordableqty`long", ## 실물가능수량@@
                "ordableruseqty": "ordableruseqty`long", ## 재사용가능수량(매도)@@
                "flctqty": "flctqty`long", ## 변동수량@@
                "secbalqtyd2": "secbalqtyd2`long", ## 잔고수량(d2)@@
                "sellableqty": "sellableqty`long", ## 매도주문가능수량@@
                "unercsellordqty": "unercsellordqty`long", ## 미체결매도주문수량@@
                "avrpchsprc": "avrpchsprc`long", ## 평균매입가@@
                "pchsant": "pchsant`long", ## 매입금액@@
                "deposit": "deposit`long", ## 예수금@@
                "substamt": "substamt`long", ## 대용금@@
                "csgnmnymgn": "csgnmnymgn`long", ## 위탁증거금현금@@
                "csgnsubstmgn": "csgnsubstmgn`long", ## 위탁증거금대용@@
                "crdtpldgruseamt": "crdtpldgruseamt`long", ## 신용담보재사용금@@
                "ordablemny": "ordablemny`long", ## 주문가능현금@@
                "ordablesubstamt": "ordablesubstamt`long", ## 주문가능대용@@
                "ruseableamt": "ruseableamt`long##재사용가능금액@@"
            }
        }
    },
    "SC4": { ## 주식주문거부
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
                "ordxctptncode": "ordxctptncode`char", ## 주문체결유형코드@@
                "ordmktcode": "ordmktcode`char", ## 주문시장코드@@
                "ordptncode": "ordptncode`char", ## 주문유형코드@@
                "mgmtbrnno": "mgmtbrnno`char", ## 관리지점번호@@
                "accno1": "accno1`char", ## 계좌번호@@
                "accno2": "accno2`char", ## 계좌번호@@
                "acntnm": "acntnm`char", ## 계좌명@@
                "Isuno": "Isuno`char", ## 종목번호@@
                "Isunm": "Isunm`char", ## 종목명@@
                "ordno": "ordno`long", ## 주문번호@@
                "orgordno": "orgordno`long", ## 원주문번호@@
                "execno": "execno`long", ## 체결번호@@
                "ordqty": "ordqty`long", ## 주문수량@@
                "ordprc": "ordprc`long", ## 주문가격@@
                "execqty": "execqty`long", ## 체결수량@@
                "execprc": "execprc`long", ## 체결가격@@
                "mdfycnfqty": "mdfycnfqty`long", ## 정정확인수량@@
                "mdfycnfprc": "mdfycnfprc`long", ## 정정확인가격@@
                "canccnfqty": "canccnfqty`long", ## 취소확인수량@@
                "rjtqty": "rjtqty`long", ## 거부수량@@
                "ordtrxptncode": "ordtrxptncode`long", ## 주문처리유형코드@@
                "mtiordseqno": "mtiordseqno`long", ## 복수주문일련번호@@
                "ordcndi": "ordcndi`char", ## 주문조건@@
                "ordprcptncode": "ordprcptncode`char", ## 호가유형코드@@
                "nsavtrdqty": "nsavtrdqty`long", ## 비저축체결수량@@
                "shtnIsuno": "shtnIsuno`char", ## 단축종목번호@@
                "opdrtnno": "opdrtnno`char", ## 운용지시번호@@
                "cvrgordtp": "cvrgordtp`char", ## 반대매매주문구분@@
                "unercqty": "unercqty`long", ## 미체결수량(주문)@@
                "orgordunercqty": "orgordunercqty`long", ## 원주문미체결수량@@
                "orgordmdfyqty": "orgordmdfyqty`long", ## 원주문정정수량@@
                "orgordcancqty": "orgordcancqty`long", ## 원주문취소수량@@
                "ordavrexecprc": "ordavrexecprc`long", ## 주문평균체결가격@@
                "ordamt": "ordamt`long", ## 주문금액@@
                "stdIsuno": "stdIsuno`char", ## 표준종목번호@@
                "bfstdIsuno": "bfstdIsuno`char", ## 전표준종목번호@@
                "bnstp": "bnstp`char", ## 매매구분@@
                "ordtrdptncode": "ordtrdptncode`char", ## 주문거래유형코드@@
                "mgntrncode": "mgntrncode`char", ## 신용거래코드@@
                "adduptp": "adduptp`char", ## 수수료합산코드@@
                "commdacode": "commdacode`char", ## 통신매체코드@@
                "Loandt": "Loandt`char", ## 대출일@@
                "mbrnmbrno": "mbrnmbrno`long", ## 회원/비회원사번호@@
                "ordacntno": "ordacntno`char", ## 주문계좌번호@@
                "agrgbrnno": "agrgbrnno`char", ## 집계지점번호@@
                "mgempno": "mgempno`char", ## 관리사원번호@@
                "futsLnkbrnno": "futsLnkbrnno`char", ## 선물연계지점번호@@
                "futsLnkacntno": "futsLnkacntno`char", ## 선물연계계좌번호@@
                "futsmkttp": "futsmkttp`char", ## 선물시장구분@@
                "regmktcode": "regmktcode`char", ## 등록시장코드@@
                "mnymgnrat": "mnymgnrat`long", ## 현금증거금률@@
                "substmgnrat": "substmgnrat`long", ## 대용증거금률@@
                "mnyexecamt": "mnyexecamt`long", ## 현금체결금액@@
                "ubstexecamt": "ubstexecamt`long", ## 대용체결금액@@
                "cmsnamtexecamt": "cmsnamtexecamt`long", ## 수수료체결금액@@
                "crdtpldgexecamt": "crdtpldgexecamt`long", ## 신용담보체결금액@@
                "crdtexecamt": "crdtexecamt`long", ## 신용체결금액@@
                "prdayruseexecval": "prdayruseexecval`long", ## 전일재사용체결금액@@
                "crdayruseexecval": "crdayruseexecval`long", ## 금일재사용체결금액@@
                "spotexecqty": "spotexecqty`long", ## 실물체결수량@@
                "stslexecqty": "stslexecqty`long", ## 공매도체결수량@@
                "strtgcode": "strtgcode`char", ## 전략코드@@
                "grpId": "grpId`char", ## 그룹Id@@
                "ordseqno": "ordseqno`long", ## 주문회차@@
                "ptflno": "ptflno`long", ## 포트폴리오번호@@
                "bskno": "bskno`long", ## 바스켓번호@@
                "trchno": "trchno`long", ## 트렌치번호@@
                "itemno": "itemno`long", ## 아이템번호@@
                "orduserId": "orduserId`char", ## 주문자Id@@
                "brwmgmtYn": "brwmgmtYn`long", ## 차입관리여부@@
                "frgrunqno": "frgrunqno`char", ## 외국인고유번호@@
                "trtzxLevytp": "trtzxLevytp`char", ## 거래세징수구분@@
                "lptp": "lptp`char", ## 유동성공급자구분@@
                "exectime": "exectime`char", ## 체결시각@@
                "rcptexectime": "rcptexectime`char", ## 거래소수신체결시각@@
                "rmndLoanamt": "rmndLoanamt`long", ## 잔여대출금액@@
                "secbalqty": "secbalqty`long", ## 잔고수량@@
                "spotordableqty": "spotordableqty`long", ## 실물가능수량@@
                "ordableruseqty": "ordableruseqty`long", ## 재사용가능수량(매도)@@
                "flctqty": "flctqty`long", ## 변동수량@@
                "secbalqtyd2": "secbalqtyd2`long", ## 잔고수량(d2)@@
                "sellableqty": "sellableqty`long", ## 매도주문가능수량@@
                "unercsellordqty": "unercsellordqty`long", ## 미체결매도주문수량@@
                "avrpchsprc": "avrpchsprc`long", ## 평균매입가@@
                "pchsant": "pchsant`long", ## 매입금액@@
                "deposit": "deposit`long", ## 예수금@@
                "substamt": "substamt`long", ## 대용금@@
                "csgnmnymgn": "csgnmnymgn`long", ## 위탁증거금현금@@
                "csgnsubstmgn": "csgnsubstmgn`long", ## 위탁증거금대용@@
                "crdtpldgruseamt": "crdtpldgruseamt`long", ## 신용담보재사용금@@
                "ordablemny": "ordablemny`long", ## 주문가능현금@@
                "ordablesubstamt": "ordablesubstamt`long", ## 주문가능대용@@
                "ruseableamt": "ruseableamt`long##재사용가능금액@@"
            }
        }
    },
    "SHC": { ## 상/하한가근접진입(SHC)
        "input": {
            "InBlock": {
                "updnlmtgubun": " ##상/하한구분@@"
            }
        },
        "output": {
            "OutBlock": {
                "sijanggubun": "sijanggubun`char", ## 거래소/코스닥구분@@
                "hname": "hname`char", ## 종목명@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "drate": "drate`float", ## 등락율@@
                "volume": "volume`long", ## 누적거래량@@
                "volincrate": "volincrate`float", ## 거래증가율@@
                "updnlmtprice": "updnlmtprice`long", ## 상/하한가@@
                "updnlmtdrate": "updnlmtdrate`float", ## 상/하한가대비율@@
                "jnilvolume": "jnilvolume`long", ## 전일거래량@@
                "shcode": "shcode`char", ## 단축코드@@
                "gwangubun": "gwangubun`char", ## 관리구분@@
                "undergubun": "undergubun`char", ## 이상급등구분@@
                "tgubun": "tgubun`char", ## 투자유의구분@@
                "wgubun": "wgubun`char", ## 우선주구분@@
                "dishonest": "dishonest`char", ## 불성실구분@@
                "jkrate": "jkrate`char", ## 증거금률@@
                "updnlmtdaycnt": "updnlmtdaycnt`long##상한가/하한가연속일수@@"
            }
        }
    },
    "SHD": { ## 상/하한가근접이탈(SHD)
        "input": {
            "InBlock": {
                "updnlmtgubun": " ##상/하한구분@@"
            }
        },
        "output": {
            "OutBlock": {
                "sijanggubun": "sijanggubun`char", ## 거래소/코스닥구분@@
                "hname": "hname`char", ## 종목명@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "drate": "drate`float", ## 등락율@@
                "volume": "volume`long", ## 누적거래량@@
                "volincrate": "volincrate`float", ## 거래증가율@@
                "updnlmtprice": "updnlmtprice`long", ## 상/하한가@@
                "updnlmtdrate": "updnlmtdrate`float", ## 상/하한가대비율@@
                "jnilvolume": "jnilvolume`long", ## 전일거래량@@
                "shcode": "shcode`char", ## 단축코드@@
                "gwangubun": "gwangubun`char", ## 관리구분@@
                "undergubun": "undergubun`char", ## 이상급등구분@@
                "tgubun": "tgubun`char", ## 투자유의구분@@
                "wgubun": "wgubun`char", ## 우선주구분@@
                "dishonest": "dishonest`char", ## 불성실구분@@
                "jkrate": "jkrate`char##증거금률@@"
            }
        }
    },
    "SHI": { ## 상/하한가진입(SHI)
        "input": {
            "InBlock": {
                "updnlmtgubun": " ##상/하한구분@@"
            }
        },
        "output": {
            "OutBlock": {
                "sijanggubun": "sijanggubun`char", ## 거래소/코스닥구분@@
                "hname": "hname`char", ## 종목명@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "drate": "drate`float", ## 등락율@@
                "volume": "volume`long", ## 누적거래량@@
                "volincrate": "volincrate`float", ## 거래증가율@@
                "totofferrem": "totofferrem`long", ## 매도호가총수량@@
                "totbidrem": "totbidrem`long", ## 매수호가총수량@@
                "updnlmtstime": "updnlmtstime`char", ## 상한가/하한가최종진입시간@@
                "updnlmtdaycnt": "updnlmtdaycnt`long", ## 상한가/하한가연속일수@@
                "jnilvolume": "jnilvolume`long", ## 전일거래량@@
                "shcode": "shcode`char", ## 단축코드@@
                "gwangubun": "gwangubun`char", ## 관리구분@@
                "undergubun": "undergubun`char", ## 이상급등구분@@
                "tgubun": "tgubun`char", ## 투자유의구분@@
                "wgubun": "wgubun`char", ## 우선주구분@@
                "dishonest": "dishonest`char", ## 불성실구분@@
                "jkrate": "jkrate`char##증거금률@@"
            }
        }
    },
    "SHO": { ## 상/하한가이탈(SHO)
        "input": {
            "InBlock": {
                "updnlmtgubun": " ##상/하한구분@@"
            }
        },
        "output": {
            "OutBlock": {
                "sijanggubun": "sijanggubun`char", ## 거래소/코스닥구분@@
                "hname": "hname`char", ## 종목명@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "drate": "drate`float", ## 등락율@@
                "volume": "volume`long", ## 누적거래량@@
                "volincrate": "volincrate`float", ## 거래증가율@@
                "updnlmtprice": "updnlmtprice`long", ## 상/하한가@@
                "updnlmtchange": "updnlmtchange`long", ## 상/하한가대비@@
                "updnlmtdrate": "updnlmtdrate`float", ## 상/하한가대비율@@
                "jnilvolume": "jnilvolume`long", ## 전일거래량@@
                "shcode": "shcode`char", ## 단축코드@@
                "gwangubun": "gwangubun`char", ## 관리구분@@
                "undergubun": "undergubun`char", ## 이상급등구분@@
                "tgubun": "tgubun`char", ## 투자유의구분@@
                "wgubun": "wgubun`char", ## 우선주구분@@
                "dishonest": "dishonest`char", ## 불성실구분@@
                "jkrate": "jkrate`char##증거금률@@"
            }
        }
    },
    "t0150": { ## 주식당일매매일지/수수료(t0150)
        "input": {
            "t0150InBlock": {
                "accno": " ", ## 계좌번호@@
                "cts_medosu": " ", ## CTS_매매구분@@
                "cts_expcode": " ", ## CTS_종목번호@@
                "cts_price": " ", ## CTS_단가@@
                "cts_middiv": " ##CTS_매체@@"
            }
        },
        "output": {
            "t0150OutBlock": {
                "mdqty": "mdqty`long", ## 매도수량@@
                "mdamt": "mdamt`long", ## 매도약정금액@@
                "mdfee": "mdfee`long", ## 매도수수료@@
                "mdtax": "mdtax`long", ## 매도거래세@@
                "mdargtax": "mdargtax`long", ## 매도농특세@@
                "tmdtax": "tmdtax`long", ## 매도제비용합@@
                "mdadjamt": "mdadjamt`long", ## 매도정산금액@@
                "msqty": "msqty`long", ## 매수수량@@
                "msamt": "msamt`long", ## 매수약정금액@@
                "msfee": "msfee`long", ## 매수수수료@@
                "tmstax": "tmstax`long", ## 매수제비용합@@
                "msadjamt": "msadjamt`long", ## 매수정산금액@@
                "tqty": "tqty`long", ## 합계수량@@
                "tamt": "tamt`long", ## 합계약정금액@@
                "tfee": "tfee`long", ## 합계수수료@@
                "tottax": "tottax`long", ## 합계거래세@@
                "targtax": "targtax`long", ## 합계농특세@@
                "ttax": "ttax`long", ## 합계제비용합@@
                "tadjamt": "tadjamt`long", ## 합계정산금액@@
                "cts_medosu": "cts_medosu`char", ## CTS_매매구분@@
                "cts_expcode": "cts_expcode`char", ## CTS_종목번호@@
                "cts_price": "cts_price`char", ## CTS_단가@@
                "cts_middiv": "cts_middiv`char##CTS_매체@@"
            },
            "t0150OutBlock1": {
                "medosu": "medosu`char", ## 매매구분@@
                "expcode": "expcode`char", ## 종목번호@@
                "qty": "qty`long", ## 수량@@
                "price": "price`long", ## 단가@@
                "amt": "amt`long", ## 약정금액@@
                "fee": "fee`long", ## 수수료@@
                "tax": "tax`long", ## 거래세@@
                "argtax": "argtax`long", ## 농특세@@
                "adjamt": "adjamt`long", ## 정산금액@@
                "middiv": "middiv`char##매체@@"
            }
        }
    },
    "t0151": { ## 주식당일매매일지/수수료(전일)(t0151)
        "input": {
            "t0151InBlock": {
                "date": " ", ## 일자@@
                "accno": " ", ## 계좌번호@@
                "cts_medosu": " ", ## CTS_매매구분@@
                "cts_expcode": " ", ## CTS_종목번호@@
                "cts_price": " ", ## CTS_단가@@
                "cts_middiv": " ##CTS_매체@@"
            }
        },
        "output": {
            "t0151OutBlock": {
                "mdqty": "mdqty`long", ## 매도수량@@
                "mdamt": "mdamt`long", ## 매도약정금액@@
                "mdfee": "mdfee`long", ## 매도수수료@@
                "mdtax": "mdtax`long", ## 매도거래세@@
                "mdargtax": "mdargtax`long", ## 매도농특세@@
                "tmdtax": "tmdtax`long", ## 매도제비용합@@
                "mdadjamt": "mdadjamt`long", ## 매도정산금액@@
                "msqty": "msqty`long", ## 매수수량@@
                "msamt": "msamt`long", ## 매수약정금액@@
                "msfee": "msfee`long", ## 매수수수료@@
                "tmstax": "tmstax`long", ## 매수제비용합@@
                "msadjamt": "msadjamt`long", ## 매수정산금액@@
                "tqty": "tqty`long", ## 합계수량@@
                "tamt": "tamt`long", ## 합계약정금액@@
                "tfee": "tfee`long", ## 합계수수료@@
                "tottax": "tottax`long", ## 합계거래세@@
                "targtax": "targtax`long", ## 합계농특세@@
                "ttax": "ttax`long", ## 합계제비용합@@
                "tadjamt": "tadjamt`long", ## 합계정산금액@@
                "cts_medosu": "cts_medosu`char", ## CTS_매매구분@@
                "cts_expcode": "cts_expcode`char", ## CTS_종목번호@@
                "cts_price": "cts_price`char", ## CTS_단가@@
                "cts_middiv": "cts_middiv`char##CTS_매체@@"
            },
            "t0151OutBlock1": {
                "medosu": "medosu`char", ## 매매구분@@
                "expcode": "expcode`char", ## 종목번호@@
                "qty": "qty`long", ## 수량@@
                "price": "price`long", ## 단가@@
                "amt": "amt`long", ## 약정금액@@
                "fee": "fee`long", ## 수수료@@
                "tax": "tax`long", ## 거래세@@
                "argtax": "argtax`long", ## 농특세@@
                "adjamt": "adjamt`long", ## 정산금액@@
                "middiv": "middiv`char##매체@@"
            }
        }
    },
    "t0167": { ## 서버시간조회(t0167)
        "input": {
            "t0167InBlock": {
                "id": " ##id@@"
            }
        },
        "output": {
            "t0167OutBlock": {
                "dt": "dt`char", ## 일자(YYYYMMDD)@@
                "time": "time`char##시간(HHMMSSssssss)@@"
            }
        }
    },
    "t0424": { ## 주식잔고2(t0424)
        "input": {
            "t0424InBlock": {
                "accno": " ", ## 계좌번호@@
                "passwd": " ", ## 비밀번호@@
                "prcgb": " ", ## 단가구분@@
                "chegb": " ", ## 체결구분@@
                "dangb": " ", ## 단일가구분@@
                "charge": " ", ## 제비용포함여부@@
                "cts_expcode": " ##CTS_종목번호@@"
            }
        },
        "output": {
            "t0424OutBlock": {
                "sunamt": "sunamt`long", ## 추정순자산@@
                "dtsunik": "dtsunik`long", ## 실현손익@@
                "mamt": "mamt`long", ## 매입금액@@
                "sunamt1": "sunamt1`long", ## 추정D2예수금@@
                "cts_expcode": "cts_expcode`char", ## CTS_종목번호@@
                "tappamt": "tappamt`long", ## 평가금액@@
                "tdtsunik": "tdtsunik`long##평가손익@@"
            },
            "t0424OutBlock1": {
                "expcode": "expcode`char", ## 종목번호@@
                "jangb": "jangb`char", ## 잔고구분@@
                "janqty": "janqty`long", ## 잔고수량@@
                "mdposqt": "mdposqt`long", ## 매도가능수량@@
                "pamt": "pamt`long", ## 평균단가@@
                "mamt": "mamt`long", ## 매입금액@@
                "sinamt": "sinamt`long", ## 대출금액@@
                "lastdt": "lastdt`char", ## 만기일자@@
                "msat": "msat`long", ## 당일매수금액@@
                "mpms": "mpms`long", ## 당일매수단가@@
                "mdat": "mdat`long", ## 당일매도금액@@
                "mpmd": "mpmd`long", ## 당일매도단가@@
                "jsat": "jsat`long", ## 전일매수금액@@
                "jpms": "jpms`long", ## 전일매수단가@@
                "jdat": "jdat`long", ## 전일매도금액@@
                "jpmd": "jpmd`long", ## 전일매도단가@@
                "sysprocseq": "sysprocseq`long", ## 처리순번@@
                "loandt": "loandt`char", ## 대출일자@@
                "hname": "hname`char", ## 종목명@@
                "marketgb": "marketgb`char", ## 시장구분@@
                "jonggb": "jonggb`char", ## 종목구분@@
                "janrt": "janrt`float", ## 보유비중@@
                "price": "price`long", ## 현재가@@
                "appamt": "appamt`long", ## 평가금액@@
                "dtsunik": "dtsunik`long", ## 평가손익@@
                "sunikrt": "sunikrt`float", ## 수익율@@
                "fee": "fee`long", ## 수수료@@
                "tax": "tax`long", ## 제세금@@
                "sininter": "sininter`long##신용이자@@"
            }
        }
    },
    "t0425": { ## 주식체결/미체결(t0425)
        "input": {
            "t0425InBlock": {
                "accno": " ", ## 계좌번호@@
                "passwd": " ", ## 비밀번호@@
                "expcode": " ", ## 종목번호@@
                "chegb": " ", ## 체결구분@@
                "medosu": " ", ## 매매구분@@
                "sortgb": " ", ## 정렬순서@@
                "cts_ordno": " ##주문번호@@"
            }
        },
        "output": {
            "t0425OutBlock": {
                "tqty": "tqty`long", ## 총주문수량@@
                "tcheqty": "tcheqty`long", ## 총체결수량@@
                "tordrem": "tordrem`long", ## 총미체결수량@@
                "cmss": "cmss`long", ## 추정수수료@@
                "tamt": "tamt`long", ## 총주문금액@@
                "tmdamt": "tmdamt`long", ## 총매도체결금액@@
                "tmsamt": "tmsamt`long", ## 총매수체결금액@@
                "tax": "tax`long", ## 추정제세금@@
                "cts_ordno": "cts_ordno`char##주문번호@@"
            },
            "t0425OutBlock1": {
                "ordno": "ordno`long", ## 주문번호@@
                "expcode": "expcode`char", ## 종목번호@@
                "medosu": "medosu`char", ## 구분@@
                "qty": "qty`long", ## 주문수량@@
                "price": "price`long", ## 주문가격@@
                "cheqty": "cheqty`long", ## 체결수량@@
                "cheprice": "cheprice`long", ## 체결가격@@
                "ordrem": "ordrem`long", ## 미체결잔량@@
                "cfmqty": "cfmqty`long", ## 확인수량@@
                "status": "status`char", ## 상태@@
                "orgordno": "orgordno`long", ## 원주문번호@@
                "ordgb": "ordgb`char", ## 유형@@
                "ordtime": "ordtime`char", ## 주문시간@@
                "ordermtd": "ordermtd`char", ## 주문매체@@
                "sysprocseq": "sysprocseq`long", ## 처리순번@@
                "hogagb": "hogagb`char", ## 호가유형@@
                "price1": "price1`long", ## 현재가@@
                "orggb": "orggb`char", ## 주문구분@@
                "singb": "singb`char", ## 신용구분@@
                "loandt": "loandt`char##대출일자@@"
            }
        }
    },
    "t0434": { ## 선물/옵션체결/미체결(t0434)
        "input": {
            "t0434InBlock": {
                "accno": " ", ## 계좌번호@@
                "passwd": " ", ## 비밀번호@@
                "expcode": " ", ## 종목번호@@
                "chegb": " ", ## 체결구분@@
                "sortgb": " ", ## 정렬순서@@
                "cts_ordno": " ##CTS_주문번호@@"
            }
        },
        "output": {
            "t0434OutBlock": {
                "cts_ordno": "cts_ordno`char##CTS_주문번호@@"
            },
            "t0434OutBlock1": {
                "ordno": "ordno`long", ## 주문번호@@
                "orgordno": "orgordno`long", ## 원주문번호@@
                "medosu": "medosu`char", ## 구분@@
                "ordgb": "ordgb`char", ## 유형@@
                "qty": "qty`long", ## 주문수량@@
                "price": "price`float", ## 주문가격@@
                "cheqty": "cheqty`long", ## 체결수량@@
                "cheprice": "cheprice`float", ## 체결가격@@
                "ordrem": "ordrem`long", ## 미체결잔량@@
                "status": "status`char", ## 상태@@
                "ordtime": "ordtime`char", ## 주문시간@@
                "ordermtd": "ordermtd`char", ## 주문매체@@
                "expcode": "expcode`char", ## 종목번호@@
                "rtcode": "rtcode`char", ## 사유코드@@
                "sysprocseq": "sysprocseq`long", ## 처리순번@@
                "hogatype": "hogatype`char##호가타입@@"
            }
        }
    },
    "t0441": { ## 선물/옵션잔고평가(이동평균)(t0441)
        "input": {
            "t0441InBlock": {
                "accno": " ", ## 계좌번호@@
                "passwd": " ", ## 비밀번호@@
                "cts_expcode": " ", ## CTS_종목번호@@
                "cts_medocd": " ##CTS_매매구분@@"
            }
        },
        "output": {
            "t0441OutBlock": {
                "tdtsunik": "tdtsunik`long", ## 매매손익합계@@
                "cts_expcode": "cts_expcode`char", ## CTS_종목번호@@
                "cts_medocd": "cts_medocd`char", ## CTS_매매구분@@
                "tappamt": "tappamt`long", ## 평가금액@@
                "tsunik": "tsunik`long##평가손익@@"
            },
            "t0441OutBlock1": {
                "expcode": "expcode`char", ## 종목번호@@
                "medosu": "medosu`char", ## 구분@@
                "jqty": "jqty`long", ## 잔고수량@@
                "cqty": "cqty`long", ## 청산가능수량@@
                "pamt": "pamt`float", ## 평균단가@@
                "mamt": "mamt`long", ## 총매입금액@@
                "medocd": "medocd`char", ## 매매구분@@
                "dtsunik": "dtsunik`long", ## 매매손익@@
                "sysprocseq": "sysprocseq`long", ## 처리순번@@
                "price": "price`float", ## 현재가@@
                "appamt": "appamt`long", ## 평가금액@@
                "dtsunik1": "dtsunik1`long", ## 평가손익@@
                "sunikrt": "sunikrt`float##수익율@@"
            }
        }
    },
    "t1101": { ## 주식현재가호가조회(t1101)
        "input": {
            "t1101InBlock": {
                "shcode": " ##단축코드@@"
            }
        },
        "output": {
            "t1101OutBlock": {
                "hname": "hname`char", ## 한글명@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 누적거래량@@
                "jnilclose": "jnilclose`long", ## 전일종가@@
                "offerho1": "offerho1`long", ## 매도호가1@@
                "bidho1": "bidho1`long", ## 매수호가1@@
                "offerrem1": "offerrem1`long", ## 매도호가수량1@@
                "bidrem1": "bidrem1`long", ## 매수호가수량1@@
                "preoffercha1": "preoffercha1`long", ## 직전매도대비수량1@@
                "prebidcha1": "prebidcha1`long", ## 직전매수대비수량1@@
                "offerho2": "offerho2`long", ## 매도호가2@@
                "bidho2": "bidho2`long", ## 매수호가2@@
                "offerrem2": "offerrem2`long", ## 매도호가수량2@@
                "bidrem2": "bidrem2`long", ## 매수호가수량2@@
                "preoffercha2": "preoffercha2`long", ## 직전매도대비수량2@@
                "prebidcha2": "prebidcha2`long", ## 직전매수대비수량2@@
                "offerho3": "offerho3`long", ## 매도호가3@@
                "bidho3": "bidho3`long", ## 매수호가3@@
                "offerrem3": "offerrem3`long", ## 매도호가수량3@@
                "bidrem3": "bidrem3`long", ## 매수호가수량3@@
                "preoffercha3": "preoffercha3`long", ## 직전매도대비수량3@@
                "prebidcha3": "prebidcha3`long", ## 직전매수대비수량3@@
                "offerho4": "offerho4`long", ## 매도호가4@@
                "bidho4": "bidho4`long", ## 매수호가4@@
                "offerrem4": "offerrem4`long", ## 매도호가수량4@@
                "bidrem4": "bidrem4`long", ## 매수호가수량4@@
                "preoffercha4": "preoffercha4`long", ## 직전매도대비수량4@@
                "prebidcha4": "prebidcha4`long", ## 직전매수대비수량4@@
                "offerho5": "offerho5`long", ## 매도호가5@@
                "bidho5": "bidho5`long", ## 매수호가5@@
                "offerrem5": "offerrem5`long", ## 매도호가수량5@@
                "bidrem5": "bidrem5`long", ## 매수호가수량5@@
                "preoffercha5": "preoffercha5`long", ## 직전매도대비수량5@@
                "prebidcha5": "prebidcha5`long", ## 직전매수대비수량5@@
                "offerho6": "offerho6`long", ## 매도호가6@@
                "bidho6": "bidho6`long", ## 매수호가6@@
                "offerrem6": "offerrem6`long", ## 매도호가수량6@@
                "bidrem6": "bidrem6`long", ## 매수호가수량6@@
                "preoffercha6": "preoffercha6`long", ## 직전매도대비수량6@@
                "prebidcha6": "prebidcha6`long", ## 직전매수대비수량6@@
                "offerho7": "offerho7`long", ## 매도호가7@@
                "bidho7": "bidho7`long", ## 매수호가7@@
                "offerrem7": "offerrem7`long", ## 매도호가수량7@@
                "bidrem7": "bidrem7`long", ## 매수호가수량7@@
                "preoffercha7": "preoffercha7`long", ## 직전매도대비수량7@@
                "prebidcha7": "prebidcha7`long", ## 직전매수대비수량7@@
                "offerho8": "offerho8`long", ## 매도호가8@@
                "bidho8": "bidho8`long", ## 매수호가8@@
                "offerrem8": "offerrem8`long", ## 매도호가수량8@@
                "bidrem8": "bidrem8`long", ## 매수호가수량8@@
                "preoffercha8": "preoffercha8`long", ## 직전매도대비수량8@@
                "prebidcha8": "prebidcha8`long", ## 직전매수대비수량8@@
                "offerho9": "offerho9`long", ## 매도호가9@@
                "bidho9": "bidho9`long", ## 매수호가9@@
                "offerrem9": "offerrem9`long", ## 매도호가수량9@@
                "bidrem9": "bidrem9`long", ## 매수호가수량9@@
                "preoffercha9": "preoffercha9`long", ## 직전매도대비수량9@@
                "prebidcha9": "prebidcha9`long", ## 직전매수대비수량9@@
                "offerho10": "offerho10`long", ## 매도호가10@@
                "bidho10": "bidho10`long", ## 매수호가10@@
                "offerrem10": "offerrem10`long", ## 매도호가수량10@@
                "bidrem10": "bidrem10`long", ## 매수호가수량10@@
                "preoffercha10": "preoffercha10`long", ## 직전매도대비수량10@@
                "prebidcha10": "prebidcha10`long", ## 직전매수대비수량10@@
                "offer": "offer`long", ## 매도호가수량합@@
                "bid": "bid`long", ## 매수호가수량합@@
                "preoffercha": "preoffercha`long", ## 직전매도대비수량합@@
                "prebidcha": "prebidcha`long", ## 직전매수대비수량합@@
                "hotime": "hotime`char", ## 수신시간@@
                "yeprice": "yeprice`long", ## 예상체결가격@@
                "yevolume": "yevolume`long", ## 예상체결수량@@
                "yesign": "yesign`char", ## 예상체결전일구분@@
                "yechange": "yechange`long", ## 예상체결전일대비@@
                "yediff": "yediff`float", ## 예상체결등락율@@
                "tmoffer": "tmoffer`long", ## 시간외매도잔량@@
                "tmbid": "tmbid`long", ## 시간외매수잔량@@
                "ho_status": "ho_status`char", ## 동시구분@@
                "shcode": "shcode`char", ## 단축코드@@
                "uplmtprice": "uplmtprice`long", ## 상한가@@
                "dnlmtprice": "dnlmtprice`long", ## 하한가@@
                "open": "open`long", ## 시가@@
                "high": "high`long", ## 고가@@
                "low": "low`long##저가@@"
            }
        }
    },
    "t1102": { ## 주식현재가(시세)조회(t1102)
        "input": {
            "t1102InBlock": {
                "shcode": " ##단축코드@@"
            }
        },
        "output": {
            "t1102OutBlock": {
                "hname": "hname`char", ## 한글명@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 누적거래량@@
                "recprice": "recprice`long", ## 기준가(평가가격)@@
                "avg": "avg`long", ## 가중평균@@
                "uplmtprice": "uplmtprice`long", ## 상한가(최고호가가격)@@
                "dnlmtprice": "dnlmtprice`long", ## 하한가(최저호가가격)@@
                "jnilvolume": "jnilvolume`long", ## 전일거래량@@
                "volumediff": "volumediff`long", ## 거래량차@@
                "open": "open`long", ## 시가@@
                "opentime": "opentime`char", ## 시가시간@@
                "high": "high`long", ## 고가@@
                "hightime": "hightime`char", ## 고가시간@@
                "low": "low`long", ## 저가@@
                "lowtime": "lowtime`char", ## 저가시간@@
                "high52w": "high52w`long", ## 52최고가@@
                "high52wdate": "high52wdate`char", ## 52최고가일@@
                "low52w": "low52w`long", ## 52최저가@@
                "low52wdate": "low52wdate`char", ## 52최저가일@@
                "exhratio": "exhratio`float", ## 소진율@@
                "per": "per`float", ## PER@@
                "pbrx": "pbrx`float", ## PBRX@@
                "listing": "listing`long", ## 상장주식수(천)@@
                "jkrate": "jkrate`long", ## 증거금율@@
                "memedan": "memedan`char", ## 수량단위@@
                "offernocd1": "offernocd1`char", ## 매도증권사코드1@@
                "bidnocd1": "bidnocd1`char", ## 매수증권사코드1@@
                "offerno1": "offerno1`char", ## 매도증권사명1@@
                "bidno1": "bidno1`char", ## 매수증권사명1@@
                "dvol1": "dvol1`long", ## 총매도수량1@@
                "svol1": "svol1`long", ## 총매수수량1@@
                "dcha1": "dcha1`long", ## 매도증감1@@
                "scha1": "scha1`long", ## 매수증감1@@
                "ddiff1": "ddiff1`float", ## 매도비율1@@
                "sdiff1": "sdiff1`float", ## 매수비율1@@
                "offernocd2": "offernocd2`char", ## 매도증권사코드2@@
                "bidnocd2": "bidnocd2`char", ## 매수증권사코드2@@
                "offerno2": "offerno2`char", ## 매도증권사명2@@
                "bidno2": "bidno2`char", ## 매수증권사명2@@
                "dvol2": "dvol2`long", ## 총매도수량2@@
                "svol2": "svol2`long", ## 총매수수량2@@
                "dcha2": "dcha2`long", ## 매도증감2@@
                "scha2": "scha2`long", ## 매수증감2@@
                "ddiff2": "ddiff2`float", ## 매도비율2@@
                "sdiff2": "sdiff2`float", ## 매수비율2@@
                "offernocd3": "offernocd3`char", ## 매도증권사코드3@@
                "bidnocd3": "bidnocd3`char", ## 매수증권사코드3@@
                "offerno3": "offerno3`char", ## 매도증권사명3@@
                "bidno3": "bidno3`char", ## 매수증권사명3@@
                "dvol3": "dvol3`long", ## 총매도수량3@@
                "svol3": "svol3`long", ## 총매수수량3@@
                "dcha3": "dcha3`long", ## 매도증감3@@
                "scha3": "scha3`long", ## 매수증감3@@
                "ddiff3": "ddiff3`float", ## 매도비율3@@
                "sdiff3": "sdiff3`float", ## 매수비율3@@
                "offernocd4": "offernocd4`char", ## 매도증권사코드4@@
                "bidnocd4": "bidnocd4`char", ## 매수증권사코드4@@
                "offerno4": "offerno4`char", ## 매도증권사명4@@
                "bidno4": "bidno4`char", ## 매수증권사명4@@
                "dvol4": "dvol4`long", ## 총매도수량4@@
                "svol4": "svol4`long", ## 총매수수량4@@
                "dcha4": "dcha4`long", ## 매도증감4@@
                "scha4": "scha4`long", ## 매수증감4@@
                "ddiff4": "ddiff4`float", ## 매도비율4@@
                "sdiff4": "sdiff4`float", ## 매수비율4@@
                "offernocd5": "offernocd5`char", ## 매도증권사코드5@@
                "bidnocd5": "bidnocd5`char", ## 매수증권사코드5@@
                "offerno5": "offerno5`char", ## 매도증권사명5@@
                "bidno5": "bidno5`char", ## 매수증권사명5@@
                "dvol5": "dvol5`long", ## 총매도수량5@@
                "svol5": "svol5`long", ## 총매수수량5@@
                "dcha5": "dcha5`long", ## 매도증감5@@
                "scha5": "scha5`long", ## 매수증감5@@
                "ddiff5": "ddiff5`float", ## 매도비율5@@
                "sdiff5": "sdiff5`float", ## 매수비율5@@
                "fwdvl": "fwdvl`long", ## 외국계매도합계수량@@
                "ftradmdcha": "ftradmdcha`long", ## 외국계매도직전대비@@
                "ftradmddiff": "ftradmddiff`float", ## 외국계매도비율@@
                "fwsvl": "fwsvl`long", ## 외국계매수합계수량@@
                "ftradmscha": "ftradmscha`long", ## 외국계매수직전대비@@
                "ftradmsdiff": "ftradmsdiff`float", ## 외국계매수비율@@
                "vol": "vol`float", ## 회전율@@
                "shcode": "shcode`char", ## 단축코드@@
                "value": "value`long", ## 누적거래대금@@
                "jvolume": "jvolume`long", ## 전일동시간거래량@@
                "highyear": "highyear`long", ## 연중최고가@@
                "highyeardate": "highyeardate`char", ## 연중최고일자@@
                "lowyear": "lowyear`long", ## 연중최저가@@
                "lowyeardate": "lowyeardate`char", ## 연중최저일자@@
                "target": "target`long", ## 목표가@@
                "capital": "capital`long", ## 자본금@@
                "abscnt": "abscnt`long", ## 유동주식수@@
                "parprice": "parprice`long", ## 액면가@@
                "gsmm": "gsmm`char", ## 결산월@@
                "subprice": "subprice`long", ## 대용가@@
                "total": "total`long", ## 시가총액@@
                "listdate": "listdate`char", ## 상장일@@
                "name": "name`char", ## 전분기명@@
                "bfsales": "bfsales`long", ## 전분기매출액@@
                "bfoperatingincome": "bfoperatingincome`long", ## 전분기영업이익@@
                "bfordinaryincome": "bfordinaryincome`long", ## 전분기경상이익@@
                "bfnetincome": "bfnetincome`long", ## 전분기순이익@@
                "bfeps": "bfeps`float", ## 전분기EPS@@
                "name2": "name2`char", ## 전전분기명@@
                "bfsales2": "bfsales2`long", ## 전전분기매출액@@
                "bfoperatingincome2": "bfoperatingincome2`long", ## 전전분기영업이익@@
                "bfordinaryincome2": "bfordinaryincome2`long", ## 전전분기경상이익@@
                "bfnetincome2": "bfnetincome2`long", ## 전전분기순이익@@
                "bfeps2": "bfeps2`float", ## 전전분기EPS@@
                "salert": "salert`float", ## 전년대비매출액@@
                "opert": "opert`float", ## 전년대비영업이익@@
                "ordrt": "ordrt`float", ## 전년대비경상이익@@
                "netrt": "netrt`float", ## 전년대비순이익@@
                "epsrt": "epsrt`float", ## 전년대비EPS@@
                "info1": "info1`char", ## 락구분@@
                "info2": "info2`char", ## 관리/급등구분@@
                "info3": "info3`char", ## 정지/연장구분@@
                "info4": "info4`char", ## 투자/불성실구분@@
                "janginfo": "janginfo`char", ## 장구분@@
                "t_per": "t_per`float", ## T.PER@@
                "tonghwa": "tonghwa`char", ## 통화ISO코드@@
                "dval1": "dval1`long", ## 총매도대금1@@
                "sval1": "sval1`long", ## 총매수대금1@@
                "dval2": "dval2`long", ## 총매도대금2@@
                "sval2": "sval2`long", ## 총매수대금2@@
                "dval3": "dval3`long", ## 총매도대금3@@
                "sval3": "sval3`long", ## 총매수대금3@@
                "dval4": "dval4`long", ## 총매도대금4@@
                "sval4": "sval4`long", ## 총매수대금4@@
                "dval5": "dval5`long", ## 총매도대금5@@
                "sval5": "sval5`long", ## 총매수대금5@@
                "davg1": "davg1`long", ## 총매도평단가1@@
                "savg1": "savg1`long", ## 총매수평단가1@@
                "davg2": "davg2`long", ## 총매도평단가2@@
                "savg2": "savg2`long", ## 총매수평단가2@@
                "davg3": "davg3`long", ## 총매도평단가3@@
                "savg3": "savg3`long", ## 총매수평단가3@@
                "davg4": "davg4`long", ## 총매도평단가4@@
                "savg4": "savg4`long", ## 총매수평단가4@@
                "davg5": "davg5`long", ## 총매도평단가5@@
                "savg5": "savg5`long", ## 총매수평단가5@@
                "ftradmdval": "ftradmdval`long", ## 외국계매도대금@@
                "ftradmsval": "ftradmsval`long", ## 외국계매수대금@@
                "ftradmdvag": "ftradmdvag`long", ## 외국계매도평단가@@
                "ftradmsvag": "ftradmsvag`long", ## 외국계매수평단가@@
                "info5": "info5`char", ## 투자주의환기@@
                "spac_gubun": "spac_gubun`char", ## 기업인수목적회사여부@@
                "issueprice": "issueprice`long", ## 발행가격@@
                "alloc_gubun": "alloc_gubun`char", ## 배분적용구분코드@@1:배분발생2:배분해제그외:미발생
                "alloc_text": "alloc_text`char", ## 배분적용구분@@
                "shterm_text": "shterm_text`char", ## 단기과열/VI발동@@
                "svi_uplmtprice": "svi_uplmtprice`long", ## 정적VI상한가@@
                "svi_dnlmtprice": "svi_dnlmtprice`long", ## 정적VI하한가@@
                "low_lqdt_gu": "low_lqdt_gu`char", ## 저유동성종목여부@@
                "abnormal_rise_gu": "abnormal_rise_gu`char", ## 이상급등종목여부@@
                "lend_text": "lend_text`char", ## 대차불가표시@@
                "ty_text": "ty_text`char##ETF/ETN투자유의@@"
            }
        }
    },
    "t1104": { ## 주식현재가시세메모(t1104)
        "input": {
            "t1104InBlock": {
                "code": " ", ## 종목코드@@
                "nrec": " ##건수@@"
            },
            "t1104InBlock1": {
                "indx": " ", ## 인덱스@@
                "gubn": " ", ## 조건구분@@
                "dat1": " ", ## 데이타1@@
                "dat2": " ##데이타2@@"
            }
        },
        "output": {
            "t1104OutBlock": {
                "nrec": "nrec`char##출력건수@@"
            },
            "t1104OutBlock1": {
                "indx": "indx`char", ## 인덱스@@
                "gubn": "gubn`char", ## 조건구분@@
                "vals": "vals`char##출력값@@"
            }
        }
    },
    "t1105": { ## 주식피못/디마크조회(t1105)
        "input": {
            "t1105InBlock": {
                "shcode": " ##단축코드@@"
            }
        },
        "output": {
            "t1105OutBlock": {
                "shcode": "shcode`char", ## 단축코드@@
                "pbot": "pbot`long", ## 피봇@@
                "offer1": "offer1`long", ## 1차저항@@
                "supp1": "supp1`long", ## 1차지지@@
                "offer2": "offer2`long", ## 2차저항@@
                "supp2": "supp2`long", ## 2차지지@@
                "stdprc": "stdprc`long", ## 기준가격@@
                "offerd": "offerd`long", ## D저항@@
                "suppd": "suppd`long##D지지@@"
            }
        }
    },
    "t1301": { ## 주식시간대별체결조회(t1301)
        "input": {
            "t1301InBlock": {
                "shcode": " ", ## 단축코드@@
                "cvolume": "0", ## 특이거래량@@
                "starttime": " ", ## 시작시간@@
                "endtime": " ", ## 종료시간@@
                "cts_time": " ##시간CTS@@"
            }
        },
        "output": {
            "t1301OutBlock": {
                "cts_time": "cts_time`char##시간CTS@@"
            },
            "t1301OutBlock1": {
                "chetime": "chetime`char", ## 시간@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "cvolume": "cvolume`long", ## 체결수량@@
                "chdegree": "chdegree`float", ## 체결강도@@
                "volume": "volume`long", ## 거래량@@
                "mdvolume": "mdvolume`long", ## 매도체결수량@@
                "mdchecnt": "mdchecnt`long", ## 매도체결건수@@
                "msvolume": "msvolume`long", ## 매수체결수량@@
                "mschecnt": "mschecnt`long", ## 매수체결건수@@
                "revolume": "revolume`long", ## 순체결량@@
                "rechecnt": "rechecnt`long##순체결건수@@"
            }
        }
    },
    "t1302": { ## 주식분별주가조회(t1302)
        "input": {
            "t1302InBlock": {
                "shcode": " ", ## 단축코드@@
                "gubun": " ", ## 작업구분@@
                "time": " ", ## 시간@@
                "cnt": "0##건수@@"
            }
        },
        "output": {
            "t1302OutBlock": {
                "cts_time": "cts_time`char##시간CTS@@"
            },
            "t1302OutBlock1": {
                "chetime": "chetime`char", ## 시간@@
                "close": "close`long", ## 종가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "chdegree": "chdegree`float", ## 체결강도@@
                "mdvolume": "mdvolume`long", ## 매도체결수량@@
                "msvolume": "msvolume`long", ## 매수체결수량@@
                "revolume": "revolume`long", ## 순매수체결량@@
                "mdchecnt": "mdchecnt`long", ## 매도체결건수@@
                "mschecnt": "mschecnt`long", ## 매수체결건수@@
                "rechecnt": "rechecnt`long", ## 순체결건수@@
                "volume": "volume`long", ## 거래량@@
                "open": "open`long", ## 시가@@
                "high": "high`long", ## 고가@@
                "low": "low`long", ## 저가@@
                "cvolume": "cvolume`long", ## 체결량@@
                "mdchecnttm": "mdchecnttm`long", ## 매도체결건수(시간)@@
                "mschecnttm": "mschecnttm`long", ## 매수체결건수(시간)@@
                "totofferrem": "totofferrem`long", ## 매도잔량@@
                "totbidrem": "totbidrem`long", ## 매수잔량@@
                "mdvolumetm": "mdvolumetm`long", ## 시간별매도체결량@@
                "msvolumetm": "msvolumetm`long##시간별매수체결량@@"
            }
        }
    },
    "t1305": { ## 기간별주가(t1305)
        "input": {
            "t1305InBlock": {
                "shcode": " ", ## 단축코드@@
                "dwmcode": "0", ## 일주월구분@@
                "date": " ", ## 날짜@@
                "idx": "0", ## IDX@@
                "cnt": "0##건수@@"
            }
        },
        "output": {
            "t1305OutBlock": {
                "cnt": "cnt`long", ## CNT@@
                "date": "date`char", ## 날짜@@
                "idx": "idx`long##IDX@@"
            },
            "t1305OutBlock1": {
                "date": "date`char", ## 날짜@@
                "open": "open`long", ## 시가@@
                "high": "high`long", ## 고가@@
                "low": "low`long", ## 저가@@
                "close": "close`long", ## 종가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 누적거래량@@
                "diff_vol": "diff_vol`float", ## 거래증가율@@
                "chdegree": "chdegree`float", ## 체결강도@@
                "sojinrate": "sojinrate`float", ## 소진율@@
                "changerate": "changerate`float", ## 회전율@@
                "fpvolume": "fpvolume`long", ## 외인순매수@@
                "covolume": "covolume`long", ## 기관순매수@@
                "shcode": "shcode`char", ## 종목코드@@
                "value": "value`long", ## 누적거래대금@@단위:백만
                "ppvolume": "ppvolume`long", ## 개인순매수@@
                "o_sign": "o_sign`char", ## 시가대비구분@@
                "o_change": "o_change`long", ## 시가대비@@
                "o_diff": "o_diff`float", ## 시가기준등락율@@
                "h_sign": "h_sign`char", ## 고가대비구분@@
                "h_change": "h_change`long", ## 고가대비@@
                "h_diff": "h_diff`float", ## 고가기준등락율@@
                "l_sign": "l_sign`char", ## 저가대비구분@@
                "l_change": "l_change`long", ## 저가대비@@
                "l_diff": "l_diff`float", ## 저가기준등락율@@
                "marketcap": "marketcap`long##시가총액@@단위:백만"
            }
        }
    },
    "t1308": { ## 주식시간대별체결조회챠트(t1308)
        "input": {
            "t1308InBlock": {
                "shcode": " ", ## 단축코드@@
                "starttime": " ", ## 시작시간@@
                "endtime": " ", ## 종료시간@@
                "bun_term": " ##분간격@@"
            }
        },
        "output": {
            "t1308OutBlock1": {
                "chetime": "chetime`char", ## 시간@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "cvolume": "cvolume`long", ## 체결수량@@
                "chdegvol": "chdegvol`float", ## 체결강도(거래량)@@
                "chdegcnt": "chdegcnt`float", ## 체결강도(건수)@@
                "volume": "volume`long", ## 거래량@@
                "mdvolume": "mdvolume`long", ## 매도체결수량@@
                "mdchecnt": "mdchecnt`long", ## 매도체결건수@@
                "msvolume": "msvolume`long", ## 매수체결수량@@
                "mschecnt": "mschecnt`long", ## 매수체결건수@@
                "open": "open`long", ## 시가@@
                "high": "high`long", ## 고가@@
                "low": "low`long##저가@@"
            }
        }
    },
    "t1310": { ## 주식당일전일분틱조회(t1310)
        "input": {
            "t1310InBlock": {
                "daygb": " ", ## 당일전일구분@@
                "timegb": " ", ## 분틱구분@@
                "shcode": " ", ## 단축코드@@
                "endtime": " ", ## 종료시간@@
                "cts_time": " ##시간CTS@@"
            }
        },
        "output": {
            "t1310OutBlock": {
                "cts_time": "cts_time`char##시간CTS@@"
            },
            "t1310OutBlock1": {
                "chetime": "chetime`char", ## 시간@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "cvolume": "cvolume`long", ## 체결수량@@
                "chdegree": "chdegree`float", ## 체결강도@@
                "volume": "volume`long", ## 거래량@@
                "mdvolume": "mdvolume`long", ## 매도체결수량@@
                "mdchecnt": "mdchecnt`long", ## 매도체결건수@@
                "msvolume": "msvolume`long", ## 매수체결수량@@
                "mschecnt": "mschecnt`long", ## 매수체결건수@@
                "revolume": "revolume`long", ## 순체결량@@
                "rechecnt": "rechecnt`long##순체결건수@@"
            }
        }
    },
    "t1403": { ## 신규상장종목조회(t1403)
        "input": {
            "t1403InBlock": {
                "gubun": " ", ## 구분@@
                "styymm": " ", ## 시작상장월@@
                "enyymm": " ", ## 종료상장월@@
                "idx": "0##IDX@@"
            }
        },
        "output": {
            "t1403OutBlock": {
                "idx": "idx`long##IDX@@"
            },
            "t1403OutBlock1": {
                "hname": "hname`char", ## 한글명@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 누적거래량@@
                "kmprice": "kmprice`long", ## 공모가@@
                "date": "date`char", ## 등록일@@
                "recprice": "recprice`long", ## 등록일기준가@@
                "kmdiff": "kmdiff`float", ## 기준가등락율@@
                "close": "close`long", ## 등록일종가@@
                "recdiff": "recdiff`float", ## 등록일등락율@@
                "shcode": "shcode`char##종목코드@@"
            }
        }
    },
    "t1404": { ## 관리/불성실/투자유의조회(t1404)
        "input": {
            "t1404InBlock": {
                "gubun": " ", ## 구분@@
                "jongchk": " ", ## 종목체크@@
                "cts_shcode": " ##종목코드_CTS@@"
            }
        },
        "output": {
            "t1404OutBlock": {
                "cts_shcode": "cts_shcode`char##종목코드_CTS@@"
            },
            "t1404OutBlock1": {
                "hname": "hname`char", ## 한글명@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 누적거래량@@
                "date": "date`char", ## 지정일@@
                "tprice": "tprice`long", ## 지정일주가@@
                "tchange": "tchange`long", ## 지정일대비@@
                "tdiff": "tdiff`float", ## 대비율@@
                "reason": "reason`char", ## 사유@@
                "shcode": "shcode`char", ## 종목코드@@
                "edate": "edate`char##해제일@@"
            }
        }
    },
    "t1405": { ## 투자경고/매매정지/정리매매조회(t1405)
        "input": {
            "t1405InBlock": {
                "gubun": " ", ## 구분@@
                "jongchk": " ", ## 종목체크@@
                "cts_shcode": " ##종목코드_CTS@@"
            }
        },
        "output": {
            "t1405OutBlock": {
                "cts_shcode": "cts_shcode`char##종목코드_CTS@@"
            },
            "t1405OutBlock1": {
                "hname": "hname`char", ## 한글명@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 누적거래량@@
                "date": "date`char", ## 지정일@@
                "edate": "edate`char", ## 해제일@@
                "shcode": "shcode`char##종목코드@@"
            }
        }
    },
    "t1410": { ## 초저유동성조회(t1410)
        "input": {
            "t1410InBlock": {
                "gubun": " ", ## 구분@@
                "cts_shcode": " ##종목코드_CTS@@"
            }
        },
        "output": {
            "t1410OutBlock": {
                "cts_shcode": "cts_shcode`char##종목코드_CTS@@"
            },
            "t1410OutBlock1": {
                "hname": "hname`char", ## 한글명@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 누적거래량@@
                "shcode": "shcode`char##종목코드@@"
            }
        }
    },
    "t1411": { ## 증거금율별종목조회(t1411)
        "input": {
            "t1411InBlock": {
                "gubun": " ", ## 시장구분@@
                "jongchk": " ", ## 위탁신용구분@@
                "jkrate": " ", ## 증거금율구분@@
                "shcode": " ", ## 종목코드@@
                "idx": "0##IDX@@"
            }
        },
        "output": {
            "t1411OutBlock": {
                "jkrate": "jkrate`long", ## 위탁증거금율@@
                "sjkrate": "sjkrate`long", ## 신용증거금율@@
                "idx": "idx`long##IDX@@"
            },
            "t1411OutBlock1": {
                "shcode": "shcode`char", ## 종목코드@@
                "hname": "hname`char", ## 종목명@@
                "jkrate": "jkrate`long", ## 위탁증거금율@@
                "sjkrate": "sjkrate`long", ## 신용증거금율@@
                "subprice": "subprice`long", ## 대용가@@
                "recprice": "recprice`long", ## 전일종가@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long##누적거래량@@"
            }
        }
    },
    "t1422": { ## 상/하한(t1422)
        "input": {
            "t1422InBlock": {
                "qrygb": " ", ## 조회구분@@
                "gubun": " ", ## 구분@@
                "jnilgubun": " ", ## 전일구분@@
                "sign": " ", ## 상하한구분@@
                "jc_num": "0", ## 대상제외@@
                "sprice": "0", ## 시작가격@@
                "eprice": "0", ## 종료가격@@
                "volume": "0", ## 거래량@@
                "idx": "0##IDX@@"
            }
        },
        "output": {
            "t1422OutBlock": {
                "cnt": "cnt`long", ## CNT@@
                "idx": "idx`long##IDX@@"
            },
            "t1422OutBlock1": {
                "hname": "hname`char", ## 한글명@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 누적거래량@@
                "diff_vol": "diff_vol`float", ## 거래증가율@@
                "offerrem1": "offerrem1`long", ## 매도잔량@@
                "bidrem1": "bidrem1`long", ## 매수잔량@@
                "last": "last`char", ## 최종진입@@
                "lmtdaycnt": "lmtdaycnt`long", ## 연속@@
                "jnilvolume": "jnilvolume`long", ## 전일거래량@@
                "shcode": "shcode`char##종목코드@@"
            }
        }
    },
    "t1427": { ## 상/하한가직전(t1427)
        "input": {
            "t1427InBlock": {
                "qrygb": " ", ## 조회구분@@
                "gubun": " ", ## 구분@@
                "signgubun": " ", ## 상하한가구분@@
                "diff": "0", ## 등락율@@
                "jc_num": "0", ## 대상제외@@
                "sprice": "0", ## 시작가격@@
                "eprice": "0", ## 종료가격@@
                "volume": "0", ## 거래량@@
                "idx": "0", ## IDX@@
                "jshex": " ##전일상하한제외@@"
            }
        },
        "output": {
            "t1427OutBlock": {
                "cnt": "cnt`long", ## CNT@@
                "idx": "idx`long##IDX@@"
            },
            "t1427OutBlock1": {
                "hname": "hname`char", ## 한글명@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 누적거래량@@
                "diff_vol": "diff_vol`float", ## 거래증가율@@
                "lmtprice": "lmtprice`long", ## 상한가/하한가@@
                "rate": "rate`float", ## 대비율@@
                "shcode": "shcode`char", ## 종목코드@@
                "jnilvolume": "jnilvolume`long", ## 전일거래량@@
                "open": "open`long", ## 시가@@
                "high": "high`long", ## 고가@@
                "low": "low`long", ## 저가@@
                "lmtdaycnt": "lmtdaycnt`long", ## 연속@@
                "value": "value`long", ## 거래대금@@
                "total": "total`long##시가총액@@"
            }
        }
    },
    "t1442": { ## 신고/신저가(t1442)
        "input": {
            "t1442InBlock": {
                "gubun": " ", ## 구분@@
                "type1": " ", ## 신고신저@@
                "type2": " ", ## 기간@@
                "type3": " ", ## 유지여부@@
                "jc_num": "0", ## 대상제외@@
                "sprice": "0", ## 시작가격@@
                "eprice": "0", ## 종료가격@@
                "volume": "0", ## 거래량@@
                "idx": "0", ## IDX@@
                "jc_num2": "0##대상제외2@@"
            }
        },
        "output": {
            "t1442OutBlock": {
                "idx": "idx`long##IDX@@"
            },
            "t1442OutBlock1": {
                "shcode": "shcode`char", ## 종목코드@@
                "hname": "hname`char", ## 종목명@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 거래량@@
                "pastprice": "pastprice`long", ## 이전가@@
                "pastsign": "pastsign`char", ## 이전가대비구분@@
                "pastchange": "pastchange`long", ## 이전가대비@@
                "pastdiff": "pastdiff`float##이전가대비율@@"
            }
        }
    },
    "t1444": { ## 시가총액상위(t1444)
        "input": {
            "t1444InBlock": {
                "upcode": " ", ## 업종코드@@
                "idx": "0##IDX@@"
            }
        },
        "output": {
            "t1444OutBlock": {
                "idx": "idx`long##IDX@@"
            },
            "t1444OutBlock1": {
                "shcode": "shcode`char", ## 종목코드@@
                "hname": "hname`char", ## 종목명@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 거래량@@
                "vol_rate": "vol_rate`float", ## 거래비중@@
                "total": "total`long", ## 시가총액@@
                "rate": "rate`float", ## 비중@@
                "for_rate": "for_rate`float##외인비중@@"
            }
        }
    },
    "t1449": { ## 가격대별매매비중조회(t1449)
        "input": {
            "t1449InBlock": {
                "shcode": " ", ## 단축코드@@
                "dategb": " ##일자구분@@"
            }
        },
        "output": {
            "t1449OutBlock": {
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 거래량@@
                "msvolume": "msvolume`long", ## 매수체결량@@
                "mdvolume": "mdvolume`long##매도체결량@@"
            },
            "t1449OutBlock1": {
                "price": "price`long", ## 체결가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "tickdiff": "tickdiff`float", ## 등락율@@
                "cvolume": "cvolume`long", ## 체결수량@@
                "diff": "diff`float", ## 비중@@
                "mdvolume": "mdvolume`long", ## 매도체결량@@
                "msvolume": "msvolume`long", ## 매수체결량@@
                "msdiff": "msdiff`float##매수비율@@"
            }
        }
    },
    "t1452": { ## 거래량상위(t1452)
        "input": {
            "t1452InBlock": {
                "gubun": " ", ## 구분@@
                "jnilgubun": " ", ## 전일구분@@
                "sdiff": "0", ## 시작등락율@@
                "ediff": "0", ## 종료등락율@@
                "jc_num": "0", ## 대상제외@@
                "sprice": "0", ## 시작가격@@
                "eprice": "0", ## 종료가격@@
                "volume": "0", ## 거래량@@
                "idx": "0##IDX@@"
            }
        },
        "output": {
            "t1452OutBlock": {
                "idx": "idx`long##IDX@@"
            },
            "t1452OutBlock1": {
                "hname": "hname`char", ## 종목명@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 누적거래량@@
                "vol": "vol`float", ## 회전율@@
                "jnilvolume": "jnilvolume`long", ## 전일거래량@@
                "bef_diff": "bef_diff`float", ## 전일비@@
                "shcode": "shcode`char##종목코드@@"
            }
        }
    },
    "t1463": { ## 거래대금상위(t1463)
        "input": {
            "t1463InBlock": {
                "gubun": " ", ## 구분@@
                "jnilgubun": " ", ## 전일구분@@
                "jc_num": "0", ## 대상제외@@
                "sprice": "0", ## 시작가격@@
                "eprice": "0", ## 종료가격@@
                "volume": "0", ## 거래량@@
                "idx": "0", ## IDX@@
                "jc_num2": "0##대상제외2@@"
            }
        },
        "output": {
            "t1463OutBlock": {
                "idx": "idx`long##IDX@@"
            },
            "t1463OutBlock1": {
                "hname": "hname`char", ## 한글명@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 누적거래량@@
                "value": "value`long", ## 거래대금@@
                "jnilvalue": "jnilvalue`long", ## 전일거래대금@@
                "bef_diff": "bef_diff`float", ## 전일비@@
                "shcode": "shcode`char", ## 종목코드@@
                "filler": "filler`char", ## filler@@
                "jnilvolume": "jnilvolume`long##전일거래량@@"
            }
        }
    },
    "t1471": { ## 시간대별호가잔량추이(t1471)
        "input": {
            "t1471InBlock": {
                "shcode": " ", ## 종목코드@@
                "gubun": " ", ## 분구분@@
                "time": " ", ## 시간@@
                "cnt": " ##자료개수@@"
            }
        },
        "output": {
            "t1471OutBlock": {
                "time": "time`char", ## 시간CTS@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long##누적거래량@@"
            },
            "t1471OutBlock1": {
                "time": "time`char", ## 체결시간@@
                "preoffercha1": "preoffercha1`long", ## 메도증감@@
                "offerrem1": "offerrem1`long", ## 매도우선잔량@@
                "offerho1": "offerho1`long", ## 매도우선호가@@
                "bidho1": "bidho1`long", ## 매수우선호가@@
                "bidrem1": "bidrem1`long", ## 매수우선잔량@@
                "prebidcha1": "prebidcha1`long", ## 매수증감@@
                "totofferrem": "totofferrem`long", ## 총매도@@
                "totbidrem": "totbidrem`long", ## 총매수@@
                "totsun": "totsun`long", ## 순매수@@
                "msrate": "msrate`float", ## 매수비율@@
                "close": "close`long##종가@@"
            }
        }
    },
    "t1475": { ## 체결강도추이(t1475)
        "input": {
            "t1475InBlock": {
                "shcode": " ", ## 종목코드@@
                "vptype": " ", ## 상승하락@@
                "datacnt": "0", ## 데이터개수@@
                "date": "0", ## 기준일자@@
                "time": "0", ## 기준시간@@
                "rankcnt": "0", ## 랭크카운터@@
                "gubun": " ##조회구분@@"
            }
        },
        "output": {
            "t1475OutBlock": {
                "date": "date`long", ## 기준일자@@
                "time": "time`long", ## 기준시간@@
                "rankcnt": "rankcnt`long##랭크카운터@@"
            },
            "t1475OutBlock1": {
                "datetime": "datetime`char", ## 일자@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 거래량@@
                "todayvp": "todayvp`float", ## 당일VP@@
                "ma5vp": "ma5vp`float", ## 5일MAVP@@
                "ma20vp": "ma20vp`float", ## 20일MAVP@@
                "ma60vp": "ma60vp`float##60일MAVP@@"
            }
        }
    },
    "t1485": { ## 예상지수(t1485)
        "input": {
            "t1485InBlock": {
                "upcode": " ", ## 업종코드@@
                "gubun": " ##조회구분@@"
            }
        },
        "output": {
            "t1485OutBlock": {
                "pricejisu": "pricejisu`float", ## 현재지수@@
                "sign": "sign`char", ## 지수전일대비구분@@
                "change": "change`float", ## 전일대비@@
                "volume": "volume`long", ## 거래량@@
                "yhighjo": "yhighjo`long", ## 상승종목수@@
                "yupjo": "yupjo`long", ## 상한종목수@@
                "yunchgjo": "yunchgjo`long", ## 보합종목수@@
                "ylowjo": "ylowjo`long", ## 하락종목수@@
                "ydownjo": "ydownjo`long", ## 하한종목수@@
                "ytrajo": "ytrajo`long##거래형성수@@"
            },
            "t1485OutBlock1": {
                "chetime": "chetime`char", ## 시간@@
                "jisu": "jisu`float", ## 예상지수@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`float", ## 전일대비@@
                "volume": "volume`long", ## 예상체결량@@
                "volcha": "volcha`long", ## 예상체결량직전대비@@
                "diff": "diff`float##예상등락율@@"
            }
        }
    },
    "t1486": { ## 시간별예상체결가(t1486)
        "input": {
            "t1486InBlock": {
                "shcode": " ", ## 단축코드@@
                "cts_time": " ", ## 시간CTS@@
                "cnt": "0##조회건수@@"
            }
        },
        "output": {
            "t1486OutBlock": {
                "cts_time": "cts_time`char##시간CTS@@"
            },
            "t1486OutBlock1": {
                "chetime": "chetime`char", ## 시간@@
                "price": "price`long", ## 예상체결가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "cvolume": "cvolume`long", ## 예상체결량@@
                "offerho1": "offerho1`long", ## 매도호가@@
                "bidho1": "bidho1`long", ## 매수호가@@
                "offerrem1": "offerrem1`long", ## 매도잔량@@
                "bidrem1": "bidrem1`long##매수잔량@@"
            }
        }
    },
    "t1488": { ## 예상체결가등락율상위조회(t1488)
        "input": {
            "t1488InBlock": {
                "gubun": " ", ## 거래소구분@@
                "sign": " ", ## 상하락구분@@
                "jgubun": " ", ## 장구분@@
                "jongchk": " ", ## 종목체크@@
                "idx": "0", ## IDX@@
                "volume": " ", ## 거래량@@
                "yesprice": "0", ## 예상체결시작가격@@
                "yeeprice": "0", ## 예상체결종료가격@@
                "yevolume": "0##예상체결량@@"
            }
        },
        "output": {
            "t1488OutBlock": {
                "idx": "idx`long##IDX@@"
            },
            "t1488OutBlock1": {
                "hname": "hname`char", ## 한글명@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 누적거래량@@
                "offerrem": "offerrem`long", ## 매도잔량@@
                "offerho": "offerho`long", ## 매도호가@@
                "bidho": "bidho`long", ## 매수호가@@
                "bidrem": "bidrem`long", ## 매수잔량@@
                "cnt": "cnt`long", ## 연속일수@@
                "shcode": "shcode`char", ## 종목코드@@
                "jkrate": "jkrate`char", ## 증거금율@@
                "jnilvolume": "jnilvolume`long##전일거래량@@"
            }
        }
    },
    "t1489": { ## 예상체결량상위조회(t1489)
        "input": {
            "t1489InBlock": {
                "gubun": " ", ## 거래소구분@@
                "jgubun": " ", ## 장구분@@
                "jongchk": " ", ## 종목체크@@
                "idx": "0", ## IDX@@
                "yesprice": "0", ## 예상체결시작가격@@
                "yeeprice": "0", ## 예상체결종료가격@@
                "yevolume": "0##예상체결량@@"
            }
        },
        "output": {
            "t1489OutBlock": {
                "idx": "idx`long##IDX@@"
            },
            "t1489OutBlock1": {
                "hname": "hname`char", ## 한글명@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 예상거래량@@
                "offerho": "offerho`long", ## 매도호가@@
                "bidho": "bidho`long", ## 매수호가@@
                "shcode": "shcode`char", ## 종목코드@@
                "jnilvolume": "jnilvolume`long##전일거래량@@"
            }
        }
    },
    "t1511": { ## 업종현재가(t1511)
        "input": {
            "t1511InBlock": {
                "upcode": " ##업종코드@@"
            }
        },
        "output": {
            "t1511OutBlock": {
                "gubun": "gubun`char", ## 업종구분@@
                "hname": "hname`char", ## 업종명@@
                "pricejisu": "pricejisu`float", ## 현재지수@@
                "jniljisu": "jniljisu`float", ## 전일지수@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`float", ## 전일대비@@
                "diffjisu": "diffjisu`float", ## 지수등락율@@
                "jnilvolume": "jnilvolume`long", ## 전일거래량@@
                "volume": "volume`long", ## 당일거래량@@
                "volumechange": "volumechange`long", ## 거래량전일대비@@
                "volumerate": "volumerate`float", ## 거래량비율@@
                "jnilvalue": "jnilvalue`long", ## 전일거래대금@@
                "value": "value`long", ## 당일거래대금@@
                "valuechange": "valuechange`long", ## 거래대금전일대비@@
                "valuerate": "valuerate`float", ## 거래대금비율@@
                "openjisu": "openjisu`float", ## 시가지수@@
                "opendiff": "opendiff`float", ## 시가등락율@@
                "opentime": "opentime`char", ## 시가시간@@
                "highjisu": "highjisu`float", ## 고가지수@@
                "highdiff": "highdiff`float", ## 고가등락율@@
                "hightime": "hightime`char", ## 고가시간@@
                "lowjisu": "lowjisu`float", ## 저가지수@@
                "lowdiff": "lowdiff`float", ## 저가등락율@@
                "lowtime": "lowtime`char", ## 저가시간@@
                "whjisu": "whjisu`float", ## 52주최고지수@@
                "whchange": "whchange`float", ## 52주최고현재가대비@@
                "whjday": "whjday`char", ## 52주최고지수일자@@
                "wljisu": "wljisu`float", ## 52주최저지수@@
                "wlchange": "wlchange`float", ## 52주최저현재가대비@@
                "wljday": "wljday`char", ## 52주최저지수일자@@
                "yhjisu": "yhjisu`float", ## 연중최고지수@@
                "yhchange": "yhchange`float", ## 연중최고현재가대비@@
                "yhjday": "yhjday`char", ## 연중최고지수일자@@
                "yljisu": "yljisu`float", ## 연중최저지수@@
                "ylchange": "ylchange`float", ## 연중최저현재가대비@@
                "yljday": "yljday`char", ## 연중최저지수일자@@
                "firstjcode": "firstjcode`char", ## 첫번째지수코드@@
                "firstjname": "firstjname`char", ## 첫번째지수명@@
                "firstjisu": "firstjisu`float", ## 첫번째지수@@
                "firsign": "firsign`char", ## 첫번째대비구분@@
                "firchange": "firchange`float", ## 첫번째전일대비@@
                "firdiff": "firdiff`float", ## 첫번째등락율@@
                "secondjcode": "secondjcode`char", ## 두번째지수코드@@
                "secondjname": "secondjname`char", ## 두번째지수명@@
                "secondjisu": "secondjisu`float", ## 두번째지수@@
                "secsign": "secsign`char", ## 두번째대비구분@@
                "secchange": "secchange`float", ## 두번째전일대비@@
                "secdiff": "secdiff`float", ## 두번째등락율@@
                "thirdjcode": "thirdjcode`char", ## 세번째지수코드@@
                "thirdjname": "thirdjname`char", ## 세번째지수명@@
                "thirdjisu": "thirdjisu`float", ## 세번째지수@@
                "thrsign": "thrsign`char", ## 세번째대비구분@@
                "thrchange": "thrchange`float", ## 세번째전일대비@@
                "thrdiff": "thrdiff`float", ## 세번째등락율@@
                "fourthjcode": "fourthjcode`char", ## 네번째지수코드@@
                "fourthjname": "fourthjname`char", ## 네번째지수명@@
                "fourthjisu": "fourthjisu`float", ## 네번째지수@@
                "forsign": "forsign`char", ## 네번째대비구분@@
                "forchange": "forchange`float", ## 네번째전일대비@@
                "fordiff": "fordiff`float", ## 네번째등락율@@
                "highjo": "highjo`long", ## 상승종목수@@
                "upjo": "upjo`long", ## 상한종목수@@
                "unchgjo": "unchgjo`long", ## 보합종목수@@
                "lowjo": "lowjo`long", ## 하락종목수@@
                "downjo": "downjo`long##하한종목수@@"
            }
        }
    },
    "t1514": { ## 업종기간별추이(t1514)
        "input": {
            "t1514InBlock": {
                "upcode": " ", ## 업종코드@@
                "gubun1": " ", ## 구분1@@
                "gubun2": " ", ## 구분2@@
                "cts_date": " ", ## CTS_일자@@
                "cnt": "0", ## 조회건수@@
                "rate_gbn": " ##비중구분@@"
            }
        },
        "output": {
            "t1514OutBlock": {
                "cts_date": "cts_date`char##CTS_일자@@"
            },
            "t1514OutBlock1": {
                "date": "date`char", ## 일자@@
                "jisu": "jisu`float", ## 지수@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`float", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 거래량@@
                "diff_vol": "diff_vol`float", ## 거래증가율@@
                "value1": "value1`long", ## 거래대금1@@
                "high": "high`long", ## 상승@@
                "unchg": "unchg`long", ## 보합@@
                "low": "low`long", ## 하락@@
                "uprate": "uprate`float", ## 상승종목비율@@
                "frgsvolume": "frgsvolume`long", ## 외인순매수@@
                "openjisu": "openjisu`float", ## 시가@@
                "highjisu": "highjisu`float", ## 고가@@
                "lowjisu": "lowjisu`float", ## 저가@@
                "value2": "value2`long", ## 거래대금2@@
                "up": "up`long", ## 상한@@
                "down": "down`long", ## 하한@@
                "totjo": "totjo`long", ## 종목수@@
                "orgsvolume": "orgsvolume`long", ## 기관순매수@@
                "upcode": "upcode`char", ## 업종코드@@
                "rate": "rate`float", ## 거래비중@@
                "divrate": "divrate`float##업종배당수익률@@"
            }
        }
    },
    "t1516": { ## 업종별종목시세(t1516)
        "input": {
            "t1516InBlock": {
                "upcode": " ", ## 업종코드@@
                "gubun": " ", ## 구분@@
                "shcode": " ##종목코드@@"
            }
        },
        "output": {
            "t1516OutBlock": {
                "shcode": "shcode`char", ## 종목코드@@
                "pricejisu": "pricejisu`float", ## 지수@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`float", ## 전일대비@@
                "jdiff": "jdiff`float##등락율@@"
            },
            "t1516OutBlock1": {
                "hname": "hname`char", ## 종목명@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 누적거래량@@
                "open": "open`long", ## 시가@@
                "high": "high`long", ## 고가@@
                "low": "low`long", ## 저가@@
                "sojinrate": "sojinrate`float", ## 소진율@@
                "beta": "beta`float", ## 베타계수@@
                "perx": "perx`float", ## PER@@
                "frgsvolume": "frgsvolume`long", ## 외인순매수@@
                "orgsvolume": "orgsvolume`long", ## 기관순매수@@
                "diff_vol": "diff_vol`float", ## 거래증가율@@
                "shcode": "shcode`char", ## 종목코드@@
                "total": "total`long", ## 시가총액@@
                "value": "value`long##거래대금@@"
            }
        }
    },
    "t1531": { ## 테마별종목(t1531)
        "input": {
            "t1531InBlock": {
                "tmname": " ", ## 테마명@@
                "tmcode": " ##테마코드@@"
            }
        },
        "output": {
            "t1531OutBlock": {
                "tmname": "tmname`char", ## 테마명@@
                "avgdiff": "avgdiff`float", ## 평균등락율@@
                "tmcode": "tmcode`char##테마코드@@"
            }
        }
    },
    "t1532": { ## 종목별테마(t1532)
        "input": {
            "t1532InBlock": {
                "shcode": " ##종목코드@@"
            }
        },
        "output": {
            "t1532OutBlock": {
                "tmname": "tmname`char", ## 테마명@@
                "avgdiff": "avgdiff`float", ## 평균등락율@@
                "tmcode": "tmcode`char##테마코드@@"
            }
        }
    },
    "t1533": { ## 특이테마(t1533)
        "input": {
            "t1533InBlock": {
                "gubun": " ", ## 구분@@
                "chgdate": "0##대비일자@@"
            }
        },
        "output": {
            "t1533OutBlock": {
                "bdate": "bdate`char##일자@@"
            },
            "t1533OutBlock1": {
                "tmname": "tmname`char", ## 테마명@@
                "totcnt": "totcnt`long", ## 전체@@
                "upcnt": "upcnt`long", ## 상승@@
                "dncnt": "dncnt`long", ## 하락@@
                "uprate": "uprate`float", ## 상승비율@@
                "diff_vol": "diff_vol`float", ## 거래증가율@@
                "avgdiff": "avgdiff`float", ## 평균등락율@@
                "chgdiff": "chgdiff`float", ## 대비등락율@@
                "tmcode": "tmcode`char##테마코드@@"
            }
        }
    },
    "t1537": { ## 테마종목별시세조회(t1537)
        "input": {
            "t1537InBlock": {
                "tmcode": " ##테마코드@@"
            }
        },
        "output": {
            "t1537OutBlock": {
                "upcnt": "upcnt`long", ## 상승종목수@@
                "tmcnt": "tmcnt`long", ## 테마종목수@@
                "uprate": "uprate`long", ## 상승종목비율@@
                "tmname": "tmname`char##테마명@@"
            },
            "t1537OutBlock1": {
                "hname": "hname`char", ## 종목명@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 누적거래량@@
                "jniltime": "jniltime`float", ## 전일동시간@@
                "shcode": "shcode`char", ## 종목코드@@
                "yeprice": "yeprice`long", ## 예상체결가@@
                "open": "open`long", ## 시가@@
                "high": "high`long", ## 고가@@
                "low": "low`long", ## 저가@@
                "value": "value`long", ## 누적거래대금@@단위:백만
                "marketcap": "marketcap`long##시가총액@@단위:백만"
            }
        }
    },
    "t1601": { ## 투자자별종합(t1601)
        "input": {
            "t1601InBlock": {
                "gubun1": " ", ## 주식금액수량구분1@@
                "gubun2": " ", ## 옵션금액수량구분2@@
                "gubun3": " ", ## 금액단위@@
                "gubun4": " ##선물금액수량구분4@@"
            }
        },
        "output": {
            "t1601OutBlock1": {
                "tjjcode_08": "tjjcode_08`char", ## 개인투자자코드@@
                "ms_08": "ms_08`long", ## 개인매수@@
                "md_08": "md_08`long", ## 개인매도@@
                "rate_08": "rate_08`long", ## 개인증감@@
                "svolume_08": "svolume_08`long", ## 개인순매수@@
                "jjcode_17": "jjcode_17`char", ## 외국인투자자코드@@
                "ms_17": "ms_17`long", ## 외국인매수@@
                "md_17": "md_17`long", ## 외국인매도@@
                "rate_17": "rate_17`long", ## 외국인증감@@
                "svolume_17": "svolume_17`long", ## 외국인순매수@@
                "jjcode_18": "jjcode_18`char", ## 기관계투자자코드@@
                "ms_18": "ms_18`long", ## 기관계매수@@
                "md_18": "md_18`long", ## 기관계매도@@
                "rate_18": "rate_18`long", ## 기관계증감@@
                "svolume_18": "svolume_18`long", ## 기관계순매수@@
                "jjcode_01": "jjcode_01`char", ## 증권투자자코드@@
                "ms_01": "ms_01`long", ## 증권매수@@
                "md_01": "md_01`long", ## 증권매도@@
                "rate_01": "rate_01`long", ## 증권증감@@
                "svolume_01": "svolume_01`long", ## 증권순매수@@
                "jjcode_03": "jjcode_03`char", ## 투신투자자코드@@
                "ms_03": "ms_03`long", ## 투신매수@@
                "md_03": "md_03`long", ## 투신매도@@
                "rate_03": "rate_03`long", ## 투신증감@@
                "svolume_03": "svolume_03`long", ## 투신순매수@@
                "jjcode_04": "jjcode_04`char", ## 은행투자자코드@@
                "ms_04": "ms_04`long", ## 은행매수@@
                "md_04": "md_04`long", ## 은행매도@@
                "rate_04": "rate_04`long", ## 은행증감@@
                "svolume_04": "svolume_04`long", ## 은행순매수@@
                "jjcode_02": "jjcode_02`char", ## 보험투자자코드@@
                "ms_02": "ms_02`long", ## 보험매수@@
                "md_02": "md_02`long", ## 보험매도@@
                "rate_02": "rate_02`long", ## 보험증감@@
                "svolume_02": "svolume_02`long", ## 보험순매수@@
                "jjcode_05": "jjcode_05`char", ## 종금투자자코드@@
                "ms_05": "ms_05`long", ## 종금매수@@
                "md_05": "md_05`long", ## 종금매도@@
                "rate_05": "rate_05`long", ## 종금증감@@
                "svolume_05": "svolume_05`long", ## 종금순매수@@
                "jjcode_06": "jjcode_06`char", ## 기금투자자코드@@
                "ms_06": "ms_06`long", ## 기금매수@@
                "md_06": "md_06`long", ## 기금매도@@
                "rate_06": "rate_06`long", ## 기금증감@@
                "svolume_06": "svolume_06`long", ## 기금순매수@@
                "jjcode_11": "jjcode_11`char", ## 국가투자코드@@
                "ms_11": "ms_11`long", ## 국가매수@@
                "md_11": "md_11`long", ## 국가매도@@
                "rate_11": "rate_11`long", ## 국가증감@@
                "svolume_11": "svolume_11`long", ## 국가순매수@@
                "jjcode_07": "jjcode_07`char", ## 기타투자자코드@@
                "ms_07": "ms_07`long", ## 기타매수@@
                "md_07": "md_07`long", ## 기타매도@@
                "rate_07": "rate_07`long", ## 기타증감@@
                "svolume_07": "svolume_07`long", ## 기타순매수@@
                "jjcode_00": "jjcode_00`char", ## 사모펀드투자자코드@@
                "ms_00": "ms_00`long", ## 사모펀드매수@@
                "md_00": "md_00`long", ## 사모펀드매도@@
                "rate_00": "rate_00`long", ## 사모펀드증감@@
                "svolume_00": "svolume_00`long##사모펀드순매수@@"
            },
            "t1601OutBlock2": {
                "tjjcode_08": "tjjcode_08`char", ## 개인투자자코드@@
                "ms_08": "ms_08`long", ## 개인매수@@
                "md_08": "md_08`long", ## 개인매도@@
                "rate_08": "rate_08`long", ## 개인증감@@
                "svolume_08": "svolume_08`long", ## 개인순매수@@
                "jjcode_17": "jjcode_17`char", ## 외국인투자자코드@@
                "ms_17": "ms_17`long", ## 외국인매수@@
                "md_17": "md_17`long", ## 외국인매도@@
                "rate_17": "rate_17`long", ## 외국인증감@@
                "svolume_17": "svolume_17`long", ## 외국인순매수@@
                "jjcode_18": "jjcode_18`char", ## 기관계투자자코드@@
                "ms_18": "ms_18`long", ## 기관계매수@@
                "md_18": "md_18`long", ## 기관계매도@@
                "rate_18": "rate_18`long", ## 기관계증감@@
                "svolume_18": "svolume_18`long", ## 기관계순매수@@
                "jjcode_01": "jjcode_01`char", ## 증권투자자코드@@
                "ms_01": "ms_01`long", ## 증권매수@@
                "md_01": "md_01`long", ## 증권매도@@
                "rate_01": "rate_01`long", ## 증권증감@@
                "svolume_01": "svolume_01`long", ## 증권순매수@@
                "jjcode_03": "jjcode_03`char", ## 투신투자자코드@@
                "ms_03": "ms_03`long", ## 투신매수@@
                "md_03": "md_03`long", ## 투신매도@@
                "rate_03": "rate_03`long", ## 투신증감@@
                "svolume_03": "svolume_03`long", ## 투신순매수@@
                "jjcode_04": "jjcode_04`char", ## 은행투자자코드@@
                "ms_04": "ms_04`long", ## 은행매수@@
                "md_04": "md_04`long", ## 은행매도@@
                "rate_04": "rate_04`long", ## 은행증감@@
                "svolume_04": "svolume_04`long", ## 은행순매수@@
                "jjcode_02": "jjcode_02`char", ## 보험투자자코드@@
                "ms_02": "ms_02`long", ## 보험매수@@
                "md_02": "md_02`long", ## 보험매도@@
                "rate_02": "rate_02`long", ## 보험증감@@
                "svolume_02": "svolume_02`long", ## 보험순매수@@
                "jjcode_05": "jjcode_05`char", ## 종금투자자코드@@
                "ms_05": "ms_05`long", ## 종금매수@@
                "md_05": "md_05`long", ## 종금매도@@
                "rate_05": "rate_05`long", ## 종금증감@@
                "svolume_05": "svolume_05`long", ## 종금순매수@@
                "jjcode_06": "jjcode_06`char", ## 기금투자자코드@@
                "ms_06": "ms_06`long", ## 기금매수@@
                "md_06": "md_06`long", ## 기금매도@@
                "rate_06": "rate_06`long", ## 기금증감@@
                "svolume_06": "svolume_06`long", ## 기금순매수@@
                "jjcode_11": "jjcode_11`char", ## 국가투자코드@@
                "ms_11": "ms_11`long", ## 국가매수@@
                "md_11": "md_11`long", ## 국가매도@@
                "rate_11": "rate_11`long", ## 국가증감@@
                "svolume_11": "svolume_11`long", ## 국가순매수@@
                "jjcode_07": "jjcode_07`char", ## 기타투자자코드@@
                "ms_07": "ms_07`long", ## 기타매수@@
                "md_07": "md_07`long", ## 기타매도@@
                "rate_07": "rate_07`long", ## 기타증감@@
                "svolume_07": "svolume_07`long", ## 기타순매수@@
                "jjcode_00": "jjcode_00`char", ## 사모펀드투자자코드@@
                "ms_00": "ms_00`long", ## 사모펀드매수@@
                "md_00": "md_00`long", ## 사모펀드매도@@
                "rate_00": "rate_00`long", ## 사모펀드증감@@
                "svolume_00": "svolume_00`long##사모펀드순매수@@"
            },
            "t1601OutBlock3": {
                "tjjcode_08": "tjjcode_08`char", ## 개인투자자코드@@
                "ms_08": "ms_08`long", ## 개인매수@@
                "md_08": "md_08`long", ## 개인매도@@
                "rate_08": "rate_08`long", ## 개인증감@@
                "svolume_08": "svolume_08`long", ## 개인순매수@@
                "jjcode_17": "jjcode_17`char", ## 외국인투자자코드@@
                "ms_17": "ms_17`long", ## 외국인매수@@
                "md_17": "md_17`long", ## 외국인매도@@
                "rate_17": "rate_17`long", ## 외국인증감@@
                "svolume_17": "svolume_17`long", ## 외국인순매수@@
                "jjcode_18": "jjcode_18`char", ## 기관계투자자코드@@
                "ms_18": "ms_18`long", ## 기관계매수@@
                "md_18": "md_18`long", ## 기관계매도@@
                "rate_18": "rate_18`long", ## 기관계증감@@
                "svolume_18": "svolume_18`long", ## 기관계순매수@@
                "jjcode_01": "jjcode_01`char", ## 증권투자자코드@@
                "ms_01": "ms_01`long", ## 증권매수@@
                "md_01": "md_01`long", ## 증권매도@@
                "rate_01": "rate_01`long", ## 증권증감@@
                "svolume_01": "svolume_01`long", ## 증권순매수@@
                "jjcode_03": "jjcode_03`char", ## 투신투자자코드@@
                "ms_03": "ms_03`long", ## 투신매수@@
                "md_03": "md_03`long", ## 투신매도@@
                "rate_03": "rate_03`long", ## 투신증감@@
                "svolume_03": "svolume_03`long", ## 투신순매수@@
                "jjcode_04": "jjcode_04`char", ## 은행투자자코드@@
                "ms_04": "ms_04`long", ## 은행매수@@
                "md_04": "md_04`long", ## 은행매도@@
                "rate_04": "rate_04`long", ## 은행증감@@
                "svolume_04": "svolume_04`long", ## 은행순매수@@
                "jjcode_02": "jjcode_02`char", ## 보험투자자코드@@
                "ms_02": "ms_02`long", ## 보험매수@@
                "md_02": "md_02`long", ## 보험매도@@
                "rate_02": "rate_02`long", ## 보험증감@@
                "svolume_02": "svolume_02`long", ## 보험순매수@@
                "jjcode_05": "jjcode_05`char", ## 종금투자자코드@@
                "ms_05": "ms_05`long", ## 종금매수@@
                "md_05": "md_05`long", ## 종금매도@@
                "rate_05": "rate_05`long", ## 종금증감@@
                "svolume_05": "svolume_05`long", ## 종금순매수@@
                "jjcode_06": "jjcode_06`char", ## 기금투자자코드@@
                "ms_06": "ms_06`long", ## 기금매수@@
                "md_06": "md_06`long", ## 기금매도@@
                "rate_06": "rate_06`long", ## 기금증감@@
                "svolume_06": "svolume_06`long", ## 기금순매수@@
                "jjcode_11": "jjcode_11`char", ## 국가투자코드@@
                "ms_11": "ms_11`long", ## 국가매수@@
                "md_11": "md_11`long", ## 국가매도@@
                "rate_11": "rate_11`long", ## 국가증감@@
                "svolume_11": "svolume_11`long", ## 국가순매수@@
                "jjcode_07": "jjcode_07`char", ## 기타투자자코드@@
                "ms_07": "ms_07`long", ## 기타매수@@
                "md_07": "md_07`long", ## 기타매도@@
                "rate_07": "rate_07`long", ## 기타증감@@
                "svolume_07": "svolume_07`long", ## 기타순매수@@
                "jjcode_00": "jjcode_00`char", ## 사모펀드투자자코드@@
                "ms_00": "ms_00`long", ## 사모펀드매수@@
                "md_00": "md_00`long", ## 사모펀드매도@@
                "rate_00": "rate_00`long", ## 사모펀드증감@@
                "svolume_00": "svolume_00`long##사모펀드순매수@@"
            },
            "t1601OutBlock4": {
                "tjjcode_08": "tjjcode_08`char", ## 개인투자자코드@@
                "ms_08": "ms_08`long", ## 개인매수@@
                "md_08": "md_08`long", ## 개인매도@@
                "rate_08": "rate_08`long", ## 개인증감@@
                "svolume_08": "svolume_08`long", ## 개인순매수@@
                "jjcode_17": "jjcode_17`char", ## 외국인투자자코드@@
                "ms_17": "ms_17`long", ## 외국인매수@@
                "md_17": "md_17`long", ## 외국인매도@@
                "rate_17": "rate_17`long", ## 외국인증감@@
                "svolume_17": "svolume_17`long", ## 외국인순매수@@
                "jjcode_18": "jjcode_18`char", ## 기관계투자자코드@@
                "ms_18": "ms_18`long", ## 기관계매수@@
                "md_18": "md_18`long", ## 기관계매도@@
                "rate_18": "rate_18`long", ## 기관계증감@@
                "svolume_18": "svolume_18`long", ## 기관계순매수@@
                "jjcode_01": "jjcode_01`char", ## 증권투자자코드@@
                "ms_01": "ms_01`long", ## 증권매수@@
                "md_01": "md_01`long", ## 증권매도@@
                "rate_01": "rate_01`long", ## 증권증감@@
                "svolume_01": "svolume_01`long", ## 증권순매수@@
                "jjcode_03": "jjcode_03`char", ## 투신투자자코드@@
                "ms_03": "ms_03`long", ## 투신매수@@
                "md_03": "md_03`long", ## 투신매도@@
                "rate_03": "rate_03`long", ## 투신증감@@
                "svolume_03": "svolume_03`long", ## 투신순매수@@
                "jjcode_04": "jjcode_04`char", ## 은행투자자코드@@
                "ms_04": "ms_04`long", ## 은행매수@@
                "md_04": "md_04`long", ## 은행매도@@
                "rate_04": "rate_04`long", ## 은행증감@@
                "svolume_04": "svolume_04`long", ## 은행순매수@@
                "jjcode_02": "jjcode_02`char", ## 보험투자자코드@@
                "ms_02": "ms_02`long", ## 보험매수@@
                "md_02": "md_02`long", ## 보험매도@@
                "rate_02": "rate_02`long", ## 보험증감@@
                "svolume_02": "svolume_02`long", ## 보험순매수@@
                "jjcode_05": "jjcode_05`char", ## 종금투자자코드@@
                "ms_05": "ms_05`long", ## 종금매수@@
                "md_05": "md_05`long", ## 종금매도@@
                "rate_05": "rate_05`long", ## 종금증감@@
                "svolume_05": "svolume_05`long", ## 종금순매수@@
                "jjcode_06": "jjcode_06`char", ## 기금투자자코드@@
                "ms_06": "ms_06`long", ## 기금매수@@
                "md_06": "md_06`long", ## 기금매도@@
                "rate_06": "rate_06`long", ## 기금증감@@
                "svolume_06": "svolume_06`long", ## 기금순매수@@
                "jjcode_11": "jjcode_11`char", ## 국가투자코드@@
                "ms_11": "ms_11`long", ## 국가매수@@
                "md_11": "md_11`long", ## 국가매도@@
                "rate_11": "rate_11`long", ## 국가증감@@
                "svolume_11": "svolume_11`long", ## 국가순매수@@
                "jjcode_07": "jjcode_07`char", ## 기타투자자코드@@
                "ms_07": "ms_07`long", ## 기타매수@@
                "md_07": "md_07`long", ## 기타매도@@
                "rate_07": "rate_07`long", ## 기타증감@@
                "svolume_07": "svolume_07`long", ## 기타순매수@@
                "jjcode_00": "jjcode_00`char", ## 사모펀드투자자코드@@
                "ms_00": "ms_00`long", ## 사모펀드매수@@
                "md_00": "md_00`long", ## 사모펀드매도@@
                "rate_00": "rate_00`long", ## 사모펀드증감@@
                "svolume_00": "svolume_00`long##사모펀드순매수@@"
            },
            "t1601OutBlock5": {
                "tjjcode_08": "tjjcode_08`char", ## 개인투자자코드@@
                "ms_08": "ms_08`long", ## 개인매수@@
                "md_08": "md_08`long", ## 개인매도@@
                "rate_08": "rate_08`long", ## 개인증감@@
                "svolume_08": "svolume_08`long", ## 개인순매수@@
                "jjcode_17": "jjcode_17`char", ## 외국인투자자코드@@
                "ms_17": "ms_17`long", ## 외국인매수@@
                "md_17": "md_17`long", ## 외국인매도@@
                "rate_17": "rate_17`long", ## 외국인증감@@
                "svolume_17": "svolume_17`long", ## 외국인순매수@@
                "jjcode_18": "jjcode_18`char", ## 기관계투자자코드@@
                "ms_18": "ms_18`long", ## 기관계매수@@
                "md_18": "md_18`long", ## 기관계매도@@
                "rate_18": "rate_18`long", ## 기관계증감@@
                "svolume_18": "svolume_18`long", ## 기관계순매수@@
                "jjcode_01": "jjcode_01`char", ## 증권투자자코드@@
                "ms_01": "ms_01`long", ## 증권매수@@
                "md_01": "md_01`long", ## 증권매도@@
                "rate_01": "rate_01`long", ## 증권증감@@
                "svolume_01": "svolume_01`long", ## 증권순매수@@
                "jjcode_03": "jjcode_03`char", ## 투신투자자코드@@
                "ms_03": "ms_03`long", ## 투신매수@@
                "md_03": "md_03`long", ## 투신매도@@
                "rate_03": "rate_03`long", ## 투신증감@@
                "svolume_03": "svolume_03`long", ## 투신순매수@@
                "jjcode_04": "jjcode_04`char", ## 은행투자자코드@@
                "ms_04": "ms_04`long", ## 은행매수@@
                "md_04": "md_04`long", ## 은행매도@@
                "rate_04": "rate_04`long", ## 은행증감@@
                "svolume_04": "svolume_04`long", ## 은행순매수@@
                "jjcode_02": "jjcode_02`char", ## 보험투자자코드@@
                "ms_02": "ms_02`long", ## 보험매수@@
                "md_02": "md_02`long", ## 보험매도@@
                "rate_02": "rate_02`long", ## 보험증감@@
                "svolume_02": "svolume_02`long", ## 보험순매수@@
                "jjcode_05": "jjcode_05`char", ## 종금투자자코드@@
                "ms_05": "ms_05`long", ## 종금매수@@
                "md_05": "md_05`long", ## 종금매도@@
                "rate_05": "rate_05`long", ## 종금증감@@
                "svolume_05": "svolume_05`long", ## 종금순매수@@
                "jjcode_06": "jjcode_06`char", ## 기금투자자코드@@
                "ms_06": "ms_06`long", ## 기금매수@@
                "md_06": "md_06`long", ## 기금매도@@
                "rate_06": "rate_06`long", ## 기금증감@@
                "svolume_06": "svolume_06`long", ## 기금순매수@@
                "jjcode_11": "jjcode_11`char", ## 국가투자코드@@
                "ms_11": "ms_11`long", ## 국가매수@@
                "md_11": "md_11`long", ## 국가매도@@
                "rate_11": "rate_11`long", ## 국가증감@@
                "svolume_11": "svolume_11`long", ## 국가순매수@@
                "jjcode_07": "jjcode_07`char", ## 기타투자자코드@@
                "ms_07": "ms_07`long", ## 기타매수@@
                "md_07": "md_07`long", ## 기타매도@@
                "rate_07": "rate_07`long", ## 기타증감@@
                "svolume_07": "svolume_07`long", ## 기타순매수@@
                "jjcode_00": "jjcode_00`char", ## 사모펀드투자자코드@@
                "ms_00": "ms_00`long", ## 사모펀드매수@@
                "md_00": "md_00`long", ## 사모펀드매도@@
                "rate_00": "rate_00`long", ## 사모펀드증감@@
                "svolume_00": "svolume_00`long##사모펀드순매수@@"
            },
            "t1601OutBlock6": {
                "tjjcode_08": "tjjcode_08`char", ## 개인투자자코드@@
                "ms_08": "ms_08`long", ## 개인매수@@
                "md_08": "md_08`long", ## 개인매도@@
                "rate_08": "rate_08`long", ## 개인증감@@
                "svolume_08": "svolume_08`long", ## 개인순매수@@
                "jjcode_17": "jjcode_17`char", ## 외국인투자자코드@@
                "ms_17": "ms_17`long", ## 외국인매수@@
                "md_17": "md_17`long", ## 외국인매도@@
                "rate_17": "rate_17`long", ## 외국인증감@@
                "svolume_17": "svolume_17`long", ## 외국인순매수@@
                "jjcode_18": "jjcode_18`char", ## 기관계투자자코드@@
                "ms_18": "ms_18`long", ## 기관계매수@@
                "md_18": "md_18`long", ## 기관계매도@@
                "rate_18": "rate_18`long", ## 기관계증감@@
                "svolume_18": "svolume_18`long", ## 기관계순매수@@
                "jjcode_01": "jjcode_01`char", ## 증권투자자코드@@
                "ms_01": "ms_01`long", ## 증권매수@@
                "md_01": "md_01`long", ## 증권매도@@
                "rate_01": "rate_01`long", ## 증권증감@@
                "svolume_01": "svolume_01`long", ## 증권순매수@@
                "jjcode_03": "jjcode_03`char", ## 투신투자자코드@@
                "ms_03": "ms_03`long", ## 투신매수@@
                "md_03": "md_03`long", ## 투신매도@@
                "rate_03": "rate_03`long", ## 투신증감@@
                "svolume_03": "svolume_03`long", ## 투신순매수@@
                "jjcode_04": "jjcode_04`char", ## 은행투자자코드@@
                "ms_04": "ms_04`long", ## 은행매수@@
                "md_04": "md_04`long", ## 은행매도@@
                "rate_04": "rate_04`long", ## 은행증감@@
                "svolume_04": "svolume_04`long", ## 은행순매수@@
                "jjcode_02": "jjcode_02`char", ## 보험투자자코드@@
                "ms_02": "ms_02`long", ## 보험매수@@
                "md_02": "md_02`long", ## 보험매도@@
                "rate_02": "rate_02`long", ## 보험증감@@
                "svolume_02": "svolume_02`long", ## 보험순매수@@
                "jjcode_05": "jjcode_05`char", ## 종금투자자코드@@
                "ms_05": "ms_05`long", ## 종금매수@@
                "md_05": "md_05`long", ## 종금매도@@
                "rate_05": "rate_05`long", ## 종금증감@@
                "svolume_05": "svolume_05`long", ## 종금순매수@@
                "jjcode_06": "jjcode_06`char", ## 기금투자자코드@@
                "ms_06": "ms_06`long", ## 기금매수@@
                "md_06": "md_06`long", ## 기금매도@@
                "rate_06": "rate_06`long", ## 기금증감@@
                "svolume_06": "svolume_06`long", ## 기금순매수@@
                "jjcode_11": "jjcode_11`char", ## 국가투자코드@@
                "ms_11": "ms_11`long", ## 국가매수@@
                "md_11": "md_11`long", ## 국가매도@@
                "rate_11": "rate_11`long", ## 국가증감@@
                "svolume_11": "svolume_11`long", ## 국가순매수@@
                "jjcode_07": "jjcode_07`char", ## 기타투자자코드@@
                "ms_07": "ms_07`long", ## 기타매수@@
                "md_07": "md_07`long", ## 기타매도@@
                "rate_07": "rate_07`long", ## 기타증감@@
                "svolume_07": "svolume_07`long", ## 기타순매수@@
                "jjcode_00": "jjcode_00`char", ## 사모펀드투자자코드@@
                "ms_00": "ms_00`long", ## 사모펀드매수@@
                "md_00": "md_00`long", ## 사모펀드매도@@
                "rate_00": "rate_00`long", ## 사모펀드증감@@
                "svolume_00": "svolume_00`long##사모펀드순매수@@"
            }
        }
    },
    "t1602": { ## 시간대별투자자매매추이(t1602)
        "input": {
            "t1602InBlock": {
                "market": " ", ## 시장구분@@
                "upcode": " ", ## 업종코드@@
                "gubun1": " ", ## 수량구분@@
                "gubun2": " ", ## 전일분구분@@
                "cts_time": " ", ## CTSTIME@@
                "cts_idx": "0", ## CTSIDX@@
                "cnt": "0", ## 조회건수@@
                "gubun3": " ##직전대비구분@@C:직전대비"
            }
        },
        "output": {
            "t1602OutBlock": {
                "cts_time": "cts_time`char", ## CTSTIME@@
                "tjjcode_08": "tjjcode_08`char", ## 개인투자자코드@@
                "ms_08": "ms_08`long", ## 개인매수@@
                "md_08": "md_08`long", ## 개인매도@@
                "rate_08": "rate_08`long", ## 개인증감@@
                "svolume_08": "svolume_08`long", ## 개인순매수@@
                "jjcode_17": "jjcode_17`char", ## 외국인투자자코드@@
                "ms_17": "ms_17`long", ## 외국인매수@@
                "md_17": "md_17`long", ## 외국인매도@@
                "rate_17": "rate_17`long", ## 외국인증감@@
                "svolume_17": "svolume_17`long", ## 외국인순매수@@
                "jjcode_18": "jjcode_18`char", ## 기관계투자자코드@@
                "ms_18": "ms_18`long", ## 기관계매수@@
                "md_18": "md_18`long", ## 기관계매도@@
                "rate_18": "rate_18`long", ## 기관계증감@@
                "svolume_18": "svolume_18`long", ## 기관계순매수@@
                "jjcode_01": "jjcode_01`char", ## 증권투자자코드@@
                "ms_01": "ms_01`long", ## 증권매수@@
                "md_01": "md_01`long", ## 증권매도@@
                "rate_01": "rate_01`long", ## 증권증감@@
                "svolume_01": "svolume_01`long", ## 증권순매수@@
                "jjcode_03": "jjcode_03`char", ## 투신투자자코드@@
                "ms_03": "ms_03`long", ## 투신매수@@
                "md_03": "md_03`long", ## 투신매도@@
                "rate_03": "rate_03`long", ## 투신증감@@
                "svolume_03": "svolume_03`long", ## 투신순매수@@
                "jjcode_04": "jjcode_04`char", ## 은행투자자코드@@
                "ms_04": "ms_04`long", ## 은행매수@@
                "md_04": "md_04`long", ## 은행매도@@
                "rate_04": "rate_04`long", ## 은행증감@@
                "svolume_04": "svolume_04`long", ## 은행순매수@@
                "jjcode_02": "jjcode_02`char", ## 보험투자자코드@@
                "ms_02": "ms_02`long", ## 보험매수@@
                "md_02": "md_02`long", ## 보험매도@@
                "rate_02": "rate_02`long", ## 보험증감@@
                "svolume_02": "svolume_02`long", ## 보험순매수@@
                "jjcode_05": "jjcode_05`char", ## 종금투자자코드@@
                "ms_05": "ms_05`long", ## 종금매수@@
                "md_05": "md_05`long", ## 종금매도@@
                "rate_05": "rate_05`long", ## 종금증감@@
                "svolume_05": "svolume_05`long", ## 종금순매수@@
                "jjcode_06": "jjcode_06`char", ## 기금투자자코드@@
                "ms_06": "ms_06`long", ## 기금매수@@
                "md_06": "md_06`long", ## 기금매도@@
                "rate_06": "rate_06`long", ## 기금증감@@
                "svolume_06": "svolume_06`long", ## 기금순매수@@
                "jjcode_07": "jjcode_07`char", ## 기타투자자코드@@
                "ms_07": "ms_07`long", ## 기타매수@@
                "md_07": "md_07`long", ## 기타매도@@
                "rate_07": "rate_07`long", ## 기타증감@@
                "svolume_07": "svolume_07`long", ## 기타순매수@@
                "jjcode_11": "jjcode_11`char", ## 국가투자자코드@@
                "ms_11": "ms_11`long", ## 국가매수@@
                "md_11": "md_11`long", ## 국가매도@@
                "rate_11": "rate_11`long", ## 국가증감@@
                "svolume_11": "svolume_11`long", ## 국가순매수@@
                "jjcode_00": "jjcode_00`char", ## 사모펀드코드@@
                "ms_00": "ms_00`long", ## 사모펀드매수@@
                "md_00": "md_00`long", ## 사모펀드매도@@
                "rate_00": "rate_00`long", ## 사모펀드증감@@
                "svolume_00": "svolume_00`long##사모펀드순매수@@"
            },
            "t1602OutBlock1": {
                "time": "time`char", ## 시간@@
                "sv_08": "sv_08`long", ## 개인순매수@@
                "sv_17": "sv_17`long", ## 외국인순매수@@
                "sv_18": "sv_18`long", ## 기관계순매수@@
                "sv_01": "sv_01`long", ## 증권순매수@@
                "sv_03": "sv_03`long", ## 투신순매수@@
                "sv_04": "sv_04`long", ## 은행순매수@@
                "sv_02": "sv_02`long", ## 보험순매수@@
                "sv_05": "sv_05`long", ## 종금순매수@@
                "sv_06": "sv_06`long", ## 기금순매수@@
                "sv_07": "sv_07`long", ## 기타순매수@@
                "sv_11": "sv_11`long", ## 국가순매수@@
                "sv_00": "sv_00`long##사모펀드순매수@@"
            }
        }
    },
    "t1603": { ## 시간대별투자자매매추이상세(t1603)
        "input": {
            "t1603InBlock": {
                "market": " ", ## 시장구분@@
                "gubun1": " ", ## 투자자구분@@
                "gubun2": " ", ## 전일분구분@@
                "cts_time": " ", ## CTSTIME@@
                "cts_idx": "0", ## CTSIDX@@
                "cnt": "0", ## 조회건수@@
                "upcode": " ##업종코드@@"
            }
        },
        "output": {
            "t1603OutBlock": {
                "cts_idx": "cts_idx`long", ## CTSIDX@@
                "cts_time": "cts_time`char##CTSTIME@@"
            },
            "t1603OutBlock1": {
                "time": "time`char", ## 시간@@
                "tjjcode": "tjjcode`char", ## 투자자구분@@
                "msvolume": "msvolume`long", ## 매수수량@@
                "mdvolume": "mdvolume`long", ## 매도수량@@
                "msvalue": "msvalue`long", ## 매수금액@@
                "mdvalue": "mdvalue`long", ## 매도금액@@
                "svolume": "svolume`long", ## 순매수수량@@
                "svalue": "svalue`long##순매수금액@@"
            }
        }
    },
    "t1615": { ## 투자자매매종합1(t1615)
        "input": {
            "t1615InBlock": {
                "gubun1": " ", ## 주식구분@@
                "gubun2": " ##옵션구분@@"
            }
        },
        "output": {
            "t1615OutBlock": {
                "dwvolume": "dwvolume`long", ## 위탁매도수량@@
                "dwvalue": "dwvalue`long", ## 위탁매도금액@@
                "djvolume": "djvolume`long", ## 자기매도수량@@
                "djvalue": "djvalue`long", ## 자기매도금액@@
                "sum_volume": "sum_volume`long", ## 합계수량@@
                "sum_value": "sum_value`long##합계금액@@"
            },
            "t1615OutBlock1": {
                "hname": "hname`char", ## 시장명@@
                "sv_08": "sv_08`long", ## 개인@@
                "sv_17": "sv_17`long", ## 외국인@@
                "sv_18": "sv_18`long", ## 기관계@@
                "sv_07": "sv_07`long##증권@@"
            }
        }
    },
    "t1617": { ## 투자자매매종합2(t1617)
        "input": {
            "t1617InBlock": {
                "gubun1": " ", ## 시장구분@@1:코스피2:코스닥3:선물4:콜옵션5:풋옵션6:주식선물
                "gubun2": " ", ## 수량금액구분@@1:수량2:금액
                "gubun3": " ", ## 일자구분@@1:시간대별2:일별
                "cts_date": " ", ## CTSDATE(연속키값-일자)@@
                "cts_time": " ##CTSTIME(연속키값-시간)@@"
            }
        },
        "output": {
            "t1617OutBlock": {
                "cts_date": "cts_date`char", ## CTSDATE@@
                "cts_time": "cts_time`char", ## CTSTIME@@
                "ms_08": "ms_08`long", ## 개인매수@@
                "md_08": "md_08`long", ## 개인매도@@
                "sv_08": "sv_08`long", ## 개인순매수@@
                "ms_17": "ms_17`long", ## 외국인매수@@
                "md_17": "md_17`long", ## 외국인매도@@
                "sv_17": "sv_17`long", ## 외국인순매수@@
                "ms_18": "ms_18`long", ## 기관계매수@@
                "md_18": "md_18`long", ## 기관계매도@@
                "sv_18": "sv_18`long", ## 기관계순매수@@
                "ms_01": "ms_01`long", ## 증권매수@@
                "md_01": "md_01`long", ## 증권매도@@
                "sv_01": "sv_01`long##증권순매수@@"
            },
            "t1617OutBlock1": {
                "date": "date`char", ## 날짜@@
                "time": "time`char", ## 시간@@
                "sv_08": "sv_08`long", ## 개인@@
                "sv_17": "sv_17`long", ## 외국인@@
                "sv_18": "sv_18`long", ## 기관계@@
                "sv_01": "sv_01`long##증권@@"
            }
        }
    },
    "t1621": { ## 업종별분별투자자매매동향(챠트용)
        "input": {
            "t1621InBlock": {
                "upcode": " ", ## 업종코드@@
                "nmin": "0", ## N분@@
                "cnt": "0", ## 조회건수@@
                "bgubun": " ##전일분@@"
            }
        },
        "output": {
            "t1621OutBlock": {
                "indcode": "indcode`char", ## 개인투자자코드@@
                "forcode": "forcode`char", ## 외국인투자자코드@@
                "syscode": "syscode`char", ## 기관계투자자코드@@
                "stocode": "stocode`char", ## 증권투자자코드@@
                "invcode": "invcode`char", ## 투신투자자코드@@
                "bancode": "bancode`char", ## 은행투자자코드@@
                "inscode": "inscode`char", ## 보험투자자코드@@
                "fincode": "fincode`char", ## 종금투자자코드@@
                "moncode": "moncode`char", ## 기금투자자코드@@
                "etccode": "etccode`char", ## 기타투자자코드@@
                "natcode": "natcode`char", ## 국가투자자코드@@
                "pefcode": "pefcode`char", ## 사모펀드투자자코드@@
                "jisucd": "jisucd`char", ## 기준지수코드@@
                "jisunm": "jisunm`char##기준지수명@@"
            },
            "t1621OutBlock1": {
                "date": "date`char", ## 일자@@
                "time": "time`char", ## 시간@@
                "datetime": "datetime`char", ## 일자시간@@
                "indmsvol": "indmsvol`long", ## 개인순매수거래량@@
                "indmsamt": "indmsamt`double", ## 개인순매수거래대금@@
                "formsvol": "formsvol`long", ## 외국인순매수거래량@@
                "formsamt": "formsamt`double", ## 외국인순매수거래대금@@
                "sysmsvol": "sysmsvol`long", ## 기관계순매수거래량@@
                "sysmsamt": "sysmsamt`double", ## 기관계순매수거래대금@@
                "stomsvol": "stomsvol`long", ## 증권순매수거래량@@
                "stomsamt": "stomsamt`double", ## 증권순매수거래대금@@
                "invmsvol": "invmsvol`long", ## 투신순매수거래량@@
                "invmsamt": "invmsamt`double", ## 투신순매수거래대금@@
                "banmsvol": "banmsvol`long", ## 은행순매수거래량@@
                "banmsamt": "banmsamt`double", ## 은행순매수거래대금@@
                "insmsvol": "insmsvol`long", ## 보험순매수거래량@@
                "insmsamt": "insmsamt`double", ## 보험순매수거래대금@@
                "finmsvol": "finmsvol`long", ## 종금순매수거래량@@
                "finmsamt": "finmsamt`double", ## 종금순매수거래대금@@
                "monmsvol": "monmsvol`long", ## 기금순매수거래량@@
                "monmsamt": "monmsamt`double", ## 기금순매수거래대금@@
                "etcmsvol": "etcmsvol`long", ## 기타순매수거래량@@
                "etcmsamt": "etcmsamt`double", ## 기타순매수거래대금@@
                "natmsvol": "natmsvol`long", ## 국가순매수거래량@@
                "natmsamt": "natmsamt`double", ## 국가순매수거래대금@@
                "pefmsvol": "pefmsvol`long", ## 사모펀드순매수거래량@@
                "pefmsamt": "pefmsamt`double", ## 사모펀드순매수거래대금@@
                "upclose": "upclose`float", ## 기준지수@@
                "upcvolume": "upcvolume`long", ## 기준체결거래량@@
                "upvolume": "upvolume`double", ## 기준누적거래량@@
                "upvalue": "upvalue`double##기준거래대금@@"
            }
        }
    },
    "t1631": { ## 프로그램매매종합조회(t1631)
        "input": {
            "t1631InBlock": {
                "gubun": " ", ## 구분@@
                "dgubun": " ", ## 일자구분@@
                "sdate": " ", ## 시작일자@@
                "edate": " ##종료일자@@"
            }
        },
        "output": {
            "t1631OutBlock": {
                "cdhrem": "cdhrem`long", ## 매도차익미체결잔량@@
                "bdhrem": "bdhrem`long", ## 매도비차익미체결잔량@@
                "tcdrem": "tcdrem`long", ## 매도차익주문수량@@
                "tbdrem": "tbdrem`long", ## 매도비차익주문수량@@
                "cshrem": "cshrem`long", ## 매수차익미체결잔량@@
                "bshrem": "bshrem`long", ## 매수비차익미체결잔량@@
                "tcsrem": "tcsrem`long", ## 매수차익주문수량@@
                "tbsrem": "tbsrem`long##매수비차익주문수량@@"
            },
            "t1631OutBlock1": {
                "offervolume": "offervolume`long", ## 매도수량@@
                "offervalue": "offervalue`long", ## 매도금액@@
                "bidvolume": "bidvolume`long", ## 매수수량@@
                "bidvalue": "bidvalue`long", ## 매수금액@@
                "volume": "volume`long", ## 순매수수량@@
                "value": "value`long##순매수금액@@"
            }
        }
    },
    "t1632": { ## 시간대별프로그램매매추이(t1632)
        "input": {
            "t1632InBlock": {
                "gubun": " ", ## 구분@@
                "gubun1": " ", ## 금액수량구분@@
                "gubun2": " ", ## 직전대비증감@@
                "gubun3": " ", ## 전일구분@@
                "date": " ", ## 일자@@
                "time": " ##시간@@"
            }
        },
        "output": {
            "t1632OutBlock": {
                "date": "date`char", ## 날짜CTS@@
                "time": "time`char", ## 시간CTS@@
                "idx": "idx`long##IDX@@"
            },
            "t1632OutBlock1": {
                "time": "time`char", ## 시간@@
                "k200jisu": "k200jisu`float", ## KP200@@
                "sign": "sign`char", ## 대비구분@@
                "change": "change`float", ## 대비@@
                "k200basis": "k200basis`float", ## BASIS@@
                "tot3": "tot3`long", ## 전체순매수@@
                "tot1": "tot1`long", ## 전체매수@@
                "tot2": "tot2`long", ## 전체매도@@
                "cha3": "cha3`long", ## 차익순매수@@
                "cha1": "cha1`long", ## 차익매수@@
                "cha2": "cha2`long", ## 차익매도@@
                "bcha3": "bcha3`long", ## 비차익순매수@@
                "bcha1": "bcha1`long", ## 비차익매수@@
                "bcha2": "bcha2`long##비차익매도@@"
            }
        }
    },
    "t1633": { ## 기간별프로그램매매추이(t1633)
        "input": {
            "t1633InBlock": {
                "gubun": " ", ## 시장구분@@
                "gubun1": " ", ## 금액수량구분@@
                "gubun2": " ", ## 수치누적구분@@
                "gubun3": " ", ## 일주월구분@@
                "fdate": " ", ## from일자@@
                "tdate": " ", ## to일자@@
                "gubun4": " ", ## 직전대비증감구분@@
                "date": " ##날짜@@"
            }
        },
        "output": {
            "t1633OutBlock": {
                "date": "date`char", ## 날짜@@
                "idx": "idx`long##IDX@@"
            },
            "t1633OutBlock1": {
                "date": "date`char", ## 일자@@
                "jisu": "jisu`float", ## KP200@@
                "sign": "sign`char", ## 대비구분@@
                "change": "change`float", ## 대비@@
                "tot3": "tot3`long", ## 전체순매수@@
                "tot1": "tot1`long", ## 전체매수@@
                "tot2": "tot2`long", ## 전체매도@@
                "cha3": "cha3`long", ## 차익순매수@@
                "cha1": "cha1`long", ## 차익매수@@
                "cha2": "cha2`long", ## 차익매도@@
                "bcha3": "bcha3`long", ## 비차익순매수@@
                "bcha1": "bcha1`long", ## 비차익매수@@
                "bcha2": "bcha2`long", ## 비차익매도@@
                "volume": "volume`long##거래량@@"
            }
        }
    },
    "t1636": { ## 종목별프로그램매매동향(t1636)
        "input": {
            "t1636InBlock": {
                "gubun": " ", ## 구분@@
                "gubun1": " ", ## 금액수량구분@@
                "gubun2": " ", ## 정렬기준@@
                "shcode": " ", ## 종목코드@@
                "cts_idx": "0##IDXCTS@@"
            }
        },
        "output": {
            "t1636OutBlock": {
                "cts_idx": "cts_idx`long##IDXCTS@@"
            },
            "t1636OutBlock1": {
                "rank": "rank`long", ## 순위@@
                "hname": "hname`char", ## 종목명@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 대비구분@@
                "change": "change`long", ## 대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 거래량@@
                "svalue": "svalue`long", ## 순매수금액@@
                "offervalue": "offervalue`long", ## 매도금액@@
                "stksvalue": "stksvalue`long", ## 매수금액@@
                "svolume": "svolume`long", ## 순매수수량@@
                "offervolume": "offervolume`long", ## 매도수량@@
                "stksvolume": "stksvolume`long", ## 매수수량@@
                "sgta": "sgta`long", ## 시가총액@@
                "rate": "rate`float", ## 비중@@
                "shcode": "shcode`char##종목코드@@"
            }
        }
    },
    "t1637": { ## 종목별프로그램매매추이(t1637)
        "input": {
            "t1637InBlock": {
                "gubun1": " ", ## 수량금액구분@@0:수량1:금액
                "gubun2": " ", ## 시간일별구분@@0:시간1:일자
                "shcode": " ", ## 종목코드@@
                "date": " ", ## 일자@@
                "time": " ", ## 시간@@
                "cts_idx": "0##IDXCTS@@9999:차트"
            }
        },
        "output": {
            "t1637OutBlock": {
                "cts_idx": "cts_idx`long##IDXCTS@@"
            },
            "t1637OutBlock1": {
                "date": "date`char", ## 일자@@
                "time": "time`char", ## 시간@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 대비구분@@
                "change": "change`long", ## 대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 거래량@@
                "svalue": "svalue`long", ## 순매수금액@@
                "offervalue": "offervalue`long", ## 매도금액@@
                "stksvalue": "stksvalue`long", ## 매수금액@@
                "svolume": "svolume`long", ## 순매수수량@@
                "offervolume": "offervolume`long", ## 매도수량@@
                "stksvolume": "stksvolume`long", ## 매수수량@@
                "shcode": "shcode`char##종목코드@@"
            }
        }
    },
    "t1638": { ## 종목별잔량/사전공시(t1638)
        "input": {
            "t1638InBlock": {
                "gubun1": " ", ## 구분@@
                "shcode": " ", ## 종목코드@@
                "gubun2": " ##정렬@@"
            }
        },
        "output": {
            "t1638OutBlock": {
                "rank": "rank`long", ## 순위@@
                "hname": "hname`char", ## 한글명@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "sigatotrt": "sigatotrt`float", ## 시총비중@@
                "obuyvol": "obuyvol`long", ## 순매수잔량@@
                "buyrem": "buyrem`long", ## 매수잔량@@
                "psgvolume": "psgvolume`long", ## 매수공시수량@@
                "sellrem": "sellrem`long", ## 매도잔량@@
                "pdgvolume": "pdgvolume`long", ## 매도공시수량@@
                "sigatot": "sigatot`long", ## 시가총액@@
                "shcode": "shcode`char##종목코드@@"
            }
        }
    },
    "t1640": { ## 프로그램매매종합조회(미니)(t1640)
        "input": {
            "t1640InBlock": {
                "gubun": " ##구분@@"
            }
        },
        "output": {
            "t1640OutBlock": {
                "offervolume": "offervolume`long", ## 매도수량@@
                "bidvolume": "bidvolume`long", ## 매수수량@@
                "volume": "volume`long", ## 순매수수량@@
                "offerdiff": "offerdiff`long", ## 매도증감@@
                "biddiff": "biddiff`long", ## 매수증감@@
                "sundiff": "sundiff`long", ## 순매수증감@@
                "basis": "basis`float", ## 베이시스@@
                "offervalue": "offervalue`double", ## 매도금액@@
                "bidvalue": "bidvalue`double", ## 매수금액@@
                "value": "value`double", ## 순매수금액@@
                "offervaldiff": "offervaldiff`double", ## 매도금액증감@@
                "bidvaldiff": "bidvaldiff`double", ## 매수금액증감@@
                "sunvaldiff": "sunvaldiff`double##순매수증감@@"
            }
        }
    },
    "t1662": { ## 시간대별프로그램매매추이(차트)(t1662)
        "input": {
            "t1662InBlock": {
                "gubun": " ", ## 구분@@
                "gubun1": " ", ## 금액수량구분@@
                "gubun3": " ##전일구분@@"
            }
        },
        "output": {
            "t1662OutBlock": {
                "time": "time`char", ## 시간@@
                "k200jisu": "k200jisu`float", ## KP200@@
                "sign": "sign`char", ## 대비구분@@
                "change": "change`float", ## 대비@@
                "k200basis": "k200basis`float", ## BASIS@@
                "tot3": "tot3`long", ## 전체순매수@@
                "tot1": "tot1`long", ## 전체매수@@
                "tot2": "tot2`long", ## 전체매도@@
                "cha3": "cha3`long", ## 차익순매수@@
                "cha1": "cha1`long", ## 차익매수@@
                "cha2": "cha2`long", ## 차익매도@@
                "bcha3": "bcha3`long", ## 비차익순매수@@
                "bcha1": "bcha1`long", ## 비차익매수@@
                "bcha2": "bcha2`long", ## 비차익매도@@
                "volume": "volume`long##거래량@@"
            }
        }
    },
    "t1664": { ## 투자자매매종합(챠트)
        "input": {
            "t1664InBlock": {
                "mgubun": " ", ## 시장구분@@
                "vagubun": " ", ## 금액수량구분@@
                "bdgubun": " ", ## 시간일별구분@@
                "cnt": "0##조회건수@@"
            }
        },
        "output": {
            "t1664OutBlock1": {
                "dt": "dt`char", ## 일자시간@@
                "tjj01": "tjj01`double", ## 증권순매수@@
                "tjj02": "tjj02`double", ## 보험순매수@@
                "tjj03": "tjj03`double", ## 투신순매수@@
                "tjj04": "tjj04`double", ## 은행순매수@@
                "tjj05": "tjj05`double", ## 종금순매수@@
                "tjj06": "tjj06`double", ## 기금순매수@@
                "tjj07": "tjj07`double", ## 기타순매수@@
                "tjj08": "tjj08`double", ## 개인순매수@@
                "tjj17": "tjj17`double", ## 외국인순매수@@
                "tjj18": "tjj18`double", ## 기관순매수@@
                "cha": "cha`double", ## 차익순매수@@
                "bicha": "bicha`double", ## 비차익순매수@@
                "totcha": "totcha`double", ## 종합순매수@@
                "basis": "basis`float##베이시스@@"
            }
        }
    },
    "t1665": { ## 기간별투자자매매추이(챠트)
        "input": {
            "t1665InBlock": {
                "market": " ", ## 시장구분@@1:kospi2:kp2003:kosdaq4:선물5:풋옵션6:콜옵션
                "upcode": " ", ## 업종코드@@
                "gubun2": " ", ## 수치구분@@1:수치2:누적
                "gubun3": " ", ## 단위구분@@1:일2:주3:월
                "from_date": " ", ## 시작날짜@@
                "to_date": " ##종료날짜@@"
            }
        },
        "output": {
            "t1665OutBlock": {
                "mcode": "mcode`char", ## 시장코드@@
                "mname": "mname`char##시장명@@"
            },
            "t1665OutBlock1": {
                "date": "date`char", ## 일자@@
                "sv_08": "sv_08`long", ## 개인수량@@
                "sv_17": "sv_17`long", ## 외인계수량(등록+미등록)@@
                "sv_18": "sv_18`long", ## 기관계수량@@
                "sv_01": "sv_01`long", ## 증권수량@@
                "sv_03": "sv_03`long", ## 투신수량@@
                "sv_04": "sv_04`long", ## 은행수량@@
                "sv_02": "sv_02`long", ## 보험수량@@
                "sv_05": "sv_05`long", ## 종금수량@@
                "sv_06": "sv_06`long", ## 기금수량@@
                "sv_07": "sv_07`long", ## 기타수량@@
                "sv_00": "sv_00`long", ## 사모펀드수량@@
                "sv_09": "sv_09`long", ## 등록외국인수량@@
                "sv_10": "sv_10`long", ## 미등록외국인수량@@
                "sv_11": "sv_11`long", ## 국가수량@@
                "sv_99": "sv_99`long", ## 기타계수량(기타+국가)@@
                "sa_08": "sa_08`double", ## 개인금액@@
                "sa_17": "sa_17`double", ## 외인계금액(등록+미등록)@@
                "sa_18": "sa_18`double", ## 기관계금액@@
                "sa_01": "sa_01`double", ## 증권금액@@
                "sa_03": "sa_03`double", ## 투신금액@@
                "sa_04": "sa_04`double", ## 은행금액@@
                "sa_02": "sa_02`double", ## 보험금액@@
                "sa_05": "sa_05`double", ## 종금금액@@
                "sa_06": "sa_06`double", ## 기금금액@@
                "sa_07": "sa_07`double", ## 기타금액@@
                "sa_00": "sa_00`double", ## 사모펀드금액@@
                "sa_09": "sa_09`double", ## 등록외국인금액@@
                "sa_10": "sa_10`double", ## 미등록외국인금액@@
                "sa_11": "sa_11`double", ## 국가금액@@
                "sa_99": "sa_99`double", ## 기타계금액(기타+국가)@@
                "jisu": "jisu`float##시장지수@@"
            }
        }
    },
    "t1701": { ## 외인기관종목별동향(t1701)
        "input": {
            "t1701InBlock": {
                "shcode": " ", ## 종목코드@@
                "gubun": " ", ## 구분@@
                "fromdt": " ", ## 시작일자@@
                "todt": " ", ## 종료일자@@
                "prapp": "0", ## PR적용@@
                "prgubun": " ", ## PR적용구분@@
                "orggubun": " ", ## 기관적용@@
                "frggubun": " ##외인적용@@"
            }
        },
        "output": {
            "t1701OutBlock": {
                "date": "date`char", ## 일자@@
                "close": "close`long", ## 종가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 누적거래량@@
                "psnvolume": "psnvolume`long", ## 개인@@
                "orgvolume": "orgvolume`long", ## 기관@@
                "frgvolume": "frgvolume`long", ## 외국인@@
                "frgvolumesum": "frgvolumesum`long", ## 외국계@@
                "pgmvolume": "pgmvolume`long", ## 프로그램@@
                "listing": "listing`long", ## 보유주식수@@
                "listupdn": "listupdn`long", ## 발행증감@@
                "sjrate": "sjrate`float##소진율@@"
            }
        }
    },
    "t1702": { ## 외인기관종목별동향(t1702)
        "input": {
            "t1702InBlock": {
                "shcode": " ", ## 종목코드@@
                "todt": " ", ## 종료일자@@
                "volvalgb": " ", ## 금액수량구분@@0:금액1:수량2:단가
                "msmdgb": " ", ## 매수매도구분@@0:순매수1:매수2:매도
                "cumulgb": " ", ## 누적구분@@0:일간1:누적
                "cts_date": " ", ## CTSDATE@@
                "cts_idx": "0##CTSIDX@@"
            }
        },
        "output": {
            "t1702OutBlock": {
                "cts_idx": "cts_idx`long", ## CTSIDX@@
                "cts_date": "cts_date`char##CTSDATE@@"
            },
            "t1702OutBlock1": {
                "date": "date`char", ## 일자@@
                "close": "close`long", ## 종가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 누적거래량@@
                "amt0000": "amt0000`long", ## 사모펀드@@
                "amt0001": "amt0001`long", ## 증권@@
                "amt0002": "amt0002`long", ## 보험@@
                "amt0003": "amt0003`long", ## 투신@@
                "amt0004": "amt0004`long", ## 은행@@
                "amt0005": "amt0005`long", ## 종금@@
                "amt0006": "amt0006`long", ## 기금@@
                "amt0007": "amt0007`long", ## 기타법인@@
                "amt0008": "amt0008`long", ## 개인@@
                "amt0009": "amt0009`long", ## 등록외국인@@
                "amt0010": "amt0010`long", ## 미등록외국인@@
                "amt0011": "amt0011`long", ## 국가외@@
                "amt0018": "amt0018`long", ## 기관@@
                "amt0088": "amt0088`long", ## 외인계(등록+미등록)@@
                "amt0099": "amt0099`long##기타계(기타+국가)@@"
            }
        }
    },
    "t1717": { ## 외인기관종목별동향(t1717)
        "input": {
            "t1717InBlock": {
                "shcode": " ", ## 종목코드@@
                "gubun": " ", ## 구분@@0:일간순매수1:기간누적순매수
                "fromdt": " ", ## 시작일자(일간조회일경우는space)@@
                "todt": " ##종료일자@@"
            }
        },
        "output": {
            "t1717OutBlock": {
                "date": "date`char", ## 일자@@
                "close": "close`long", ## 종가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 누적거래량@@
                "tjj0000_vol": "tjj0000_vol`long", ## 사모펀드(순매수량)@@
                "tjj0001_vol": "tjj0001_vol`long", ## 증권(순매수량)@@
                "tjj0002_vol": "tjj0002_vol`long", ## 보험(순매수량)@@
                "tjj0003_vol": "tjj0003_vol`long", ## 투신(순매수량)@@
                "tjj0004_vol": "tjj0004_vol`long", ## 은행(순매수량)@@
                "tjj0005_vol": "tjj0005_vol`long", ## 종금(순매수량)@@
                "tjj0006_vol": "tjj0006_vol`long", ## 기금(순매수량)@@
                "tjj0007_vol": "tjj0007_vol`long", ## 기타법인(순매수량)@@
                "tjj0008_vol": "tjj0008_vol`long", ## 개인(순매수량)@@
                "tjj0009_vol": "tjj0009_vol`long", ## 등록외국인(순매수량)@@
                "tjj0010_vol": "tjj0010_vol`long", ## 미등록외국인(순매수량)@@
                "tjj0011_vol": "tjj0011_vol`long", ## 국가외(순매수량)@@
                "tjj0018_vol": "tjj0018_vol`long", ## 기관(순매수량)@@
                "tjj0016_vol": "tjj0016_vol`long", ## 외인계(순매수량)(등록+미등록)@@
                "tjj0017_vol": "tjj0017_vol`long", ## 기타계(순매수량)(기타+국가)@@
                "tjj0000_dan": "tjj0000_dan`long", ## 사모펀드(단가)@@
                "tjj0001_dan": "tjj0001_dan`long", ## 증권(단가)@@
                "tjj0002_dan": "tjj0002_dan`long", ## 보험(단가)@@
                "tjj0003_dan": "tjj0003_dan`long", ## 투신(단가)@@
                "tjj0004_dan": "tjj0004_dan`long", ## 은행(단가)@@
                "tjj0005_dan": "tjj0005_dan`long", ## 종금(단가)@@
                "tjj0006_dan": "tjj0006_dan`long", ## 기금(단가)@@
                "tjj0007_dan": "tjj0007_dan`long", ## 기타법인(단가)@@
                "tjj0008_dan": "tjj0008_dan`long", ## 개인(단가)@@
                "tjj0009_dan": "tjj0009_dan`long", ## 등록외국인(단가)@@
                "tjj0010_dan": "tjj0010_dan`long", ## 미등록외국인(단가)@@
                "tjj0011_dan": "tjj0011_dan`long", ## 국가외(단가)@@
                "tjj0018_dan": "tjj0018_dan`long", ## 기관(단가)@@
                "tjj0016_dan": "tjj0016_dan`long", ## 외인계(단가)(등록+미등록)@@
                "tjj0017_dan": "tjj0017_dan`long##기타계(단가)(기타+국가)@@"
            }
        }
    },
    "t1752": { ## 종목별상위회원사(t1752)
        "input": {
            "t1752InBlock": {
                "shcode": " ", ## 종목코드@@
                "traddate1": " ", ## 조회날짜1@@
                "traddate2": " ", ## 조회날짜2@@
                "fwgubun1": " ", ## 외국계구분@@
                "cts_idx": "0##CTSIDX@@"
            }
        },
        "output": {
            "t1752OutBlock": {
                "fwdvl": "fwdvl`long", ## 외국계매도@@
                "fwsvl": "fwsvl`long", ## 외국계매수@@
                "cts_idx": "cts_idx`long##CTSIDX@@"
            },
            "t1752OutBlock1": {
                "tradname": "tradname`char", ## 회원사@@
                "tradmdvol": "tradmdvol`long", ## 매도수량@@
                "tradmsvol": "tradmsvol`long", ## 매수수량@@
                "tradmssvol": "tradmssvol`long", ## 순매수@@
                "wintrd": "wintrd`long", ## 창구거래@@
                "winrat": "winrat`float", ## 비중@@
                "tradno": "tradno`char", ## 회원사코드@@
                "wgubun": "wgubun`char", ## 외국계여부@@
                "swinrat": "swinrat`float##순비중@@"
            }
        }
    },
    "t1764": { ## 회원사리스트(t1764)
        "input": {
            "t1764InBlock": {
                "shcode": " ", ## 종목코드@@
                "gubun1": " ##구분1@@"
            }
        },
        "output": {
            "t1764OutBlock": {
                "rank": "rank`long", ## 순위@@
                "tradno": "tradno`char", ## 거래원번호@@
                "tradname": "tradname`char##거래원이름@@"
            }
        }
    },
    "t1771": { ## 종목별회원사추이(t1771)
        "input": {
            "t1771InBlock": {
                "shcode": " ", ## 종목코드@@
                "tradno": " ", ## 거래원코드@@
                "gubun1": " ", ## 구분1@@
                "traddate1": " ", ## 거래원날짜1@@
                "traddate2": " ", ## 거래원날짜2@@
                "cts_idx": "0", ## CTSIDX@@
                "cnt": "0##요청건수@@"
            }
        },
        "output": {
            "t1771OutBlock": {
                "cts_idx": "cts_idx`long##CTSIDX@@"
            },
            "t1771OutBlock2": {
                "traddate": "traddate`char", ## 날짜@@
                "tradtime": "tradtime`char", ## 시간@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 대비구분@@
                "change": "change`long", ## 대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 거래량@@
                "tradmdcha": "tradmdcha`long", ## 매도@@
                "tradmscha": "tradmscha`long", ## 매수@@
                "tradmdval": "tradmdval`long", ## 매도대금@@
                "tradmsval": "tradmsval`long", ## 매수대금@@
                "tradmsscha": "tradmsscha`long", ## 순매수@@
                "tradmttvolume": "tradmttvolume`long", ## 누적순매수@@
                "tradavg": "tradavg`long", ## 평균단가@@
                "tradmttavg": "tradmttavg`long##누적평균단가@@"
            }
        }
    },
    "t1809": { ## 신호조회(t1809)
        "input": {
            "t1809InBlock": {
                "gubun": " ", ## 신호구분@@
                "jmGb": " ", ## 종목구분@@
                "jmcode": " ", ## 종목코드@@
                "cts": " ##NEXTKEY@@"
            }
        },
        "output": {
            "t1809OutBlock": {
                "cts": "cts`char##NEXTKEY@@"
            },
            "t1809OutBlock1": {
                "date": "date`char", ## 일자@@
                "time": "time`char", ## 시간@@
                "signal_id": "signal_id`char", ## 신호ID@@
                "signal_desc": "signal_desc`char", ## 신호명@@
                "point": "point`char", ## 신호강도@@
                "keyword": "keyword`char", ## 뉴스신호키워드@@
                "seq": "seq`char", ## 신호별구분@@
                "gubun": "gubun`char", ## 신호구분@@
                "jmcode": "jmcode`char", ## 신호종목@@
                "price": "price`long", ## 종목가격@@
                "sign": "sign`char", ## 종목등락부호@@
                "chgrate": "chgrate`float", ## 대비등락율@@
                "volume": "volume`long", ## 거래량@@
                "datetime": "datetime`char##신호일시@@"
            }
        }
    },
    "t1825": { ## 종목Q클릭검색(씽큐스마트)(t1825)
        "input": {
            "t1825InBlock": {
                "search_cd": " ", ## 검색코드@@
                "gubun": " ##구분@@0:전체1:코스피2:코스닥"
            }
        },
        "output": {
            "t1825OutBlock": {
                "JongCnt": "JongCnt`long##검색종목수@@"
            },
            "t1825OutBlock1": {
                "shcode": "shcode`char", ## 종목코드@@
                "hname": "hname`char", ## 종목명@@
                "sign": "sign`char", ## 전일대비구분@@
                "signcnt": "signcnt`long", ## 연속봉수@@
                "close": "close`long", ## 현재가@@
                "change": "change`long", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 거래량@@
                "volumerate": "volumerate`float##거래량전일대비율@@"
            }
        }
    },
    "t1826": { ## 종목Q클릭검색리스트조회(씽큐스마트)(t1826)
        "input": {
            "t1826InBlock": {
                "search_gb": " ##검색구분@@0:핵심검색1:지표검색2:시세동향3:투자자동향"
            }
        },
        "output": {
            "t1826OutBlock": {
                "search_cd": "search_cd`char", ## 검색코드@@
                "search_nm": "search_nm`char##검색명@@"
            }
        }
    },
    "t1857": { ## e종목검색(신버전API용)
        "input": {
            "t1857InBlock": {
                "sRealFlag": " ", ## 실시간구분@@0:조회 1:실시간
                "sSearchFlag": " ", ## 종목검색구분@@F:파일 S:서버
                "query_index": " ##종목검색입력값@@"
            }
        },
        "output": {
            "t1857OutBlock": {
                "result_count": "result_count`long", ## 검색종목수@@
                "result_time": "result_time`char", ## 포착시간@@
                "AlertNum": "AlertNum`char##실시간키@@"
            },
            "t1857OutBlock1": {
                "shcode": "shcode`char", ## 종목코드@@
                "hname": "hname`char", ## 종목명@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 거래량@@
                "JobFlag": "JobFlag`char##종목상태@@N:진입 R:재진입 O:이탈"
            }
        }
    },
    "t1866": { ## 서버저장조건리스트조회(API)(t1866)
        "input": {
            "t1866InBlock": {
                "user_id": " ", ## 로그인ID@@
                "gb": " ", ## 조회구분@@
                "group_name": " ", ## 그룹명@@
                "cont": " ", ## 연속여부@@
                "contkey": " ##연속키@@"
            }
        },
        "output": {
            "t1866OutBlock": {
                "result_count": "result_count`long", ## 저장조건수@@
                "cont": "cont`char", ## 연속여부@@
                "contkey": "contkey`char##연속키@@"
            },
            "t1866OutBlock1": {
                "query_index": "query_index`char", ## 서버저장인덱스@@
                "group_name": "group_name`char", ## 그룹명@@
                "query_name": "query_name`char##조건저장명@@"
            }
        }
    },
    "t1901": { ## ETF현재가(시세)조회(t1901)
        "input": {
            "t1901InBlock": {
                "shcode": " ##단축코드@@"
            }
        },
        "output": {
            "t1901OutBlock": {
                "hname": "hname`char", ## 한글명@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`float", ## 누적거래량@@
                "recprice": "recprice`long", ## 기준가@@
                "avg": "avg`long", ## 가중평균@@
                "uplmtprice": "uplmtprice`long", ## 상한가@@
                "dnlmtprice": "dnlmtprice`long", ## 하한가@@
                "jnilvolume": "jnilvolume`float", ## 전일거래량@@
                "volumediff": "volumediff`long", ## 거래량차@@
                "open": "open`long", ## 시가@@
                "opentime": "opentime`char", ## 시가시간@@
                "high": "high`long", ## 고가@@
                "hightime": "hightime`char", ## 고가시간@@
                "low": "low`long", ## 저가@@
                "lowtime": "lowtime`char", ## 저가시간@@
                "high52w": "high52w`long", ## 52최고가@@
                "high52wdate": "high52wdate`char", ## 52최고가일@@
                "low52w": "low52w`long", ## 52최저가@@
                "low52wdate": "low52wdate`char", ## 52최저가일@@
                "exhratio": "exhratio`float", ## 소진율@@
                "flmtvol": "flmtvol`float", ## 외국인보유수량@@
                "per": "per`float", ## PER@@
                "listing": "listing`long", ## 상장주식수(천)@@
                "jkrate": "jkrate`long", ## 증거금율@@
                "vol": "vol`float", ## 회전율@@
                "shcode": "shcode`char", ## 단축코드@@
                "value": "value`long", ## 누적거래대금@@
                "highyear": "highyear`long", ## 연중최고가@@
                "highyeardate": "highyeardate`char", ## 연중최고일자@@
                "lowyear": "lowyear`long", ## 연중최저가@@
                "lowyeardate": "lowyeardate`char", ## 연중최저일자@@
                "upname": "upname`char", ## 업종명@@
                "upcode": "upcode`char", ## 업종코드@@
                "upprice": "upprice`float", ## 업종현재가@@
                "upsign": "upsign`char", ## 업종전일비구분@@
                "upchange": "upchange`float", ## 업종전일대비@@
                "updiff": "updiff`float", ## 업종등락율@@
                "futname": "futname`char", ## 선물최근월물명@@
                "futcode": "futcode`char", ## 선물최근월물코드@@
                "futprice": "futprice`float", ## 선물현재가@@
                "futsign": "futsign`char", ## 선물전일비구분@@
                "futchange": "futchange`float", ## 선물전일대비@@
                "futdiff": "futdiff`float", ## 선물등락율@@
                "nav": "nav`float", ## NAV@@
                "navsign": "navsign`char", ## NAV전일대비구분@@
                "navchange": "navchange`float", ## NAV전일대비@@
                "navdiff": "navdiff`float", ## NAV등락율@@
                "cocrate": "cocrate`float", ## 추적오차율@@
                "kasis": "kasis`float", ## 괴리율@@
                "subprice": "subprice`long", ## 대용가@@
                "offerno1": "offerno1`char", ## 매도증권사코드1@@
                "bidno1": "bidno1`char", ## 매수증권사코드1@@
                "dvol1": "dvol1`long", ## 총매도수량1@@
                "svol1": "svol1`long", ## 총매수수량1@@
                "dcha1": "dcha1`long", ## 매도증감1@@
                "scha1": "scha1`long", ## 매수증감1@@
                "ddiff1": "ddiff1`float", ## 매도비율1@@
                "sdiff1": "sdiff1`float", ## 매수비율1@@
                "offerno2": "offerno2`char", ## 매도증권사코드2@@
                "bidno2": "bidno2`char", ## 매수증권사코드2@@
                "dvol2": "dvol2`long", ## 총매도수량2@@
                "svol2": "svol2`long", ## 총매수수량2@@
                "dcha2": "dcha2`long", ## 매도증감2@@
                "scha2": "scha2`long", ## 매수증감2@@
                "ddiff2": "ddiff2`float", ## 매도비율2@@
                "sdiff2": "sdiff2`float", ## 매수비율2@@
                "offerno3": "offerno3`char", ## 매도증권사코드3@@
                "bidno3": "bidno3`char", ## 매수증권사코드3@@
                "dvol3": "dvol3`long", ## 총매도수량3@@
                "svol3": "svol3`long", ## 총매수수량3@@
                "dcha3": "dcha3`long", ## 매도증감3@@
                "scha3": "scha3`long", ## 매수증감3@@
                "ddiff3": "ddiff3`float", ## 매도비율3@@
                "sdiff3": "sdiff3`float", ## 매수비율3@@
                "offerno4": "offerno4`char", ## 매도증권사코드4@@
                "bidno4": "bidno4`char", ## 매수증권사코드4@@
                "dvol4": "dvol4`long", ## 총매도수량4@@
                "svol4": "svol4`long", ## 총매수수량4@@
                "dcha4": "dcha4`long", ## 매도증감4@@
                "scha4": "scha4`long", ## 매수증감4@@
                "ddiff4": "ddiff4`float", ## 매도비율4@@
                "sdiff4": "sdiff4`float", ## 매수비율4@@
                "offerno5": "offerno5`char", ## 매도증권사코드5@@
                "bidno5": "bidno5`char", ## 매수증권사코드5@@
                "dvol5": "dvol5`long", ## 총매도수량5@@
                "svol5": "svol5`long", ## 총매수수량5@@
                "dcha5": "dcha5`long", ## 매도증감5@@
                "scha5": "scha5`long", ## 매수증감5@@
                "ddiff5": "ddiff5`float", ## 매도비율5@@
                "sdiff5": "sdiff5`float", ## 매수비율5@@
                "fwdvl": "fwdvl`long", ## 외국계매도합계수량@@
                "ftradmdcha": "ftradmdcha`long", ## 외국계매도직전대비@@
                "ftradmddiff": "ftradmddiff`float", ## 외국계매도비율@@
                "fwsvl": "fwsvl`long", ## 외국계매수합계수량@@
                "ftradmscha": "ftradmscha`long", ## 외국계매수직전대비@@
                "ftradmsdiff": "ftradmsdiff`float", ## 외국계매수비율@@
                "upname2": "upname2`char", ## 참고지수명@@
                "upcode2": "upcode2`char", ## 참고지수코드@@
                "upprice2": "upprice2`float", ## 참고지수현재가@@
                "jnilnav": "jnilnav`float", ## 전일NAV@@
                "jnilnavsign": "jnilnavsign`char", ## 전일NAV전일대비구분@@
                "jnilnavchange": "jnilnavchange`float", ## 전일NAV전일대비@@
                "jnilnavdiff": "jnilnavdiff`float", ## 전일NAV등락율@@
                "etftotcap": "etftotcap`long", ## 순자산총액(억원)@@
                "spread": "spread`float", ## 스프레드@@
                "leverage": "leverage`long", ## 레버리지@@
                "taxgubun": "taxgubun`char", ## 과세구분@@
                "opcom_nmk": "opcom_nmk`char", ## 운용사@@
                "lp_nm1": "lp_nm1`char", ## LP1@@
                "lp_nm2": "lp_nm2`char", ## LP2@@
                "lp_nm3": "lp_nm3`char", ## LP3@@
                "lp_nm4": "lp_nm4`char", ## LP4@@
                "lp_nm5": "lp_nm5`char", ## LP5@@
                "etf_cp": "etf_cp`char", ## 복제방법@@
                "etf_kind": "etf_kind`char", ## 상품유형(Filler)@@
                "vi_gubun": "vi_gubun`char", ## VI발동해제@@
                "etn_kind_cd": "etn_kind_cd`char", ## ETN상품분류@@
                "lastymd": "lastymd`char", ## ETN만기일@@
                "payday": "payday`char", ## ETN지급일@@
                "lastdate": "lastdate`char", ## ETN최종거래일@@
                "issuernmk": "issuernmk`char", ## ETN발행시장참가자@@
                "last_sdate": "last_sdate`char", ## ETN만기상환가격결정시작일@@
                "last_edate": "last_edate`char", ## ETN만기상환가격결정종료일@@
                "lp_holdvol": "lp_holdvol`char", ## ETNLP보유수량@@
                "listdate": "listdate`char", ## 상장일@@
                "etp_gb": "etp_gb`char", ## ETP상품구분코드@@1:ETF(투자회사형)2:ETF(수익증권형)3:ETN4:손실제한ETN
                "etn_elback_yn": "etn_elback_yn`char", ## ETN조기상환가능여부@@ETN조기상환가능여부Y/N2017.03.27
                "settletype": "settletype`char", ## 최종결제@@01:현금02:실물03:현금+실물
                "idx_asset_class1": "idx_asset_class1`char", ## 지수자산분류코드(대분류)@@
                "ty_text": "ty_text`char##ETF/ETN투자유의@@"
            }
        }
    },
    "t1902": { ## ETF시간별추이(t1902)
        "input": {
            "t1902InBlock": {
                "shcode": " ", ## 단축코드@@
                "time": " ##시간@@"
            }
        },
        "output": {
            "t1902OutBlock": {
                "time": "time`char", ## 시간@@
                "hname": "hname`char", ## 종목명@@
                "upname": "upname`char##업종지수명@@"
            },
            "t1902OutBlock1": {
                "time": "time`char", ## 시간@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "volume": "volume`float", ## 누적거래량@@
                "navdiff": "navdiff`float", ## NAV대비@@
                "nav": "nav`float", ## NAV@@
                "navchange": "navchange`float", ## 전일대비@@
                "crate": "crate`float", ## 추적오차@@
                "grate": "grate`float", ## 괴리@@
                "jisu": "jisu`float", ## 지수@@
                "jichange": "jichange`float", ## 전일대비@@
                "jirate": "jirate`float##전일대비율@@"
            }
        }
    },
    "t1903": { ## ETF일별추이(t1903)
        "input": {
            "t1903InBlock": {
                "shcode": " ", ## 단축코드@@
                "date": " ##일자@@"
            }
        },
        "output": {
            "t1903OutBlock": {
                "date": "date`char", ## 일자@@
                "hname": "hname`char", ## 종목명@@
                "upname": "upname`char##업종지수명@@"
            },
            "t1903OutBlock1": {
                "date": "date`char", ## 일자@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "volume": "volume`float", ## 누적거래량@@
                "navdiff": "navdiff`float", ## NAV대비@@
                "nav": "nav`float", ## NAV@@
                "navchange": "navchange`float", ## 전일대비@@
                "crate": "crate`float", ## 추적오차@@
                "grate": "grate`float", ## 괴리@@
                "jisu": "jisu`float", ## 지수@@
                "jichange": "jichange`float", ## 전일대비@@
                "jirate": "jirate`float##전일대비율@@"
            }
        }
    },
    "t1904": { ## ETF구성종목조회(t1904)
        "input": {
            "t1904InBlock": {
                "shcode": " ", ## ETF단축코드@@
                "date": " ", ## PDF적용일자@@
                "sgb": " ##정렬기준@@1:평가금액2:증권수"
            }
        },
        "output": {
            "t1904OutBlock": {
                "chk_tday": "chk_tday`char", ## 당일구분@@
                "date": "date`char", ## PDF적용일자@@
                "price": "price`long", ## ETF현재가@@
                "sign": "sign`char", ## ETF전일대비구분@@
                "change": "change`long", ## ETF전일대비@@
                "diff": "diff`float", ## ETF등락율@@
                "volume": "volume`long", ## ETF누적거래량@@
                "nav": "nav`float", ## NAV@@
                "navsign": "navsign`char", ## NAV전일대비구분@@
                "navchange": "navchange`float", ## NAV전일대비@@
                "navdiff": "navdiff`float", ## NAV등락율@@
                "jnilnav": "jnilnav`float", ## 전일NAV@@
                "jnilnavsign": "jnilnavsign`char", ## 전일NAV전일대비구분@@
                "jnilnavchange": "jnilnavchange`float", ## 전일NAV전일대비@@
                "jnilnavdiff": "jnilnavdiff`float", ## 전일NAV등락율@@
                "upname": "upname`char", ## 업종명@@
                "upcode": "upcode`char", ## 업종코드@@
                "upprice": "upprice`float", ## 업종현재가@@
                "upsign": "upsign`char", ## 업종전일비구분@@
                "upchange": "upchange`float", ## 업종전일대비@@
                "updiff": "updiff`float", ## 업종등락율@@
                "futname": "futname`char", ## 선물최근월물명@@
                "futcode": "futcode`char", ## 선물최근월물코드@@
                "futprice": "futprice`float", ## 선물현재가@@
                "futsign": "futsign`char", ## 선물전일비구분@@
                "futchange": "futchange`float", ## 선물전일대비@@
                "futdiff": "futdiff`float", ## 선물등락율@@
                "upname2": "upname2`char", ## 참고지수명@@
                "upcode2": "upcode2`char", ## 참고지수코드@@
                "upprice2": "upprice2`float", ## 참고지수현재가@@
                "etftotcap": "etftotcap`long", ## 순자산총액@@단위:억
                "etfnum": "etfnum`long", ## 구성종목수@@
                "etfcunum": "etfcunum`long", ## CU주식수@@
                "cash": "cash`long", ## 현금@@
                "opcom_nmk": "opcom_nmk`char", ## 운용사명@@
                "tot_pval": "tot_pval`long", ## 전종목평가금액합@@
                "tot_sigatval": "tot_sigatval`long##전종목구성시가총액합@@"
            },
            "t1904OutBlock1": {
                "shcode": "shcode`char", ## 단축코드@@
                "hname": "hname`char", ## 한글명@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 누적거래량@@
                "value": "value`long", ## 거래대금(백만)@@
                "icux": "icux`long", ## 단위증권수(계약수/원화현금/USD현금/창고증권)@@
                "parprice": "parprice`long", ## 액면금액/설정현금액@@
                "pvalue": "pvalue`long", ## 평가금액@@
                "sigatvalue": "sigatvalue`long", ## 구성시가총액@@
                "profitdate": "profitdate`char", ## PDF적용일자@@
                "weight": "weight`float", ## 비중(평가금액)@@
                "diff2": "diff2`float##ETF종목과등락차@@"
            }
        }
    },
    "t1906": { ## ETFLP호가(t1906)
        "input": {
            "t1906InBlock": {
                "shcode": " ##단축코드@@"
            }
        },
        "output": {
            "t1906OutBlock": {
                "hname": "hname`char", ## 한글명@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 누적거래량@@
                "lp_offerrem1": "lp_offerrem1`long", ## LP매도호가수량1@@
                "lp_bidrem1": "lp_bidrem1`long", ## LP매수호가수량1@@
                "lp_offerrem2": "lp_offerrem2`long", ## LP매도호가수량2@@
                "lp_bidrem2": "lp_bidrem2`long", ## LP매수호가수량2@@
                "lp_offerrem3": "lp_offerrem3`long", ## LP매도호가수량3@@
                "lp_bidrem3": "lp_bidrem3`long", ## LP매수호가수량3@@
                "lp_offerrem4": "lp_offerrem4`long", ## LP매도호가수량4@@
                "lp_bidrem4": "lp_bidrem4`long", ## LP매수호가수량4@@
                "lp_offerrem5": "lp_offerrem5`long", ## LP매도호가수량5@@
                "lp_bidrem5": "lp_bidrem5`long", ## LP매수호가수량5@@
                "lp_offerrem6": "lp_offerrem6`long", ## LP매도호가수량6@@
                "lp_bidrem6": "lp_bidrem6`long", ## LP매수호가수량6@@
                "lp_offerrem7": "lp_offerrem7`long", ## LP매도호가수량7@@
                "lp_bidrem7": "lp_bidrem7`long", ## LP매수호가수량7@@
                "lp_offerrem8": "lp_offerrem8`long", ## LP매도호가수량8@@
                "lp_bidrem8": "lp_bidrem8`long", ## LP매수호가수량8@@
                "lp_offerrem9": "lp_offerrem9`long", ## LP매도호가수량9@@
                "lp_bidrem9": "lp_bidrem9`long", ## LP매수호가수량9@@
                "lp_offerrem10": "lp_offerrem10`long", ## LP매도호가수량10@@
                "lp_bidrem10": "lp_bidrem10`long", ## LP매수호가수량10@@
                "jnilclose": "jnilclose`long", ## 전일종가@@
                "offerho1": "offerho1`long", ## 매도호가1@@
                "bidho1": "bidho1`long", ## 매수호가1@@
                "offerrem1": "offerrem1`long", ## 매도호가수량1@@
                "bidrem1": "bidrem1`long", ## 매수호가수량1@@
                "preoffercha1": "preoffercha1`long", ## 직전매도대비수량1@@
                "prebidcha1": "prebidcha1`long", ## 직전매수대비수량1@@
                "offerho2": "offerho2`long", ## 매도호가2@@
                "bidho2": "bidho2`long", ## 매수호가2@@
                "offerrem2": "offerrem2`long", ## 매도호가수량2@@
                "bidrem2": "bidrem2`long", ## 매수호가수량2@@
                "preoffercha2": "preoffercha2`long", ## 직전매도대비수량2@@
                "prebidcha2": "prebidcha2`long", ## 직전매수대비수량2@@
                "offerho3": "offerho3`long", ## 매도호가3@@
                "bidho3": "bidho3`long", ## 매수호가3@@
                "offerrem3": "offerrem3`long", ## 매도호가수량3@@
                "bidrem3": "bidrem3`long", ## 매수호가수량3@@
                "preoffercha3": "preoffercha3`long", ## 직전매도대비수량3@@
                "prebidcha3": "prebidcha3`long", ## 직전매수대비수량3@@
                "offerho4": "offerho4`long", ## 매도호가4@@
                "bidho4": "bidho4`long", ## 매수호가4@@
                "offerrem4": "offerrem4`long", ## 매도호가수량4@@
                "bidrem4": "bidrem4`long", ## 매수호가수량4@@
                "preoffercha4": "preoffercha4`long", ## 직전매도대비수량4@@
                "prebidcha4": "prebidcha4`long", ## 직전매수대비수량4@@
                "offerho5": "offerho5`long", ## 매도호가5@@
                "bidho5": "bidho5`long", ## 매수호가5@@
                "offerrem5": "offerrem5`long", ## 매도호가수량5@@
                "bidrem5": "bidrem5`long", ## 매수호가수량5@@
                "preoffercha5": "preoffercha5`long", ## 직전매도대비수량5@@
                "prebidcha5": "prebidcha5`long", ## 직전매수대비수량5@@
                "offerho6": "offerho6`long", ## 매도호가6@@
                "bidho6": "bidho6`long", ## 매수호가6@@
                "offerrem6": "offerrem6`long", ## 매도호가수량6@@
                "bidrem6": "bidrem6`long", ## 매수호가수량6@@
                "preoffercha6": "preoffercha6`long", ## 직전매도대비수량6@@
                "prebidcha6": "prebidcha6`long", ## 직전매수대비수량6@@
                "offerho7": "offerho7`long", ## 매도호가7@@
                "bidho7": "bidho7`long", ## 매수호가7@@
                "offerrem7": "offerrem7`long", ## 매도호가수량7@@
                "bidrem7": "bidrem7`long", ## 매수호가수량7@@
                "preoffercha7": "preoffercha7`long", ## 직전매도대비수량7@@
                "prebidcha7": "prebidcha7`long", ## 직전매수대비수량7@@
                "offerho8": "offerho8`long", ## 매도호가8@@
                "bidho8": "bidho8`long", ## 매수호가8@@
                "offerrem8": "offerrem8`long", ## 매도호가수량8@@
                "bidrem8": "bidrem8`long", ## 매수호가수량8@@
                "preoffercha8": "preoffercha8`long", ## 직전매도대비수량8@@
                "prebidcha8": "prebidcha8`long", ## 직전매수대비수량8@@
                "offerho9": "offerho9`long", ## 매도호가9@@
                "bidho9": "bidho9`long", ## 매수호가9@@
                "offerrem9": "offerrem9`long", ## 매도호가수량9@@
                "bidrem9": "bidrem9`long", ## 매수호가수량9@@
                "preoffercha9": "preoffercha9`long", ## 직전매도대비수량9@@
                "prebidcha9": "prebidcha9`long", ## 직전매수대비수량9@@
                "offerho10": "offerho10`long", ## 매도호가10@@
                "bidho10": "bidho10`long", ## 매수호가10@@
                "offerrem10": "offerrem10`long", ## 매도호가수량10@@
                "bidrem10": "bidrem10`long", ## 매수호가수량10@@
                "preoffercha10": "preoffercha10`long", ## 직전매도대비수량10@@
                "prebidcha10": "prebidcha10`long", ## 직전매수대비수량10@@
                "offer": "offer`long", ## 매도호가수량합@@
                "bid": "bid`long", ## 매수호가수량합@@
                "preoffercha": "preoffercha`long", ## 직전매도대비수량합@@
                "prebidcha": "prebidcha`long", ## 직전매수대비수량합@@
                "hotime": "hotime`char", ## 수신시간@@
                "yeprice": "yeprice`long", ## 예상체결가격@@
                "yevolume": "yevolume`long", ## 예상체결수량@@
                "yesign": "yesign`char", ## 예상체결전일구분@@
                "yechange": "yechange`long", ## 예상체결전일대비@@
                "yediff": "yediff`float", ## 예상체결등락율@@
                "tmoffer": "tmoffer`long", ## 시간외매도잔량@@
                "tmbid": "tmbid`long", ## 시간외매수잔량@@
                "ho_status": "ho_status`char", ## 동시구분@@
                "shcode": "shcode`char", ## 단축코드@@
                "uplmtprice": "uplmtprice`long", ## 상한가@@
                "dnlmtprice": "dnlmtprice`long", ## 하한가@@
                "open": "open`long", ## 시가@@
                "high": "high`long", ## 고가@@
                "low": "low`long##저가@@"
            }
        }
    },
    "t1921": { ## 신용거래동향(t1921)
        "input": {
            "t1921InBlock": {
                "shcode": " ", ## 종목코드@@
                "gubun": " ", ## 융자대주구분@@
                "date": " ", ## 날짜@@
                "idx": "0##IDX@@"
            }
        },
        "output": {
            "t1921OutBlock": {
                "cnt": "cnt`long", ## CNT@@
                "date": "date`char", ## 날짜@@
                "idx": "idx`long##IDX@@"
            },
            "t1921OutBlock1": {
                "mmdate": "mmdate`char", ## 날짜@@
                "close": "close`long", ## 종가@@
                "sign": "sign`char", ## 전일대비구분@@
                "jchange": "jchange`long", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "nvolume": "nvolume`long", ## 신규@@
                "svolume": "svolume`long", ## 상환@@
                "jvolume": "jvolume`long", ## 잔고@@
                "price": "price`long", ## 금액@@
                "change": "change`long", ## 대비@@
                "gyrate": "gyrate`float", ## 공여율@@
                "jkrate": "jkrate`float", ## 잔고율@@
                "shcode": "shcode`char##종목코드@@"
            }
        }
    },
    "t1926": { ## 종목별신용정보(t1926)
        "input": {
            "t1926InBlock": {
                "shcode": " ##종목코드@@"
            }
        },
        "output": {
            "t1926OutBlock": {
                "ynvolume": "ynvolume`long", ## 융자신규수량@@
                "ysvolume": "ysvolume`long", ## 융자상환수량@@
                "yjvolume": "yjvolume`long", ## 융자잔고수량@@
                "yvchange": "yvchange`long", ## 융자수량대비@@
                "ygrate": "ygrate`float", ## 융자공여율@@
                "yjrate": "yjrate`float", ## 융자잔고율@@
                "ynprice": "ynprice`long", ## 융자신규금액@@
                "ysprice": "ysprice`long", ## 융자상환금액@@
                "yjprice": "yjprice`long", ## 융자잔고금액@@
                "yachange": "yachange`long", ## 융자금액대비@@
                "dnvolume": "dnvolume`long", ## 대주신규수량@@
                "dsvolume": "dsvolume`long", ## 대주상환수량@@
                "djvolume": "djvolume`long", ## 대주잔고수량@@
                "dvchange": "dvchange`long", ## 대주수량대비@@
                "dgrate": "dgrate`float", ## 대주공여율@@
                "djrate": "djrate`float", ## 대주잔고율@@
                "dnprice": "dnprice`long", ## 대주신규금액@@
                "dsprice": "dsprice`long", ## 대주상환금액@@
                "djprice": "djprice`long", ## 대주잔고금액@@
                "dachange": "dachange`long", ## 대주금액대비@@
                "mmdate": "mmdate`char", ## 결제일@@
                "close": "close`long", ## 결제일종가@@
                "volume": "volume`long", ## 결제일거래량@@
                "value": "value`long", ## 결제일거래대금@@
                "pr5days": "pr5days`float", ## 주가5일증가율@@
                "pr20days": "pr20days`float", ## 주가20일증가율@@
                "yj5days": "yj5days`float", ## 융자5일증가율@@
                "yj20days": "yj20days`float", ## 융자20일증가율@@
                "dj5days": "dj5days`float", ## 대주5일증가율@@
                "dj20days": "dj20days`float##대주20일증가율@@"
            }
        }
    },
    "t1927": { ## 공매도일별추이(t1927)
        "input": {
            "t1927InBlock": {
                "shcode": " ", ## 종목코드@@
                "date": " ", ## 일자@@
                "sdate": " ", ## 시작일자@@
                "edate": " ##종료일자@@"
            }
        },
        "output": {
            "t1927OutBlock": {
                "date": "date`char##일자CTS@@"
            },
            "t1927OutBlock1": {
                "date": "date`char", ## 일자@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 거래량@@
                "value": "value`long", ## 거래대금@@
                "gm_vo": "gm_vo`long", ## 공매도수량@@
                "gm_va": "gm_va`long", ## 공매도대금@@
                "gm_per": "gm_per`float", ## 공매도거래비중@@
                "gm_avg": "gm_avg`long", ## 평균공매도단가@@
                "gm_vo_sum": "gm_vo_sum`long", ## 누적공매도수량@@
                "gm_vo1": "gm_vo1`long", ## 업틱룰적용공매도수량@@
                "gm_va1": "gm_va1`long", ## 업틱룰적용공매도대금@@
                "gm_vo2": "gm_vo2`long", ## 업틱룰예외공매도수량@@
                "gm_va2": "gm_va2`long##업틱룰예외공매도대금@@"
            }
        }
    },
    "t1941": { ## 종목별대차거래일간추이(t1941)
        "input": {
            "t1941InBlock": {
                "shcode": " ", ## 종목코드@@
                "sdate": " ", ## 시작일자@@
                "edate": " ##종료일자@@"
            }
        },
        "output": {
            "t1941OutBlock1": {
                "date": "date`char", ## 일자@@
                "price": "price`long", ## 종가@@
                "sign": "sign`char", ## 대비구분@@
                "change": "change`long", ## 대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 거래량@@
                "upvolume": "upvolume`long", ## 당일체결@@
                "dnvolume": "dnvolume`long", ## 당일상환@@
                "tovolume": "tovolume`long", ## 당일잔고@@
                "tovalue": "tovalue`long", ## 잔고금액@@
                "shcode": "shcode`char", ## 종목코드@@
                "tovoldif": "tovoldif`long##대차증감@@"
            }
        }
    },
    "t1950": { ## ELW현재가(시세)조회(t1950)
        "input": {
            "t1950InBlock": {
                "shcode": " ##ELW단축코드@@"
            }
        },
        "output": {
            "t1950OutBlock": {
                "hname": "hname`char", ## 한글명@@
                "chetime": "chetime`char", ## 체결시간@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "cvolume": "cvolume`long", ## 체결량@@
                "volume": "volume`float", ## 누적거래량@@
                "recprice": "recprice`long", ## 기준가@@
                "avg": "avg`long", ## 가중평균@@
                "jnilvolume": "jnilvolume`float", ## 전일거래량@@
                "jvolume": "jvolume`float", ## 전일동시간거래량@@
                "jnilclose": "jnilclose`long", ## 전일종가@@
                "volumechg": "volumechg`float", ## 거래량차@@
                "volumediff": "volumediff`float", ## 거래량차등락율@@
                "open": "open`long", ## 시가@@
                "odiff": "odiff`float", ## 시가등락율@@
                "opentime": "opentime`char", ## 시가시간@@
                "high": "high`long", ## 고가@@
                "hdiff": "hdiff`float", ## 고가등락율@@
                "hightime": "hightime`char", ## 고가시간@@
                "low": "low`long", ## 저가@@
                "ldiff": "ldiff`float", ## 저가등락율@@
                "lowtime": "lowtime`char", ## 저가시간@@
                "high52w": "high52w`long", ## 52최고가@@
                "high52wdiff": "high52wdiff`float", ## 52최고가등락율@@
                "high52wdate": "high52wdate`char", ## 52최고가일@@
                "low52w": "low52w`long", ## 52최저가@@
                "low52wdiff": "low52wdiff`float", ## 52최저가등락율@@
                "low52wdate": "low52wdate`char", ## 52최저가일@@
                "exhratio": "exhratio`float", ## 소진율@@
                "listing": "listing`float", ## 상장주식수(천)@@
                "memedan": "memedan`char", ## 수량단위@@
                "vol": "vol`float", ## 회전율@@
                "parity": "parity`float", ## 패리티@@
                "berate": "berate`float", ## 손익분기@@
                "gearing": "gearing`float", ## 기어링@@
                "elwexec": "elwexec`float", ## 행사가@@
                "issueprice": "issueprice`long", ## 발행가@@
                "convrate": "convrate`float", ## 전환비율@@
                "lastdate": "lastdate`char", ## 최종거래일@@
                "capt": "capt`float", ## 자본지지@@
                "egearing": "egearing`float", ## e.기어링@@
                "premium": "premium`float", ## 프리미엄@@
                "spread": "spread`float", ## 스프레드@@
                "espread": "espread`float", ## 최대스프레드@@
                "theoryprice": "theoryprice`float", ## 이론가@@
                "impv": "impv`float", ## 내재변동성@@
                "moneyness": "moneyness`char", ## 상태@@
                "delt": "delt`float", ## 델타@@
                "gama": "gama`float", ## 감마@@
                "vega": "vega`float", ## 베가@@
                "ceta": "ceta`float", ## 쎄타@@
                "rhox": "rhox`float", ## 로@@
                "bjandatecnt": "bjandatecnt`long", ## 잔존일수@@
                "mmsdate": "mmsdate`char", ## 행사개시일@@
                "mmedate": "mmedate`char", ## 행사종료일@@
                "payday": "payday`char", ## 지급일@@
                "listdate": "listdate`char", ## 발행일@@
                "lpmem": "lpmem`char", ## LP회원사@@
                "lp_holdvol": "lp_holdvol`float", ## LP보유수량@@
                "bcode": "bcode`char", ## 기초자산코드@@
                "bgubun": "bgubun`char", ## 기초자산구분@@
                "bprice": "bprice`long", ## 기초자산현재가@@
                "bsign": "bsign`char", ## 기초자산전일비구분@@
                "bchange": "bchange`long", ## 기초자산전일비@@
                "bdiff": "bdiff`float", ## 기초자산등락율@@
                "bvolume": "bvolume`float", ## 기초자산거래량@@
                "info1": "info1`char", ## 락구분@@
                "info2": "info2`char", ## 관리/급등구분@@
                "info3": "info3`char", ## 정지/연장구분@@
                "info4": "info4`char", ## 투자/불성실구분@@
                "janginfo": "janginfo`char", ## 장구분@@
                "basketgb": "basketgb`char", ## 바스켓구분@@
                "basketcnt": "basketcnt`long", ## 바스켓갯수@@
                "elwtype": "elwtype`char", ## ELW권리행사방식@@
                "settletype": "settletype`char", ## ELW결제방법@@
                "lpord": "lpord`char", ## LP사주문가능여부@@
                "elwdetail": "elwdetail`char", ## 권리내용@@
                "valuation": "valuation`char##만기평가가격방식@@"
            },
            "t1950OutBlock1": {
                "bskcode": "bskcode`char", ## 기초자산코드@@
                "bskbno": "bskbno`long", ## 기초자산비율@@
                "bskprice": "bskprice`long", ## 기초자산현재가@@
                "bsksign": "bsksign`char", ## 기초자산전일비구분@@
                "bskchange": "bskchange`long", ## 기초자산전일비@@
                "bskdiff": "bskdiff`float", ## 기초자산등락율@@
                "bskvolume": "bskvolume`float", ## 기초자산거래량@@
                "bskjnilclose": "bskjnilclose`long##기초자산전일종가@@"
            }
        }
    },
    "t1951": { ## ELW시간대별체결조회(t1951)
        "input": {
            "t1951InBlock": {
                "shcode": " ", ## 단축코드@@
                "cvolume": "0", ## 특이거래량@@
                "starttime": " ", ## 시작시간@@
                "endtime": " ", ## 종료시간@@
                "cts_time": " ##시간CTS@@"
            }
        },
        "output": {
            "t1951OutBlock": {
                "cts_time": "cts_time`char##시간CTS@@"
            },
            "t1951OutBlock1": {
                "chetime": "chetime`char", ## 시간@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "cvolume": "cvolume`long", ## 체결수량@@
                "chdegree": "chdegree`float", ## 체결강도@@
                "volume": "volume`long", ## 거래량@@
                "mdvolume": "mdvolume`long", ## 매도체결수량@@
                "mdchecnt": "mdchecnt`long", ## 매도체결건수@@
                "msvolume": "msvolume`long", ## 매수체결수량@@
                "mschecnt": "mschecnt`long", ## 매수체결건수@@
                "revolume": "revolume`long", ## 순체결량@@
                "rechecnt": "rechecnt`long##순체결건수@@"
            }
        }
    },
    "t1954": { ## ELW일별주가(t1954)
        "input": {
            "t1954InBlock": {
                "shcode": " ", ## 단축코드@@
                "date": " ", ## 날짜@@
                "cnt": "0##건수@@"
            }
        },
        "output": {
            "t1954OutBlock": {
                "date": "date`char", ## 날짜@@
                "bsjgubun": "bsjgubun`char", ## 기초자산구분@@
                "bscode": "bscode`char", ## 기초자산코드(현물)@@
                "bjcode": "bjcode`char##기초자산코드(지수)@@"
            },
            "t1954OutBlock1": {
                "date": "date`char", ## 날짜@@
                "open": "open`long", ## 시가@@
                "high": "high`long", ## 고가@@
                "low": "low`long", ## 저가@@
                "close": "close`long", ## 종가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`float", ## 거래량@@
                "bsprice": "bsprice`long", ## 기초자산(현물)@@
                "bjprice": "bjprice`float", ## 기초자산(지수)@@
                "bsign": "bsign`char", ## 전일대비구분@@
                "bschange": "bschange`long", ## 전일대비(현물)@@
                "bjchange": "bjchange`float", ## 전일대비(지수)@@
                "bdiff": "bdiff`float", ## 등락율@@
                "bvolume": "bvolume`float", ## 기초자산거래량@@
                "parity": "parity`float", ## 패리티@@
                "egearing": "egearing`float", ## e.기어링@@
                "premium": "premium`float", ## 프리미엄@@
                "berate": "berate`float", ## 손익분기@@
                "capt": "capt`float", ## 자본지지@@
                "gearing": "gearing`float", ## 기어링@@
                "mness": "mness`char##Moneyness@@"
            }
        }
    },
    "t1955": { ## ELW지표검색(t1955)
        "input": {
            "t1955InBlock": {
                "chkitem": " ", ## 기초자산chk구분@@
                "cbitem": " ", ## 기초자산코드@@
                "chkissuer": " ", ## 발행사chk구분@@
                "cbissuer": " ", ## 발행사@@
                "chkcallput": " ", ## 권리chk구분@@
                "cbcallput": " ", ## 권리@@call:01.put:02
                "chkexec": " ", ## 행사가chk구분@@
                "cbexec": " ", ## 행사가@@>=:1.<=:2
                "chktype": " ", ## 행사방식chk구분@@
                "cbtype": " ", ## 행사방식@@
                "chksettle": " ", ## 결제방법chk구분@@
                "cbsettle": " ", ## 결제방법@@
                "chklast": " ", ## 만기chk구분@@
                "cblast": " ", ## 만기월별@@
                "chkelwexec": " ", ## 행사가격chk구분@@
                "elwexecs": "0.0", ## 행사가이상@@
                "elwexece": "0.0", ## 행사가이하@@
                "chkvolume": " ", ## 거래량chk구분@@
                "volumes": "0.0", ## 거래량이상@@
                "volumee": "0.0", ## 거래량이하@@
                "chkrate": " ", ## 등락율chk구분@@
                "rates": "0.0", ## 등락율이상@@
                "ratee": "0.0", ## 등락율이하@@
                "chkpremium": " ", ## 프리미엄chk구분@@
                "premiums": "0.0", ## 프리미엄이상@@
                "premiume": "0.0", ## 프리미엄이하@@
                "chkparity": " ", ## 패리티chk구분@@
                "paritys": "0.0", ## 패리티이상@@
                "paritye": "0.0", ## 패리티이하@@
                "chkberate": " ", ## 손익분기chk구분@@
                "berates": "0.0", ## 손익분기이상@@
                "beratee": "0.0", ## 손익분기이하@@
                "chkcapt": " ", ## 자본지지chk구분@@
                "capts": "0.0", ## 자본지지이상@@
                "capte": "0.0", ## 자본지지이하@@
                "chkegearing": " ", ## e.기어링chk구분@@
                "egearings": "0.0", ## e.기어링이상@@
                "egearinge": "0.0", ## e.기어링이하@@
                "chkgearing": " ", ## 기어링chk구분@@
                "gearings": "0.0", ## 기어링이상@@
                "gearinge": "0.0", ## 기어링이하@@
                "chkdelta": " ", ## 델타chk구분@@
                "deltas": "0.0", ## 델타이상@@
                "deltae": "0.0", ## 델타이하@@
                "chktheta": " ", ## 쎄타chk구분@@
                "thetas": "0.0", ## 쎄타이상@@
                "thetae": "0.0", ## 쎄타이하@@
                "chkduedate": " ", ## 최종거래일chk구분@@
                "duedates": " ", ## 최종거래일이상@@
                "duedatee": " ", ## 최종거래일이하@@
                "chkkoba": " ", ## 조기종료chk구분@@
                "cbkoba": " ##조기종료@@0:전체1:조기종료만2:조기종료제외"
            }
        },
        "output": {
            "t1955OutBlock": {
                "cnt": "cnt`long##종목갯수@@"
            },
            "t1955OutBlock1": {
                "hname": "hname`char", ## 종목명@@
                "shcode": "shcode`char", ## 종목코드@@
                "issuernmk": "issuernmk`char", ## 발행사@@
                "itemcode": "itemcode`char", ## 기초자산코드@@
                "cpgubun": "cpgubun`char", ## 콜/풋구분@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`float", ## 거래량@@
                "jnilvolume": "jnilvolume`float", ## 전일거래량@@
                "elwexec": "elwexec`float", ## 행사가@@
                "item": "item`char", ## 기초자산명@@
                "bprice": "bprice`float", ## 기초자산가@@
                "bsign": "bsign`char", ## 기초전일대비구분@@
                "bchange": "bchange`float", ## 기초전일대비@@
                "bdiff": "bdiff`float", ## 기초등락율@@
                "premium": "premium`float", ## 프리미엄@@
                "parity": "parity`float", ## 패리티@@
                "berate": "berate`float", ## 손익분기@@
                "capt": "capt`float", ## 자본지지@@
                "egearing": "egearing`float", ## e.기어링@@
                "gearing": "gearing`float", ## 기어링@@
                "lastdate": "lastdate`char", ## 최종거래일@@
                "delta": "delta`float", ## 델타@@
                "theta": "theta`float##쎄타@@"
            }
        }
    },
    "t1956": { ## ELW현재가(확정지급액)조회(t1956)
        "input": {
            "t1956InBlock": {
                "shcode": " ##단축코드@@"
            }
        },
        "output": {
            "t1956OutBlock": {
                "hname": "hname`char", ## 한글명@@
                "chetime": "chetime`char", ## 체결시간@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "cvolume": "cvolume`long", ## 체결량@@
                "volume": "volume`float", ## 누적거래량@@
                "recprice": "recprice`long", ## 기준가@@
                "avg": "avg`long", ## 가중평균@@
                "jnilvolume": "jnilvolume`float", ## 전일거래량@@
                "jvolume": "jvolume`float", ## 전일동시간거래량@@
                "jnilclose": "jnilclose`long", ## 전일종가@@
                "volumechg": "volumechg`float", ## 거래량차@@
                "volumediff": "volumediff`float", ## 거래량차등락율@@
                "open": "open`long", ## 시가@@
                "odiff": "odiff`float", ## 시가등락율@@
                "opentime": "opentime`char", ## 시가시간@@
                "high": "high`long", ## 고가@@
                "hdiff": "hdiff`float", ## 고가등락율@@
                "hightime": "hightime`char", ## 고가시간@@
                "low": "low`long", ## 저가@@
                "ldiff": "ldiff`float", ## 저가등락율@@
                "lowtime": "lowtime`char", ## 저가시간@@
                "high52w": "high52w`long", ## 52최고가@@
                "high52wdiff": "high52wdiff`float", ## 52최고가등락율@@
                "high52wdate": "high52wdate`char", ## 52최고가일@@
                "low52w": "low52w`long", ## 52최저가@@
                "low52wdiff": "low52wdiff`float", ## 52최저가등락율@@
                "low52wdate": "low52wdate`char", ## 52최저가일@@
                "exhratio": "exhratio`float", ## 소진율@@
                "listing": "listing`float", ## 상장주식수(천)@@
                "memedan": "memedan`char", ## 수량단위@@
                "vol": "vol`float", ## 회전율@@
                "parity": "parity`float", ## 패리티@@
                "berate": "berate`float", ## 손익분기@@
                "gearing": "gearing`float", ## 기어링@@
                "elwexec": "elwexec`float", ## 행사가@@
                "issueprice": "issueprice`long", ## 발행가@@
                "convrate": "convrate`float", ## 전환비율@@
                "lastdate": "lastdate`char", ## 최종거래일@@
                "capt": "capt`float", ## 자본지지@@
                "egearing": "egearing`float", ## e.기어링@@
                "premium": "premium`float", ## 프리미엄@@
                "spread": "spread`float", ## 스프레드@@
                "espread": "espread`float", ## 최대스프레드@@
                "theoryprice": "theoryprice`float", ## 이론가@@
                "impv": "impv`float", ## 내재변동성@@
                "moneyness": "moneyness`char", ## 상태@@
                "delt": "delt`float", ## 델타@@
                "gama": "gama`float", ## 감마@@
                "vega": "vega`float", ## 베가@@
                "ceta": "ceta`float", ## 쎄타@@
                "rhox": "rhox`float", ## 로@@
                "bjandatecnt": "bjandatecnt`long", ## 잔존일수@@
                "mmsdate": "mmsdate`char", ## 행사개시일@@
                "mmedate": "mmedate`char", ## 행사종료일@@
                "payday": "payday`char", ## 지급일@@
                "listdate": "listdate`char", ## 발행일@@
                "lpmem": "lpmem`char", ## LP회원사@@
                "lp_holdvol": "lp_holdvol`float", ## LP보유수량@@
                "bcode": "bcode`char", ## 기초자산코드@@
                "bgubun": "bgubun`char", ## 기초자산구분@@
                "bprice": "bprice`long", ## 기초자산현재가@@
                "bsign": "bsign`char", ## 기초자산전일비구분@@
                "bchange": "bchange`long", ## 기초자산전일비@@
                "bdiff": "bdiff`float", ## 기초자산등락율@@
                "bvolume": "bvolume`float", ## 기초자산거래량@@
                "info1": "info1`char", ## 락구분@@
                "info2": "info2`char", ## 관리/급등구분@@
                "info3": "info3`char", ## 정지/연장구분@@
                "info4": "info4`char", ## 투자/불성실구분@@
                "janginfo": "janginfo`char", ## 장구분@@
                "basketgb": "basketgb`char", ## 바스켓구분@@
                "basketcnt": "basketcnt`long", ## 바스켓갯수@@
                "elwtype": "elwtype`char", ## ELW권리행사방식@@
                "settletype": "settletype`char", ## ELW결제방법@@
                "lpord": "lpord`char", ## LP사주문가능여부@@
                "elwdetail": "elwdetail`char", ## 권리내용@@
                "valuation": "valuation`char", ## 만기평가가격방식@@
                "givemoney": "givemoney`float##확정지급액@@"
            },
            "t1956OutBlock1": {
                "bskcode": "bskcode`char", ## 기초자산코드@@
                "bskbno": "bskbno`long", ## 기초자산비율@@
                "bskprice": "bskprice`long", ## 기초자산현재가@@
                "bsksign": "bsksign`char", ## 기초자산전일비구분@@
                "bskchange": "bskchange`long", ## 기초자산전일비@@
                "bskdiff": "bskdiff`float", ## 기초자산등락율@@
                "bskvolume": "bskvolume`float", ## 기초자산거래량@@
                "bskjnilclose": "bskjnilclose`long##기초자산전일종가@@"
            }
        }
    },
    "t1958": { ## ELW종목비교(t1958)
        "input": {
            "t1958InBlock": {
                "shcode1": " ", ## 종목코드1@@
                "shcode2": " ##종목코드2@@"
            }
        },
        "output": {
            "t1958OutBlock": {
                "hname": "hname`char", ## 종목명@@
                "item1": "item1`char", ## 기초자산@@
                "issuernmk": "issuernmk`char", ## 발행사@@
                "elwopt": "elwopt`char", ## 콜풋구분@@
                "elwtype": "elwtype`char", ## 행사방식@@
                "settletype": "settletype`char", ## 결제방법@@
                "elwexec": "elwexec`float", ## 행사가@@
                "convrate": "convrate`float", ## 전환비율@@
                "listing": "listing`float", ## 발행수량@@
                "mmsdate": "mmsdate`char", ## 행사개시일@@
                "lastdate": "lastdate`char", ## 최종거래일@@
                "nofdays": "nofdays`long", ## 거래잔존일수@@
                "payday": "payday`char", ## 지급일@@
                "parity": "parity`float", ## 패리티@@
                "premium": "premium`float", ## 프리미엄@@
                "berate": "berate`float", ## 손익분기@@
                "capt": "capt`float", ## 자본지지@@
                "gearing": "gearing`float", ## 기어링@@
                "egearing": "egearing`float", ## e.기어링@@
                "price": "price`long", ## 가격@@
                "volume": "volume`float", ## 거래량@@
                "diff": "diff`float##등락율@@"
            },
            "t1958OutBlock1": {
                "hname": "hname`char", ## 종목명@@
                "item1": "item1`char", ## 기초자산@@
                "issuernmk": "issuernmk`char", ## 발행사@@
                "elwopt": "elwopt`char", ## 콜풋구분@@
                "elwtype": "elwtype`char", ## 행사방식@@
                "settletype": "settletype`char", ## 결제방법@@
                "elwexec": "elwexec`float", ## 행사가@@
                "convrate": "convrate`float", ## 전환비율@@
                "listing": "listing`float", ## 발행수량@@
                "mmsdate": "mmsdate`char", ## 행사개시일@@
                "lastdate": "lastdate`char", ## 최종거래일@@
                "nofdays": "nofdays`long", ## 거래잔존일수@@
                "payday": "payday`char", ## 지급일@@
                "parity": "parity`float", ## 패리티@@
                "premium": "premium`float", ## 프리미엄@@
                "berate": "berate`float", ## 손익분기@@
                "capt": "capt`float", ## 자본지지@@
                "gearing": "gearing`float", ## 기어링@@
                "egearing": "egearing`float", ## e.기어링@@
                "price": "price`long", ## 가격@@
                "volume": "volume`float", ## 거래량@@
                "diff": "diff`float##등락율@@"
            },
            "t1958OutBlock2": {
                "hnamecmp": "hnamecmp`char", ## 종목명비교@@
                "item1cmp": "item1cmp`char", ## 기초자산비교@@
                "issuernmkcmp": "issuernmkcmp`char", ## 발행사비교@@
                "elwoptcmp": "elwoptcmp`char", ## 콜풋구분비교@@
                "elwtypecmp": "elwtypecmp`char", ## 행사방식비교@@
                "settlecmp": "settlecmp`char", ## 결제방법비교@@
                "elwexeccmp": "elwexeccmp`float", ## 행사가비교@@
                "convcmp": "convcmp`float", ## 전환비율비교@@
                "listingcmp": "listingcmp`float", ## 발행수량비교@@
                "mmsdatecmp": "mmsdatecmp`char", ## 행사개시일비교@@
                "lastdatecmp": "lastdatecmp`char", ## 최종거래일비교@@
                "nofdayscmp": "nofdayscmp`char", ## 거래잔존일수비교@@
                "paydaycmp": "paydaycmp`char", ## 지급일비교@@
                "paritycmp": "paritycmp`float", ## 패리티비교@@
                "premiumcmp": "premiumcmp`float", ## 프리미엄비교@@
                "beratecmp": "beratecmp`float", ## 손익분기비교@@
                "captcmp": "captcmp`float", ## 자본지지비교@@
                "gearingcmp": "gearingcmp`float", ## 기어링비교@@
                "egearingcmp": "egearingcmp`float", ## e.기어링비교@@
                "pricecmp": "pricecmp`long", ## 가격비교@@
                "volumecmp": "volumecmp`float", ## 거래량비교@@
                "diffcmp": "diffcmp`float##등락율비교@@"
            }
        }
    },
    "t1959": { ## LP대상종목정보조회(t1959)
        "input": {
            "t1959InBlock": {
                "shcode": " ##종목코드@@"
            }
        },
        "output": {
            "t1959OutBlock1": {
                "shcode": "shcode`char", ## 종목코드@@
                "hname": "hname`char", ## 종목명@@
                "price": "price`char", ## 현재가@@
                "sign": "sign`char", ## 부호@@
                "change": "change`char", ## 대비@@
                "rate": "rate`float", ## 등락율@@
                "volume": "volume`char", ## 누적거래량@@
                "value": "value`char", ## 누적거래대금@@
                "lp_gb": "lp_gb`char", ## LP주문가능여부@@
                "lp_mem_nm1": "lp_mem_nm1`char", ## LP회원사명1@@
                "lp_mem_nm2": "lp_mem_nm2`char", ## LP회원사명2@@
                "lp_mem_nm3": "lp_mem_nm3`char", ## LP회원사명3@@
                "lp_mem_nm4": "lp_mem_nm4`char", ## LP회원사명4@@
                "lp_mem_nm5": "lp_mem_nm5`char", ## LP회원사명5@@
                "lp_min_qty": "lp_min_qty`char", ## LP최소호가수량@@
                "lp_st_date": "lp_st_date`char", ## LP시작일@@
                "lp_end_date": "lp_end_date`char", ## LP종료일@@
                "lp_spread": "lp_spread`float##LP스프레드@@"
            }
        }
    },
    "t1960": { ## ELW등락율상위(t1960)
        "input": {
            "t1960InBlock": {
                "gubun": " ", ## 상승하락@@0:상승1:하락
                "ggubun": " ", ## 권리유형구분@@00:EX01:콜02:풋'':전체
                "itemcode": " ", ## 기초자산종목@@
                "lastdate": " ", ## 조회만기일@@
                "exgubun": " ", ## 대상제외@@
                "sprice": "0", ## 시작가격@@
                "eprice": "0", ## 종료가격@@
                "volume": "0", ## 거래량@@
                "sjanday": "0", ## 잔존시작일수@@
                "ejanday": "0", ## 잔존종료일수@@
                "idx": "0##IDX@@"
            }
        },
        "output": {
            "t1960OutBlock": {
                "idx": "idx`long##IDX@@"
            },
            "t1960OutBlock1": {
                "hname": "hname`char", ## 한글명@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`double", ## 누적거래량@@
                "elwexec": "elwexec`double", ## 행사가@@
                "convrate": "convrate`double", ## 전환비율@@
                "lastdate": "lastdate`char", ## 만기일@@
                "itemcode": "itemcode`char", ## 기초자산종목코드@@
                "itemshcode": "itemshcode`char", ## 기초자산단축코드@@
                "itemname": "itemname`char", ## 기초자산종목명@@
                "itemprice": "itemprice`char", ## 기초자산현재가@@
                "itemsign": "itemsign`char", ## 기초자산대비구분@@
                "itemchange": "itemchange`char", ## 기초자산전일대비@@
                "itemdiff": "itemdiff`double", ## 기초자산등락율@@
                "elwshcode": "elwshcode`char", ## ELW종목코드@@
                "bepoint": "bepoint`double##손익분기점@@"
            }
        }
    },
    "t1961": { ## ELW거래량상위(t1961)
        "input": {
            "t1961InBlock": {
                "gubun": " ", ## 당일전일@@0:당일1:전일
                "ggubun": " ", ## 권리유형구분@@00:EX01:콜02:풋'':전체
                "itemcode": " ", ## 기초자산종목@@
                "lastdate": " ", ## 조회만기일@@
                "exgubun": " ", ## 대상제외@@
                "sprice": "0", ## 시작가격@@
                "eprice": "0", ## 종료가격@@
                "volume": "0", ## 거래량@@
                "sjanday": "0", ## 잔존시작일수@@
                "ejanday": "0", ## 잔존종료일수@@
                "idx": "0##IDX@@"
            }
        },
        "output": {
            "t1961OutBlock": {
                "idx": "idx`long##IDX@@"
            },
            "t1961OutBlock1": {
                "hname": "hname`char", ## 한글명@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`double", ## 누적거래량@@
                "jnilvolume": "jnilvolume`double", ## 전일거래량@@
                "elwexec": "elwexec`double", ## 행사가@@
                "convrate": "convrate`double", ## 전환비율@@
                "lastdate": "lastdate`char", ## 만기일@@
                "itemcode": "itemcode`char", ## 기초자산종목코드@@
                "itemshcode": "itemshcode`char", ## 기초자산단축코드@@
                "itemname": "itemname`char", ## 기초자산종목명@@
                "itemprice": "itemprice`char", ## 기초자산현재가@@
                "itemsign": "itemsign`char", ## 기초자산대비구분@@
                "itemchange": "itemchange`char", ## 기초자산전일대비@@
                "itemdiff": "itemdiff`double", ## 기초자산등락율@@
                "elwshcode": "elwshcode`char##ELW종목코드@@"
            }
        }
    },
    "t1964": { ## ELW전광판(t1964)
        "input": {
            "t1964InBlock": {
                "item": " ", ## 기초자산코드@@
                "issuercd": " ", ## 발행사@@
                "lastmonth": " ", ## 만기월물@@
                "elwopt": " ", ## 콜풋구분@@
                "atmgubun": " ", ## 머니구분@@
                "elwtype": " ", ## 권리행사방식@@
                "settletype": " ", ## 결제방법@@
                "elwexecgubun": " ", ## 행사기초자산구분@@
                "fromrat": " ", ## 시작비율@@
                "torat": " ", ## 종료비율@@
                "volume": " ##거래량@@"
            }
        },
        "output": {
            "t1964OutBlock1": {
                "shcode": "shcode`char", ## ELW코드@@
                "hname": "hname`char", ## 종목명@@
                "item1": "item1`char", ## 기초자산코드@@
                "itemnm": "itemnm`char", ## 기초자산명@@
                "issuernmk": "issuernmk`char", ## 발행사@@
                "elwopt": "elwopt`char", ## 콜풋구분@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 거래량@@
                "elwexec": "elwexec`float", ## 행사가@@
                "jandatecnt": "jandatecnt`long", ## 잔존일수@@
                "convrate": "convrate`float", ## 전환비율@@
                "lastdate": "lastdate`char", ## 최종거래일@@
                "mmsdate": "mmsdate`char", ## 행사개시일@@
                "payday": "payday`char", ## 지급일@@
                "listing": "listing`long", ## 발행수량@@
                "atmgbnm": "atmgbnm`char", ## 머니구분@@
                "parity": "parity`float", ## 패리티@@
                "preminum": "preminum`float", ## 프리미엄@@
                "spread": "spread`float", ## 스프래드@@
                "berate": "berate`float", ## 손익분기율@@
                "capt": "capt`float", ## 자본지지율@@
                "gearing": "gearing`float", ## 기어링@@
                "egearing": "egearing`float", ## e기어링@@
                "itemprice": "itemprice`long", ## 기초자산현재가@@
                "itemsign": "itemsign`char", ## 기초자산전일대비구분@@
                "itemchange": "itemchange`long", ## 기초자산전일대비@@
                "itemdiff": "itemdiff`float", ## 기초자산등락율@@
                "itemvolume": "itemvolume`long", ## 기초자산거래량@@
                "jnilvolume": "jnilvolume`long", ## 전일거래량@@
                "theoryprice": "theoryprice`float", ## 이론가@@
                "lp_rate": "lp_rate`float", ## LP보유비율@@
                "impv": "impv`float", ## 내재변동성@@
                "delta": "delta`float", ## 델타@@
                "theta": "theta`float##쎄타@@"
            }
        }
    },
    "t1966": { ## ELW거래대금상위(t1966)
        "input": {
            "t1966InBlock": {
                "gubun": " ", ## 당일전일@@0:당일1:전일
                "ggubun": " ", ## 권리유형구분@@00:EX01:콜02:풋'':전체
                "itemcode": " ", ## 기초자산종목@@
                "lastdate": " ", ## 조회만기일@@
                "exgubun": " ", ## 대상제외@@
                "sprice": "0", ## 시작가격@@
                "eprice": "0", ## 종료가격@@
                "volume": "0", ## 거래량@@
                "sjanday": "0", ## 잔존시작일수@@
                "ejanday": "0", ## 잔존종료일수@@
                "idx": "0##IDX@@"
            }
        },
        "output": {
            "t1966OutBlock": {
                "idx": "idx`long##IDX@@"
            },
            "t1966OutBlock1": {
                "hname": "hname`char", ## 한글명@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "value": "value`double", ## 누적거래대금@@
                "jnilvalue": "jnilvalue`double", ## 전일거래대금@@
                "elwexec": "elwexec`double", ## 행사가@@
                "convrate": "convrate`double", ## 전환비율@@
                "lastdate": "lastdate`char", ## 만기일@@
                "itemcode": "itemcode`char", ## 기초자산종목코드@@
                "itemshcode": "itemshcode`char", ## 기초자산단축코드@@
                "itemname": "itemname`char", ## 기초자산종목명@@
                "itemprice": "itemprice`char", ## 기초자산현재가@@
                "itemsign": "itemsign`char", ## 기초자산대비구분@@
                "itemchange": "itemchange`char", ## 기초자산전일대비@@
                "itemdiff": "itemdiff`double", ## 기초자산등락율@@
                "elwshcode": "elwshcode`char##ELW종목코드@@"
            }
        }
    },
    "t1971": { ## ELW현재가호가조회(t1971)
        "input": {
            "t1971InBlock": {
                "shcode": " ##단축코드@@"
            }
        },
        "output": {
            "t1971OutBlock": {
                "hname": "hname`char", ## 한글명@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`float", ## 누적거래량@@
                "jnilclose": "jnilclose`long", ## 전일종가@@
                "offerho1": "offerho1`long", ## 매도호가1@@
                "bidho1": "bidho1`long", ## 매수호가1@@
                "offerrem1": "offerrem1`long", ## 매도호가수량1@@
                "lp_offerrem1": "lp_offerrem1`long", ## LP매도호가수량1@@
                "bidrem1": "bidrem1`long", ## 매수호가수량1@@
                "lp_bidrem1": "lp_bidrem1`long", ## LP매수호가수량1@@
                "preoffercha1": "preoffercha1`long", ## 직전매도대비수량1@@
                "prebidcha1": "prebidcha1`long", ## 직전매수대비수량1@@
                "offerho2": "offerho2`long", ## 매도호가2@@
                "bidho2": "bidho2`long", ## 매수호가2@@
                "offerrem2": "offerrem2`long", ## 매도호가수량2@@
                "lp_offerrem2": "lp_offerrem2`long", ## LP매도호가수량2@@
                "bidrem2": "bidrem2`long", ## 매수호가수량2@@
                "lp_bidrem2": "lp_bidrem2`long", ## LP매수호가수량2@@
                "preoffercha2": "preoffercha2`long", ## 직전매도대비수량2@@
                "prebidcha2": "prebidcha2`long", ## 직전매수대비수량2@@
                "offerho3": "offerho3`long", ## 매도호가3@@
                "bidho3": "bidho3`long", ## 매수호가3@@
                "offerrem3": "offerrem3`long", ## 매도호가수량3@@
                "lp_offerrem3": "lp_offerrem3`long", ## LP매도호가수량3@@
                "bidrem3": "bidrem3`long", ## 매수호가수량3@@
                "lp_bidrem3": "lp_bidrem3`long", ## LP매수호가수량3@@
                "preoffercha3": "preoffercha3`long", ## 직전매도대비수량3@@
                "prebidcha3": "prebidcha3`long", ## 직전매수대비수량3@@
                "offerho4": "offerho4`long", ## 매도호가4@@
                "bidho4": "bidho4`long", ## 매수호가4@@
                "offerrem4": "offerrem4`long", ## 매도호가수량4@@
                "lp_offerrem4": "lp_offerrem4`long", ## LP매도호가수량4@@
                "bidrem4": "bidrem4`long", ## 매수호가수량4@@
                "lp_bidrem4": "lp_bidrem4`long", ## LP매수호가수량4@@
                "preoffercha4": "preoffercha4`long", ## 직전매도대비수량4@@
                "prebidcha4": "prebidcha4`long", ## 직전매수대비수량4@@
                "offerho5": "offerho5`long", ## 매도호가5@@
                "bidho5": "bidho5`long", ## 매수호가5@@
                "offerrem5": "offerrem5`long", ## 매도호가수량5@@
                "lp_offerrem5": "lp_offerrem5`long", ## LP매도호가수량5@@
                "bidrem5": "bidrem5`long", ## 매수호가수량5@@
                "lp_bidrem5": "lp_bidrem5`long", ## LP매수호가수량5@@
                "preoffercha5": "preoffercha5`long", ## 직전매도대비수량5@@
                "prebidcha5": "prebidcha5`long", ## 직전매수대비수량5@@
                "offerho6": "offerho6`long", ## 매도호가6@@
                "bidho6": "bidho6`long", ## 매수호가6@@
                "offerrem6": "offerrem6`long", ## 매도호가수량6@@
                "lp_offerrem6": "lp_offerrem6`long", ## LP매도호가수량6@@
                "bidrem6": "bidrem6`long", ## 매수호가수량6@@
                "lp_bidrem6": "lp_bidrem6`long", ## LP매수호가수량6@@
                "preoffercha6": "preoffercha6`long", ## 직전매도대비수량6@@
                "prebidcha6": "prebidcha6`long", ## 직전매수대비수량6@@
                "offerho7": "offerho7`long", ## 매도호가7@@
                "bidho7": "bidho7`long", ## 매수호가7@@
                "offerrem7": "offerrem7`long", ## 매도호가수량7@@
                "lp_offerrem7": "lp_offerrem7`long", ## LP매도호가수량7@@
                "bidrem7": "bidrem7`long", ## 매수호가수량7@@
                "lp_bidrem7": "lp_bidrem7`long", ## LP매수호가수량7@@
                "preoffercha7": "preoffercha7`long", ## 직전매도대비수량7@@
                "prebidcha7": "prebidcha7`long", ## 직전매수대비수량7@@
                "offerho8": "offerho8`long", ## 매도호가8@@
                "bidho8": "bidho8`long", ## 매수호가8@@
                "offerrem8": "offerrem8`long", ## 매도호가수량8@@
                "lp_offerrem8": "lp_offerrem8`long", ## LP매도호가수량8@@
                "bidrem8": "bidrem8`long", ## 매수호가수량8@@
                "lp_bidrem8": "lp_bidrem8`long", ## LP매수호가수량8@@
                "preoffercha8": "preoffercha8`long", ## 직전매도대비수량8@@
                "prebidcha8": "prebidcha8`long", ## 직전매수대비수량8@@
                "offerho9": "offerho9`long", ## 매도호가9@@
                "bidho9": "bidho9`long", ## 매수호가9@@
                "offerrem9": "offerrem9`long", ## 매도호가수량9@@
                "lp_offerrem9": "lp_offerrem9`long", ## LP매도호가수량9@@
                "bidrem9": "bidrem9`long", ## 매수호가수량9@@
                "lp_bidrem9": "lp_bidrem9`long", ## LP매수호가수량9@@
                "preoffercha9": "preoffercha9`long", ## 직전매도대비수량9@@
                "prebidcha9": "prebidcha9`long", ## 직전매수대비수량9@@
                "offerho10": "offerho10`long", ## 매도호가10@@
                "bidho10": "bidho10`long", ## 매수호가10@@
                "offerrem10": "offerrem10`long", ## 매도호가수량10@@
                "lp_offerrem10": "lp_offerrem10`long", ## LP매도호가수량10@@
                "bidrem10": "bidrem10`long", ## 매수호가수량10@@
                "lp_bidrem10": "lp_bidrem10`long", ## LP매수호가수량10@@
                "preoffercha10": "preoffercha10`long", ## 직전매도대비수량10@@
                "prebidcha10": "prebidcha10`long", ## 직전매수대비수량10@@
                "offer": "offer`long", ## 매도호가수량합@@
                "bid": "bid`long", ## 매수호가수량합@@
                "preoffercha": "preoffercha`long", ## 직전매도대비수량합@@
                "prebidcha": "prebidcha`long", ## 직전매수대비수량합@@
                "hotime": "hotime`char", ## 수신시간@@
                "yeprice": "yeprice`long", ## 예상체결가격@@
                "yevolume": "yevolume`float", ## 예상체결수량@@
                "yesign": "yesign`char", ## 예상체결전일구분@@
                "yechange": "yechange`long", ## 예상체결전일대비@@
                "yediff": "yediff`float", ## 예상체결등락율@@
                "tmoffer": "tmoffer`long", ## 시간외매도잔량@@
                "tmbid": "tmbid`long", ## 시간외매수잔량@@
                "ho_status": "ho_status`char", ## 동시구분@@
                "open": "open`long", ## 시가@@
                "high": "high`long", ## 고가@@
                "low": "low`long", ## 저가@@
                "invidx": "invidx`char", ## ELW권리형태@@1:표준2:디지털3:조기종료
                "koba_stdprc": "koba_stdprc`float", ## KO베리어@@
                "koba_acc_rt": "koba_acc_rt`float", ## KO접근도@@
                "koba_yn": "koba_yn`char##KO발생여부(Y/N)@@"
            }
        }
    },
    "t1972": { ## ELW현재가(거래원)조회(t1972)
        "input": {
            "t1972InBlock": {
                "shcode": " ##단축코드@@"
            }
        },
        "output": {
            "t1972OutBlock": {
                "hname": "hname`char", ## 한글명@@
                "expcode": "expcode`char", ## 표준코드@@
                "shcode": "shcode`char", ## 단축코드@@
                "offerno1": "offerno1`char", ## 매도증권사코드1@@
                "bidno1": "bidno1`char", ## 매수증권사코드1@@
                "dvol1": "dvol1`long", ## 총매도수량1@@
                "svol1": "svol1`long", ## 총매수수량1@@
                "dcha1": "dcha1`long", ## 매도증감1@@
                "scha1": "scha1`long", ## 매수증감1@@
                "ddiff1": "ddiff1`float", ## 매도비율1@@
                "sdiff1": "sdiff1`float", ## 매수비율1@@
                "offerno2": "offerno2`char", ## 매도증권사코드2@@
                "bidno2": "bidno2`char", ## 매수증권사코드2@@
                "dvol2": "dvol2`long", ## 총매도수량2@@
                "svol2": "svol2`long", ## 총매수수량2@@
                "dcha2": "dcha2`long", ## 매도증감2@@
                "scha2": "scha2`long", ## 매수증감2@@
                "ddiff2": "ddiff2`float", ## 매도비율2@@
                "sdiff2": "sdiff2`float", ## 매수비율2@@
                "offerno3": "offerno3`char", ## 매도증권사코드3@@
                "bidno3": "bidno3`char", ## 매수증권사코드3@@
                "dvol3": "dvol3`long", ## 총매도수량3@@
                "svol3": "svol3`long", ## 총매수수량3@@
                "dcha3": "dcha3`long", ## 매도증감3@@
                "scha3": "scha3`long", ## 매수증감3@@
                "ddiff3": "ddiff3`float", ## 매도비율3@@
                "sdiff3": "sdiff3`float", ## 매수비율3@@
                "offerno4": "offerno4`char", ## 매도증권사코드4@@
                "bidno4": "bidno4`char", ## 매수증권사코드4@@
                "dvol4": "dvol4`long", ## 총매도수량4@@
                "svol4": "svol4`long", ## 총매수수량4@@
                "dcha4": "dcha4`long", ## 매도증감4@@
                "scha4": "scha4`long", ## 매수증감4@@
                "ddiff4": "ddiff4`float", ## 매도비율4@@
                "sdiff4": "sdiff4`float", ## 매수비율4@@
                "offerno5": "offerno5`char", ## 매도증권사코드5@@
                "bidno5": "bidno5`char", ## 매수증권사코드5@@
                "dvol5": "dvol5`long", ## 총매도수량5@@
                "svol5": "svol5`long", ## 총매수수량5@@
                "dcha5": "dcha5`long", ## 매도증감5@@
                "scha5": "scha5`long", ## 매수증감5@@
                "ddiff5": "ddiff5`float", ## 매도비율5@@
                "sdiff5": "sdiff5`float", ## 매수비율5@@
                "fwdvl": "fwdvl`long", ## 외국계매도합계수량@@
                "fwsvl": "fwsvl`long", ## 외국계매수합계수량@@
                "ftradmdcha": "ftradmdcha`long", ## 외국계매도직전대비@@
                "ftradmscha": "ftradmscha`long", ## 외국계매수직전대비@@
                "fwddiff": "fwddiff`float", ## 외국계매도합계비율@@
                "fwsdiff": "fwsdiff`float##외국계매수합계비율@@"
            }
        }
    },
    "t1973": { ## ELW시간대별예상체결조회(t1973)
        "input": {
            "t1973InBlock": {
                "shcode": " ", ## 단축코드@@
                "cts_time": " ##시간CTS@@"
            }
        },
        "output": {
            "t1973OutBlock": {
                "cts_time": "cts_time`char##시간CTS@@"
            },
            "t1973OutBlock1": {
                "chetime": "chetime`char", ## 시간@@
                "yeprice": "yeprice`long", ## 예상체결가격@@
                "yegubun": "yegubun`char", ## 예상체결구분@@
                "jnilysign": "jnilysign`char", ## 전일종가대비구분@@
                "jnilychange": "jnilychange`long", ## 전일종가대비@@
                "yediff": "yediff`float", ## 예상체결등락율@@
                "yevolume": "yevolume`long", ## 예상체결량@@
                "ymdvolume": "ymdvolume`long", ## 예상매도체결량@@
                "ymsvolume": "ymsvolume`long##예상매수체결량@@"
            }
        }
    },
    "t1974": { ## ELW기초자산동일종목(t1974)
        "input": {
            "t1974InBlock": {
                "shcode": " ##종목코드@@"
            }
        },
        "output": {
            "t1974OutBlock": {
                "cnt": "cnt`long##종목갯수@@"
            },
            "t1974OutBlock1": {
                "shcode": "shcode`char", ## 종목코드@@
                "hname": "hname`char", ## 종목명@@
                "cpgubun": "cpgubun`char", ## 콜/풋구분@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`float##거래량@@"
            }
        }
    },
    "t1981": { ## 기초자산리스트조회(t1981)
        "input": {
            "t1981InBlock": {
                "mkt_gb": " ##시장구분@@0:전체1:코스피2:코스닥"
            }
        },
        "output": {
            "t1981OutBlock": {
                "ksp_cnt": "ksp_cnt`char", ## 코스피종목건수@@
                "ksd_cnt": "ksd_cnt`char##코스닥종목건수@@"
            },
            "t1981OutBlock1": {
                "shcode": "shcode`char", ## 단축코드@@
                "expcode": "expcode`char", ## 표준코드@@
                "hname": "hname`char", ## 종목명@@
                "price": "price`char", ## 현재가@@
                "sign": "sign`char", ## 부호@@
                "change": "change`char", ## 대비@@
                "rate": "rate`float", ## 등락율@@
                "volume": "volume`char", ## 누적거래량(주)@@
                "value": "value`char", ## 누적거래대금(백만)@@
                "mkt_gb": "mkt_gb`char##시장구분@@"
            }
        }
    },
    "t2101": { ## 선물/옵션현재가(시세)조회(t2101)
        "input": {
            "t2101InBlock": {
                "focode": " ##단축코드@@"
            }
        },
        "output": {
            "t2101OutBlock": {
                "hname": "hname`char", ## 한글명@@
                "price": "price`float", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`float", ## 전일대비@@
                "jnilclose": "jnilclose`float", ## 전일종가@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 거래량@@
                "value": "value`long", ## 거래대금@@
                "mgjv": "mgjv`long", ## 미결제량@@
                "mgjvdiff": "mgjvdiff`long", ## 미결제증감@@
                "open": "open`float", ## 시가@@
                "high": "high`float", ## 고가@@
                "low": "low`float", ## 저가@@
                "uplmtprice": "uplmtprice`float", ## 상한가@@
                "dnlmtprice": "dnlmtprice`float", ## 하한가@@
                "high52w": "high52w`float", ## 52최고가@@
                "low52w": "low52w`float", ## 52최저가@@
                "basis": "basis`float", ## 베이시스@@
                "recprice": "recprice`float", ## 기준가@@
                "theoryprice": "theoryprice`float", ## 이론가@@
                "glyl": "glyl`float", ## 괴리율@@
                "cbhprice": "cbhprice`float", ## CB상한가@@
                "cblprice": "cblprice`float", ## CB하한가@@
                "lastmonth": "lastmonth`char", ## 만기일@@
                "jandatecnt": "jandatecnt`long", ## 잔여일@@
                "pricejisu": "pricejisu`float", ## 종합지수@@
                "jisusign": "jisusign`char", ## 종합지수전일대비구분@@
                "jisuchange": "jisuchange`float", ## 종합지수전일대비@@
                "jisudiff": "jisudiff`float", ## 종합지수등락율@@
                "kospijisu": "kospijisu`float", ## KOSPI200지수@@
                "kospisign": "kospisign`char", ## KOSPI200전일대비구분@@
                "kospichange": "kospichange`float", ## KOSPI200전일대비@@
                "kospidiff": "kospidiff`float", ## KOSPI200등락율@@
                "listhprice": "listhprice`float", ## 상장최고가@@
                "listlprice": "listlprice`float", ## 상장최저가@@
                "delt": "delt`float", ## 델타@@
                "gama": "gama`float", ## 감마@@
                "ceta": "ceta`float", ## 세타@@
                "vega": "vega`float", ## 베가@@
                "rhox": "rhox`float", ## 로우@@
                "gmprice": "gmprice`float", ## 근월물현재가@@
                "gmsign": "gmsign`char", ## 근월물전일대비구분@@
                "gmchange": "gmchange`float", ## 근월물전일대비@@
                "gmdiff": "gmdiff`float", ## 근월물등락율@@
                "theorypriceg": "theorypriceg`float", ## 이론가@@
                "histimpv": "histimpv`float", ## 역사적변동성@@
                "impv": "impv`float", ## 내재변동성@@
                "sbasis": "sbasis`float", ## 시장BASIS@@
                "ibasis": "ibasis`float", ## 이론BASIS@@
                "gmfutcode": "gmfutcode`char", ## 근월물종목코드@@
                "actprice": "actprice`float", ## 행사가@@
                "greeks_time": "greeks_time`char", ## 거래소민감도수신시간@@
                "greeks_confirm": "greeks_confirm`char", ## 거래소민감도확정여부@@
                "danhochk": "danhochk`char", ## 단일가호가여부@@
                "yeprice": "yeprice`float", ## 예상체결가@@
                "jnilysign": "jnilysign`char", ## 예상체결가전일종가대비구분@@
                "jnilychange": "jnilychange`float", ## 예상체결가전일종가대비@@
                "jnilydrate": "jnilydrate`float", ## 예상체결가전일종가등락율@@
                "alloc_gubun": "alloc_gubun`char", ## 배분구분@@1:배분개시2:배분해제0:미발생
                "bjandatecnt": "bjandatecnt`long", ## 잔여일(영업일)@@
                "focode": "focode`char", ## 종목코드@@
                "dy_gubun": "dy_gubun`char", ## 실시간가격제한여부@@0:대상아님1:적용중2:미적용중3:일시해제
                "dy_uplmtprice": "dy_uplmtprice`float", ## 실시간상한가@@
                "dy_dnlmtprice": "dy_dnlmtprice`float", ## 실시간하한가@@
                "updnstep_gubun": "updnstep_gubun`char", ## 가격제한폭확대@@0:미확대1:확대2:대상아님
                "upstep": "upstep`char", ## 상한적용단계@@
                "dnstep": "dnstep`char", ## 하한적용단계@@
                "uplmtprice_3rd": "uplmtprice_3rd`float", ## 3단계상한가@@
                "dnlmtprice_3rd": "dnlmtprice_3rd`float##3단계하한가@@"
            }
        }
    },
    "t2105": { ## 선물/옵션현재가호가조회(t2105)
        "input": {
            "t2105InBlock": {
                "shcode": " ##단축코드@@"
            }
        },
        "output": {
            "t2105OutBlock": {
                "hname": "hname`char", ## 종목명@@
                "price": "price`float", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`float", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 거래량@@
                "stimeqrt": "stimeqrt`float", ## 거래량전일동시간비율@@
                "jnilclose": "jnilclose`float", ## 전일종가@@
                "offerho1": "offerho1`float", ## 매도호가1@@
                "bidho1": "bidho1`float", ## 매수호가1@@
                "offerrem1": "offerrem1`long", ## 매도호가수량1@@
                "bidrem1": "bidrem1`long", ## 매수호가수량1@@
                "dcnt1": "dcnt1`long", ## 매도호가건수1@@
                "scnt1": "scnt1`long", ## 매수호가건수1@@
                "offerho2": "offerho2`float", ## 매도호가2@@
                "bidho2": "bidho2`float", ## 매수호가2@@
                "offerrem2": "offerrem2`long", ## 매도호가수량2@@
                "bidrem2": "bidrem2`long", ## 매수호가수량2@@
                "dcnt2": "dcnt2`long", ## 매도호가건수2@@
                "scnt2": "scnt2`long", ## 매수호가건수2@@
                "offerho3": "offerho3`float", ## 매도호가3@@
                "bidho3": "bidho3`float", ## 매수호가3@@
                "offerrem3": "offerrem3`long", ## 매도호가수량3@@
                "bidrem3": "bidrem3`long", ## 매수호가수량3@@
                "dcnt3": "dcnt3`long", ## 매도호가건수3@@
                "scnt3": "scnt3`long", ## 매수호가건수3@@
                "offerho4": "offerho4`float", ## 매도호가4@@
                "bidho4": "bidho4`float", ## 매수호가4@@
                "offerrem4": "offerrem4`long", ## 매도호가수량4@@
                "bidrem4": "bidrem4`long", ## 매수호가수량4@@
                "dcnt4": "dcnt4`long", ## 매도호가건수4@@
                "scnt4": "scnt4`long", ## 매수호가건수4@@
                "offerho5": "offerho5`float", ## 매도호가5@@
                "bidho5": "bidho5`float", ## 매수호가5@@
                "offerrem5": "offerrem5`long", ## 매도호가수량5@@
                "bidrem5": "bidrem5`long", ## 매수호가수량5@@
                "dcnt5": "dcnt5`long", ## 매도호가건수5@@
                "scnt5": "scnt5`long", ## 매수호가건수5@@
                "dvol": "dvol`long", ## 매도호가총수량@@
                "svol": "svol`long", ## 매수호가총수량@@
                "toffernum": "toffernum`long", ## 총매도호가건수@@
                "tbidnum": "tbidnum`long", ## 총매수호가건수@@
                "time": "time`char", ## 수신시간@@
                "shcode": "shcode`char##단축코드@@"
            }
        }
    },
    "t2106": { ## 선물/옵션현재가시세메모(t2106)
        "input": {
            "t2106InBlock": {
                "code": " ", ## 종목코드@@
                "nrec": " ##건수@@"
            },
            "t2106InBlock1": {
                "indx": " ", ## 인덱스@@
                "gubn": " ", ## 조건구분@@
                "dat1": " ", ## 데이타1@@
                "dat2": " ##데이타2@@"
            }
        },
        "output": {
            "t2106OutBlock": {
                "nrec": "nrec`char##출력건수@@"
            },
            "t2106OutBlock1": {
                "indx": "indx`char", ## 인덱스@@
                "gubn": "gubn`char", ## 조건구분@@
                "vals": "vals`char##출력값@@"
            }
        }
    },
    "t2201": { ## 선물옵션시간대별체결조회(t2201)
        "input": {
            "t2201InBlock": {
                "focode": " ", ## 단축코드@@
                "cvolume": "0", ## 특이거래량@@
                "stime": " ", ## 시작시간@@
                "etime": " ", ## 종료시간@@
                "cts_time": " ##시간CTS@@"
            }
        },
        "output": {
            "t2201OutBlock": {
                "cts_time": "cts_time`char##시간CTS@@"
            },
            "t2201OutBlock1": {
                "chetime": "chetime`char", ## 시간@@
                "price": "price`float", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`float", ## 전일대비@@
                "cvolume": "cvolume`long", ## 체결수량@@
                "chdegree": "chdegree`float", ## 체결강도@@
                "offerho": "offerho`float", ## 매도호가@@
                "bidho": "bidho`float", ## 매수호가@@
                "volume": "volume`double", ## 거래량@@
                "openyak": "openyak`long", ## 미결수량@@
                "jnilopenupdn": "jnilopenupdn`long", ## 미결전일증감@@
                "ibasis": "ibasis`float", ## 이론BASIS@@
                "sbasis": "sbasis`float", ## 시장BASIS@@
                "kasis": "kasis`float", ## 괴리율@@
                "value": "value`double", ## 거래대금@@
                "j_openupdn": "j_openupdn`long", ## 미결직전증감@@
                "n_msvolume": "n_msvolume`double", ## 누적매수체결량@@
                "n_mdvolume": "n_mdvolume`double", ## 누적매도체결량@@
                "s_msvolume": "s_msvolume`double", ## 누적순매수체결량@@
                "n_mschecnt": "n_mschecnt`long", ## 누적매수체결건수@@
                "n_mdchecnt": "n_mdchecnt`long", ## 누적매도체결건수@@
                "s_mschecnt": "s_mschecnt`long##누적순매수체결건수@@"
            }
        }
    },
    "t2203": { ## 기간별주가(t2203)
        "input": {
            "t2203InBlock": {
                "shcode": " ", ## 단축코드@@
                "futcheck": " ", ## 선물최근월물@@
                "date": " ", ## 날짜@@
                "cts_code": " ", ## CTS종목코드@@
                "lastdate": " ", ## 전종목만기일@@
                "cnt": "0##조회요청건수@@"
            }
        },
        "output": {
            "t2203OutBlock": {
                "date": "date`char", ## 날짜@@
                "cts_code": "cts_code`char", ## CTS종목코드@@
                "lastdate": "lastdate`char", ## 전종목만기일@@
                "nowfutyn": "nowfutyn`char##최근월선물여부@@"
            },
            "t2203OutBlock1": {
                "date": "date`char", ## 날짜@@
                "open": "open`float", ## 시가@@
                "high": "high`float", ## 고가@@
                "low": "low`float", ## 저가@@
                "close": "close`float", ## 종가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`float", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 거래량@@
                "diff_vol": "diff_vol`float", ## 거래증가율@@
                "openyak": "openyak`long", ## 미결수량@@
                "openyakupdn": "openyakupdn`long", ## 미결증감@@
                "value": "value`float##거래대금@@"
            }
        }
    },
    "t2209": { ## 선물옵션틱분별체결조회챠트(t2209)
        "input": {
            "t2209InBlock": {
                "focode": " ", ## 단축코드@@
                "cgubun": " ", ## 챠트구분@@
                "bgubun": "0", ## 분구분@@
                "cnt": "0##조회건수@@"
            }
        },
        "output": {
            "t2209OutBlock1": {
                "chetime": "chetime`char", ## 시간@@
                "price": "price`float", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`float", ## 전일대비@@
                "open": "open`float", ## 시가@@
                "high": "high`float", ## 고가@@
                "low": "low`float", ## 저가@@
                "volume": "volume`double", ## 거래량@@
                "value": "value`double", ## 거래대금@@
                "openyak": "openyak`long", ## 미결수량@@
                "openupdn": "openupdn`long", ## 미결증감@@
                "cvolume": "cvolume`long", ## 체결수량@@
                "s_mschecnt": "s_mschecnt`long", ## 매수순간체결건수@@
                "s_mdchecnt": "s_mdchecnt`long", ## 매도순간체결건수@@
                "ss_mschecnt": "ss_mschecnt`long", ## 순매수순간체결건수@@
                "s_mschevol": "s_mschevol`double", ## 매수순간체결량@@
                "s_mdchevol": "s_mdchevol`double", ## 매도순간체결량@@
                "ss_mschevol": "ss_mschevol`double", ## 순매수순간체결량@@
                "chdegvol": "chdegvol`float", ## 체결강도(거래량)@@
                "chdegcnt": "chdegcnt`float##체결강도(건수)@@"
            }
        }
    },
    "t2210": { ## 선물옵션시간대별체결조회(단일출력용)
        "input": {
            "t2210InBlock": {
                "focode": " ", ## 단축코드@@
                "cvolume": "0", ## 특이거래량@@
                "stime": " ", ## 시작시간@@
                "etime": " ##종료시간@@"
            }
        },
        "output": {
            "t2210OutBlock": {
                "mdvolume": "mdvolume`long", ## 매도체결수량@@
                "mdchecnt": "mdchecnt`long", ## 매도체결건수@@
                "msvolume": "msvolume`long", ## 매수체결수량@@
                "mschecnt": "mschecnt`long##매수체결건수@@"
            }
        }
    },
    "t2301": { ## 옵션전광판(t2301)
        "input": {
            "t2301InBlock": {
                "yyyymm": " ", ## 월물@@
                "gubun": " ##미니구분@@M:미니G:정규"
            }
        },
        "output": {
            "t2301OutBlock": {
                "histimpv": "histimpv`long", ## 역사적변동성@@
                "jandatecnt": "jandatecnt`long", ## 옵션잔존일@@
                "cimpv": "cimpv`float", ## 콜옵션대표IV@@
                "pimpv": "pimpv`float", ## 풋옵션대표IV@@
                "gmprice": "gmprice`float", ## 근월물현재가@@
                "gmsign": "gmsign`char", ## 근월물전일대비구분@@
                "gmchange": "gmchange`float", ## 근월물전일대비@@
                "gmdiff": "gmdiff`float", ## 근월물등락율@@
                "gmvolume": "gmvolume`long", ## 근월물거래량@@
                "gmshcode": "gmshcode`char##근월물선물코드@@"
            },
            "t2301OutBlock1": {
                "actprice": "actprice`float", ## 행사가@@
                "optcode": "optcode`char", ## 콜옵션코드@@
                "price": "price`float", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`float", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 거래량@@
                "iv": "iv`float", ## IV@@
                "mgjv": "mgjv`long", ## 미결제약정@@
                "mgjvupdn": "mgjvupdn`long", ## 미결제약정증감@@
                "offerho1": "offerho1`float", ## 매도호가@@
                "bidho1": "bidho1`float", ## 매수호가@@
                "cvolume": "cvolume`long", ## 체결량@@
                "delt": "delt`float", ## 델타@@
                "gama": "gama`float", ## 감마@@
                "vega": "vega`float", ## 베가@@
                "ceta": "ceta`float", ## 쎄타@@
                "rhox": "rhox`float", ## 로우@@
                "theoryprice": "theoryprice`float", ## 이론가@@
                "impv": "impv`float", ## 내재가치@@
                "timevl": "timevl`float", ## 시간가치@@
                "jvolume": "jvolume`long", ## 잔고수량@@
                "parpl": "parpl`long", ## 평가손익@@
                "jngo": "jngo`long", ## 청산가능수량@@
                "offerrem1": "offerrem1`long", ## 매도잔량@@
                "bidrem1": "bidrem1`long", ## 매수잔량@@
                "open": "open`float", ## 시가@@
                "high": "high`float", ## 고가@@
                "low": "low`float", ## 저가@@
                "atmgubun": "atmgubun`char", ## ATM구분@@
                "jisuconv": "jisuconv`float", ## 지수환산@@
                "value": "value`float##거래대금@@"
            },
            "t2301OutBlock2": {
                "actprice": "actprice`float", ## 행사가@@
                "optcode": "optcode`char", ## 풋옵션코드@@
                "price": "price`float", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`float", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 거래량@@
                "iv": "iv`float", ## IV@@
                "mgjv": "mgjv`long", ## 미결제약정@@
                "mgjvupdn": "mgjvupdn`long", ## 미결제약정증감@@
                "offerho1": "offerho1`float", ## 매도호가@@
                "bidho1": "bidho1`float", ## 매수호가@@
                "cvolume": "cvolume`long", ## 체결량@@
                "delt": "delt`float", ## 델타@@
                "gama": "gama`float", ## 감마@@
                "vega": "vega`float", ## 베가@@
                "ceta": "ceta`float", ## 쎄타@@
                "rhox": "rhox`float", ## 로우@@
                "theoryprice": "theoryprice`float", ## 이론가@@
                "impv": "impv`float", ## 내재가치@@
                "timevl": "timevl`float", ## 시간가치@@
                "jvolume": "jvolume`long", ## 잔고수량@@
                "parpl": "parpl`long", ## 평가손익@@
                "jngo": "jngo`long", ## 청산가능수량@@
                "offerrem1": "offerrem1`long", ## 매도잔량@@
                "bidrem1": "bidrem1`long", ## 매수잔량@@
                "open": "open`float", ## 시가@@
                "high": "high`float", ## 고가@@
                "low": "low`float", ## 저가@@
                "atmgubun": "atmgubun`char", ## ATM구분@@
                "jisuconv": "jisuconv`float", ## 지수환산@@
                "value": "value`float##거래대금@@"
            }
        }
    },
    "t2405": { ## 선물옵션호가잔량비율챠트(t2405)
        "input": {
            "t2405InBlock": {
                "focode": " ", ## 단축코드@@
                "bgubun": " ", ## 분구분@@
                "nmin": "0", ## N분@@
                "etime": " ", ## 종료시간@@
                "hgubun": " ", ## 호가구분@@
                "cnt": "0", ## 조회건수@@
                "cts_time": " ##시간CTS@@"
            }
        },
        "output": {
            "t2405OutBlock": {
                "mdvolume": "mdvolume`double", ## 매도체결수량@@
                "mdchecnt": "mdchecnt`long", ## 매도체결건수@@
                "msvolume": "msvolume`double", ## 매수체결수량@@
                "mschecnt": "mschecnt`long", ## 매수체결건수@@
                "cts_time": "cts_time`char##시간CTS@@"
            },
            "t2405OutBlock1": {
                "time": "time`char", ## 시간@@
                "price": "price`float", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`float", ## 전일대비@@
                "volume": "volume`double", ## 누적거래량@@
                "cvolume": "cvolume`long", ## 체결수량@@
                "offerho1": "offerho1`float", ## 매도1호가@@
                "bidho1": "bidho1`float", ## 매수1호가@@
                "offerrem": "offerrem`long", ## 매도수량@@
                "bidrem": "bidrem`long", ## 매수수량@@
                "offercnt": "offercnt`long", ## 매도건수@@
                "bidcnt": "bidcnt`long", ## 매수건수@@
                "c_offerrem": "c_offerrem`long", ## 매도증감수량@@
                "c_bidrem": "c_bidrem`long", ## 매수증감수량@@
                "c_offercnt": "c_offercnt`long", ## 매도증감건수@@
                "c_bidcnt": "c_bidcnt`long", ## 매수증감건수@@
                "r_bidrem": "r_bidrem`float", ## 매수수량비율@@
                "r_bidcnt": "r_bidcnt`float", ## 매수건수비율@@
                "r_sign": "r_sign`char", ## 매수비율구분@@
                "date": "date`date##일자@@"
            }
        }
    },
    "t2421": { ## 미결제약정추이(t2421)
        "input": {
            "t2421InBlock": {
                "focode": " ", ## 종목코드@@
                "bdgubun": " ", ## 분일구분@@
                "nmin": "0", ## N분@@
                "tcgubun": " ", ## 당일연결구분@@
                "cnt": "0##조회건수@@"
            }
        },
        "output": {
            "t2421OutBlock": {
                "price": "price`float", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`float", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "cvolume": "cvolume`long", ## 체결수량@@
                "volume": "volume`double", ## 누적거래량@@
                "openyak": "openyak`long##미결제수량@@"
            },
            "t2421OutBlock1": {
                "dt": "dt`char", ## 일자시간@@
                "open": "open`float", ## 시가@@
                "high": "high`float", ## 고가@@
                "low": "low`float", ## 저가@@
                "close": "close`float", ## 종가@@
                "openopenyak": "openopenyak`long", ## 미결제시량@@
                "highopenyak": "highopenyak`long", ## 미결제고량@@
                "lowopenyak": "lowopenyak`long", ## 미결제저량@@
                "closeopenyak": "closeopenyak`long", ## 미결제종량@@
                "openupdn": "openupdn`long##미결증감@@"
            }
        }
    },
    "t2541": { ## 상품선물투자자매매동향(실시간)(t2541)
        "input": {
            "t2541InBlock": {
                "eitem": " ", ## 상품ID@@
                "market": " ", ## 시장구분@@
                "upcode": " ", ## 업종코드@@
                "gubun1": " ", ## 수량구분@@
                "gubun2": " ", ## 전일분구분@@
                "cts_time": " ", ## CTSTIME@@
                "cts_idx": "0", ## CTSIDX@@
                "cnt": "0##조회건수@@"
            }
        },
        "output": {
            "t2541OutBlock": {
                "eitem": "eitem`char", ## 상품ID@@
                "sgubun": "sgubun`char", ## 시장구분@@
                "cts_time": "cts_time`char", ## CTSTIME@@
                "tjjcode_08": "tjjcode_08`char", ## 개인투자자코드@@
                "ms_08": "ms_08`long", ## 개인매수@@
                "md_08": "md_08`long", ## 개인매도@@
                "rate_08": "rate_08`long", ## 개인증감@@
                "svolume_08": "svolume_08`long", ## 개인순매수@@
                "jjcode_17": "jjcode_17`char", ## 외국인투자자코드@@
                "ms_17": "ms_17`long", ## 외국인매수@@
                "md_17": "md_17`long", ## 외국인매도@@
                "rate_17": "rate_17`long", ## 외국인증감@@
                "svolume_17": "svolume_17`long", ## 외국인순매수@@
                "jjcode_18": "jjcode_18`char", ## 기관계투자자코드@@
                "ms_18": "ms_18`long", ## 기관계매수@@
                "md_18": "md_18`long", ## 기관계매도@@
                "rate_18": "rate_18`long", ## 기관계증감@@
                "svolume_18": "svolume_18`long", ## 기관계순매수@@
                "jjcode_01": "jjcode_01`char", ## 증권투자자코드@@
                "ms_01": "ms_01`long", ## 증권매수@@
                "md_01": "md_01`long", ## 증권매도@@
                "rate_01": "rate_01`long", ## 증권증감@@
                "svolume_01": "svolume_01`long", ## 증권순매수@@
                "jjcode_03": "jjcode_03`char", ## 투신투자자코드@@
                "ms_03": "ms_03`long", ## 투신매수@@
                "md_03": "md_03`long", ## 투신매도@@
                "rate_03": "rate_03`long", ## 투신증감@@
                "svolume_03": "svolume_03`long", ## 투신순매수@@
                "jjcode_04": "jjcode_04`char", ## 은행투자자코드@@
                "ms_04": "ms_04`long", ## 은행매수@@
                "md_04": "md_04`long", ## 은행매도@@
                "rate_04": "rate_04`long", ## 은행증감@@
                "svolume_04": "svolume_04`long", ## 은행순매수@@
                "jjcode_02": "jjcode_02`char", ## 보험투자자코드@@
                "ms_02": "ms_02`long", ## 보험매수@@
                "md_02": "md_02`long", ## 보험매도@@
                "rate_02": "rate_02`long", ## 보험증감@@
                "svolume_02": "svolume_02`long", ## 보험순매수@@
                "jjcode_05": "jjcode_05`char", ## 종금투자자코드@@
                "ms_05": "ms_05`long", ## 종금매수@@
                "md_05": "md_05`long", ## 종금매도@@
                "rate_05": "rate_05`long", ## 종금증감@@
                "svolume_05": "svolume_05`long", ## 종금순매수@@
                "jjcode_06": "jjcode_06`char", ## 기금투자자코드@@
                "ms_06": "ms_06`long", ## 기금매수@@
                "md_06": "md_06`long", ## 기금매도@@
                "rate_06": "rate_06`long", ## 기금증감@@
                "svolume_06": "svolume_06`long", ## 기금순매수@@
                "jjcode_07": "jjcode_07`char", ## 기타투자자코드@@
                "ms_07": "ms_07`long", ## 기타매수@@
                "md_07": "md_07`long", ## 기타매도@@
                "rate_07": "rate_07`long", ## 기타증감@@
                "svolume_07": "svolume_07`long", ## 기타순매수@@
                "jjcode_11": "jjcode_11`char", ## 국가투자자코드@@
                "ms_11": "ms_11`long", ## 국가매수@@
                "md_11": "md_11`long", ## 국가매도@@
                "rate_11": "rate_11`long", ## 국가증감@@
                "svolume_11": "svolume_11`long", ## 국가순매수@@
                "jjcode_00": "jjcode_00`char", ## 사모펀드코드@@
                "ms_00": "ms_00`long", ## 사모펀드매수@@
                "md_00": "md_00`long", ## 사모펀드매도@@
                "rate_00": "rate_00`long", ## 사모펀드증감@@
                "svolume_00": "svolume_00`long##사모펀드순매수@@"
            },
            "t2541OutBlock1": {
                "time": "time`char", ## 시간@@
                "sv_08": "sv_08`long", ## 개인순매수@@
                "sv_17": "sv_17`long", ## 외국인순매수@@
                "sv_18": "sv_18`long", ## 기관계순매수@@
                "sv_01": "sv_01`long", ## 증권순매수@@
                "sv_03": "sv_03`long", ## 투신순매수@@
                "sv_04": "sv_04`long", ## 은행순매수@@
                "sv_02": "sv_02`long", ## 보험순매수@@
                "sv_05": "sv_05`long", ## 종금순매수@@
                "sv_06": "sv_06`long", ## 기금순매수@@
                "sv_07": "sv_07`long", ## 기타순매수@@
                "sv_11": "sv_11`long", ## 국가순매수@@
                "sv_00": "sv_00`long##사모펀드순매수@@"
            }
        }
    },
    "t2545": { ## 상품선물투자자매매동향(챠트용)
        "input": {
            "t2545InBlock": {
                "eitem": " ", ## 상품ID@@
                "sgubun": " ", ## 시장구분@@
                "upcode": " ", ## 업종코드@@
                "nmin": "0", ## N분@@
                "cnt": "0", ## 조회건수@@
                "bgubun": " ##전일분@@"
            }
        },
        "output": {
            "t2545OutBlock": {
                "eitem": "eitem`char", ## 상품ID@@
                "sgubun": "sgubun`char", ## 시장구분@@
                "indcode": "indcode`char", ## 개인투자자코드@@
                "forcode": "forcode`char", ## 외국인투자자코드@@
                "syscode": "syscode`char", ## 기관계투자자코드@@
                "stocode": "stocode`char", ## 증권투자자코드@@
                "invcode": "invcode`char", ## 투신투자자코드@@
                "bancode": "bancode`char", ## 은행투자자코드@@
                "inscode": "inscode`char", ## 보험투자자코드@@
                "fincode": "fincode`char", ## 종금투자자코드@@
                "moncode": "moncode`char", ## 기금투자자코드@@
                "etccode": "etccode`char", ## 기타투자자코드@@
                "natcode": "natcode`char", ## 국가투자자코드@@
                "pefcode": "pefcode`char", ## 사모펀드투자자코드@@
                "jisucd": "jisucd`char", ## 기준지수코드@@
                "jisunm": "jisunm`char##기준지수명@@"
            },
            "t2545OutBlock1": {
                "date": "date`char", ## 일자@@
                "time": "time`char", ## 시간@@
                "datetime": "datetime`char", ## 일자시간@@
                "indmsvol": "indmsvol`long", ## 개인순매수거래량@@
                "indmsamt": "indmsamt`double", ## 개인순매수거래대금@@
                "formsvol": "formsvol`long", ## 외국인순매수거래량@@
                "formsamt": "formsamt`double", ## 외국인순매수거래대금@@
                "sysmsvol": "sysmsvol`long", ## 기관계순매수거래량@@
                "sysmsamt": "sysmsamt`double", ## 기관계순매수거래대금@@
                "stomsvol": "stomsvol`long", ## 증권순매수거래량@@
                "stomsamt": "stomsamt`double", ## 증권순매수거래대금@@
                "invmsvol": "invmsvol`long", ## 투신순매수거래량@@
                "invmsamt": "invmsamt`double", ## 투신순매수거래대금@@
                "banmsvol": "banmsvol`long", ## 은행순매수거래량@@
                "banmsamt": "banmsamt`double", ## 은행순매수거래대금@@
                "insmsvol": "insmsvol`long", ## 보험순매수거래량@@
                "insmsamt": "insmsamt`double", ## 보험순매수거래대금@@
                "finmsvol": "finmsvol`long", ## 종금순매수거래량@@
                "finmsamt": "finmsamt`double", ## 종금순매수거래대금@@
                "monmsvol": "monmsvol`long", ## 기금순매수거래량@@
                "monmsamt": "monmsamt`double", ## 기금순매수거래대금@@
                "etcmsvol": "etcmsvol`long", ## 기타순매수거래량@@
                "etcmsamt": "etcmsamt`double", ## 기타순매수거래대금@@
                "natmsvol": "natmsvol`long", ## 국가순매수거래량@@
                "natmsamt": "natmsamt`double", ## 국가순매수거래대금@@
                "pefmsvol": "pefmsvol`long", ## 사모펀드순매수거래량@@
                "pefmsamt": "pefmsamt`double", ## 사모펀드순매수거래대금@@
                "upclose": "upclose`float", ## 기준지수@@
                "upcvolume": "upcvolume`long", ## 기준체결거래량@@
                "upvolume": "upvolume`double", ## 기준누적거래량@@
                "upvalue": "upvalue`double##기준거래대금@@"
            }
        }
    },
    "t2830": { ## EUREXKOSPI200옵션선물현재가(시세)조회(t2830)
        "input": {
            "t2830InBlock": {
                "focode": " ##단축코드@@"
            }
        },
        "output": {
            "t2830OutBlock": {
                "hname": "hname`char", ## 한글명@@
                "price": "price`float", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`float", ## 전일대비@@
                "jnilclose": "jnilclose`float", ## 전일종가@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 거래량@@
                "value": "value`long", ## 거래대금@@
                "open": "open`float", ## 시가@@
                "high": "high`float", ## 고가@@
                "low": "low`float", ## 저가@@
                "recprice": "recprice`float", ## 기준가@@
                "theoryprice": "theoryprice`float", ## 이론가@@
                "actprice": "actprice`float", ## 행사가@@
                "impv": "impv`float", ## 내재가치@@
                "timevl": "timevl`float", ## 시간가치@@
                "kospijisu": "kospijisu`float", ## KOSPI200지수@@
                "kospisign": "kospisign`char", ## KOSPI200전일대비구분@@
                "kospichange": "kospichange`float", ## KOSPI200전일대비@@
                "kospidiff": "kospidiff`float", ## KOSPI200등락율@@
                "cmeprice": "cmeprice`float", ## CME야간선물현재가@@
                "cmesign": "cmesign`char", ## CME야간선물전일대비구분@@
                "cmechange": "cmechange`float", ## CME야간선물전일대비@@
                "cmediff": "cmediff`float", ## CME야간선물등락율@@
                "cmefocode": "cmefocode`char", ## CME야간선물종목코드@@
                "uplmtprice": "uplmtprice`float", ## 정규장적용상한가@@
                "dnlmtprice": "dnlmtprice`float", ## 정규장적용하한가@@
                "focode": "focode`char", ## 단축코드@@
                "yeprice": "yeprice`float", ## 예상체결가@@
                "ysign": "ysign`char", ## 전일대비구분@@
                "ychange": "ychange`float", ## 전일대비@@
                "ydiff": "ydiff`float", ## 등락율@@
                "danhochk": "danhochk`char", ## 단일가호가여부@@
                "jnilvolume": "jnilvolume`long", ## 전일거래량@@
                "jnilvalue": "jnilvalue`long", ## 전일거래대금@@
                "uplmtprice_3rd": "uplmtprice_3rd`float", ## 정규장3단계상한가@@
                "dnlmtprice_3rd": "dnlmtprice_3rd`float##정규장3단계하한가@@"
            }
        }
    },
    "t2831": { ## EUREXKOSPI200옵션선물호가조회(t2831)
        "input": {
            "t2831InBlock": {
                "shcode": " ##단축코드@@"
            }
        },
        "output": {
            "t2831OutBlock": {
                "hname": "hname`char", ## 종목명@@
                "price": "price`float", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`float", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 거래량@@
                "jnilclose": "jnilclose`float", ## 전일종가@@
                "offerho1": "offerho1`float", ## 매도호가1@@
                "bidho1": "bidho1`float", ## 매수호가1@@
                "offerrem1": "offerrem1`long", ## 매도호가수량1@@
                "bidrem1": "bidrem1`long", ## 매수호가수량1@@
                "dcnt1": "dcnt1`long", ## 매도호가건수1@@
                "scnt1": "scnt1`long", ## 매수호가건수1@@
                "offerho2": "offerho2`float", ## 매도호가2@@
                "bidho2": "bidho2`float", ## 매수호가2@@
                "offerrem2": "offerrem2`long", ## 매도호가수량2@@
                "bidrem2": "bidrem2`long", ## 매수호가수량2@@
                "dcnt2": "dcnt2`long", ## 매도호가건수2@@
                "scnt2": "scnt2`long", ## 매수호가건수2@@
                "offerho3": "offerho3`float", ## 매도호가3@@
                "bidho3": "bidho3`float", ## 매수호가3@@
                "offerrem3": "offerrem3`long", ## 매도호가수량3@@
                "bidrem3": "bidrem3`long", ## 매수호가수량3@@
                "dcnt3": "dcnt3`long", ## 매도호가건수3@@
                "scnt3": "scnt3`long", ## 매수호가건수3@@
                "offerho4": "offerho4`float", ## 매도호가4@@
                "bidho4": "bidho4`float", ## 매수호가4@@
                "offerrem4": "offerrem4`long", ## 매도호가수량4@@
                "bidrem4": "bidrem4`long", ## 매수호가수량4@@
                "dcnt4": "dcnt4`long", ## 매도호가건수4@@
                "scnt4": "scnt4`long", ## 매수호가건수4@@
                "offerho5": "offerho5`float", ## 매도호가5@@
                "bidho5": "bidho5`float", ## 매수호가5@@
                "offerrem5": "offerrem5`long", ## 매도호가수량5@@
                "bidrem5": "bidrem5`long", ## 매수호가수량5@@
                "dcnt5": "dcnt5`long", ## 매도호가건수5@@
                "scnt5": "scnt5`long", ## 매수호가건수5@@
                "dvol": "dvol`long", ## 매도호가총수량@@
                "svol": "svol`long", ## 매수호가총수량@@
                "toffernum": "toffernum`long", ## 총매도호가건수@@
                "tbidnum": "tbidnum`long", ## 총매수호가건수@@
                "time": "time`char", ## 수신시간@@
                "shcode": "shcode`char##단축코드@@"
            }
        }
    },
    "t2832": { ## EUREX야간옵션선물시간대별체결조회(t2832)
        "input": {
            "t2832InBlock": {
                "focode": " ", ## 단축코드@@
                "cvolume": "0", ## 특이거래량@@
                "stime": " ", ## 시작시간@@
                "etime": " ", ## 종료시간@@
                "cts_time": " ##시간CTS@@"
            }
        },
        "output": {
            "t2832OutBlock": {
                "cts_time": "cts_time`char##시간CTS@@"
            },
            "t2832OutBlock1": {
                "chetime": "chetime`char", ## 시간@@
                "price": "price`float", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`float", ## 전일대비@@
                "cvolume": "cvolume`long", ## 체결수량@@
                "chdegree": "chdegree`float", ## 체결강도@@
                "offerho": "offerho`float", ## 매도호가@@
                "bidho": "bidho`float", ## 매수호가@@
                "volume": "volume`double", ## 거래량@@
                "n_msvolume": "n_msvolume`double", ## 누적매수체결량@@
                "n_mdvolume": "n_mdvolume`double", ## 누적매도체결량@@
                "s_msvolume": "s_msvolume`double", ## 누적순매수체결량@@
                "n_mschecnt": "n_mschecnt`long", ## 누적매수체결건수@@
                "n_mdchecnt": "n_mdchecnt`long", ## 누적매도체결건수@@
                "s_mschecnt": "s_mschecnt`long##누적순매수체결건수@@"
            }
        }
    },
    "t2833": { ## EUREX야간옵션선물기간별추이(t2833)
        "input": {
            "t2833InBlock": {
                "shcode": " ", ## 단축코드@@
                "futcheck": " ", ## 선물최근월물@@
                "date": " ", ## 날짜@@
                "cts_code": " ", ## CTS종목코드@@
                "lastdate": " ", ## 전종목만기일@@
                "cnt": "0##조회요청건수@@"
            }
        },
        "output": {
            "t2833OutBlock": {
                "date": "date`char", ## 날짜@@
                "cts_code": "cts_code`char", ## CTS종목코드@@
                "lastdate": "lastdate`char", ## 전종목만기일@@
                "nowfutyn": "nowfutyn`char##최근월선물여부@@"
            },
            "t2833OutBlock1": {
                "date": "date`char", ## 날짜@@
                "open": "open`float", ## 시가@@
                "high": "high`float", ## 고가@@
                "low": "low`float", ## 저가@@
                "close": "close`float", ## 종가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`float", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 거래량@@
                "diff_vol": "diff_vol`float##거래증가율@@"
            }
        }
    },
    "t2835": { ## EUREX옵션선물시세전광판(t2835)
        "input": {
            "t2835InBlock": {
                "yyyymm": " ##월물@@"
            }
        },
        "output": {
            "t2835OutBlock": {
                "gmprice": "gmprice`float", ## 근월물현재가@@
                "gmsign": "gmsign`char", ## 근월물전일대비구분@@
                "gmchange": "gmchange`float", ## 근월물전일대비@@
                "gmdiff": "gmdiff`float", ## 근월물등락율@@
                "gmvolume": "gmvolume`long", ## 근월물거래량@@
                "gmshcode": "gmshcode`char##근월물선물코드@@"
            },
            "t2835OutBlock1": {
                "actprice": "actprice`float", ## 행사가@@
                "optcode": "optcode`char", ## 콜옵션코드@@
                "price": "price`float", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`float", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 거래량@@
                "offerho1": "offerho1`float", ## 매도호가@@
                "bidho1": "bidho1`float", ## 매수호가@@
                "cvolume": "cvolume`long", ## 체결량@@
                "impv": "impv`float", ## 내재가치@@
                "timevl": "timevl`float", ## 시간가치@@
                "offerrem1": "offerrem1`long", ## 매도잔량@@
                "bidrem1": "bidrem1`long", ## 매수잔량@@
                "open": "open`float", ## 시가@@
                "high": "high`float", ## 고가@@
                "low": "low`float", ## 저가@@
                "atmgubun": "atmgubun`char", ## ATM구분@@
                "jisuconv": "jisuconv`float##지수환산@@"
            },
            "t2835OutBlock2": {
                "actprice": "actprice`float", ## 행사가@@
                "optcode": "optcode`char", ## 풋옵션코드@@
                "price": "price`float", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`float", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 거래량@@
                "offerho1": "offerho1`float", ## 매도호가@@
                "bidho1": "bidho1`float", ## 매수호가@@
                "cvolume": "cvolume`long", ## 체결량@@
                "impv": "impv`float", ## 내재가치@@
                "timevl": "timevl`float", ## 시간가치@@
                "offerrem1": "offerrem1`long", ## 매도잔량@@
                "bidrem1": "bidrem1`long", ## 매수잔량@@
                "open": "open`float", ## 시가@@
                "high": "high`float", ## 고가@@
                "low": "low`float", ## 저가@@
                "atmgubun": "atmgubun`char", ## ATM구분@@
                "jisuconv": "jisuconv`float##지수환산@@"
            }
        }
    },
    "t3102": { ## 뉴스본문(t3102)
        "input": {
            "t3102InBlock": {
                "sNewsno": " ##뉴스번호@@"
            }
        },
        "output": {
            "t3102OutBlock": {
                "sJongcode": "sJongcode`char##뉴스종목@@"
            },
            "t3102OutBlock1": {
                "sBody": "sBody`char##뉴스본문@@"
            },
            "t3102OutBlock2": {
                "sTitle": "sTitle`char##뉴스타이틀@@"
            }
        }
    },
    "t3202": { ## 종목별증시일정(t3202)
        "input": {
            "t3202InBlock": {
                "shcode": " ", ## 종목코드@@
                "date": " ##조회일자@@"
            }
        },
        "output": {
            "t3202OutBlock": {
                "recdt": "recdt`char", ## 기준일@@
                "tableid": "tableid`char", ## 테이블아이디@@
                "upgu": "upgu`char", ## 업무구분@@
                "custno": "custno`char", ## 발행체번호@@
                "custnm": "custnm`char", ## 발행회사명@@
                "shcode": "shcode`char", ## 종목코드@@
                "upunm": "upunm`char##업무명@@"
            }
        }
    },
    "t3320": { ## FNG_요약(t3320)
        "input": {
            "t3320InBlock": {
                "gicode": " ##종목코드@@"
            }
        },
        "output": {
            "t3320OutBlock": {
                "upgubunnm": "upgubunnm`char", ## 업종구분명@@
                "sijangcd": "sijangcd`char", ## 시장구분@@
                "marketnm": "marketnm`char", ## 시장구분명@@
                "company": "company`char", ## 한글기업명@@
                "baddress": "baddress`char", ## 본사주소@@
                "btelno": "btelno`char", ## 본사전화번호@@
                "gsyyyy": "gsyyyy`char", ## 최근결산년도@@
                "gsmm": "gsmm`char", ## 결산월@@
                "gsym": "gsym`char", ## 최근결산년월@@
                "lstprice": "lstprice`long", ## 주당액면가@@
                "gstock": "gstock`long", ## 주식수@@
                "homeurl": "homeurl`char", ## Homepage@@
                "grdnm": "grdnm`char", ## 그룹명@@
                "foreignratio": "foreignratio`float", ## 외국인@@
                "irtel": "irtel`char", ## 주담전화@@
                "capital": "capital`float", ## 자본금@@
                "sigavalue": "sigavalue`float", ## 시가총액@@
                "cashsis": "cashsis`float", ## 배당금@@
                "cashrate": "cashrate`float", ## 배당수익율@@
                "price": "price`long", ## 현재가@@
                "jnilclose": "jnilclose`long", ## 전일종가@@
                "notice1": "notice1`char", ## 위험고지구분1_정리매매@@
                "notice2": "notice2`char", ## 위험고지구분2_투자위험@@
                "notice3": "notice3`char##위험고지구분3_단기과열@@"
            },
            "t3320OutBlock1": {
                "gicode": "gicode`char", ## 기업코드@@
                "gsym": "gsym`char", ## 결산년월@@
                "gsgb": "gsgb`char", ## 결산구분@@
                "per": "per`float", ## PER@@
                "eps": "eps`float", ## EPS@@
                "pbr": "pbr`float", ## PBR@@
                "roa": "roa`float", ## ROA@@
                "roe": "roe`float", ## ROE@@
                "ebitda": "ebitda`float", ## EBITDA@@
                "evebitda": "evebitda`float", ## EVEBITDA@@
                "par": "par`float", ## 액면가@@
                "sps": "sps`float", ## SPS@@
                "cps": "cps`float", ## CPS@@
                "bps": "bps`float", ## BPS@@
                "t_per": "t_per`float", ## T.PER@@
                "t_eps": "t_eps`float", ## T.EPS@@
                "peg": "peg`float", ## PEG@@
                "t_peg": "t_peg`float", ## T.PEG@@
                "t_gsym": "t_gsym`char##최근분기년도@@"
            }
        }
    },
    "t3341": { ## 재무순위종합(t3341)
        "input": {
            "t3341InBlock": {
                "gubun": " ", ## 시장구분@@
                "gubun1": " ", ## 순위구분@@1:매출액증가율2:영업이익증가율3:세전계속이익증가율4:부채비율5:유보율6:EPS7:BPS8:ROE9:PERa:PBRb:PEG
                "gubun2": " ", ## 대비구분@@
                "idx": "0##IDX@@"
            }
        },
        "output": {
            "t3341OutBlock": {
                "cnt": "cnt`long", ## CNT@@
                "idx": "idx`long##IDX@@"
            },
            "t3341OutBlock1": {
                "rank": "rank`long", ## 순위@@
                "hname": "hname`char", ## 기업명@@
                "salesgrowth": "salesgrowth`long", ## 매출액증가율@@
                "operatingincomegrowt": "operatingincomegrowt`long", ## 영업이익증가율@@
                "ordinaryincomegrowth": "ordinaryincomegrowth`long", ## 경상이익증가율@@
                "liabilitytoequity": "liabilitytoequity`long", ## 부채비율@@
                "enterpriseratio": "enterpriseratio`long", ## 유보율@@
                "eps": "eps`long", ## EPS@@
                "bps": "bps`long", ## BPS@@
                "roe": "roe`long", ## ROE@@
                "shcode": "shcode`char", ## 종목코드@@
                "per": "per`float", ## PER@@
                "pbr": "pbr`float", ## PBR@@
                "peg": "peg`float##PEG@@"
            }
        }
    },
    "t3401": { ## 투자의견(t3401)
        "input": {
            "t3401InBlock": {
                "shcode": " ", ## 종목코드@@
                "gubun1": " ", ## 구분@@
                "tradno": " ", ## 회원사코드@@
                "cts_date": " ##IDXDATE@@"
            }
        },
        "output": {
            "t3401OutBlock": {
                "cts_date": "cts_date`char", ## IDXDATE@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 대비속성@@
                "change": "change`long", ## 대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 거래량@@
                "value": "value`long##거래대금@@"
            },
            "t3401OutBlock1": {
                "shcode": "shcode`char", ## 종목코드@@
                "tradno": "tradno`char", ## 회원사코드@@
                "date": "date`char", ## 의견일자@@
                "tradname": "tradname`char", ## 회원사명@@
                "bopn": "bopn`char", ## 투자의견변경후@@
                "nopn": "nopn`char", ## 투자의견변경전@@
                "boga": "boga`long", ## 목표가변경전@@
                "noga": "noga`long", ## 목표가변경후@@
                "close": "close`long##의견일종가@@"
            }
        }
    },
    "t3518": { ## 해외실시간지수(t3518)
        "input": {
            "t3518InBlock": {
                "kind": " ", ## 종목종류@@
                "symbol": " ", ## SYMBOL@@
                "cnt": "0", ## 입력건수@@
                "jgbn": " ", ## 조회구분@@
                "nmin": "0", ## N분@@
                "cts_date": " ", ## CTS_DATE@@
                "cts_time": " ##CTS_TIME@@"
            }
        },
        "output": {
            "t3518OutBlock": {
                "cts_date": "cts_date`char", ## CTS_DATE@@
                "cts_time": "cts_time`char##CTS_TIME@@"
            },
            "t3518OutBlock1": {
                "date": "date`char", ## 일자@@
                "time": "time`char", ## 시간@@
                "open": "open`double", ## 시가@@
                "high": "high`double", ## 고가@@
                "low": "low`double", ## 저가@@
                "price": "price`double", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`double", ## 전일대비@@
                "uprate": "uprate`double", ## 등락율@@
                "volume": "volume`double", ## 누적거래량@@
                "bidho": "bidho`double", ## 매수호가@@
                "offerho": "offerho`double", ## 매도호가@@
                "bidrem": "bidrem`double", ## 매수잔량@@
                "offerrem": "offerrem`double", ## 매도잔량@@
                "kind": "kind`char", ## 종목종류@@
                "symbol": "symbol`char", ## SYMBOL@@
                "exid": "exid`char", ## EXID@@
                "kodate": "kodate`char", ## 한국일자@@
                "kotime": "kotime`char##한국시간@@"
            }
        }
    },
    "t3521": { ## 해외지수조회(API용)(t3521)
        "input": {
            "t3521InBlock": {
                "kind": " ", ## 종목종류@@
                "symbol": " ##SYMBOL@@"
            }
        },
        "output": {
            "t3521OutBlock": {
                "symbol": "symbol`char", ## 심벌@@
                "hname": "hname`char", ## 지수명@@
                "close": "close`float", ## 지수@@
                "sign": "sign`char", ## 대비구분@@
                "change": "change`float", ## 대비@@
                "diff": "diff`float", ## 등락율@@
                "date": "date`char##일자@@"
            }
        }
    },
    "t4201": { ## 주식챠트(종합)(t4201)
        "input": {
            "t4201InBlock": {
                "shcode": " ", ## 단축코드@@
                "gubun": " ", ## 주기구분@@0:틱1:분2:일3:주4:월
                "ncnt": "1", ## 틱개수@@
                "qrycnt": "2000", ## 건수(500건이하)@@
                "tdgb": " ", ## 당일구분@@0:전체1:당일만
                "sdate": " ", ## 시작일자@@
                "edate": " ", ## 종료일자@@
                "cts_date": " ", ## 연속일자@@
                "cts_time": " ", ## 연속시간@@
                "cts_daygb": " ##연속당일구분@@0:연속전체1:연속당일만2:연속전일만"
            }
        },
        "output": {
            "t4201OutBlock": {
                "shcode": "shcode`char", ## 단축코드@@
                "jisiga": "jisiga`long", ## 전일시가@@
                "jihigh": "jihigh`long", ## 전일고가@@
                "jilow": "jilow`long", ## 전일저가@@
                "jiclose": "jiclose`long", ## 전일종가@@
                "jivolume": "jivolume`long", ## 전일거래량@@
                "disiga": "disiga`long", ## 당일시가@@
                "dihigh": "dihigh`long", ## 당일고가@@
                "dilow": "dilow`long", ## 당일저가@@
                "diclose": "diclose`long", ## 당일종가@@
                "highend": "highend`long", ## 상한가@@
                "lowend": "lowend`long", ## 하한가@@
                "cts_date": "cts_date`char", ## 연속일자@@
                "cts_time": "cts_time`char", ## 연속시간@@
                "cts_daygb": "cts_daygb`char##연속당일구분@@"
            },
            "t4201OutBlock1": {
                "date": "date`char", ## 날짜@@
                "time": "time`char", ## 시간@@
                "open": "open`long", ## 시가@@
                "high": "high`long", ## 고가@@
                "low": "low`long", ## 저가@@
                "close": "close`long", ## 종가@@
                "jdiff_vol": "jdiff_vol`long", ## 거래량@@
                "value": "value`long", ## 거래대금@@
                "jongchk": "jongchk`long", ## 수정구분@@
                "rate": "rate`double", ## 수정비율@@
                "pricechk": "pricechk`long", ## 수정주가반영항목@@
                "ratevalue": "ratevalue`long##수정비율반영거래대금@@"
            }
        }
    },
    "t4203": { ## 업종챠트(종합)(t4203)
        "input": {
            "t4203InBlock": {
                "shcode": " ", ## 단축코드@@
                "gubun": " ", ## 주기구분@@0:틱1:분2:일3:주4:월
                "ncnt": "1", ## 틱개수@@
                "qrycnt": "2000", ## 건수@@
                "tdgb": " ", ## 당일구분@@0:전체1:당일만
                "sdate": " ", ## 시작일자@@
                "edate": " ", ## 종료일자@@
                "cts_date": " ", ## 연속일자@@
                "cts_time": " ", ## 연속시간@@
                "cts_daygb": " ##연속당일구분@@0:연속전체1:연속당일만2:연속전일만"
            }
        },
        "output": {
            "t4203OutBlock": {
                "shcode": "shcode`char", ## 단축코드@@
                "jisiga": "jisiga`float", ## 전일시가@@
                "jihigh": "jihigh`float", ## 전일고가@@
                "jilow": "jilow`float", ## 전일저가@@
                "jiclose": "jiclose`float", ## 전일종가@@
                "jivolume": "jivolume`long", ## 전일거래량@@
                "disiga": "disiga`float", ## 당일시가@@
                "dihigh": "dihigh`float", ## 당일고가@@
                "dilow": "dilow`float", ## 당일저가@@
                "diclose": "diclose`float", ## 당일종가@@
                "disvalue": "disvalue`long", ## 당일거래대금@@
                "cts_date": "cts_date`char", ## 연속일자@@
                "cts_time": "cts_time`char", ## 연속시간@@
                "cts_daygb": "cts_daygb`char##연속당일구분@@"
            },
            "t4203OutBlock1": {
                "date": "date`char", ## 날짜@@
                "time": "time`char", ## 시간@@
                "open": "open`float", ## 시가@@
                "high": "high`float", ## 고가@@
                "low": "low`float", ## 저가@@
                "close": "close`float", ## 종가@@
                "jdiff_vol": "jdiff_vol`long", ## 거래량@@
                "value": "value`long##거래대금@@"
            }
        }
    },
    "t8401": { ## 주식선물마스터조회(API용)(t8401)
        "input": {
            "t8401InBlock": {
                "dummy": " ##Dummy@@"
            }
        },
        "output": {
            "t8401OutBlock": {
                "hname": "hname`char", ## 종목명@@
                "shcode": "shcode`char", ## 단축코드@@
                "expcode": "expcode`char", ## 확장코드@@
                "basecode": "basecode`char##기초자산코드@@"
            }
        }
    },
    "t8402": { ## 주식선물현재가조회(API용)(t8402)
        "input": {
            "t8402InBlock": {
                "focode": " ##단축코드@@"
            }
        },
        "output": {
            "t8402OutBlock": {
                "hname": "hname`char", ## 한글명@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "jnilclose": "jnilclose`long", ## 전일종가@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 거래량@@
                "stimeqrt": "stimeqrt`double", ## 거래량전일동시간비율@@
                "value": "value`long", ## 거래대금@@
                "mgjv": "mgjv`long", ## 미결제량@@
                "mgjvdiff": "mgjvdiff`long", ## 미결제증감@@
                "open": "open`long", ## 시가@@
                "high": "high`long", ## 고가@@
                "low": "low`long", ## 저가@@
                "uplmtprice": "uplmtprice`long", ## 상한가@@
                "dnlmtprice": "dnlmtprice`long", ## 하한가@@
                "high52w": "high52w`long", ## 52최고가@@
                "low52w": "low52w`long", ## 52최저가@@
                "basis": "basis`float", ## 베이시스@@
                "recprice": "recprice`long", ## 기준가@@
                "theoryprice": "theoryprice`long", ## 이론가@@
                "glyl": "glyl`float", ## 괴리율@@
                "lastmonth": "lastmonth`char", ## 만기일@@
                "jandatecnt": "jandatecnt`long", ## 잔여일@@
                "pricejisu": "pricejisu`float", ## 종합지수@@
                "jisusign": "jisusign`char", ## 종합지수전일대비구분@@
                "jisuchange": "jisuchange`float", ## 종합지수전일대비@@
                "jisudiff": "jisudiff`float", ## 종합지수등락율@@
                "kospijisu": "kospijisu`float", ## KOSPI200지수@@
                "kospisign": "kospisign`char", ## KOSPI200전일대비구분@@
                "kospichange": "kospichange`float", ## KOSPI200전일대비@@
                "kospidiff": "kospidiff`float", ## KOSPI200등락율@@
                "listhprice": "listhprice`long", ## 상장최고가@@
                "listlprice": "listlprice`long", ## 상장최저가@@
                "delt": "delt`float", ## 델타@@
                "gama": "gama`float", ## 감마@@
                "ceta": "ceta`float", ## 세타@@
                "vega": "vega`float", ## 베가@@
                "rhox": "rhox`float", ## 로우@@
                "gmprice": "gmprice`long", ## 근월물현재가@@
                "gmsign": "gmsign`char", ## 근월물전일대비구분@@
                "gmchange": "gmchange`long", ## 근월물전일대비@@
                "gmdiff": "gmdiff`float", ## 근월물등락율@@
                "theorypriceg": "theorypriceg`long", ## 이론가@@
                "histimpv": "histimpv`float", ## 역사적변동성@@
                "impv": "impv`float", ## 내재변동성@@
                "sbasis": "sbasis`long", ## 시장BASIS@@
                "ibasis": "ibasis`long", ## 이론BASIS@@
                "gmfutcode": "gmfutcode`char", ## 근월물종목코드@@
                "actprice": "actprice`long", ## 행사가@@
                "shcode": "shcode`char", ## 기초자산단축코드@@
                "basehname": "basehname`char", ## 기초자산한글명@@
                "baseprice": "baseprice`long", ## 기초자산현재가@@
                "basesign": "basesign`char", ## 기초자산현재가대비구분@@
                "basechange": "basechange`long", ## 기초자산현재가전일대비@@
                "basediff": "basediff`float", ## 기초자산등락률@@
                "basevol": "basevol`long", ## 기초자산거래량@@
                "baseprevol": "baseprevol`long", ## 기초자산전일거래량@@
                "basebidprc": "basebidprc`long", ## 기초자산매수호가@@
                "baseaskprc": "baseaskprc`long", ## 기초자산매도호가@@
                "basefornetbid": "basefornetbid`long", ## 기초자산외국계회원사순매수@@
                "prodgrp": "prodgrp`char", ## 상품군@@
                "mulcnt": "mulcnt`float", ## 승수@@
                "danhochk": "danhochk`char", ## 단일가호가여부@@
                "yeprice": "yeprice`long", ## 예상체결가@@
                "jnilysign": "jnilysign`char", ## 예상체결가전일종가대비구분@@
                "jnilychange": "jnilychange`long", ## 예상체결가전일종가대비@@
                "jnilydrate": "jnilydrate`float##예상체결가전일종가등락율@@"
            }
        }
    },
    "t8403": { ## 주식선물호가조회(API용)(t8403)
        "input": {
            "t8403InBlock": {
                "shcode": " ##단축코드@@"
            }
        },
        "output": {
            "t8403OutBlock": {
                "hname": "hname`char", ## 종목명@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 거래량@@
                "stimeqrt": "stimeqrt`float", ## 거래량전일동시간비율@@
                "jnilclose": "jnilclose`long", ## 전일종가@@
                "offerho1": "offerho1`long", ## 매도호가1@@
                "bidho1": "bidho1`long", ## 매수호가1@@
                "offerrem1": "offerrem1`long", ## 매도호가수량1@@
                "bidrem1": "bidrem1`long", ## 매수호가수량1@@
                "dcnt1": "dcnt1`long", ## 매도호가건수1@@
                "scnt1": "scnt1`long", ## 매수호가건수1@@
                "offerho2": "offerho2`long", ## 매도호가2@@
                "bidho2": "bidho2`long", ## 매수호가2@@
                "offerrem2": "offerrem2`long", ## 매도호가수량2@@
                "bidrem2": "bidrem2`long", ## 매수호가수량2@@
                "dcnt2": "dcnt2`long", ## 매도호가건수2@@
                "scnt2": "scnt2`long", ## 매수호가건수2@@
                "offerho3": "offerho3`long", ## 매도호가3@@
                "bidho3": "bidho3`long", ## 매수호가3@@
                "offerrem3": "offerrem3`long", ## 매도호가수량3@@
                "bidrem3": "bidrem3`long", ## 매수호가수량3@@
                "dcnt3": "dcnt3`long", ## 매도호가건수3@@
                "scnt3": "scnt3`long", ## 매수호가건수3@@
                "offerho4": "offerho4`long", ## 매도호가4@@
                "bidho4": "bidho4`long", ## 매수호가4@@
                "offerrem4": "offerrem4`long", ## 매도호가수량4@@
                "bidrem4": "bidrem4`long", ## 매수호가수량4@@
                "dcnt4": "dcnt4`long", ## 매도호가건수4@@
                "scnt4": "scnt4`long", ## 매수호가건수4@@
                "offerho5": "offerho5`long", ## 매도호가5@@
                "bidho5": "bidho5`long", ## 매수호가5@@
                "offerrem5": "offerrem5`long", ## 매도호가수량5@@
                "bidrem5": "bidrem5`long", ## 매수호가수량5@@
                "dcnt5": "dcnt5`long", ## 매도호가건수5@@
                "scnt5": "scnt5`long", ## 매수호가건수5@@
                "offerho6": "offerho6`long", ## 매도호가6@@
                "bidho6": "bidho6`long", ## 매수호가6@@
                "offerrem6": "offerrem6`long", ## 매도호가수량6@@
                "bidrem6": "bidrem6`long", ## 매수호가수량6@@
                "dcnt6": "dcnt6`long", ## 매도호가건수6@@
                "scnt6": "scnt6`long", ## 매수호가건수6@@
                "offerho7": "offerho7`long", ## 매도호가7@@
                "bidho7": "bidho7`long", ## 매수호가7@@
                "offerrem7": "offerrem7`long", ## 매도호가수량7@@
                "bidrem7": "bidrem7`long", ## 매수호가수량7@@
                "dcnt7": "dcnt7`long", ## 매도호가건수7@@
                "scnt7": "scnt7`long", ## 매수호가건수7@@
                "offerho8": "offerho8`long", ## 매도호가8@@
                "bidho8": "bidho8`long", ## 매수호가8@@
                "offerrem8": "offerrem8`long", ## 매도호가수량8@@
                "bidrem8": "bidrem8`long", ## 매수호가수량8@@
                "dcnt8": "dcnt8`long", ## 매도호가건수8@@
                "scnt8": "scnt8`long", ## 매수호가건수8@@
                "offerho9": "offerho9`long", ## 매도호가9@@
                "bidho9": "bidho9`long", ## 매수호가9@@
                "offerrem9": "offerrem9`long", ## 매도호가수량9@@
                "bidrem9": "bidrem9`long", ## 매수호가수량9@@
                "dcnt9": "dcnt9`long", ## 매도호가건수9@@
                "scnt9": "scnt9`long", ## 매수호가건수9@@
                "offerho10": "offerho10`long", ## 매도호가10@@
                "bidho10": "bidho10`long", ## 매수호가10@@
                "offerrem10": "offerrem10`long", ## 매도호가수량10@@
                "bidrem10": "bidrem10`long", ## 매수호가수량10@@
                "dcnt10": "dcnt10`long", ## 매도호가건수10@@
                "scnt10": "scnt10`long", ## 매수호가건수10@@
                "dvol": "dvol`long", ## 매도호가총수량@@
                "svol": "svol`long", ## 매수호가총수량@@
                "toffernum": "toffernum`long", ## 총매도호가건수@@
                "tbidnum": "tbidnum`long", ## 총매수호가건수@@
                "time": "time`char", ## 수신시간@@
                "shcode": "shcode`char##단축코드@@"
            }
        }
    },
    "t8404": { ## 주식선물시간대별체결조회(API용)(t8404)
        "input": {
            "t8404InBlock": {
                "focode": " ", ## 단축코드@@
                "cvolume": "0", ## 특이거래량@@
                "stime": " ", ## 시작시간@@
                "etime": " ", ## 종료시간@@
                "cts_time": " ##시간CTS@@"
            }
        },
        "output": {
            "t8404OutBlock": {
                "cts_time": "cts_time`char##시간CTS@@"
            },
            "t8404OutBlock1": {
                "chetime": "chetime`char", ## 시간@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`float", ## 전일대비@@
                "cvolume": "cvolume`long", ## 체결수량@@
                "chdegree": "chdegree`float", ## 체결강도@@
                "offerho": "offerho`long", ## 매도호가@@
                "bidho": "bidho`long", ## 매수호가@@
                "volume": "volume`double", ## 거래량@@
                "openyak": "openyak`long", ## 미결수량@@
                "jnilopenupdn": "jnilopenupdn`long", ## 미결전일증감@@
                "ibasis": "ibasis`long", ## 이론BASIS@@
                "sbasis": "sbasis`long", ## 시장BASIS@@
                "kasis": "kasis`float", ## 괴리율@@
                "value": "value`double", ## 거래대금@@
                "j_openupdn": "j_openupdn`long", ## 미결직전증감@@
                "n_msvolume": "n_msvolume`double", ## 누적매수체결량@@
                "n_mdvolume": "n_mdvolume`double", ## 누적매도체결량@@
                "s_msvolume": "s_msvolume`double", ## 누적순매수체결량@@
                "n_mschecnt": "n_mschecnt`long", ## 누적매수체결건수@@
                "n_mdchecnt": "n_mdchecnt`long", ## 누적매도체결건수@@
                "s_mschecnt": "s_mschecnt`long##누적순매수체결건수@@"
            }
        }
    },
    "t8405": { ## 주식선물기간별주가(API용)(t8405)
        "input": {
            "t8405InBlock": {
                "shcode": " ", ## 단축코드@@
                "futcheck": " ", ## 선물최근월물@@
                "date": " ", ## 날짜@@
                "cts_code": " ", ## CTS종목코드@@
                "lastdate": " ", ## 전종목만기일@@
                "cnt": "0##조회요청건수@@"
            }
        },
        "output": {
            "t8405OutBlock": {
                "date": "date`char", ## 날짜@@
                "cts_code": "cts_code`char", ## CTS종목코드@@
                "lastdate": "lastdate`char", ## 전종목만기일@@
                "nowfutyn": "nowfutyn`char##최근월선물여부@@"
            },
            "t8405OutBlock1": {
                "date": "date`char", ## 날짜@@
                "open": "open`long", ## 시가@@
                "high": "high`long", ## 고가@@
                "low": "low`long", ## 저가@@
                "close": "close`long", ## 종가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 거래량@@
                "diff_vol": "diff_vol`float", ## 거래증가율@@
                "openyak": "openyak`long", ## 미결수량@@
                "openyakupdn": "openyakupdn`long", ## 미결증감@@
                "value": "value`float##거래대금@@"
            }
        }
    },
    "t8406": { ## 주식선물틱분별체결조회(API용)(t8406)
        "input": {
            "t8406InBlock": {
                "focode": " ", ## 단축코드@@
                "cgubun": " ", ## 챠트구분@@
                "bgubun": "0", ## 분구분@@
                "cnt": "0##조회건수@@"
            }
        },
        "output": {
            "t8406OutBlock1": {
                "chetime": "chetime`char", ## 시간@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "open": "open`long", ## 시가@@
                "high": "high`long", ## 고가@@
                "low": "low`long", ## 저가@@
                "volume": "volume`double", ## 거래량@@
                "value": "value`double", ## 거래대금@@
                "openyak": "openyak`long", ## 미결수량@@
                "openupdn": "openupdn`long", ## 미결증감@@
                "cvolume": "cvolume`long", ## 체결수량@@
                "s_mschecnt": "s_mschecnt`long", ## 매수순간체결건수@@
                "s_mdchecnt": "s_mdchecnt`long", ## 매도순간체결건수@@
                "ss_mschecnt": "ss_mschecnt`long", ## 순매수순간체결건수@@
                "s_mschevol": "s_mschevol`double", ## 매수순간체결량@@
                "s_mdchevol": "s_mdchevol`double", ## 매도순간체결량@@
                "ss_mschevol": "ss_mschevol`double", ## 순매수순간체결량@@
                "chdegvol": "chdegvol`float", ## 체결강도(거래량)@@
                "chdegcnt": "chdegcnt`float##체결강도(건수)@@"
            }
        }
    },
    "t8407": { ## API용주식멀티현재가조회(t8407)
        "input": {
            "t8407InBlock": {
                "nrec": "0", ## 건수@@
                "shcode": " ##종목코드@@"
            }
        },
        "output": {
            "t8407OutBlock1": {
                "shcode": "shcode`char", ## 종목코드@@
                "hname": "hname`char", ## 종목명@@
                "price": "price`long", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`long", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 누적거래량@@
                "offerho": "offerho`long", ## 매도호가@@
                "bidho": "bidho`long", ## 매수호가@@
                "cvolume": "cvolume`long", ## 체결수량@@
                "chdegree": "chdegree`float", ## 체결강도@@
                "open": "open`long", ## 시가@@
                "high": "high`long", ## 고가@@
                "low": "low`long", ## 저가@@
                "value": "value`long", ## 거래대금(백만)@@
                "offerrem": "offerrem`long", ## 우선매도잔량@@
                "bidrem": "bidrem`long", ## 우선매수잔량@@
                "totofferrem": "totofferrem`long", ## 총매도잔량@@
                "totbidrem": "totbidrem`long", ## 총매수잔량@@
                "jnilclose": "jnilclose`long", ## 전일종가@@
                "uplmtprice": "uplmtprice`long", ## 상한가@@
                "dnlmtprice": "dnlmtprice`long##하한가@@"
            }
        }
    },
    "t8411": { ## 주식챠트(틱/n틱)(t8411)
        "input": {
            "t8411InBlock": {
                "shcode": " ", ## 단축코드@@
                "ncnt": "1", ## 단위(n틱)@@
                "qrycnt": "2000", ## 요청건수@@최대-압축:2000비압축:500
                "nday": " ", ## 조회영업일수@@0:미사용1>=사용
                "sdate": " ", ## 시작일자@@
                "stime": " ", ## 시작시간(현재미사용)@@
                "edate": " ", ## 종료일자@@
                "etime": " ", ## 종료시간(현재미사용)@@
                "cts_date": " ", ## 연속일자@@
                "cts_time": " ", ## 연속시간@@
                "comp_yn": "Y##압축여부@@Y:압축N:비압축"
            }
        },
        "output": {
            "t8411OutBlock": {
                "shcode": "shcode`char", ## 단축코드@@
                "jisiga": "jisiga`long", ## 전일시가@@
                "jihigh": "jihigh`long", ## 전일고가@@
                "jilow": "jilow`long", ## 전일저가@@
                "jiclose": "jiclose`long", ## 전일종가@@
                "jivolume": "jivolume`long", ## 전일거래량@@
                "disiga": "disiga`long", ## 당일시가@@
                "dihigh": "dihigh`long", ## 당일고가@@
                "dilow": "dilow`long", ## 당일저가@@
                "diclose": "diclose`long", ## 당일종가@@
                "highend": "highend`long", ## 상한가@@
                "lowend": "lowend`long", ## 하한가@@
                "cts_date": "cts_date`char", ## 연속일자@@
                "cts_time": "cts_time`char", ## 연속시간@@
                "s_time": "s_time`char", ## 장시작시간(HHMMSS)@@
                "e_time": "e_time`char", ## 장종료시간(HHMMSS)@@
                "dshmin": "dshmin`char", ## 동시호가처리시간@@MM:분
                "rec_count": "rec_count`long##레코드카운트@@"
            },
            "t8411OutBlock1": {
                "date": "date`char", ## 날짜@@
                "time": "time`char", ## 시간@@
                "open": "open`long", ## 시가@@
                "high": "high`long", ## 고가@@
                "low": "low`long", ## 저가@@
                "close": "close`long", ## 종가@@
                "jdiff_vol": "jdiff_vol`long", ## 거래량@@
                "jongchk": "jongchk`long", ## 수정구분@@
                "rate": "rate`double", ## 수정비율@@
                "pricechk": "pricechk`long##수정주가반영항목@@"
            }
        }
    },
    "t8412": { ## 주식챠트(N분)(t8412)
        "input": {
            "t8412InBlock": {
                "shcode": " ", ## 단축코드@@
                "ncnt": "1", ## 단위(n분)@@
                "qrycnt": "2000", ## 요청건수@@최대-압축:2000비압축:500
                "nday": " ", ## 조회영업일수@@0:미사용1>=사용
                "sdate": " ", ## 시작일자@@
                "stime": " ", ## 시작시간(현재미사용)@@
                "edate": " ", ## 종료일자@@
                "etime": " ", ## 종료시간(현재미사용)@@
                "cts_date": " ", ## 연속일자@@
                "cts_time": " ", ## 연속시간@@
                "comp_yn": "Y##압축여부@@Y:압축N:비압축"
            }
        },
        "output": {
            "t8412OutBlock": {
                "shcode": "shcode`char", ## 단축코드@@
                "jisiga": "jisiga`long", ## 전일시가@@
                "jihigh": "jihigh`long", ## 전일고가@@
                "jilow": "jilow`long", ## 전일저가@@
                "jiclose": "jiclose`long", ## 전일종가@@
                "jivolume": "jivolume`long", ## 전일거래량@@
                "disiga": "disiga`long", ## 당일시가@@
                "dihigh": "dihigh`long", ## 당일고가@@
                "dilow": "dilow`long", ## 당일저가@@
                "diclose": "diclose`long", ## 당일종가@@
                "highend": "highend`long", ## 상한가@@
                "lowend": "lowend`long", ## 하한가@@
                "cts_date": "cts_date`char", ## 연속일자@@
                "cts_time": "cts_time`char", ## 연속시간@@
                "s_time": "s_time`char", ## 장시작시간(HHMMSS)@@
                "e_time": "e_time`char", ## 장종료시간(HHMMSS)@@
                "dshmin": "dshmin`char", ## 동시호가처리시간@@MM:분
                "rec_count": "rec_count`long##레코드카운트@@"
            },
            "t8412OutBlock1": {
                "date": "date`char", ## 날짜@@
                "time": "time`char", ## 시간@@
                "open": "open`long", ## 시가@@
                "high": "high`long", ## 고가@@
                "low": "low`long", ## 저가@@
                "close": "close`long", ## 종가@@
                "jdiff_vol": "jdiff_vol`long", ## 거래량@@
                "value": "value`long", ## 거래대금@@
                "jongchk": "jongchk`long", ## 수정구분@@
                "rate": "rate`double", ## 수정비율@@
                "sign": "sign`char##종가등락구분@@1:상한2:상승3:보합4:하한5:하락"
            }
        }
    },
    "t8413": { ## 주식챠트(일주월)(t8413)
        "input": {
            "t8413InBlock": {
                "shcode": " ", ## 단축코드@@
                "gubun": " ", ## 주기구분@@2:일3:주4:월
                "qrycnt": "2000", ## 요청건수@@최대-압축:2000비압축:500
                "sdate": " ", ## 시작일자@@
                "edate": " ", ## 종료일자@@
                "cts_date": " ", ## 연속일자@@
                "comp_yn": "Y##압축여부@@Y:압축N:비압축"
            }
        },
        "output": {
            "t8413OutBlock": {
                "shcode": "shcode`char", ## 단축코드@@
                "jisiga": "jisiga`long", ## 전일시가@@
                "jihigh": "jihigh`long", ## 전일고가@@
                "jilow": "jilow`long", ## 전일저가@@
                "jiclose": "jiclose`long", ## 전일종가@@
                "jivolume": "jivolume`long", ## 전일거래량@@
                "disiga": "disiga`long", ## 당일시가@@
                "dihigh": "dihigh`long", ## 당일고가@@
                "dilow": "dilow`long", ## 당일저가@@
                "diclose": "diclose`long", ## 당일종가@@
                "highend": "highend`long", ## 상한가@@
                "lowend": "lowend`long", ## 하한가@@
                "cts_date": "cts_date`char", ## 연속일자@@
                "s_time": "s_time`char", ## 장시작시간(HHMMSS)@@
                "e_time": "e_time`char", ## 장종료시간(HHMMSS)@@
                "dshmin": "dshmin`char", ## 동시호가처리시간@@MM:분
                "rec_count": "rec_count`long##레코드카운트@@"
            },
            "t8413OutBlock1": {
                "date": "date`char", ## 날짜@@
                "open": "open`long", ## 시가@@
                "high": "high`long", ## 고가@@
                "low": "low`long", ## 저가@@
                "close": "close`long", ## 종가@@
                "jdiff_vol": "jdiff_vol`long", ## 거래량@@
                "value": "value`long", ## 거래대금@@
                "jongchk": "jongchk`long", ## 수정구분@@
                "rate": "rate`double", ## 수정비율@@
                "pricechk": "pricechk`long", ## 수정주가반영항목@@
                "ratevalue": "ratevalue`long", ## 수정비율반영거래대금@@
                "sign": "sign`char##종가등락구분@@1:상한2:상승3:보합4:하한5:하락주식일만사용"
            }
        }
    },
    "t8414": { ## 선물옵션차트(틱/n틱)(t8414)
        "input": {
            "t8414InBlock": {
                "shcode": " ", ## 단축코드@@
                "ncnt": "1", ## 단위(n틱)@@
                "qrycnt": "2000", ## 요청건수@@최대-압축:2000비압축:500
                "nday": " ", ## 조회영업일수@@0:미사용1>=사용
                "sdate": " ", ## 시작일자@@
                "stime": " ", ## 시작시간(현재미사용)@@
                "edate": " ", ## 종료일자@@
                "etime": " ", ## 종료시간(현재미사용)@@
                "cts_date": " ", ## 연속일자@@
                "cts_time": " ", ## 연속시간@@
                "comp_yn": "Y##압축여부@@Y:압축N:비압축"
            }
        },
        "output": {
            "t8414OutBlock": {
                "shcode": "shcode`char", ## 단축코드@@
                "jisiga": "jisiga`float", ## 전일시가@@
                "jihigh": "jihigh`float", ## 전일고가@@
                "jilow": "jilow`float", ## 전일저가@@
                "jiclose": "jiclose`float", ## 전일종가@@
                "jivolume": "jivolume`long", ## 전일거래량@@
                "disiga": "disiga`float", ## 당일시가@@
                "dihigh": "dihigh`float", ## 당일고가@@
                "dilow": "dilow`float", ## 당일저가@@
                "diclose": "diclose`float", ## 당일종가@@
                "highend": "highend`float", ## 상한가@@
                "lowend": "lowend`float", ## 하한가@@
                "cts_date": "cts_date`char", ## 연속일자@@
                "cts_time": "cts_time`char", ## 연속시간@@
                "s_time": "s_time`char", ## 장시작시간(HHMMSS)@@
                "e_time": "e_time`char", ## 장종료시간(HHMMSS)@@
                "dshmin": "dshmin`char", ## 동시호가처리시간@@MM:분
                "rec_count": "rec_count`long##레코드카운트@@"
            },
            "t8414OutBlock1": {
                "date": "date`char", ## 날짜@@
                "time": "time`char", ## 시간@@
                "open": "open`float", ## 시가@@
                "high": "high`float", ## 고가@@
                "low": "low`float", ## 저가@@
                "close": "close`float", ## 종가@@
                "jdiff_vol": "jdiff_vol`long", ## 거래량@@
                "openyak": "openyak`long##미결제약정@@"
            }
        }
    },
    "t8415": { ## 선물/옵션챠트(N분)(t8415)
        "input": {
            "t8415InBlock": {
                "shcode": " ", ## 단축코드@@
                "ncnt": "1", ## 단위(n분)@@
                "qrycnt": "2000", ## 요청건수@@최대-압축:2000비압축:500
                "nday": " ", ## 조회영업일수@@0:미사용1>=사용
                "sdate": " ", ## 시작일자@@
                "stime": " ", ## 시작시간(현재미사용)@@
                "edate": " ", ## 종료일자@@
                "etime": " ", ## 종료시간(현재미사용)@@
                "cts_date": " ", ## 연속일자@@
                "cts_time": " ", ## 연속시간@@
                "comp_yn": "Y##압축여부@@Y:압축N:비압축"
            }
        },
        "output": {
            "t8415OutBlock": {
                "shcode": "shcode`char", ## 단축코드@@
                "jisiga": "jisiga`float", ## 전일시가@@
                "jihigh": "jihigh`float", ## 전일고가@@
                "jilow": "jilow`float", ## 전일저가@@
                "jiclose": "jiclose`float", ## 전일종가@@
                "jivolume": "jivolume`long", ## 전일거래량@@
                "disiga": "disiga`float", ## 당일시가@@
                "dihigh": "dihigh`float", ## 당일고가@@
                "dilow": "dilow`float", ## 당일저가@@
                "diclose": "diclose`float", ## 당일종가@@
                "highend": "highend`float", ## 상한가@@
                "lowend": "lowend`float", ## 하한가@@
                "cts_date": "cts_date`char", ## 연속일자@@
                "cts_time": "cts_time`char", ## 연속시간@@
                "s_time": "s_time`char", ## 장시작시간(HHMMSS)@@
                "e_time": "e_time`char", ## 장종료시간(HHMMSS)@@
                "dshmin": "dshmin`char", ## 동시호가처리시간@@MM:분
                "rec_count": "rec_count`long##레코드카운트@@"
            },
            "t8415OutBlock1": {
                "date": "date`char", ## 날짜@@
                "time": "time`char", ## 시간@@
                "open": "open`float", ## 시가@@
                "high": "high`float", ## 고가@@
                "low": "low`float", ## 저가@@
                "close": "close`float", ## 종가@@
                "jdiff_vol": "jdiff_vol`long", ## 누적거래량@@
                "value": "value`long", ## 거래대금@@
                "openyak": "openyak`long##미결제약정@@"
            }
        }
    },
    "t8416": { ## 선물/옵션챠트(일주월)(t8416)
        "input": {
            "t8416InBlock": {
                "shcode": " ", ## 단축코드@@
                "gubun": " ", ## 주기구분@@2:일3:주4:월
                "qrycnt": "2000", ## 요청건수@@최대-압축:2000비압축:500
                "sdate": " ", ## 시작일자@@
                "edate": " ", ## 종료일자@@
                "cts_date": " ", ## 연속일자@@
                "comp_yn": "Y##압축여부@@Y:압축N:비압축"
            }
        },
        "output": {
            "t8416OutBlock": {
                "shcode": "shcode`char", ## 단축코드@@
                "jisiga": "jisiga`float", ## 전일시가@@
                "jihigh": "jihigh`float", ## 전일고가@@
                "jilow": "jilow`float", ## 전일저가@@
                "jiclose": "jiclose`float", ## 전일종가@@
                "jivolume": "jivolume`long", ## 전일거래량@@
                "disiga": "disiga`float", ## 당일시가@@
                "dihigh": "dihigh`float", ## 당일고가@@
                "dilow": "dilow`float", ## 당일저가@@
                "diclose": "diclose`float", ## 당일종가@@
                "highend": "highend`float", ## 상한가@@
                "lowend": "lowend`float", ## 하한가@@
                "cts_date": "cts_date`char", ## 연속일자@@
                "s_time": "s_time`char", ## 장시작시간(HHMMSS)@@
                "e_time": "e_time`char", ## 장종료시간(HHMMSS)@@
                "dshmin": "dshmin`char", ## 동시호가처리시간@@MM:분
                "rec_count": "rec_count`long##레코드카운트@@"
            },
            "t8416OutBlock1": {
                "date": "date`char", ## 날짜@@
                "open": "open`float", ## 시가@@
                "high": "high`float", ## 고가@@
                "low": "low`float", ## 저가@@
                "close": "close`float", ## 종가@@
                "jdiff_vol": "jdiff_vol`long", ## 누적거래량@@
                "value": "value`long", ## 거래대금@@
                "openyak": "openyak`long##미결제약정@@"
            }
        }
    },
    "t8417": { ## 업종차트(틱/n틱)(t8417)
        "input": {
            "t8417InBlock": {
                "shcode": " ", ## 단축코드@@
                "ncnt": "1", ## 단위(n틱)@@
                "qrycnt": "2000", ## 요청건수@@최대-압축:2000비압축:500
                "nday": " ", ## 조회영업일수@@0:미사용1>=사용
                "sdate": " ", ## 시작일자@@
                "stime": " ", ## 시작시간(현재미사용)@@
                "edate": " ", ## 종료일자@@
                "etime": " ", ## 종료시간(현재미사용)@@
                "cts_date": " ", ## 연속일자@@
                "cts_time": " ", ## 연속시간@@
                "comp_yn": "Y##압축여부@@Y:압축N:비압축"
            }
        },
        "output": {
            "t8417OutBlock": {
                "shcode": "shcode`char", ## 단축코드@@
                "jisiga": "jisiga`float", ## 전일시가@@
                "jihigh": "jihigh`float", ## 전일고가@@
                "jilow": "jilow`float", ## 전일저가@@
                "jiclose": "jiclose`float", ## 전일종가@@
                "jivolume": "jivolume`long", ## 전일거래량@@
                "disiga": "disiga`float", ## 당일시가@@
                "dihigh": "dihigh`float", ## 당일고가@@
                "dilow": "dilow`float", ## 당일저가@@
                "diclose": "diclose`float", ## 당일종가@@
                "cts_date": "cts_date`char", ## 연속일자@@
                "cts_time": "cts_time`char", ## 연속시간@@
                "s_time": "s_time`char", ## 장시작시간(HHMMSS)@@
                "e_time": "e_time`char", ## 장종료시간(HHMMSS)@@
                "dshmin": "dshmin`char", ## 동시호가처리시간@@MM:분
                "rec_count": "rec_count`long##레코드카운트@@"
            },
            "t8417OutBlock1": {
                "date": "date`char", ## 날짜@@
                "time": "time`char", ## 시간@@
                "open": "open`float", ## 시가@@
                "high": "high`float", ## 고가@@
                "low": "low`float", ## 저가@@
                "close": "close`float", ## 종가@@
                "jdiff_vol": "jdiff_vol`long##거래량@@"
            }
        }
    },
    "t8418": { ## 업종챠트(N분)(t8418)
        "input": {
            "t8418InBlock": {
                "shcode": " ", ## 단축코드@@
                "ncnt": "1", ## 단위(n분)@@
                "qrycnt": "2000", ## 요청건수@@최대-압축:2000비압축:500
                "nday": " ", ## 조회영업일수@@0:미사용1>=사용
                "sdate": " ", ## 시작일자@@
                "stime": " ", ## 시작시간(현재미사용)@@
                "edate": " ", ## 종료일자@@
                "etime": " ", ## 종료시간(현재미사용)@@
                "cts_date": " ", ## 연속일자@@
                "cts_time": " ", ## 연속시간@@
                "comp_yn": "Y##압축여부@@Y:압축N:비압축"
            }
        },
        "output": {
            "t8418OutBlock": {
                "shcode": "shcode`char", ## 단축코드@@
                "jisiga": "jisiga`float", ## 전일시가@@
                "jihigh": "jihigh`float", ## 전일고가@@
                "jilow": "jilow`float", ## 전일저가@@
                "jiclose": "jiclose`float", ## 전일종가@@
                "jivolume": "jivolume`long", ## 전일거래량@@
                "disiga": "disiga`float", ## 당일시가@@
                "dihigh": "dihigh`float", ## 당일고가@@
                "dilow": "dilow`float", ## 당일저가@@
                "diclose": "diclose`float", ## 당일종가@@
                "disvalue": "disvalue`long", ## 당일거래대금@@
                "cts_date": "cts_date`char", ## 연속일자@@
                "cts_time": "cts_time`char", ## 연속시간@@
                "s_time": "s_time`char", ## 업종시작시간(HHMMSS)@@
                "e_time": "e_time`char", ## 업종종료시간(HHMMSS)@@
                "dshmin": "dshmin`char", ## 동시호가처리시간@@MM:분
                "rec_count": "rec_count`long##레코드카운트@@"
            },
            "t8418OutBlock1": {
                "date": "date`char", ## 날짜@@
                "time": "time`char", ## 시간@@
                "open": "open`float", ## 시가@@
                "high": "high`float", ## 고가@@
                "low": "low`float", ## 저가@@
                "close": "close`float", ## 종가@@
                "jdiff_vol": "jdiff_vol`long", ## 거래량@@
                "value": "value`long##거래대금@@"
            }
        }
    },
    "t8419": { ## 업종챠트(일주월)(t8419)
        "input": {
            "t8419InBlock": {
                "shcode": " ", ## 단축코드@@
                "gubun": " ", ## 주기구분@@2:일3:주4:월
                "qrycnt": "2000", ## 요청건수@@최대-압축:2000비압축:500
                "sdate": " ", ## 시작일자@@
                "edate": " ", ## 종료일자@@
                "cts_date": " ", ## 연속일자@@
                "comp_yn": "Y##압축여부@@Y:압축N:비압축"
            }
        },
        "output": {
            "t8419OutBlock": {
                "shcode": "shcode`char", ## 단축코드@@
                "jisiga": "jisiga`float", ## 전일시가@@
                "jihigh": "jihigh`float", ## 전일고가@@
                "jilow": "jilow`float", ## 전일저가@@
                "jiclose": "jiclose`float", ## 전일종가@@
                "jivolume": "jivolume`long", ## 전일거래량@@
                "disiga": "disiga`float", ## 당일시가@@
                "dihigh": "dihigh`float", ## 당일고가@@
                "dilow": "dilow`float", ## 당일저가@@
                "diclose": "diclose`float", ## 당일종가@@
                "disvalue": "disvalue`long", ## 당일거래대금@@
                "cts_date": "cts_date`char", ## 연속일자@@
                "s_time": "s_time`char", ## 업종시작시간@@
                "e_time": "e_time`char", ## 업종종료시간@@
                "dshmin": "dshmin`char", ## 동시호가처리시간@@MM:분
                "rec_count": "rec_count`long##레코드카운트@@"
            },
            "t8419OutBlock1": {
                "date": "date`char", ## 날짜@@
                "open": "open`float", ## 시가@@
                "high": "high`float", ## 고가@@
                "low": "low`float", ## 저가@@
                "close": "close`float", ## 종가@@
                "jdiff_vol": "jdiff_vol`long", ## 거래량@@
                "value": "value`long##거래대금@@"
            }
        }
    },
    "t8424": { ## 전체업종(t8424)
        "input": {
            "t8424InBlock": {
                "gubun1": " ##구분1@@"
            }
        },
        "output": {
            "t8424OutBlock": {
                "hname": "hname`char", ## 업종명@@
                "upcode": "upcode`char##업종코드@@"
            }
        }
    },
    "t8425": { ## 전체테마(t8425)
        "input": {
            "t8425InBlock": {
                "dummy": " ##Dummy@@"
            }
        },
        "output": {
            "t8425OutBlock": {
                "tmname": "tmname`char", ## 테마명@@
                "tmcode": "tmcode`char##테마코드@@"
            }
        }
    },
    "t8426": { ## 상품선물마스터조회(API용)(t8426)
        "input": {
            "t8426InBlock": {
                "dummy": " ##Dummy@@"
            }
        },
        "output": {
            "t8426OutBlock": {
                "hname": "hname`char", ## 종목명@@
                "shcode": "shcode`char", ## 단축코드@@
                "expcode": "expcode`char##확장코드@@"
            }
        }
    },
    "t8427": { ## 과거데이터시간대별조회(t8427)
        "input": {
            "t8427InBlock": {
                "fo_gbn": " ", ## 선물옵션구분@@
                "yyyy": " ", ## 조회년도@@
                "mm": " ", ## 조회월@@
                "cp_gbn": " ", ## 옵션콜풋구분@@
                "actprice": "0.0", ## 옵션행사가@@
                "focode": " ", ## 선물옵션코드@@
                "dt_gbn": " ", ## 일분구분@@
                "min_term": " ", ## 분간격@@
                "date": " ", ## 날짜@@
                "time": " ##시간@@"
            }
        },
        "output": {
            "t8427OutBlock": {
                "focode": "focode`char", ## 선물옵션코드@@
                "date": "date`char", ## 날짜@@
                "time": "time`char##시간@@"
            },
            "t8427OutBlock1": {
                "date": "date`char", ## 날짜@@
                "time": "time`char", ## 시간@@
                "open": "open`float", ## 시가@@
                "high": "high`float", ## 고가@@
                "low": "low`float", ## 저가@@
                "close": "close`float", ## 종가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`float", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 거래량@@
                "diff_vol": "diff_vol`float", ## 거래증가율@@
                "openyak": "openyak`long", ## 미결수량@@
                "openyakupdn": "openyakupdn`long", ## 미결증감@@
                "value": "value`float##거래대금@@"
            }
        }
    },
    "t8428": { ## 증시주변자금추이(t8428)
        "input": {
            "t8428InBlock": {
                "fdate": " ", ## from일자@@
                "tdate": " ", ## to일자@@
                "gubun": " ", ## 구분@@
                "key_date": " ", ## 날짜@@
                "upcode": " ", ## 업종코드@@
                "cnt": "0##조회건수@@"
            }
        },
        "output": {
            "t8428OutBlock": {
                "date": "date`char", ## 날짜CTS@@
                "idx": "idx`long##IDX@@"
            },
            "t8428OutBlock1": {
                "date": "date`char", ## 일자@@
                "jisu": "jisu`float", ## 지수@@
                "sign": "sign`char", ## 대비구분@@
                "change": "change`float", ## 대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 거래량@@
                "custmoney": "custmoney`long", ## 고객예탁금_억원@@
                "yecha": "yecha`long", ## 예탁증감_억원@@
                "vol": "vol`float", ## 회전율@@
                "outmoney": "outmoney`long", ## 미수금_억원@@
                "trjango": "trjango`long", ## 신용잔고_억원@@
                "futymoney": "futymoney`long", ## 선물예수금_억원@@
                "stkmoney": "stkmoney`long", ## 주식형_억원@@
                "mstkmoney": "mstkmoney`long", ## 혼합형_억원(주식)@@
                "mbndmoney": "mbndmoney`long", ## 혼합형_억원(채권)@@
                "bndmoney": "bndmoney`long", ## 채권형_억원@@
                "bndsmoney": "bndsmoney`long", ## 필러(구.단기채권)@@
                "mmfmoney": "mmfmoney`long##MMF_억원(주식)@@"
            }
        }
    },
    "t8429": { ## EUREX야간옵션선물틱분별체결조회챠트(t8429)
        "input": {
            "t8429InBlock": {
                "focode": " ", ## 단축코드@@
                "cgubun": " ", ## 챠트구분@@
                "bgubun": "0", ## 분구분@@
                "cnt": "0##조회건수@@"
            }
        },
        "output": {
            "t8429OutBlock1": {
                "chetime": "chetime`char", ## 시간@@
                "price": "price`float", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`float", ## 전일대비@@
                "open": "open`float", ## 시가@@
                "high": "high`float", ## 고가@@
                "low": "low`float", ## 저가@@
                "volume": "volume`double", ## 거래량@@
                "cvolume": "cvolume`long", ## 체결수량@@
                "s_mschecnt": "s_mschecnt`long", ## 매수순간체결건수@@
                "s_mdchecnt": "s_mdchecnt`long", ## 매도순간체결건수@@
                "ss_mschecnt": "ss_mschecnt`long", ## 순매수순간체결건수@@
                "s_mschevol": "s_mschevol`double", ## 매수순간체결량@@
                "s_mdchevol": "s_mdchevol`double", ## 매도순간체결량@@
                "ss_mschevol": "ss_mschevol`double", ## 순매수순간체결량@@
                "chdegvol": "chdegvol`float", ## 체결강도(거래량)@@
                "chdegcnt": "chdegcnt`float##체결강도(건수)@@"
            }
        }
    },
    "t8430": { ## 주식종목조회(t8430)
        "input": {
            "t8430InBlock": {
                "gubun": " ##구분@@0:전체1:코스피2:코스닥"
            }
        },
        "output": {
            "t8430OutBlock": {
                "hname": "hname`char", ## 종목명@@
                "shcode": "shcode`char", ## 단축코드@@
                "expcode": "expcode`char", ## 확장코드@@
                "etfgubun": "etfgubun`char", ## ETF구분@@1:ETF
                "uplmtprice": "uplmtprice`long", ## 상한가@@
                "dnlmtprice": "dnlmtprice`long", ## 하한가@@
                "jnilclose": "jnilclose`long", ## 전일가@@
                "memedan": "memedan`char", ## 주문수량단위@@
                "recprice": "recprice`long", ## 기준가@@
                "gubun": "gubun`char##구분@@1:코스피2:코스닥"
            }
        }
    },
    "t8431": { ## ELW종목조회(t8431)
        "input": {
            "t8431InBlock": {
                "dummy": " ##Dummy@@"
            }
        },
        "output": {
            "t8431OutBlock": {
                "hname": "hname`char", ## 종목명@@
                "shcode": "shcode`char", ## 단축코드@@
                "expcode": "expcode`char", ## 확장코드@@
                "uplmtprice": "uplmtprice`long", ## 상한가@@
                "dnlmtprice": "dnlmtprice`long", ## 하한가@@
                "jnilclose": "jnilclose`long", ## 전일종가@@
                "recprice": "recprice`long##기준가@@"
            }
        }
    },
    "t8432": { ## 지수선물마스터조회API용(t8432)
        "input": {
            "t8432InBlock": {
                "gubun": " ##구분@@"
            }
        },
        "output": {
            "t8432OutBlock": {
                "hname": "hname`char", ## 종목명@@
                "shcode": "shcode`char", ## 단축코드@@
                "expcode": "expcode`char", ## 확장코드@@
                "uplmtprice": "uplmtprice`float", ## 상한가@@
                "dnlmtprice": "dnlmtprice`float", ## 하한가@@
                "jnilclose": "jnilclose`float", ## 전일종가@@
                "jnilhigh": "jnilhigh`float", ## 전일고가@@
                "jnillow": "jnillow`float", ## 전일저가@@
                "recprice": "recprice`float##기준가@@"
            }
        }
    },
    "t8433": { ## 지수옵션마스터조회API용(t8433)
        "input": {
            "t8433InBlock": {
                "dummy": " ##Dummy@@"
            }
        },
        "output": {
            "t8433OutBlock": {
                "hname": "hname`char", ## 종목명@@
                "shcode": "shcode`char", ## 단축코드@@
                "expcode": "expcode`char", ## 확장코드@@
                "hprice": "hprice`float", ## 상한가@@
                "lprice": "lprice`float", ## 하한가@@
                "jnilclose": "jnilclose`float", ## 전일종가@@
                "jnilhigh": "jnilhigh`float", ## 전일고가@@
                "jnillow": "jnillow`float", ## 전일저가@@
                "recprice": "recprice`float##기준가@@"
            }
        }
    },
    "t8434": { ## 선물/옵션멀티현재가조회(t8434)
        "input": {
            "t8434InBlock": {
                "qrycnt": "2000", ## 건수@@
                "focode": " ##단축코드@@"
            }
        },
        "output": {
            "t8434OutBlock1": {
                "hname": "hname`char", ## 한글명@@
                "price": "price`float", ## 현재가@@
                "sign": "sign`char", ## 전일대비구분@@
                "change": "change`float", ## 전일대비@@
                "diff": "diff`float", ## 등락율@@
                "volume": "volume`long", ## 누적거래량@@
                "checnt": "checnt`long", ## 체결건수@@
                "focode": "focode`char##단축코드@@"
            }
        }
    },
    "t8435": { ## 파생종목마스터조회API용(t8435)
        "input": {
            "t8435InBlock": {
                "gubun": " ##구분(MF/MO)@@"
            }
        },
        "output": {
            "t8435OutBlock": {
                "hname": "hname`char", ## 종목명@@
                "shcode": "shcode`char", ## 단축코드@@
                "expcode": "expcode`char", ## 확장코드@@
                "uplmtprice": "uplmtprice`float", ## 상한가@@
                "dnlmtprice": "dnlmtprice`float", ## 하한가@@
                "jnilclose": "jnilclose`float", ## 전일종가@@
                "jnilhigh": "jnilhigh`float", ## 전일고가@@
                "jnillow": "jnillow`float", ## 전일저가@@
                "recprice": "recprice`float##기준가@@"
            }
        }
    },
    "t8436": { ## 주식종목조회 API용(t8436)
        "input": {
            "t8436InBlock": {
                "gubun": " ##구분@@0:전체1:코스피2:코스닥"
            }
        },
        "output": {
            "t8436OutBlock": {
                "hname": "hname`char", ## 종목명@@
                "shcode": "shcode`char", ## 단축코드@@
                "expcode": "expcode`char", ## 확장코드@@
                "etfgubun": "etfgubun`char", ## ETF구분@@1:ETF2:ETN
                "uplmtprice": "uplmtprice`long", ## 상한가@@
                "dnlmtprice": "dnlmtprice`long", ## 하한가@@
                "jnilclose": "jnilclose`long", ## 전일가@@
                "memedan": "memedan`char", ## 주문수량단위@@
                "recprice": "recprice`long", ## 기준가@@
                "gubun": "gubun`char", ## 구분@@1:코스피2:코스닥
                "bu12gubun": "bu12gubun`char", ## 증권그룹@@
                "spac_gubun": "spac_gubun`char", ## 기업인수목적회사여부(Y/N)@@
                "filler": "filler`char##filler(미사용)@@"
            }
        }
    },
    "t8437": { ## CME/EUREX마스터조회(API용)(t8437)
        "input": {
            "t8437InBlock": {
                "gubun": " ##구분(NF/NC/NM/NO)@@"
            }
        },
        "output": {
            "t8437OutBlock": {
                "hname": "hname`char", ## 종목명@@
                "shcode": "shcode`char", ## 종목코드@@
                "expcode": "expcode`char", ## 표준코드@@
                "tradeunit": "tradeunit`float", ## 거래승수@@
                "atmgb": "atmgb`char##ATM구분@@1:ATM2:ITM3:OTM"
            }
        }
    },
    "t9905": { ## 기초자산리스트조회(t9905)
        "input": {
            "t9905InBlock": {
                "dummy": " ##DUMMY@@"
            }
        },
        "output": {
            "t9905OutBlock1": {
                "shcode": "shcode`char", ## 단축코드@@
                "expcode": "expcode`char", ## 표준코드@@
                "hname": "hname`char##종목명@@"
            }
        }
    },
    "t9907": { ## 만기월조회(t9907)
        "input": {
            "t9907InBlock": {
                "dummy": " ##DUMMY@@"
            }
        },
        "output": {
            "t9907OutBlock1": {
                "lastym": "lastym`char", ## 만기월@@
                "lastnm": "lastnm`char##만기월명@@"
            }
        }
    },
    "t9942": { ## ELW마스터조회API용(t9942)
        "input": {
            "t9942InBlock": {
                "dummy": " ##Dummy@@"
            }
        },
        "output": {
            "t9942OutBlock": {
                "hname": "hname`char", ## 종목명@@
                "shcode": "shcode`char", ## 단축코드@@
                "expcode": "expcode`char##확장코드@@"
            }
        }
    },
    "t9943": { ## 지수선물마스터조회API용(t9943)
        "input": {
            "t9943InBlock": {
                "gubun": " ##구분@@"
            }
        },
        "output": {
            "t9943OutBlock": {
                "hname": "hname`char", ## 종목명@@
                "shcode": "shcode`char", ## 단축코드@@
                "expcode": "expcode`char##확장코드@@"
            }
        }
    },
    "t9944": { ## 지수옵션마스터조회API용(t9944)
        "input": {
            "t9944InBlock": {
                "dummy": " ##Dummy@@"
            }
        },
        "output": {
            "t9944OutBlock": {
                "hname": "hname`char", ## 종목명@@
                "shcode": "shcode`char", ## 단축코드@@
                "expcode": "expcode`char##확장코드@@"
            }
        }
    },
    "t9945": { ## 주식마스터조회API용-종목명40bytes(t9945)
        "input": {
            "t9945InBlock": {
                "gubun": " ##구분@@KSP:1KSD:2"
            }
        },
        "output": {
            "t9945OutBlock": {
                "hname": "hname`char", ## 종목명@@
                "shcode": "shcode`char", ## 단축코드@@
                "expcode": "expcode`char", ## 확장코드@@
                "etfchk": "etfchk`char", ## ETF구분@@
                "filler": "filler`char##filler@@"
            }
        }
    },
    "TC1": { ## 해외선물주문
        "input": {
            "InBlock": {}
        },
        "output": {
            "OutBlock": {
                "lineseq": "lineseq`long", ## 라인일련번호@@
                "key": "key`char", ## KEY@@
                "user": "user`char", ## 조작자ID@@
                "svc_id": "svc_id`char", ## 서비스ID@@
                "ordr_dt": "ordr_dt`char", ## 주문일자@@
                "brn_cd": "brn_cd`char", ## 지점번호@@
                "ordr_no": "ordr_no`long", ## 주문번호@@
                "orgn_ordr_no": "orgn_ordr_no`long", ## 원주문번호@@
                "mthr_ordr_no": "mthr_ordr_no`long", ## 모주문번호@@
                "ac_no": "ac_no`char", ## 계좌번호@@
                "is_cd": "is_cd`char", ## 종목코드@@
                "s_b_ccd": "s_b_ccd`char", ## 매도매수유형@@
                "ordr_ccd": "ordr_ccd`char", ## 정정취소유형@@
                "ordr_typ_cd": "ordr_typ_cd`char", ## 주문유형코드@@
                "ordr_typ_prd_ccd": "ordr_typ_prd_ccd`char", ## 주문기간코드@@
                "ordr_aplc_strt_dt": "ordr_aplc_strt_dt`char", ## 주문적용시작일자@@
                "ordr_aplc_end_dt": "ordr_aplc_end_dt`char", ## 주문적용종료일자@@
                "ordr_prc": "ordr_prc`double", ## 주문가격@@
                "cndt_ordr_prc": "cndt_ordr_prc`double", ## 주문조건가격@@
                "ordr_q": "ordr_q`long", ## 주문수량@@
                "ordr_tm": "ordr_tm`char", ## 주문시간@@
                "userid": "userid`char", ## 사용자ID@@
                "xrc_rsv_tcp_code": "xrc_rsv_tcp_code`char##만기행사유무@@"
            }
        }
    },
    "TC2": { ## 해외선물응답
        "input": {
            "InBlock": {}
        },
        "output": {
            "OutBlock": {
                "lineseq": "lineseq`long", ## 라인일련번호@@
                "key": "key`char", ## KEY@@
                "user": "user`char", ## 조작자ID@@
                "svc_id": "svc_id`char", ## 서비스ID@@
                "ordr_dt": "ordr_dt`char", ## 주문일자@@
                "brn_cd": "brn_cd`char", ## 지점번호@@
                "ordr_no": "ordr_no`long", ## 주문번호@@
                "orgn_ordr_no": "orgn_ordr_no`long", ## 원주문번호@@
                "mthr_ordr_no": "mthr_ordr_no`long", ## 모주문번호@@
                "ac_no": "ac_no`char", ## 계좌번호@@
                "is_cd": "is_cd`char", ## 종목코드@@
                "s_b_ccd": "s_b_ccd`char", ## 매도매수유형@@
                "ordr_ccd": "ordr_ccd`char", ## 정정취소유형@@
                "ordr_typ_cd": "ordr_typ_cd`char", ## 주문유형코드@@
                "ordr_typ_prd_ccd": "ordr_typ_prd_ccd`char", ## 주문기간코드@@
                "ordr_aplc_strt_dt": "ordr_aplc_strt_dt`char", ## 주문적용시작일자@@
                "ordr_aplc_end_dt": "ordr_aplc_end_dt`char", ## 주문적용종료일자@@
                "ordr_prc": "ordr_prc`double", ## 주문가격@@
                "cndt_ordr_prc": "cndt_ordr_prc`double", ## 주문조건가격@@
                "ordr_q": "ordr_q`long", ## 주문수량@@
                "ordr_tm": "ordr_tm`char", ## 주문시간@@
                "cnfr_q": "cnfr_q`long", ## 호가확인수량@@
                "rfsl_cd": "rfsl_cd`char", ## 호가거부사유코드@@
                "text": "text`char", ## 호가거부사유코드명@@
                "user_id": "user_id`char##사용자ID@@"
            }
        }
    },
    "TC3": { ## 해외선물체결
        "input": {
            "InBlock": {}
        },
        "output": {
            "OutBlock": {
                "lineseq": "lineseq`long", ## 라인일련번호@@
                "key": "key`char", ## KEY@@
                "user": "user`char", ## 조작자ID@@
                "svc_id": "svc_id`char", ## 서비스ID@@
                "ordr_dt": "ordr_dt`char", ## 주문일자@@
                "brn_cd": "brn_cd`char", ## 지점번호@@
                "ordr_no": "ordr_no`long", ## 주문번호@@
                "orgn_ordr_no": "orgn_ordr_no`long", ## 원주문번호@@
                "mthr_ordr_no": "mthr_ordr_no`long", ## 모주문번호@@
                "ac_no": "ac_no`char", ## 계좌번호@@
                "is_cd": "is_cd`char", ## 종목코드@@
                "s_b_ccd": "s_b_ccd`char", ## 매도매수유형@@
                "ordr_ccd": "ordr_ccd`char", ## 정정취소유형@@
                "ccls_q": "ccls_q`long", ## 체결수량@@
                "ccls_prc": "ccls_prc`double", ## 체결가격@@
                "ccls_no": "ccls_no`char", ## 체결번호@@
                "ccls_tm": "ccls_tm`char", ## 체결시간@@
                "avg_byng_uprc": "avg_byng_uprc`double", ## 매입평균단가@@
                "byug_amt": "byug_amt`double", ## 매입금액@@
                "clr_pl_amt": "clr_pl_amt`double", ## 청산손익@@
                "ent_fee": "ent_fee`double", ## 위탁수수료@@
                "fcm_fee": "fcm_fee`long", ## 매입잔고수량@@
                "userid": "userid`char", ## 사용자ID@@
                "now_prc": "now_prc`double", ## 현재가격@@
                "crncy_cd": "crncy_cd`char", ## 통화코드@@
                "mtrt_dt": "mtrt_dt`char", ## 만기일자@@
                "ord_prdt_tp_code": "ord_prdt_tp_code`char", ## 주문상품구분코드@@
                "exec_prdt_tp_code": "exec_prdt_tp_code`char", ## 주문상품구분코드@@
                "sprd_base_isu_yn": "sprd_base_isu_yn`char", ## 스프레드종목여부@@
                "filler1": "filler1`char", ## FILLER1@@
                "filler2": "filler2`char", ## FILLER2@@
                "sprd_is_cd": "sprd_is_cd`char##스프레드종목코드@@"
            }
        }
    },
    "VI_": { ## VI발동해제(VI_)
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
                "ref_shcode": "ref_shcode`char", ## 참조코드@@
                "time": "time`char##시간@@"
            }
        }
    },
    "WOC": { ## 해외옵션 현재가체결(WOC)
        "input": {
            "InBlock": {
                "symbol": " ##종목코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "symbol": "symbol`char", ## 종목코드@@
                "ovsdate": "ovsdate`char", ## 체결일자(현지)@@
                "kordate": "kordate`char", ## 체결일자(한국)@@
                "trdtm": "trdtm`char", ## 체결시간(현지)@@
                "kortm": "kortm`char", ## 체결시간(한국)@@
                "curpr": "curpr`double", ## 체결가격@@
                "ydiffpr": "ydiffpr`double", ## 전일대비@@
                "ydiffSign": "ydiffSign`char", ## 전일대비기호@@
                "open": "open`double", ## 시가@@
                "high": "high`double", ## 고가@@
                "low": "low`double", ## 저가@@
                "chgrate": "chgrate`float", ## 등락율@@
                "trdq": "trdq`long", ## 건별체결수량@@
                "totq": "totq`char", ## 누적체결수량@@
                "cgubun": "cgubun`char", ## 체결구분@@
                "mdvolume": "mdvolume`char", ## 매도누적체결수량@@
                "msvolume": "msvolume`char", ## 매수누적체결수량@@
                "ovsmkend": "ovsmkend`char##장마감일@@"
            }
        }
    },
    "WOH": { ## 해외옵션 호가(WOH)
        "input": {
            "InBlock": {
                "symbol": " ##종목코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "symbol": "symbol`char", ## 종목코드@@
                "hotime": "hotime`char", ## 호가시간@@
                "offerho1": "offerho1`double", ## 매도호가 1@@
                "bidho1": "bidho1`double", ## 매수호가 1@@
                "offerrem1": "offerrem1`long", ## 매도호가 잔량 1@@
                "bidrem1": "bidrem1`long", ## 매수호가 잔량 1@@
                "offerno1": "offerno1`long", ## 매도호가 건수 1@@
                "bidno1": "bidno1`long", ## 매수호가 건수 1@@
                "offerho2": "offerho2`double", ## 매도호가 2@@
                "bidho2": "bidho2`double", ## 매수호가 2@@
                "offerrem2": "offerrem2`long", ## 매도호가 잔량 2@@
                "bidrem2": "bidrem2`long", ## 매수호가 잔량 2@@
                "offerno2": "offerno2`long", ## 매도호가 건수 2@@
                "bidno2": "bidno2`long", ## 매수호가 건수 2@@
                "offerho3": "offerho3`double", ## 매도호가 3@@
                "bidho3": "bidho3`double", ## 매수호가 3@@
                "offerrem3": "offerrem3`long", ## 매도호가 잔량 3@@
                "bidrem3": "bidrem3`long", ## 매수호가 잔량 3@@
                "offerno3": "offerno3`long", ## 매도호가 건수 3@@
                "bidno3": "bidno3`long", ## 매수호가 건수 3@@
                "offerho4": "offerho4`double", ## 매도호가 4@@
                "bidho4": "bidho4`double", ## 매수호가 4@@
                "offerrem4": "offerrem4`long", ## 매도호가 잔량 4@@
                "bidrem4": "bidrem4`long", ## 매수호가 잔량 4@@
                "offerno4": "offerno4`long", ## 매도호가 건수 4@@
                "bidno4": "bidno4`long", ## 매수호가 건수 4@@
                "offerho5": "offerho5`double", ## 매도호가 5@@
                "bidho5": "bidho5`double", ## 매수호가 5@@
                "offerrem5": "offerrem5`long", ## 매도호가 잔량 5@@
                "bidrem5": "bidrem5`long", ## 매수호가 잔량 5@@
                "offerno5": "offerno5`long", ## 매도호가 건수 5@@
                "bidno5": "bidno5`long", ## 매수호가 건수 5@@
                "totoffercnt": "totoffercnt`long", ## 매도호가총건수@@
                "totbidcnt": "totbidcnt`long", ## 매수호가총건수@@
                "totofferrem": "totofferrem`long", ## 매도호가총수량@@
                "totbidrem": "totbidrem`long##매수호가총수량@@"
            }
        }
    },
    "YC3": { ## 상품선물예상체결(YC3)
        "input": {
            "InBlock": {
                "shcode": " ##단축코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "ychetime": "ychetime`char", ## 예상체결시간@@
                "yeprice": "yeprice`float", ## 예상체결가격@@
                "yevolume": "yevolume`long", ## 예상체결수량@@
                "jnilysign": "jnilysign`char", ## 예상체결가전일종가대비구분@@
                "jnilchange": "jnilchange`float", ## 예상체결가전일종가대비@@
                "jnilydrate": "jnilydrate`float", ## 예상체결가전일종가등락율@@
                "shcode": "shcode`char##단축코드@@"
            }
        }
    },
    "YFC": { ## 지수선물예상체결(YFC)
        "input": {
            "InBlock": {
                "futcode": " ##단축코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "ychetime": "ychetime`char", ## 예상체결시간@@
                "yeprice": "yeprice`float", ## 예상체결가격@@
                "jnilysign": "jnilysign`char", ## 예상체결가전일종가대비구분@@
                "jnilchange": "jnilchange`float", ## 예상체결가전일종가대비@@
                "jnilydrate": "jnilydrate`float", ## 예상체결가전일종가등락율@@
                "futcode": "futcode`char##단축코드@@"
            }
        }
    },
    "YJC": { ## 주식선물예상체결(YJC)
        "input": {
            "InBlock": {
                "futcode": " ##단축코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "ychetime": "ychetime`char", ## 예상체결시간@@
                "yeprice": "yeprice`long", ## 예상체결가격@@
                "jnilysign": "jnilysign`char", ## 예상체결가전일종가대비구분@@
                "jnilchange": "jnilchange`long", ## 예상체결가전일종가대비@@
                "jnilydrate": "jnilydrate`float", ## 예상체결가전일종가등락율@@
                "futcode": "futcode`char##단축코드@@"
            }
        }
    },
    "YJ_": { ## 예상지수(YJ)
        "input": {
            "InBlock": {
                "upcode": " ##업종코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "time": "time`char", ## 시간@@
                "jisu": "jisu`float", ## 예상지수@@
                "sign": "sign`char", ## 예상전일대비구분@@
                "change": "change`float", ## 예상전일비@@
                "drate": "drate`float", ## 예상등락율@@
                "cvolume": "cvolume`long", ## 예상체결량@@
                "volume": "volume`long", ## 누적거래량@@
                "value": "value`long", ## 예상거래대금@@
                "upcode": "upcode`char##업종코드@@"
            }
        }
    },
    "YK3": { ## KOSDAQ예상체결(YK3)
        "input": {
            "InBlock": {
                "shcode": " ##단축코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "hotime": "hotime`char", ## 호가시간@@
                "yeprice": "yeprice`long", ## 예상체결가격@@
                "yevolume": "yevolume`long", ## 예상체결수량@@
                "jnilysign": "jnilysign`char", ## 예상체결가전일종가대비구분@@
                "jnilchange": "jnilchange`long", ## 예상체결가전일종가대비@@
                "jnilydrate": "jnilydrate`float", ## 예상체결가전일종가등락율@@
                "yofferho0": "yofferho0`long", ## 예상매도호가@@
                "ybidho0": "ybidho0`long", ## 예상매수호가@@
                "yofferrem0": "yofferrem0`long", ## 예상매도호가수량@@
                "ybidrem0": "ybidrem0`long", ## 예상매수호가수량@@
                "shcode": "shcode`char##단축코드@@"
            }
        }
    },
    "YOC": { ## 지수옵션예상체결(YOC)
        "input": {
            "InBlock": {
                "optcode": " ##단축코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "ychetime": "ychetime`char", ## 예상체결시간@@
                "yeprice": "yeprice`float", ## 예상체결가격@@
                "jnilysign": "jnilysign`char", ## 예상체결가전일종가대비구분@@
                "jnilchange": "jnilchange`float", ## 예상체결가전일종가대비@@
                "jnilydrate": "jnilydrate`float", ## 예상체결가전일종가등락율@@
                "optcode": "optcode`char##단축코드@@"
            }
        }
    },
    "YS3": { ## KOSPI예상체결(YS3)
        "input": {
            "InBlock": {
                "shcode": " ##단축코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "hotime": "hotime`char", ## 호가시간@@
                "yeprice": "yeprice`long", ## 예상체결가격@@
                "yevolume": "yevolume`long", ## 예상체결수량@@
                "jnilysign": "jnilysign`char", ## 예상체결가전일종가대비구분@@
                "jnilchange": "jnilchange`long", ## 예상체결가전일종가대비@@
                "jnilydrate": "jnilydrate`float", ## 예상체결가전일종가등락율@@
                "yofferho0": "yofferho0`long", ## 예상매도호가@@
                "ybidho0": "ybidho0`long", ## 예상매수호가@@
                "yofferrem0": "yofferrem0`long", ## 예상매도호가수량@@
                "ybidrem0": "ybidrem0`long", ## 예상매수호가수량@@
                "shcode": "shcode`char##단축코드@@"
            }
        }
    },
    "Ys3_4ELW": { ## ELW예상체결(Ys3)
        "input": {
            "InBlock": {
                "shcode": " ##단축코드@@"
            }
        },
        "output": {
            "OutBlock": {
                "hotime": "hotime`char", ## 호가시간@@
                "yeprice": "yeprice`long", ## 예상체결가격@@
                "yevolume": "yevolume`long", ## 예상체결수량@@
                "jnilysign": "jnilysign`char", ## 예상체결가전일종가대비구분@@
                "jnilchange": "jnilchange`long", ## 예상체결가전일종가대비@@
                "jnilydrate": "jnilydrate`float", ## 예상체결가전일종가등락율@@
                "yofferho0": "yofferho0`long", ## 예상매도호가@@
                "ybidho0": "ybidho0`long", ## 예상매수호가@@
                "yofferrem0": "yofferrem0`long", ## 예상매도호가수량@@
                "ybidrem0": "ybidrem0`long", ## 예상매수호가수량@@
                "shcode": "shcode`char##단축코드@@"
            }
        }
    }
}
