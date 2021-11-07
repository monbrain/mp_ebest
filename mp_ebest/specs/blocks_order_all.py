
blocks = {
    "CDPCQ04700": {  ### 계좌 거래내역
        "inblock": {
            "InBlock1": {
                # "RecCnt": 0,  # {레코드갯수} 
                # "QryTp": " ",  # {조회구분} 
                # "AcntNo": " ",  # {계좌번호} 
                # "Pwd": " ",  # {비밀번호} 
                # "QrySrtDt": " ",  # {조회시작일} 
                # "QryEndDt": " ",  # {조회종료일} 
                # "SrtNo": 0,  # {시작번호} 
                # "PdptnCode": " ",  # {상품유형코드} 
                # "IsuLgclssCode": " ",  # {종목대분류코드} 
                # "IsuNo": " "  # {종목번호} 
            }
        },
        "outblock": {
            "OutBlock1": {
                # "RecCnt": "RecCnt`long",  # {레코드갯수} 
                # "QryTp": "QryTp`char",  # {조회구분} 
                # "AcntNo": "AcntNo`char",  # {계좌번호} 
                # "Pwd": "Pwd`char",  # {비밀번호} 
                # "QrySrtDt": "QrySrtDt`char",  # {조회시작일} 
                # "QryEndDt": "QryEndDt`char",  # {조회종료일} 
                # "SrtNo": "SrtNo`long",  # {시작번호} 
                # "PdptnCode": "PdptnCode`char",  # {상품유형코드} 
                # "IsuLgclssCode": "IsuLgclssCode`char",  # {종목대분류코드} 
                # "IsuNo": "IsuNo`char"  # {종목번호} 
            },
            "OutBlock2": {
                # "RecCnt": "RecCnt`long",  # {레코드갯수} 
                # "AcntNm": "AcntNm`char"  # {계좌명} 
            },
            "OutBlock3": {
                # "AcntNo": "AcntNo`char",  # {계좌번호} 
                # "TrdDt": "TrdDt`char",  # {거래일자} 
                # "TrdNo": "TrdNo`long",  # {거래번호} 
                # "TpCodeNm": "TpCodeNm`char",  # {구분코드명} 
                # "SmryNo": "SmryNo`char",  # {적요번호} 
                # "SmryNm": "SmryNm`char",  # {적요명} 
                # "CancTpNm": "CancTpNm`char",  # {취소구분} 
                # "TrdQty": "TrdQty`long",  # {거래수량} 
                # "Trtax": "Trtax`long",  # {거래세} 
                # "FcurrAdjstAmt": "FcurrAdjstAmt`double",  # {외화정산금액} 
                # "AdjstAmt": "AdjstAmt`long",  # {정산금액} 
                # "OvdSum": "OvdSum`long",  # {연체합} 
                # "DpsBfbalAmt": "DpsBfbalAmt`long",  # {예수금전잔금액} 
                # "SellPldgRfundAmt": "SellPldgRfundAmt`long",  # {매도담보상환금} 
                # "DpspdgLoanBfbalAmt": "DpspdgLoanBfbalAmt`long",  # {예탁담보대출전잔금액} 
                # "TrdmdaNm": "TrdmdaNm`char",  # {거래매체명} 
                # "OrgTrdNo": "OrgTrdNo`long",  # {원거래번호} 
                # "IsuNm": "IsuNm`char",  # {종목명} 
                # "TrdUprc": "TrdUprc`double",  # {거래단가} 
                # "CmsnAmt": "CmsnAmt`long",  # {수수료} 
                # "FcurrCmsnAmt": "FcurrCmsnAmt`double",  # {외화수수료금액} 
                # "RfundDiffAmt": "RfundDiffAmt`long",  # {상환차이금액} 
                # "RepayAmtSum": "RepayAmtSum`long",  # {변제금합계} 
                # "SecCrbalQty": "SecCrbalQty`long",  # {유가증권금잔수량} 
                # "CslLoanRfundIntrstAmt": "CslLoanRfundIntrstAmt`long",  # {매도대금담보대출상환이자금액} 
                # "DpspdgLoanCrbalAmt": "DpspdgLoanCrbalAmt`long",  # {예탁담보대출금잔금액} 
                # "TrxTime": "TrxTime`char",  # {처리시각} 
                # "Inouno": "Inouno`long",  # {출납번호} 
                # "IsuNo": "IsuNo`char",  # {종목번호} 
                # "TrdAmt": "TrdAmt`long",  # {거래금액} 
                # "ChckAmt": "ChckAmt`long",  # {수표금액} 
                # "TaxSumAmt": "TaxSumAmt`long",  # {세금합계금액} 
                # "FcurrTaxSumAmt": "FcurrTaxSumAmt`double",  # {외화세금합계금액} 
                # "IntrstUtlfee": "IntrstUtlfee`long",  # {이자이용료} 
                # "MnyDvdAmt": "MnyDvdAmt`long",  # {배당금액} 
                # "RcvblOcrAmt": "RcvblOcrAmt`long",  # {미수발생금액} 
                # "TrxBrnNo": "TrxBrnNo`char",  # {처리지점번호} 
                # "TrxBrnNm": "TrxBrnNm`char",  # {처리지점명} 
                # "DpspdgLoanAmt": "DpspdgLoanAmt`long",  # {예탁담보대출금액} 
                # "DpspdgLoanRfundAmt": "DpspdgLoanRfundAmt`long",  # {예탁담보대출상환금액} 
                # "BasePrc": "BasePrc`double",  # {기준가} 
                # "DpsCrbalAmt": "DpsCrbalAmt`long",  # {예수금금잔금액} 
                # "BoaAmt": "BoaAmt`long",  # {과표} 
                # "MnyoutAbleAmt": "MnyoutAbleAmt`long",  # {출금가능금액} 
                # "BcrLoanOcrAmt": "BcrLoanOcrAmt`long",  # {수익증권담보대출발생금} 
                # "BcrLoanBfbalAmt": "BcrLoanBfbalAmt`long",  # {수익증권담보대출전잔금} 
                # "BnsBasePrc": "BnsBasePrc`double",  # {매매기준가} 
                # "TaxchrBasePrc": "TaxchrBasePrc`double",  # {과세기준가} 
                # "TrdUnit": "TrdUnit`long",  # {거래좌수} 
                # "BalUnit": "BalUnit`long",  # {잔고좌수} 
                # "EvrTax": "EvrTax`long",  # {제세금} 
                # "EvalAmt": "EvalAmt`long",  # {평가금액} 
                # "BcrLoanRfundAmt": "BcrLoanRfundAmt`long",  # {수익증권담보대출상환금} 
                # "BcrLoanCrbalAmt": "BcrLoanCrbalAmt`long",  # {수익증권담보대출금잔금} 
                # "AddMgnOcrTotamt": "AddMgnOcrTotamt`long",  # {추가증거금발생총액} 
                # "AddMnyMgnOcrAmt": "AddMnyMgnOcrAmt`long",  # {추가현금증거금발생금액} 
                # "AddMgnDfryTotamt": "AddMgnDfryTotamt`long",  # {추가증거금납부총액} 
                # "AddMnyMgnDfryAmt": "AddMnyMgnDfryAmt`long",  # {추가현금증거금납부금액} 
                # "BnsplAmt": "BnsplAmt`long",  # {매매손익금액} 
                # "Ictax": "Ictax`long",  # {소득세} 
                # "Ihtax": "Ihtax`long",  # {주민세} 
                # "LoanDt": "LoanDt`char",  # {대출일} 
                # "CrcyCode": "CrcyCode`char",  # {통화코드} 
                # "FcurrAmt": "FcurrAmt`double",  # {외화금액} 
                # "FcurrTrdAmt": "FcurrTrdAmt`double",  # {외화거래금액} 
                # "FcurrDps": "FcurrDps`double",  # {외화예수금} 
                # "FcurrDpsBfbalAmt": "FcurrDpsBfbalAmt`double",  # {외화예수금전잔금액} 
                # "OppAcntNm": "OppAcntNm`char",  # {상대계좌명} 
                # "OppAcntNo": "OppAcntNo`char",  # {상대계좌번호} 
                # "LoanRfundAmt": "LoanRfundAmt`long",  # {대출상환금액} 
                # "LoanIntrstAmt": "LoanIntrstAmt`long",  # {대출이자금액} 
                # "AskpsnNm": "AskpsnNm`char",  # {의뢰인명} 
                # "OrdDt": "OrdDt`char",  # {주문일자} 
                # "TrdXchrat": "TrdXchrat`double",  # {거래환율} 
                # "RdctCmsn": "RdctCmsn`double",  # {감면수수료} 
                # "FcurrStmpTx": "FcurrStmpTx`double",  # {외화인지세} 
                # "FcurrElecfnTrtax": "FcurrElecfnTrtax`double",  # {외화전자금융거래세} 
                # "FcstckTrtax": "FcstckTrtax`double"  # {외화증권거래세} 
            },
            "OutBlock4": {
                # "RecCnt": "RecCnt`long",  # {레코드갯수} 
                # "PnlSumAmt": "PnlSumAmt`long",  # {손익합계금액} 
                # "CtrctAsm": "CtrctAsm`long",  # {약정누계} 
                # "CmsnAmtSumAmt": "CmsnAmtSumAmt`long"  # {수수료합계금액} 
            },
            "OutBlock5": {
                # "RecCnt": "RecCnt`long",  # {레코드갯수} 
                # "MnyinAmt": "MnyinAmt`long",  # {입금금액} 
                # "SecinAmt": "SecinAmt`long",  # {입고금액} 
                # "MnyoutAmt": "MnyoutAmt`long",  # {출금금액} 
                # "SecoutAmt": "SecoutAmt`long",  # {출고금액} 
                # "DiffAmt": "DiffAmt`long",  # {차이금액} 
                # "DiffAmt0": "DiffAmt0`long",  # {차이금액0} 
                # "SellQty": "SellQty`long",  # {매도수량} 
                # "SellAmt": "SellAmt`long",  # {매도금액} 
                # "SellCmsn": "SellCmsn`long",  # {매도수수료} 
                # "EvrTax": "EvrTax`long",  # {제세금} 
                # "FcurrSellAdjstAmt": "FcurrSellAdjstAmt`double",  # {외화매도정산금액} 
                # "BuyQty": "BuyQty`long",  # {매수수량} 
                # "BuyAmt": "BuyAmt`long",  # {매수금액} 
                # "BuyCmsn": "BuyCmsn`long",  # {매수수수료} 
                # "ExecTax": "ExecTax`long",  # {체결세금} 
                # "FcurrBuyAdjstAmt": "FcurrBuyAdjstAmt`double"  # {외화매수정산금액} 
            }
        }
    },
    "CFOFQ02400": {  ### 계좌 미결제 약정현황(평균가)
        "inblock": {
            "InBlock1": {
                # "RecCnt": 0,  # {레코드갯수} 
                # "AcntNo": " ",  # {계좌번호} 
                # "Pwd": " ",  # {비밀번호} 
                # "RegMktCode": " ",  # {등록시장코드} 
                # "BuyDt": " "  # {매수일자} 
            }
        },
        "outblock": {
            "OutBlock1": {
                # "RecCnt": "RecCnt`long",  # {레코드갯수} 
                # "AcntNo": "AcntNo`char",  # {계좌번호} 
                # "Pwd": "Pwd`char",  # {비밀번호} 
                # "RegMktCode": "RegMktCode`char",  # {등록시장코드} 
                # "BuyDt": "BuyDt`char"  # {매수일자} 
            },
            "OutBlock2": {
                # "RecCnt": "RecCnt`long",  # {레코드갯수} 
                # "AcntNm": "AcntNm`char",  # {계좌명} 
                # "FutsCtrctQty": "FutsCtrctQty`long",  # {선물약정수량} 
                # "OptCtrctQty": "OptCtrctQty`long",  # {옵션약정수량} 
                # "CtrctQty": "CtrctQty`long",  # {약정수량} 
                # "FutsCtrctAmt": "FutsCtrctAmt`long",  # {선물약정금액} 
                # "FutsBuyctrAmt": "FutsBuyctrAmt`long",  # {선물매수약정금액} 
                # "FutsSlctrAmt": "FutsSlctrAmt`long",  # {선물매도약정금액} 
                # "CalloptCtrctAmt": "CalloptCtrctAmt`long",  # {콜옵션약정금액} 
                # "CallBuyAmt": "CallBuyAmt`long",  # {콜매수금액} 
                # "CallSellAmt": "CallSellAmt`long",  # {콜매도금액} 
                # "PutoptCtrctAmt": "PutoptCtrctAmt`long",  # {풋옵션약정금액} 
                # "PutBuyAmt": "PutBuyAmt`long",  # {풋매수금액} 
                # "PutSellAmt": "PutSellAmt`long",  # {풋매도금액} 
                # "AllCtrctAmt": "AllCtrctAmt`long",  # {전체약정금액} 
                # "BuyctrAsmAmt": "BuyctrAsmAmt`long",  # {매수약정누계금액} 
                # "SlctrAsmAmt": "SlctrAsmAmt`long",  # {매도약정누계금액} 
                # "FutsPnlSum": "FutsPnlSum`long",  # {선물손익합계} 
                # "OptPnlSum": "OptPnlSum`long",  # {옵션손익합계} 
                # "AllPnlSum": "AllPnlSum`long"  # {전체손익합계} 
            },
            "OutBlock3": {
                # "FnoClssCode": "FnoClssCode`char",  # {선물옵션품목구분} 
                # "FutsSellQty": "FutsSellQty`long",  # {선물매도수량} 
                # "FutsSellPnl": "FutsSellPnl`long",  # {선물매도손익} 
                # "FutsBuyQty": "FutsBuyQty`long",  # {선물매수수량} 
                # "FutsBuyPnl": "FutsBuyPnl`long",  # {선물매수손익} 
                # "CallSellQty": "CallSellQty`long",  # {콜매도수량} 
                # "CallSellPnl": "CallSellPnl`long",  # {콜매도손익} 
                # "CallBuyQty": "CallBuyQty`long",  # {콜매수수량} 
                # "CallBuyPnl": "CallBuyPnl`long",  # {콜매수손익} 
                # "PutSellQty": "PutSellQty`long",  # {풋매도수량} 
                # "PutSellPnl": "PutSellPnl`long",  # {풋매도손익} 
                # "PutBuyQty": "PutBuyQty`long",  # {풋매수수량} 
                # "PutBuyPnl": "PutBuyPnl`long"  # {풋매수손익} 
            },
            "OutBlock4": {
                # "IsuNo": "IsuNo`char",  # {종목번호} 
                # "IsuNm": "IsuNm`char",  # {종목명} 
                # "BnsTpCode": "BnsTpCode`char",  # {매매구분} 
                # "BnsTpNm": "BnsTpNm`char",  # {매매구분} 
                # "BalQty": "BalQty`long",  # {잔고수량} 
                # "FnoAvrPrc": "FnoAvrPrc`double",  # {평균가} 
                # "BgnAmt": "BgnAmt`long",  # {당초금액} 
                # "ThdayLqdtQty": "ThdayLqdtQty`long",  # {당일청산수량} 
                # "Curprc": "Curprc`double",  # {현재가} 
                # "EvalAmt": "EvalAmt`long",  # {평가금액} 
                # "EvalPnlAmt": "EvalPnlAmt`long",  # {평가손익금액} 
                # "EvalErnrat": "EvalErnrat`double"  # {평가수익률} 
            }
        }
    },
    "ChartExcel": {  ### 챠트엑셀데이터조회
        "inblock": {
            "InBlock": {
                # "indexid": 0,  # {지표ID} 
                # "indexname": " ",  # {지표명} 
                # "indexparam": " ",  # {지표조건설정} 
                # "indexouttype": " ",  # {결과데이터 구분} 
                # "market": " ",  # {시장구분} 
                # "period": " ",  # {주기구분} 
                # "shcode": " ",  # {단축코드} 
                # "isexcelout": " ",  # {결과 지표데이터 엑셀표시 여부} 
                # "excelfilename": " ",  # {엑셀데이터 파일명} 
                # "IsReal": " "  # {실시간 데이터수신 자동등록 여부} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "indexid": "indexid`long",  # {지표ID} 
                # "rec_cnt": "rec_cnt`long",  # {레코드갯수} 
                # "validdata_cnt": "validdata_cnt`long"  # {유효 데이터 컬럼 갯수} 
            },
            "OutBlock1": {
                # "date": "date`char",  # {일자} 
                # "time": "time`char",  # {시간} 
                # "open": "open`float",  # {시가} 
                # "high": "high`float",  # {고가} 
                # "low": "low`float",  # {저가} 
                # "close": "close`float",  # {종가} 
                # "volume": "volume`float",  # {거래량} 
                # "value1": "value1`float",  # {지표값1} 
                # "value2": "value2`float",  # {지표값2} 
                # "value3": "value3`float",  # {지표값3} 
                # "value4": "value4`float",  # {지표값4} 
                # "value5": "value5`float",  # {지표값5} 
                # "pos": "pos`long"  # {위치} 
            }
        }
    },
    "ChartIndex": {  ### 챠트지표데이터조회
        "inblock": {
            "InBlock": {
                # "indexid": 0,  # {지표ID} 
                # "indexname": " ",  # {지표명} 
                # "indexparam": " ",  # {지표조건설정} 
                # "market": " ",  # {시장구분} 
                # "period": " ",  # {주기구분} 
                # "shcode": " ",  # {단축코드} 
                # "qrycnt": 0,  # {요청건수(최대 500개)} 
                # "ncnt": 0,  # {단위} n틱/n분
                # "sdate": " ",  # {시작일자} 
                # "edate": " ",  # {종료일자} 
                # "Isamend": " ",  # {수정주가 반영 여부} 
                # "Isgab": " ",  # {갭보정 여부} 
                # "IsReal": " "  # {실시간 데이터수신 자동등록 여부} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "indexid": "indexid`long",  # {지표ID} 
                # "rec_cnt": "rec_cnt`long",  # {레코드갯수} 
                # "validdata_cnt": "validdata_cnt`long"  # {유효 데이터 컬럼 갯수} 
            },
            "OutBlock1": {
                # "date": "date`char",  # {일자} 
                # "time": "time`char",  # {시간} 
                # "open": "open`float",  # {시가} 
                # "high": "high`float",  # {고가} 
                # "low": "low`float",  # {저가} 
                # "close": "close`float",  # {종가} 
                # "volume": "volume`float",  # {거래량} 
                # "value1": "value1`float",  # {지표값1} 
                # "value2": "value2`float",  # {지표값2} 
                # "value3": "value3`float",  # {지표값3} 
                # "value4": "value4`float",  # {지표값4} 
                # "value5": "value5`float",  # {지표값5} 
                # "pos": "pos`long"  # {위치} 
            }
        }
    },
    "CLNAQ00100": {  ### 예탁담보융자가능종목현황조회
        "inblock": {
            "InBlock1": {
                # "RecCnt": 0,  # {레코드갯수} 
                # "QryTp": " ",  # {조회구분} 
                # "IsuNo": " ",  # {종목번호} 
                # "SecTpCode": " ",  # {유가증권구분} 
                # "LoanIntrstGrdCode": " ",  # {대출이자등급코드} 
                # "LoanTp": " "  # {대출구분} 
            }
        },
        "outblock": {
            "OutBlock1": {
                # "RecCnt": "RecCnt`long",  # {레코드갯수} 
                # "QryTp": "QryTp`char",  # {조회구분} 
                # "IsuNo": "IsuNo`char",  # {종목번호} 
                # "SecTpCode": "SecTpCode`char",  # {유가증권구분} 
                # "LoanIntrstGrdCode": "LoanIntrstGrdCode`char",  # {대출이자등급코드} 
                # "LoanTp": "LoanTp`char"  # {대출구분} 
            },
            "OutBlock2": {
                # "IsuNo": "IsuNo`char",  # {종목번호} 
                # "IsuNm": "IsuNm`char",  # {종목명} 
                # "Parprc": "Parprc`double",  # {액면가} 
                # "PrdayCprc": "PrdayCprc`double",  # {전일종가} 
                # "RatVal": "RatVal`double",  # {비율값} 
                # "SubstPrc": "SubstPrc`double",  # {대용가} 
                # "RegTpNm": "RegTpNm`char",  # {등록구분} 
                # "SpotMgnLevyClssNm": "SpotMgnLevyClssNm`char",  # {현물증거금징수분류명} 
                # "FnoTrdStopRsnCnts": "FnoTrdStopRsnCnts`char",  # {거래정지사유} 
                # "DgrsPtnNm": "DgrsPtnNm`char",  # {요주의유형명} 
                # "AcdPtnNm": "AcdPtnNm`char",  # {사고유형} 
                # "MktTpNm": "MktTpNm`char",  # {시장구분} 
                # "LmtVal": "LmtVal`long",  # {한도값} 
                # "AcntLmtVal": "AcntLmtVal`long",  # {계좌한도값} 
                # "LoanGrdCode": "LoanGrdCode`char",  # {대출등급코드} 
                # "LoanAmt": "LoanAmt`long",  # {대출금액} 
                # "LoanAbleRat": "LoanAbleRat`double",  # {대출가능율} 
                # "LoanIntrat1": "LoanIntrat1`double",  # {대출이율1} 
                # "RegPsnId": "RegPsnId`char",  # {등록자ID} 
                # "Rat01": "Rat01`double",  # {비율값} 
                # "Rat02": "Rat02`double"  # {비율값} 
            },
            "OutBlock3": {
                # "RecCnt": "RecCnt`long",  # {레코드갯수} 
                # "LrgMnyoutSumAmt": "LrgMnyoutSumAmt`long"  # {대출금합계금액} 
            }
        }
    },
    "CSPAQ00600": {  ### 계좌별신용한도조회
        "inblock": {
            "InBlock1": {
                # "RecCnt": 0,  # {레코드갯수} 
                # "AcntNo": " ",  # {계좌번호} 
                # "InptPwd": " ",  # {입력비밀번호} 
                # "LoanDtlClssCode": " ",  # {대출상세분류코드} 
                # "IsuNo": " ",  # {종목번호} 
                # "OrdPrc": 0.0,  # {주문가} 
                # "CommdaCode": " "  # {통신매체코드} 
            }
        },
        "outblock": {
            "OutBlock1": {
                # "RecCnt": "RecCnt`long",  # {레코드갯수} 
                # "AcntNo": "AcntNo`char",  # {계좌번호} 
                # "InptPwd": "InptPwd`char",  # {입력비밀번호} 
                # "LoanDtlClssCode": "LoanDtlClssCode`char",  # {대출상세분류코드} 
                # "IsuNo": "IsuNo`char",  # {종목번호} 
                # "OrdPrc": "OrdPrc`double",  # {주문가} 
                # "CommdaCode": "CommdaCode`char"  # {통신매체코드} 
            },
            "OutBlock2": {
                # "RecCnt": "RecCnt`long",  # {레코드갯수} 
                # "AcntNm": "AcntNm`char",  # {계좌명} 
                # "OrdPrc": "OrdPrc`double",  # {주문가} 
                # "SloanLmtAmt": "SloanLmtAmt`long",  # {대주한도} 
                # "SloanAmtSum": "SloanAmtSum`long",  # {대주금액합계} 
                # "SloanNewAmt": "SloanNewAmt`long",  # {대주신규금액} 
                # "SloanRfundAmt": "SloanRfundAmt`long",  # {대주상환금액} 
                # "MktcplMloanLmtAmt": "MktcplMloanLmtAmt`long",  # {유통융자한도금액} 
                # "MktcplMloanAmtSum": "MktcplMloanAmtSum`long",  # {유통융자금액합계} 
                # "MktcplMloanNewAmt": "MktcplMloanNewAmt`long",  # {유통융자신규금액} 
                # "MktcplMloanRfundAmt": "MktcplMloanRfundAmt`long",  # {유통융자상환금액} 
                # "SfaccMloanLmtAmt": "SfaccMloanLmtAmt`long",  # {자기융자한도금액} 
                # "SfaccMloanAmtSum": "SfaccMloanAmtSum`long",  # {자기융자금액합계} 
                # "SfaccMloanNewAmt": "SfaccMloanNewAmt`long",  # {자기융자신규금액} 
                # "SfaccMloanRfundAmt": "SfaccMloanRfundAmt`long",  # {자기융자상환금액} 
                # "BrnMktcplMloanLmtAmt": "BrnMktcplMloanLmtAmt`long",  # {지점유통융자한도금액} 
                # "BrnMktcplMloanNewAmt": "BrnMktcplMloanNewAmt`long",  # {지점유통융자신규금액} 
                # "BrnMktcplMloanRfundAmt": "BrnMktcplMloanRfundAmt`long",  # {지점유통융자상환금액} 
                # "BrnMktcplMloanUseAmt": "BrnMktcplMloanUseAmt`long",  # {지점유통융자사용금액} 
                # "BrnSfaccMloanLmtAmt": "BrnSfaccMloanLmtAmt`long",  # {지점자기융자한도금액} 
                # "BrnSfaccMloanNewAmt": "BrnSfaccMloanNewAmt`long",  # {지점자기융자신규금액} 
                # "BrnSfaccMloanRfundAmt": "BrnSfaccMloanRfundAmt`long",  # {지점자기융자상환금액} 
                # "BrnSfaccMloanUseAmt": "BrnSfaccMloanUseAmt`long",  # {지점자기융자사용금액} 
                # "FirmMloanLmtMgmtYn": "FirmMloanLmtMgmtYn`char",  # {이용사융자한도관리여부} 
                # "FirmCrdtIsuRestrcTp": "FirmCrdtIsuRestrcTp`char",  # {이용사신용종목제한구분} 
                # "PldgMaintRat": "PldgMaintRat`double",  # {담보유지비율} 
                # "FirmNm": "FirmNm`char",  # {이용사명} 
                # "PldgRat": "PldgRat`double",  # {담보비율} 
                # "DpsastSum": "DpsastSum`long",  # {예탁자산합계} 
                # "LmtChgAbleAmt": "LmtChgAbleAmt`long",  # {한도변경가능금액} 
                # "OrdAbleAmt": "OrdAbleAmt`long",  # {주문가능금액} 
                # "OrdAbleQty": "OrdAbleQty`long",  # {주문가능수량} 
                # "RcvblUablOrdAbleQty": "RcvblUablOrdAbleQty`long"  # {미수불가주문가능수량} 
            }
        }
    },
    "CSPAQ12200": {  ### 현물계좌예수금 주문가능금액 총평가 조회
        "inblock": {
            "InBlock1": {
                # "RecCnt": 0,  # {레코드갯수} 
                # "MgmtBrnNo": " ",  # {관리지점번호} 
                # "AcntNo": " ",  # {계좌번호} 
                # "Pwd": " ",  # {비밀번호} 
                # "BalCreTp": " "  # {잔고생성구분} 
            }
        },
        "outblock": {
            "OutBlock1": {
                # "RecCnt": "RecCnt`long",  # {레코드갯수} 
                # "MgmtBrnNo": "MgmtBrnNo`char",  # {관리지점번호} 
                # "AcntNo": "AcntNo`char",  # {계좌번호} 
                # "Pwd": "Pwd`char",  # {비밀번호} 
                # "BalCreTp": "BalCreTp`char"  # {잔고생성구분} 
            },
            "OutBlock2": {
                # "RecCnt": "RecCnt`long",  # {레코드갯수} 
                # "BrnNm": "BrnNm`char",  # {지점명} 
                # "AcntNm": "AcntNm`char",  # {계좌명} 
                # "MnyOrdAbleAmt": "MnyOrdAbleAmt`long",  # {현금주문가능금액} 
                # "MnyoutAbleAmt": "MnyoutAbleAmt`long",  # {출금가능금액} 
                # "SeOrdAbleAmt": "SeOrdAbleAmt`long",  # {거래소금액} 
                # "KdqOrdAbleAmt": "KdqOrdAbleAmt`long",  # {코스닥금액} 
                # "BalEvalAmt": "BalEvalAmt`long",  # {잔고평가금액} 
                # "RcvblAmt": "RcvblAmt`long",  # {미수금액} 
                # "DpsastTotamt": "DpsastTotamt`long",  # {예탁자산총액} 
                # "PnlRat": "PnlRat`double",  # {손익율} 
                # "InvstOrgAmt": "InvstOrgAmt`long",  # {투자원금} 
                # "InvstPlAmt": "InvstPlAmt`long",  # {투자손익금액} 
                # "CrdtPldgOrdAmt": "CrdtPldgOrdAmt`long",  # {신용담보주문금액} 
                # "Dps": "Dps`long",  # {예수금} 
                # "SubstAmt": "SubstAmt`long",  # {대용금액} 
                # "D1Dps": "D1Dps`long",  # {D1예수금} 
                # "D2Dps": "D2Dps`long",  # {D2예수금} 
                # "MnyrclAmt": "MnyrclAmt`long",  # {현금미수금액} 
                # "MgnMny": "MgnMny`long",  # {증거금현금} 
                # "MgnSubst": "MgnSubst`long",  # {증거금대용} 
                # "ChckAmt": "ChckAmt`long",  # {수표금액} 
                # "SubstOrdAbleAmt": "SubstOrdAbleAmt`long",  # {대용주문가능금액} 
                # "MgnRat100pctOrdAbleAmt": "MgnRat100pctOrdAbleAmt`long",  # {증거금률100퍼센트주문가능금액} 
                # "MgnRat35ordAbleAmt": "MgnRat35ordAbleAmt`long",  # {증거금률35%주문가능금액} 
                # "MgnRat50ordAbleAmt": "MgnRat50ordAbleAmt`long",  # {증거금률50%주문가능금액} 
                # "PrdaySellAdjstAmt": "PrdaySellAdjstAmt`long",  # {전일매도정산금액} 
                # "PrdayBuyAdjstAmt": "PrdayBuyAdjstAmt`long",  # {전일매수정산금액} 
                # "CrdaySellAdjstAmt": "CrdaySellAdjstAmt`long",  # {금일매도정산금액} 
                # "CrdayBuyAdjstAmt": "CrdayBuyAdjstAmt`long",  # {금일매수정산금액} 
                # "D1ovdRepayRqrdAmt": "D1ovdRepayRqrdAmt`long",  # {D1연체변제소요금액} 
                # "D2ovdRepayRqrdAmt": "D2ovdRepayRqrdAmt`long",  # {D2연체변제소요금액} 
                # "D1PrsmptWthdwAbleAmt": "D1PrsmptWthdwAbleAmt`long",  # {D1추정인출가능금액} 
                # "D2PrsmptWthdwAbleAmt": "D2PrsmptWthdwAbleAmt`long",  # {D2추정인출가능금액} 
                # "DpspdgLoanAmt": "DpspdgLoanAmt`long",  # {예탁담보대출금액} 
                # "Imreq": "Imreq`long",  # {신용설정보증금} 
                # "MloanAmt": "MloanAmt`long",  # {융자금액} 
                # "ChgAfPldgRat": "ChgAfPldgRat`double",  # {변경후담보비율} 
                # "OrgPldgAmt": "OrgPldgAmt`long",  # {원담보금액} 
                # "SubPldgAmt": "SubPldgAmt`long",  # {부담보금액} 
                # "RqrdPldgAmt": "RqrdPldgAmt`long",  # {소요담보금액} 
                # "OrgPdlckAmt": "OrgPdlckAmt`long",  # {원담보부족금액} 
                # "PdlckAmt": "PdlckAmt`long",  # {담보부족금액} 
                # "AddPldgMny": "AddPldgMny`long",  # {추가담보현금} 
                # "D1OrdAbleAmt": "D1OrdAbleAmt`long",  # {D1주문가능금액} 
                # "CrdtIntdltAmt": "CrdtIntdltAmt`long",  # {신용이자미납금액} 
                # "EtclndAmt": "EtclndAmt`long",  # {기타대여금액} 
                # "NtdayPrsmptCvrgAmt": "NtdayPrsmptCvrgAmt`long",  # {익일추정반대매매금액} 
                # "OrgPldgSumAmt": "OrgPldgSumAmt`long",  # {원담보합계금액} 
                # "CrdtOrdAbleAmt": "CrdtOrdAbleAmt`long",  # {신용주문가능금액} 
                # "SubPldgSumAmt": "SubPldgSumAmt`long",  # {부담보합계금액} 
                # "CrdtPldgAmtMny": "CrdtPldgAmtMny`long",  # {신용담보금현금} 
                # "CrdtPldgSubstAmt": "CrdtPldgSubstAmt`long",  # {신용담보대용금액} 
                # "AddCrdtPldgMny": "AddCrdtPldgMny`long",  # {추가신용담보현금} 
                # "CrdtPldgRuseAmt": "CrdtPldgRuseAmt`long",  # {신용담보재사용금액} 
                # "AddCrdtPldgSubst": "AddCrdtPldgSubst`long",  # {추가신용담보대용} 
                # "CslLoanAmtdt1": "CslLoanAmtdt1`long",  # {매도대금담보대출금액} 
                # "DpslRestrcAmt": "DpslRestrcAmt`long"  # {처분제한금액} 
            }
        }
    },
    "CSPAQ12300": {  ### BEP단가조회
        "inblock": {
            "InBlock1": {
                # "RecCnt": 0,  # {레코드갯수} 
                # "AcntNo": " ",  # {계좌번호} 
                # "Pwd": " ",  # {비밀번호} 
                # "BalCreTp": " ",  # {잔고생성구분} 
                # "CmsnAppTpCode": " ",  # {수수료적용구분} 
                # "D2balBaseQryTp": " ",  # {D2잔고기준조회구분} 
                # "UprcTpCode": " "  # {단가구분} 
            }
        },
        "outblock": {
            "OutBlock1": {
                # "RecCnt": "RecCnt`long",  # {레코드갯수} 
                # "AcntNo": "AcntNo`char",  # {계좌번호} 
                # "Pwd": "Pwd`char",  # {비밀번호} 
                # "BalCreTp": "BalCreTp`char",  # {잔고생성구분} 
                # "CmsnAppTpCode": "CmsnAppTpCode`char",  # {수수료적용구분} 
                # "D2balBaseQryTp": "D2balBaseQryTp`char",  # {D2잔고기준조회구분} 
                # "UprcTpCode": "UprcTpCode`char"  # {단가구분} 
            },
            "OutBlock2": {
                # "RecCnt": "RecCnt`long",  # {레코드갯수} 
                # "BrnNm": "BrnNm`char",  # {지점명} 
                # "AcntNm": "AcntNm`char",  # {계좌명} 
                # "MnyOrdAbleAmt": "MnyOrdAbleAmt`long",  # {현금주문가능금액} 
                # "MnyoutAbleAmt": "MnyoutAbleAmt`long",  # {출금가능금액} 
                # "SeOrdAbleAmt": "SeOrdAbleAmt`long",  # {거래소금액} 
                # "KdqOrdAbleAmt": "KdqOrdAbleAmt`long",  # {코스닥금액} 
                # "HtsOrdAbleAmt": "HtsOrdAbleAmt`long",  # {HTS주문가능금액} 
                # "MgnRat100pctOrdAbleAmt": "MgnRat100pctOrdAbleAmt`long",  # {증거금률100퍼센트주문가능금액} 
                # "BalEvalAmt": "BalEvalAmt`long",  # {잔고평가금액} 
                # "PchsAmt": "PchsAmt`long",  # {매입금액} 
                # "RcvblAmt": "RcvblAmt`long",  # {미수금액} 
                # "PnlRat": "PnlRat`double",  # {손익율} 
                # "InvstOrgAmt": "InvstOrgAmt`long",  # {투자원금} 
                # "InvstPlAmt": "InvstPlAmt`long",  # {투자손익금액} 
                # "CrdtPldgOrdAmt": "CrdtPldgOrdAmt`long",  # {신용담보주문금액} 
                # "Dps": "Dps`long",  # {예수금} 
                # "D1Dps": "D1Dps`long",  # {D1예수금} 
                # "D2Dps": "D2Dps`long",  # {D2예수금} 
                # "OrdDt": "OrdDt`char",  # {주문일} 
                # "MnyMgn": "MnyMgn`long",  # {현금증거금액} 
                # "SubstMgn": "SubstMgn`long",  # {대용증거금액} 
                # "SubstAmt": "SubstAmt`long",  # {대용금액} 
                # "PrdayBuyExecAmt": "PrdayBuyExecAmt`long",  # {전일매수체결금액} 
                # "PrdaySellExecAmt": "PrdaySellExecAmt`long",  # {전일매도체결금액} 
                # "CrdayBuyExecAmt": "CrdayBuyExecAmt`long",  # {금일매수체결금액} 
                # "CrdaySellExecAmt": "CrdaySellExecAmt`long",  # {금일매도체결금액} 
                # "EvalPnlSum": "EvalPnlSum`long",  # {평가손익합계} 
                # "DpsastTotamt": "DpsastTotamt`long",  # {예탁자산총액} 
                # "Evrprc": "Evrprc`long",  # {제비용} 
                # "RuseAmt": "RuseAmt`long",  # {재사용금액} 
                # "EtclndAmt": "EtclndAmt`long",  # {기타대여금액} 
                # "PrcAdjstAmt": "PrcAdjstAmt`long",  # {가정산금액} 
                # "D1CmsnAmt": "D1CmsnAmt`long",  # {D1수수료} 
                # "D2CmsnAmt": "D2CmsnAmt`long",  # {D2수수료} 
                # "D1EvrTax": "D1EvrTax`long",  # {D1제세금} 
                # "D2EvrTax": "D2EvrTax`long",  # {D2제세금} 
                # "D1SettPrergAmt": "D1SettPrergAmt`long",  # {D1결제예정금액} 
                # "D2SettPrergAmt": "D2SettPrergAmt`long",  # {D2결제예정금액} 
                # "PrdayKseMnyMgn": "PrdayKseMnyMgn`long",  # {전일KSE현금증거금} 
                # "PrdayKseSubstMgn": "PrdayKseSubstMgn`long",  # {전일KSE대용증거금} 
                # "PrdayKseCrdtMnyMgn": "PrdayKseCrdtMnyMgn`long",  # {전일KSE신용현금증거금} 
                # "PrdayKseCrdtSubstMgn": "PrdayKseCrdtSubstMgn`long",  # {전일KSE신용대용증거금} 
                # "CrdayKseMnyMgn": "CrdayKseMnyMgn`long",  # {금일KSE현금증거금} 
                # "CrdayKseSubstMgn": "CrdayKseSubstMgn`long",  # {금일KSE대용증거금} 
                # "CrdayKseCrdtMnyMgn": "CrdayKseCrdtMnyMgn`long",  # {금일KSE신용현금증거금} 
                # "CrdayKseCrdtSubstMgn": "CrdayKseCrdtSubstMgn`long",  # {금일KSE신용대용증거금} 
                # "PrdayKdqMnyMgn": "PrdayKdqMnyMgn`long",  # {전일코스닥현금증거금} 
                # "PrdayKdqSubstMgn": "PrdayKdqSubstMgn`long",  # {전일코스닥대용증거금} 
                # "PrdayKdqCrdtMnyMgn": "PrdayKdqCrdtMnyMgn`long",  # {전일코스닥신용현금증거금} 
                # "PrdayKdqCrdtSubstMgn": "PrdayKdqCrdtSubstMgn`long",  # {전일코스닥신용대용증거금} 
                # "CrdayKdqMnyMgn": "CrdayKdqMnyMgn`long",  # {금일코스닥현금증거금} 
                # "CrdayKdqSubstMgn": "CrdayKdqSubstMgn`long",  # {금일코스닥대용증거금} 
                # "CrdayKdqCrdtMnyMgn": "CrdayKdqCrdtMnyMgn`long",  # {금일코스닥신용현금증거금} 
                # "CrdayKdqCrdtSubstMgn": "CrdayKdqCrdtSubstMgn`long",  # {금일코스닥신용대용증거금} 
                # "PrdayFrbrdMnyMgn": "PrdayFrbrdMnyMgn`long",  # {전일프리보드현금증거금} 
                # "PrdayFrbrdSubstMgn": "PrdayFrbrdSubstMgn`long",  # {전일프리보드대용증거금} 
                # "CrdayFrbrdMnyMgn": "CrdayFrbrdMnyMgn`long",  # {금일프리보드현금증거금} 
                # "CrdayFrbrdSubstMgn": "CrdayFrbrdSubstMgn`long",  # {금일프리보드대용증거금} 
                # "PrdayCrbmkMnyMgn": "PrdayCrbmkMnyMgn`long",  # {전일장외현금증거금} 
                # "PrdayCrbmkSubstMgn": "PrdayCrbmkSubstMgn`long",  # {전일장외대용증거금} 
                # "CrdayCrbmkMnyMgn": "CrdayCrbmkMnyMgn`long",  # {금일장외현금증거금} 
                # "CrdayCrbmkSubstMgn": "CrdayCrbmkSubstMgn`long",  # {금일장외대용증거금} 
                # "DpspdgQty": "DpspdgQty`long",  # {예탁담보수량} 
                # "BuyAdjstAmtD2": "BuyAdjstAmtD2`long",  # {매수정산금(D+2)} 
                # "SellAdjstAmtD2": "SellAdjstAmtD2`long",  # {매도정산금(D+2)} 
                # "RepayRqrdAmtD1": "RepayRqrdAmtD1`long",  # {변제소요금(D+1)} 
                # "RepayRqrdAmtD2": "RepayRqrdAmtD2`long",  # {변제소요금(D+2)} 
                # "LoanAmt": "LoanAmt`long"  # {대출금액} 
            },
            "OutBlock3": {
                # "IsuNo": "IsuNo`char",  # {종목번호} 
                # "IsuNm": "IsuNm`char",  # {종목명} 
                # "SecBalPtnCode": "SecBalPtnCode`char",  # {유가증권잔고유형코드} 
                # "SecBalPtnNm": "SecBalPtnNm`char",  # {유가증권잔고유형명} 
                # "BalQty": "BalQty`long",  # {잔고수량} 
                # "BnsBaseBalQty": "BnsBaseBalQty`long",  # {매매기준잔고수량} 
                # "CrdayBuyExecQty": "CrdayBuyExecQty`long",  # {금일매수체결수량} 
                # "CrdaySellExecQty": "CrdaySellExecQty`long",  # {금일매도체결수량} 
                # "SellPrc": "SellPrc`double",  # {매도가} 
                # "BuyPrc": "BuyPrc`double",  # {매수가} 
                # "SellPnlAmt": "SellPnlAmt`long",  # {매도손익금액} 
                # "PnlRat": "PnlRat`double",  # {손익율} 
                # "NowPrc": "NowPrc`double",  # {현재가} 
                # "CrdtAmt": "CrdtAmt`long",  # {신용금액} 
                # "DueDt": "DueDt`char",  # {만기일} 
                # "PrdaySellExecPrc": "PrdaySellExecPrc`double",  # {전일매도체결가} 
                # "PrdaySellQty": "PrdaySellQty`long",  # {전일매도수량} 
                # "PrdayBuyExecPrc": "PrdayBuyExecPrc`double",  # {전일매수체결가} 
                # "PrdayBuyQty": "PrdayBuyQty`long",  # {전일매수수량} 
                # "LoanDt": "LoanDt`char",  # {대출일} 
                # "AvrUprc": "AvrUprc`double",  # {평균단가} 
                # "SellAbleQty": "SellAbleQty`long",  # {매도가능수량} 
                # "SellOrdQty": "SellOrdQty`long",  # {매도주문수량} 
                # "CrdayBuyExecAmt": "CrdayBuyExecAmt`long",  # {금일매수체결금액} 
                # "CrdaySellExecAmt": "CrdaySellExecAmt`long",  # {금일매도체결금액} 
                # "PrdayBuyExecAmt": "PrdayBuyExecAmt`long",  # {전일매수체결금액} 
                # "PrdaySellExecAmt": "PrdaySellExecAmt`long",  # {전일매도체결금액} 
                # "BalEvalAmt": "BalEvalAmt`long",  # {잔고평가금액} 
                # "EvalPnl": "EvalPnl`long",  # {평가손익} 
                # "MnyOrdAbleAmt": "MnyOrdAbleAmt`long",  # {현금주문가능금액} 
                # "OrdAbleAmt": "OrdAbleAmt`long",  # {주문가능금액} 
                # "SellUnercQty": "SellUnercQty`long",  # {매도미체결수량} 
                # "SellUnsttQty": "SellUnsttQty`long",  # {매도미결제수량} 
                # "BuyUnercQty": "BuyUnercQty`long",  # {매수미체결수량} 
                # "BuyUnsttQty": "BuyUnsttQty`long",  # {매수미결제수량} 
                # "UnsttQty": "UnsttQty`long",  # {미결제수량} 
                # "UnercQty": "UnercQty`long",  # {미체결수량} 
                # "PrdayCprc": "PrdayCprc`double",  # {전일종가} 
                # "PchsAmt": "PchsAmt`long",  # {매입금액} 
                # "RegMktCode": "RegMktCode`char",  # {등록시장코드} 
                # "LoanDtlClssCode": "LoanDtlClssCode`char",  # {대출상세분류코드} 
                # "DpspdgLoanQty": "DpspdgLoanQty`long"  # {예탁담보대출수량} 
            }
        }
    },
    "CSPAQ13700": {  ### 현물계좌주문체결내역조회
        "inblock": {
            "InBlock1": {
                # "RecCnt": 0,  # {레코드갯수} 
                # "AcntNo": " ",  # {계좌번호} 
                # "InptPwd": " ",  # {입력비밀번호} 
                # "OrdMktCode": " ",  # {주문시장코드} 
                # "BnsTpCode": " ",  # {매매구분} 
                # "IsuNo": " ",  # {종목번호} 
                # "ExecYn": " ",  # {체결여부} 
                # "OrdDt": " ",  # {주문일} 
                # "SrtOrdNo2": 0,  # {시작주문번호2} 
                # "BkseqTpCode": " ",  # {역순구분} 
                # "OrdPtnCode": " "  # {주문유형코드} 
            }
        },
        "outblock": {
            "OutBlock1": {
                # "RecCnt": "RecCnt`long",  # {레코드갯수} 
                # "AcntNo": "AcntNo`char",  # {계좌번호} 
                # "InptPwd": "InptPwd`char",  # {입력비밀번호} 
                # "OrdMktCode": "OrdMktCode`char",  # {주문시장코드} 
                # "BnsTpCode": "BnsTpCode`char",  # {매매구분} 
                # "IsuNo": "IsuNo`char",  # {종목번호} 
                # "ExecYn": "ExecYn`char",  # {체결여부} 
                # "OrdDt": "OrdDt`char",  # {주문일} 
                # "SrtOrdNo2": "SrtOrdNo2`long",  # {시작주문번호2} 
                # "BkseqTpCode": "BkseqTpCode`char",  # {역순구분} 
                # "OrdPtnCode": "OrdPtnCode`char"  # {주문유형코드} 
            },
            "OutBlock2": {
                # "RecCnt": "RecCnt`long",  # {레코드갯수} 
                # "SellExecAmt": "SellExecAmt`long",  # {매도체결금액} 
                # "BuyExecAmt": "BuyExecAmt`long",  # {매수체결금액} 
                # "SellExecQty": "SellExecQty`long",  # {매도체결수량} 
                # "BuyExecQty": "BuyExecQty`long",  # {매수체결수량} 
                # "SellOrdQty": "SellOrdQty`long",  # {매도주문수량} 
                # "BuyOrdQty": "BuyOrdQty`long"  # {매수주문수량} 
            },
            "OutBlock3": {
                # "OrdDt": "OrdDt`char",  # {주문일} 
                # "MgmtBrnNo": "MgmtBrnNo`char",  # {관리지점번호} 
                # "OrdMktCode": "OrdMktCode`char",  # {주문시장코드} 
                # "OrdNo": "OrdNo`long",  # {주문번호} 
                # "OrgOrdNo": "OrgOrdNo`long",  # {원주문번호} 
                # "IsuNo": "IsuNo`char",  # {종목번호} 
                # "IsuNm": "IsuNm`char",  # {종목명} 
                # "BnsTpCode": "BnsTpCode`char",  # {매매구분} 
                # "BnsTpNm": "BnsTpNm`char",  # {매매구분} 
                # "OrdPtnCode": "OrdPtnCode`char",  # {주문유형코드} 
                # "OrdPtnNm": "OrdPtnNm`char",  # {주문유형명} 
                # "OrdTrxPtnCode": "OrdTrxPtnCode`long",  # {주문처리유형코드} 
                # "OrdTrxPtnNm": "OrdTrxPtnNm`char",  # {주문처리유형명} 
                # "MrcTpCode": "MrcTpCode`char",  # {정정취소구분} 
                # "MrcTpNm": "MrcTpNm`char",  # {정정취소구분명} 
                # "MrcQty": "MrcQty`long",  # {정정취소수량} 
                # "MrcAbleQty": "MrcAbleQty`long",  # {정정취소가능수량} 
                # "OrdQty": "OrdQty`long",  # {주문수량} 
                # "OrdPrc": "OrdPrc`double",  # {주문가격} 
                # "ExecQty": "ExecQty`long",  # {체결수량} 
                # "ExecPrc": "ExecPrc`double",  # {체결가} 
                # "ExecTrxTime": "ExecTrxTime`char",  # {체결처리시각} 
                # "LastExecTime": "LastExecTime`char",  # {최종체결시각} 
                # "OrdprcPtnCode": "OrdprcPtnCode`char",  # {호가유형코드} 
                # "OrdprcPtnNm": "OrdprcPtnNm`char",  # {호가유형명} 
                # "OrdCndiTpCode": "OrdCndiTpCode`char",  # {주문조건구분} 
                # "AllExecQty": "AllExecQty`long",  # {전체체결수량} 
                # "RegCommdaCode": "RegCommdaCode`char",  # {통신매체코드} 
                # "CommdaNm": "CommdaNm`char",  # {통신매체명} 
                # "MbrNo": "MbrNo`char",  # {회원번호} 
                # "RsvOrdYn": "RsvOrdYn`char",  # {예약주문여부} 
                # "LoanDt": "LoanDt`char",  # {대출일} 
                # "OrdTime": "OrdTime`char",  # {주문시각} 
                # "OpDrtnNo": "OpDrtnNo`char",  # {운용지시번호} 
                # "OdrrId": "OdrrId`char"  # {주문자ID} 
            }
        }
    },
    "CSPAQ22200": {  ### 현물계좌예수금 주문가능금액 총평가2
        "inblock": {
            "InBlock1": {
                # "RecCnt": 0,  # {레코드갯수} 
                # "MgmtBrnNo": " ",  # {관리지점번호} 
                # "AcntNo": " ",  # {계좌번호} 
                # "Pwd": " ",  # {비밀번호} 
                # "BalCreTp": " "  # {잔고생성구분} 
            }
        },
        "outblock": {
            "OutBlock1": {
                # "RecCnt": "RecCnt`long",  # {레코드갯수} 
                # "MgmtBrnNo": "MgmtBrnNo`char",  # {관리지점번호} 
                # "AcntNo": "AcntNo`char",  # {계좌번호} 
                # "Pwd": "Pwd`char",  # {비밀번호} 
                # "BalCreTp": "BalCreTp`char"  # {잔고생성구분} 
            },
            "OutBlock2": {
                # "RecCnt": "RecCnt`long",  # {레코드갯수} 
                # "BrnNm": "BrnNm`char",  # {지점명} 
                # "AcntNm": "AcntNm`char",  # {계좌명} 
                # "MnyOrdAbleAmt": "MnyOrdAbleAmt`long",  # {현금주문가능금액} 
                # "SubstOrdAbleAmt": "SubstOrdAbleAmt`long",  # {대용주문가능금액} 
                # "SeOrdAbleAmt": "SeOrdAbleAmt`long",  # {거래소금액} 
                # "KdqOrdAbleAmt": "KdqOrdAbleAmt`long",  # {코스닥금액} 
                # "CrdtPldgOrdAmt": "CrdtPldgOrdAmt`long",  # {신용담보주문금액} 
                # "MgnRat100pctOrdAbleAmt": "MgnRat100pctOrdAbleAmt`long",  # {증거금률100퍼센트주문가능금액} 
                # "MgnRat35ordAbleAmt": "MgnRat35ordAbleAmt`long",  # {증거금률35%주문가능금액} 
                # "MgnRat50ordAbleAmt": "MgnRat50ordAbleAmt`long",  # {증거금률50%주문가능금액} 
                # "CrdtOrdAbleAmt": "CrdtOrdAbleAmt`long",  # {신용주문가능금액} 
                # "Dps": "Dps`long",  # {예수금} 
                # "SubstAmt": "SubstAmt`long",  # {대용금액} 
                # "MgnMny": "MgnMny`long",  # {증거금현금} 
                # "MgnSubst": "MgnSubst`long",  # {증거금대용} 
                # "D1Dps": "D1Dps`long",  # {D1예수금} 
                # "D2Dps": "D2Dps`long",  # {D2예수금} 
                # "RcvblAmt": "RcvblAmt`long",  # {미수금액} 
                # "D1ovdRepayRqrdAmt": "D1ovdRepayRqrdAmt`long",  # {D1연체변제소요금액} 
                # "D2ovdRepayRqrdAmt": "D2ovdRepayRqrdAmt`long",  # {D2연체변제소요금액} 
                # "MloanAmt": "MloanAmt`long",  # {융자금액} 
                # "ChgAfPldgRat": "ChgAfPldgRat`double",  # {변경후담보비율} 
                # "RqrdPldgAmt": "RqrdPldgAmt`long",  # {소요담보금액} 
                # "PdlckAmt": "PdlckAmt`long",  # {담보부족금액} 
                # "OrgPldgSumAmt": "OrgPldgSumAmt`long",  # {원담보합계금액} 
                # "SubPldgSumAmt": "SubPldgSumAmt`long",  # {부담보합계금액} 
                # "CrdtPldgAmtMny": "CrdtPldgAmtMny`long",  # {신용담보금현금} 
                # "CrdtPldgSubstAmt": "CrdtPldgSubstAmt`long",  # {신용담보대용금액} 
                # "Imreq": "Imreq`long",  # {신용설정보증금} 
                # "CrdtPldgRuseAmt": "CrdtPldgRuseAmt`long",  # {신용담보재사용금액} 
                # "DpslRestrcAmt": "DpslRestrcAmt`long",  # {처분제한금액} 
                # "PrdaySellAdjstAmt": "PrdaySellAdjstAmt`long",  # {전일매도정산금액} 
                # "PrdayBuyAdjstAmt": "PrdayBuyAdjstAmt`long",  # {전일매수정산금액} 
                # "CrdaySellAdjstAmt": "CrdaySellAdjstAmt`long",  # {금일매도정산금액} 
                # "CrdayBuyAdjstAmt": "CrdayBuyAdjstAmt`long",  # {금일매수정산금액} 
                # "CslLoanAmtdt1": "CslLoanAmtdt1`long"  # {매도대금담보대출금액} 
            }
        }
    },
    "CSPAT00600": {  ### 현물주문
        "inblock": {
            "InBlock1": {
                # "AcntNo": " ",  # {계좌번호} 
                # "InptPwd": " ",  # {입력비밀번호} 
                # "IsuNo": " ",  # {종목번호} 
                # "OrdQty": 0,  # {주문수량} 
                # "OrdPrc": 0.0,  # {주문가} 
                # "BnsTpCode": " ",  # {매매구분} 
                # "OrdprcPtnCode": " ",  # {호가유형코드} 
                # "MgntrnCode": " ",  # {신용거래코드} 
                # "LoanDt": " ",  # {대출일} 
                # "OrdCndiTpCode": " "  # {주문조건구분} 
            }
        },
        "outblock": {
            "OutBlock1": {
                # "RecCnt": "RecCnt`long",  # {레코드갯수} 
                # "AcntNo": "AcntNo`char",  # {계좌번호} 
                # "InptPwd": "InptPwd`char",  # {입력비밀번호} 
                # "IsuNo": "IsuNo`char",  # {종목번호} 
                # "OrdQty": "OrdQty`long",  # {주문수량} 
                # "OrdPrc": "OrdPrc`double",  # {주문가} 
                # "BnsTpCode": "BnsTpCode`char",  # {매매구분} 
                # "OrdprcPtnCode": "OrdprcPtnCode`char",  # {호가유형코드} 
                # "PrgmOrdprcPtnCode": "PrgmOrdprcPtnCode`char",  # {프로그램호가유형코드} 
                # "StslAbleYn": "StslAbleYn`char",  # {공매도가능여부} 
                # "StslOrdprcTpCode": "StslOrdprcTpCode`char",  # {공매도호가구분} 
                # "CommdaCode": "CommdaCode`char",  # {통신매체코드} 
                # "MgntrnCode": "MgntrnCode`char",  # {신용거래코드} 
                # "LoanDt": "LoanDt`char",  # {대출일} 
                # "MbrNo": "MbrNo`char",  # {회원번호} 
                # "OrdCndiTpCode": "OrdCndiTpCode`char",  # {주문조건구분} 
                # "StrtgCode": "StrtgCode`char",  # {전략코드} 
                # "GrpId": "GrpId`char",  # {그룹ID} 
                # "OrdSeqNo": "OrdSeqNo`long",  # {주문회차} 
                # "PtflNo": "PtflNo`long",  # {포트폴리오번호} 
                # "BskNo": "BskNo`long",  # {바스켓번호} 
                # "TrchNo": "TrchNo`long",  # {트렌치번호} 
                # "ItemNo": "ItemNo`long",  # {아이템번호} 
                # "OpDrtnNo": "OpDrtnNo`char",  # {운용지시번호} 
                # "LpYn": "LpYn`char",  # {유동성공급자여부} 
                # "CvrgTpCode": "CvrgTpCode`char"  # {반대매매구분} 
            },
            "OutBlock2": {
                # "RecCnt": "RecCnt`long",  # {레코드갯수} 
                # "OrdNo": "OrdNo`long",  # {주문번호} 
                # "OrdTime": "OrdTime`char",  # {주문시각} 
                # "OrdMktCode": "OrdMktCode`char",  # {주문시장코드} 
                # "OrdPtnCode": "OrdPtnCode`char",  # {주문유형코드} 
                # "ShtnIsuNo": "ShtnIsuNo`char",  # {단축종목번호} 
                # "MgempNo": "MgempNo`char",  # {관리사원번호} 
                # "OrdAmt": "OrdAmt`long",  # {주문금액} 
                # "SpareOrdNo": "SpareOrdNo`long",  # {예비주문번호} 
                # "CvrgSeqno": "CvrgSeqno`long",  # {반대매매일련번호} 
                # "RsvOrdNo": "RsvOrdNo`long",  # {예약주문번호} 
                # "SpotOrdQty": "SpotOrdQty`long",  # {실물주문수량} 
                # "RuseOrdQty": "RuseOrdQty`long",  # {재사용주문수량} 
                # "MnyOrdAmt": "MnyOrdAmt`long",  # {현금주문금액} 
                # "SubstOrdAmt": "SubstOrdAmt`long",  # {대용주문금액} 
                # "RuseOrdAmt": "RuseOrdAmt`long",  # {재사용주문금액} 
                # "AcntNm": "AcntNm`char",  # {계좌명} 
                # "IsuNm": "IsuNm`char"  # {종목명} 
            }
        }
    },
    "CSPAT00700": {  ### 현물정정주문
        "inblock": {
            "InBlock1": {
                # "OrgOrdNo": 0,  # {원주문번호} 
                # "AcntNo": " ",  # {계좌번호} 
                # "InptPwd": " ",  # {입력비밀번호} 
                # "IsuNo": " ",  # {종목번호} 
                # "OrdQty": 0,  # {주문수량} 
                # "OrdprcPtnCode": " ",  # {호가유형코드} 
                # "OrdCndiTpCode": " ",  # {주문조건구분} 
                # "OrdPrc": 0.0  # {주문가} 
            }
        },
        "outblock": {
            "OutBlock1": {
                # "RecCnt": "RecCnt`long",  # {레코드갯수} 
                # "OrgOrdNo": "OrgOrdNo`long",  # {원주문번호} 
                # "AcntNo": "AcntNo`char",  # {계좌번호} 
                # "InptPwd": "InptPwd`char",  # {입력비밀번호} 
                # "IsuNo": "IsuNo`char",  # {종목번호} 
                # "OrdQty": "OrdQty`long",  # {주문수량} 
                # "OrdprcPtnCode": "OrdprcPtnCode`char",  # {호가유형코드} 
                # "OrdCndiTpCode": "OrdCndiTpCode`char",  # {주문조건구분} 
                # "OrdPrc": "OrdPrc`double",  # {주문가} 
                # "CommdaCode": "CommdaCode`char",  # {통신매체코드} 
                # "StrtgCode": "StrtgCode`char",  # {전략코드} 
                # "GrpId": "GrpId`char",  # {그룹ID} 
                # "OrdSeqNo": "OrdSeqNo`long",  # {주문회차} 
                # "PtflNo": "PtflNo`long",  # {포트폴리오번호} 
                # "BskNo": "BskNo`long",  # {바스켓번호} 
                # "TrchNo": "TrchNo`long",  # {트렌치번호} 
                # "ItemNo": "ItemNo`long"  # {아이템번호} 
            },
            "OutBlock2": {
                # "RecCnt": "RecCnt`long",  # {레코드갯수} 
                # "OrdNo": "OrdNo`long",  # {주문번호} 
                # "PrntOrdNo": "PrntOrdNo`long",  # {모주문번호} 
                # "OrdTime": "OrdTime`char",  # {주문시각} 
                # "OrdMktCode": "OrdMktCode`char",  # {주문시장코드} 
                # "OrdPtnCode": "OrdPtnCode`char",  # {주문유형코드} 
                # "ShtnIsuNo": "ShtnIsuNo`char",  # {단축종목번호} 
                # "PrgmOrdprcPtnCode": "PrgmOrdprcPtnCode`char",  # {프로그램호가유형코드} 
                # "StslOrdprcTpCode": "StslOrdprcTpCode`char",  # {공매도호가구분} 
                # "StslAbleYn": "StslAbleYn`char",  # {공매도가능여부} 
                # "MgntrnCode": "MgntrnCode`char",  # {신용거래코드} 
                # "LoanDt": "LoanDt`char",  # {대출일} 
                # "CvrgOrdTp": "CvrgOrdTp`char",  # {반대매매주문구분} 
                # "LpYn": "LpYn`char",  # {유동성공급자여부} 
                # "MgempNo": "MgempNo`char",  # {관리사원번호} 
                # "OrdAmt": "OrdAmt`long",  # {주문금액} 
                # "BnsTpCode": "BnsTpCode`char",  # {매매구분} 
                # "SpareOrdNo": "SpareOrdNo`long",  # {예비주문번호} 
                # "CvrgSeqno": "CvrgSeqno`long",  # {반대매매일련번호} 
                # "RsvOrdNo": "RsvOrdNo`long",  # {예약주문번호} 
                # "MnyOrdAmt": "MnyOrdAmt`long",  # {현금주문금액} 
                # "SubstOrdAmt": "SubstOrdAmt`long",  # {대용주문금액} 
                # "RuseOrdAmt": "RuseOrdAmt`long",  # {재사용주문금액} 
                # "AcntNm": "AcntNm`char",  # {계좌명} 
                # "IsuNm": "IsuNm`char"  # {종목명} 
            }
        }
    },
    "CSPAT00800": {  ### 현물취소주문
        "inblock": {
            "InBlock1": {
                # "OrgOrdNo": 0,  # {원주문번호} 
                # "AcntNo": " ",  # {계좌번호} 
                # "InptPwd": " ",  # {입력비밀번호} 
                # "IsuNo": " ",  # {종목번호} 
                # "OrdQty": 0  # {주문수량} 
            }
        },
        "outblock": {
            "OutBlock1": {
                # "RecCnt": "RecCnt`long",  # {레코드갯수} 
                # "OrgOrdNo": "OrgOrdNo`long",  # {원주문번호} 
                # "AcntNo": "AcntNo`char",  # {계좌번호} 
                # "InptPwd": "InptPwd`char",  # {입력비밀번호} 
                # "IsuNo": "IsuNo`char",  # {종목번호} 
                # "OrdQty": "OrdQty`long",  # {주문수량} 
                # "CommdaCode": "CommdaCode`char",  # {통신매체코드} 
                # "GrpId": "GrpId`char",  # {그룹ID} 
                # "StrtgCode": "StrtgCode`char",  # {전략코드} 
                # "OrdSeqNo": "OrdSeqNo`long",  # {주문회차} 
                # "PtflNo": "PtflNo`long",  # {포트폴리오번호} 
                # "BskNo": "BskNo`long",  # {바스켓번호} 
                # "TrchNo": "TrchNo`long",  # {트렌치번호} 
                # "ItemNo": "ItemNo`long"  # {아이템번호} 
            },
            "OutBlock2": {
                # "RecCnt": "RecCnt`long",  # {레코드갯수} 
                # "OrdNo": "OrdNo`long",  # {주문번호} 
                # "PrntOrdNo": "PrntOrdNo`long",  # {모주문번호} 
                # "OrdTime": "OrdTime`char",  # {주문시각} 
                # "OrdMktCode": "OrdMktCode`char",  # {주문시장코드} 
                # "OrdPtnCode": "OrdPtnCode`char",  # {주문유형코드} 
                # "ShtnIsuNo": "ShtnIsuNo`char",  # {단축종목번호} 
                # "PrgmOrdprcPtnCode": "PrgmOrdprcPtnCode`char",  # {프로그램호가유형코드} 
                # "StslOrdprcTpCode": "StslOrdprcTpCode`char",  # {공매도호가구분} 
                # "StslAbleYn": "StslAbleYn`char",  # {공매도가능여부} 
                # "MgntrnCode": "MgntrnCode`char",  # {신용거래코드} 
                # "LoanDt": "LoanDt`char",  # {대출일} 
                # "CvrgOrdTp": "CvrgOrdTp`char",  # {반대매매주문구분} 
                # "LpYn": "LpYn`char",  # {유동성공급자여부} 
                # "MgempNo": "MgempNo`char",  # {관리사원번호} 
                # "BnsTpCode": "BnsTpCode`char",  # {매매구분} 
                # "SpareOrdNo": "SpareOrdNo`long",  # {예비주문번호} 
                # "CvrgSeqno": "CvrgSeqno`long",  # {반대매매일련번호} 
                # "RsvOrdNo": "RsvOrdNo`long",  # {예약주문번호} 
                # "AcntNm": "AcntNm`char",  # {계좌명} 
                # "IsuNm": "IsuNm`char"  # {종목명} 
            }
        }
    },
    "CSPBQ00200": {  ### 현물계좌증거금률별주문가능수량조회
        "inblock": {
            "InBlock1": {
                # "RecCnt": 0,  # {레코드갯수} 
                # "BnsTpCode": " ",  # {매매구분} 
                # "AcntNo": " ",  # {계좌번호} 
                # "InptPwd": " ",  # {입력비밀번호} 
                # "IsuNo": " ",  # {종목번호} 
                # "OrdPrc": 0.0,  # {주문가격} 
                # "RegCommdaCode": " "  # {통신매체코드} 
            }
        },
        "outblock": {
            "OutBlock1": {
                # "RecCnt": "RecCnt`long",  # {레코드갯수} 
                # "BnsTpCode": "BnsTpCode`char",  # {매매구분} 
                # "AcntNo": "AcntNo`char",  # {계좌번호} 
                # "InptPwd": "InptPwd`char",  # {입력비밀번호} 
                # "IsuNo": "IsuNo`char",  # {종목번호} 
                # "OrdPrc": "OrdPrc`double",  # {주문가격} 
                # "RegCommdaCode": "RegCommdaCode`char"  # {통신매체코드} 
            },
            "OutBlock2": {
                # "RecCnt": "RecCnt`long",  # {레코드갯수} 
                # "AcntNm": "AcntNm`char",  # {계좌명} 
                # "IsuNm": "IsuNm`char",  # {종목명} 
                # "Dps": "Dps`long",  # {예수금} 
                # "SubstAmt": "SubstAmt`long",  # {대용금액} 
                # "CrdtPldgRuseAmt": "CrdtPldgRuseAmt`long",  # {신용담보재사용금액} 
                # "MnyOrdAbleAmt": "MnyOrdAbleAmt`long",  # {현금주문가능금액} 
                # "SubstOrdAbleAmt": "SubstOrdAbleAmt`long",  # {대용주문가능금액} 
                # "MnyMgn": "MnyMgn`long",  # {현금증거금액} 
                # "SubstMgn": "SubstMgn`long",  # {대용증거금액} 
                # "SeOrdAbleAmt": "SeOrdAbleAmt`long",  # {거래소금액} 
                # "KdqOrdAbleAmt": "KdqOrdAbleAmt`long",  # {코스닥금액} 
                # "PrsmptDpsD1": "PrsmptDpsD1`long",  # {추정예수금(D+1)} 
                # "PrsmptDpsD2": "PrsmptDpsD2`long",  # {추정예수금(D+2)} 
                # "MnyoutAbleAmt": "MnyoutAbleAmt`long",  # {출금가능금액} 
                # "RcvblAmt": "RcvblAmt`long",  # {미수금액} 
                # "CmsnRat": "CmsnRat`double",  # {수수료율} 
                # "AddLevyAmt": "AddLevyAmt`long",  # {추가징수금액} 
                # "RuseObjAmt": "RuseObjAmt`long",  # {재사용대상금액} 
                # "MnyRuseObjAmt": "MnyRuseObjAmt`long",  # {현금재사용대상금액} 
                # "FirmMgnRat": "FirmMgnRat`double",  # {이용사증거금률} 
                # "SubstRuseObjAmt": "SubstRuseObjAmt`long",  # {대용재사용대상금액} 
                # "IsuMgnRat": "IsuMgnRat`double",  # {종목증거금률} 
                # "AcntMgnRat": "AcntMgnRat`double",  # {계좌증거금률} 
                # "TrdMgnrt": "TrdMgnrt`double",  # {거래증거금률} 
                # "Cmsn": "Cmsn`long",  # {수수료} 
                # "MgnRat20pctOrdAbleAmt": "MgnRat20pctOrdAbleAmt`long",  # {증거금률20퍼센트주문가능금액} 
                # "MgnRat20OrdAbleQty": "MgnRat20OrdAbleQty`long",  # {증거금률100퍼센트현금주문가능수량?} 
                # "MgnRat30pctOrdAbleAmt": "MgnRat30pctOrdAbleAmt`long",  # {증거금률30퍼센트주문가능금액} 
                # "MgnRat30OrdAbleQty": "MgnRat30OrdAbleQty`long",  # {증거금률30퍼센트주문가능수량??} 
                # "MgnRat40pctOrdAbleAmt": "MgnRat40pctOrdAbleAmt`long",  # {증거금률40퍼센트주문가능금액} 
                # "MgnRat40OrdAbleQty": "MgnRat40OrdAbleQty`long",  # {증거금률40퍼센트주문가능수량??} 
                # "MgnRat100pctOrdAbleAmt": "MgnRat100pctOrdAbleAmt`long",  # {증거금률100퍼센트주문가능금액} 
                # "MgnRat100OrdAbleQty": "MgnRat100OrdAbleQty`long",  # {증거금률100퍼센트주문가능수량??} 
                # "MgnRat100MnyOrdAbleAmt": "MgnRat100MnyOrdAbleAmt`long",  # {증거금률100퍼센트현금주문가능금액?} 
                # "MgnRat100MnyOrdAbleQty": "MgnRat100MnyOrdAbleQty`long",  # {증거금률100퍼센트현금주문가능수량} 
                # "MgnRat20pctRuseAbleAmt": "MgnRat20pctRuseAbleAmt`long",  # {증거금률20퍼센트재사용가능금액} 
                # "MgnRat30pctRuseAbleAmt": "MgnRat30pctRuseAbleAmt`long",  # {증거금률30퍼센트재사용가능금액} 
                # "MgnRat40pctRuseAbleAmt": "MgnRat40pctRuseAbleAmt`long",  # {증거금률40퍼센트재사용가능금액} 
                # "MgnRat100pctRuseAbleAmt": "MgnRat100pctRuseAbleAmt`long",  # {증거금률100퍼센트재사용가능금액} 
                # "OrdAbleQty": "OrdAbleQty`long",  # {주문가능수량} 
                # "OrdAbleAmt": "OrdAbleAmt`long"  # {주문가능금액} 
            }
        }
    },
    "FOCCQ33600": {  ### 주식계좌 기간별수익률 상세
        "inblock": {
            "InBlock1": {
                # "RecCnt": 0,  # {레코드갯수} 
                # "AcntNo": " ",  # {계좌번호} 
                # "Pwd": " ",  # {비밀번호} 
                # "QrySrtDt": " ",  # {조회시작일} 
                # "QryEndDt": " ",  # {조회종료일} 
                # "TermTp": " "  # {기간구분} 
            }
        },
        "outblock": {
            "OutBlock1": {
                # "RecCnt": "RecCnt`long",  # {레코드갯수} 
                # "AcntNo": "AcntNo`char",  # {계좌번호} 
                # "Pwd": "Pwd`char",  # {비밀번호} 
                # "QrySrtDt": "QrySrtDt`char",  # {조회시작일} 
                # "QryEndDt": "QryEndDt`char",  # {조회종료일} 
                # "TermTp": "TermTp`char"  # {기간구분} 
            },
            "OutBlock2": {
                # "RecCnt": "RecCnt`long",  # {레코드갯수} 
                # "AcntNm": "AcntNm`char",  # {계좌명} 
                # "BnsctrAmt": "BnsctrAmt`long",  # {매매약정금액} 
                # "MnyinAmt": "MnyinAmt`long",  # {입금금액} 
                # "MnyoutAmt": "MnyoutAmt`long",  # {출금금액} 
                # "InvstAvrbalPramt": "InvstAvrbalPramt`long",  # {투자원금평잔금액} 
                # "InvstPlAmt": "InvstPlAmt`long",  # {투자손익금액} 
                # "InvstErnrat": "InvstErnrat`double"  # {투자수익률} 
            },
            "OutBlock3": {
                # "BaseDt": "BaseDt`char",  # {기준일} 
                # "FdEvalAmt": "FdEvalAmt`long",  # {기초평가금액} 
                # "EotEvalAmt": "EotEvalAmt`long",  # {기말평가금액} 
                # "InvstAvrbalPramt": "InvstAvrbalPramt`long",  # {투자원금평잔금액} 
                # "BnsctrAmt": "BnsctrAmt`long",  # {매매약정금액} 
                # "MnyinSecinAmt": "MnyinSecinAmt`long",  # {입금고액} 
                # "MnyoutSecoutAmt": "MnyoutSecoutAmt`long",  # {출금고액} 
                # "EvalPnlAmt": "EvalPnlAmt`long",  # {평가손익금액} 
                # "TermErnrat": "TermErnrat`double",  # {기간수익률} 
                # "Idx": "Idx`double"  # {지수} 
            }
        }
    },
    "t0150": {  ### 주식당일매매일지/수수료
        "inblock": {
            "InBlock": {
                # "accno": " ",  # {계좌번호} 
                # "cts_medosu": " ",  # {CTS_매매구분} 
                # "cts_expcode": " ",  # {CTS_종목번호} 
                # "cts_price": " ",  # {CTS_단가} 
                # "cts_middiv": " "  # {CTS_매체} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "mdqty": "mdqty`long",  # {매도수량} 
                # "mdamt": "mdamt`long",  # {매도약정금액} 
                # "mdfee": "mdfee`long",  # {매도수수료} 
                # "mdtax": "mdtax`long",  # {매도거래세} 
                # "mdargtax": "mdargtax`long",  # {매도농특세} 
                # "tmdtax": "tmdtax`long",  # {매도제비용합} 
                # "mdadjamt": "mdadjamt`long",  # {매도정산금액} 
                # "msqty": "msqty`long",  # {매수수량} 
                # "msamt": "msamt`long",  # {매수약정금액} 
                # "msfee": "msfee`long",  # {매수수수료} 
                # "tmstax": "tmstax`long",  # {매수제비용합} 
                # "msadjamt": "msadjamt`long",  # {매수정산금액} 
                # "tqty": "tqty`long",  # {합계수량} 
                # "tamt": "tamt`long",  # {합계약정금액} 
                # "tfee": "tfee`long",  # {합계수수료} 
                # "tottax": "tottax`long",  # {합계거래세} 
                # "targtax": "targtax`long",  # {합계농특세} 
                # "ttax": "ttax`long",  # {합계제비용합} 
                # "tadjamt": "tadjamt`long",  # {합계정산금액} 
                # "cts_medosu": "cts_medosu`char",  # {CTS_매매구분} 
                # "cts_expcode": "cts_expcode`char",  # {CTS_종목번호} 
                # "cts_price": "cts_price`char",  # {CTS_단가} 
                # "cts_middiv": "cts_middiv`char"  # {CTS_매체} 
            },
            "OutBlock1": {
                # "medosu": "medosu`char",  # {매매구분} 
                # "expcode": "expcode`char",  # {종목번호} 
                # "qty": "qty`long",  # {수량} 
                # "price": "price`long",  # {단가} 
                # "amt": "amt`long",  # {약정금액} 
                # "fee": "fee`long",  # {수수료} 
                # "tax": "tax`long",  # {거래세} 
                # "argtax": "argtax`long",  # {농특세} 
                # "adjamt": "adjamt`long",  # {정산금액} 
                # "middiv": "middiv`char"  # {매체} 
            }
        }
    },
    "t0151": {  ### 주식당일매매일지/수수료(전일)
        "inblock": {
            "InBlock": {
                # "date": " ",  # {일자} 
                # "accno": " ",  # {계좌번호} 
                # "cts_medosu": " ",  # {CTS_매매구분} 
                # "cts_expcode": " ",  # {CTS_종목번호} 
                # "cts_price": " ",  # {CTS_단가} 
                # "cts_middiv": " "  # {CTS_매체} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "mdqty": "mdqty`long",  # {매도수량} 
                # "mdamt": "mdamt`long",  # {매도약정금액} 
                # "mdfee": "mdfee`long",  # {매도수수료} 
                # "mdtax": "mdtax`long",  # {매도거래세} 
                # "mdargtax": "mdargtax`long",  # {매도농특세} 
                # "tmdtax": "tmdtax`long",  # {매도제비용합} 
                # "mdadjamt": "mdadjamt`long",  # {매도정산금액} 
                # "msqty": "msqty`long",  # {매수수량} 
                # "msamt": "msamt`long",  # {매수약정금액} 
                # "msfee": "msfee`long",  # {매수수수료} 
                # "tmstax": "tmstax`long",  # {매수제비용합} 
                # "msadjamt": "msadjamt`long",  # {매수정산금액} 
                # "tqty": "tqty`long",  # {합계수량} 
                # "tamt": "tamt`long",  # {합계약정금액} 
                # "tfee": "tfee`long",  # {합계수수료} 
                # "tottax": "tottax`long",  # {합계거래세} 
                # "targtax": "targtax`long",  # {합계농특세} 
                # "ttax": "ttax`long",  # {합계제비용합} 
                # "tadjamt": "tadjamt`long",  # {합계정산금액} 
                # "cts_medosu": "cts_medosu`char",  # {CTS_매매구분} 
                # "cts_expcode": "cts_expcode`char",  # {CTS_종목번호} 
                # "cts_price": "cts_price`char",  # {CTS_단가} 
                # "cts_middiv": "cts_middiv`char"  # {CTS_매체} 
            },
            "OutBlock1": {
                # "medosu": "medosu`char",  # {매매구분} 
                # "expcode": "expcode`char",  # {종목번호} 
                # "qty": "qty`long",  # {수량} 
                # "price": "price`long",  # {단가} 
                # "amt": "amt`long",  # {약정금액} 
                # "fee": "fee`long",  # {수수료} 
                # "tax": "tax`long",  # {거래세} 
                # "argtax": "argtax`long",  # {농특세} 
                # "adjamt": "adjamt`long",  # {정산금액} 
                # "middiv": "middiv`char"  # {매체} 
            }
        }
    },
    "t0167": {  ### 서버시간조회
        "inblock": {
            "InBlock": {
                # "id": " "  # {id} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "dt": "dt`char",  # {일자(YYYYMMDD)} 
                # "time": "time`char"  # {시간(HHMMSSssssss)} 
            }
        }
    },
    "t0424": {  ### 주식잔고2
        "inblock": {
            "InBlock": {
                # "accno": " ",  # {계좌번호} 
                # "passwd": " ",  # {비밀번호} 
                # "prcgb": " ",  # {단가구분} 
                # "chegb": " ",  # {체결구분} 
                # "dangb": " ",  # {단일가구분} 
                # "charge": " ",  # {제비용포함여부} 
                # "cts_expcode": " "  # {CTS_종목번호} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "sunamt": "sunamt`long",  # {추정순자산} 
                # "dtsunik": "dtsunik`long",  # {실현손익} 
                # "mamt": "mamt`long",  # {매입금액} 
                # "sunamt1": "sunamt1`long",  # {추정D2예수금} 
                # "cts_expcode": "cts_expcode`char",  # {CTS_종목번호} 
                # "tappamt": "tappamt`long",  # {평가금액} 
                # "tdtsunik": "tdtsunik`long"  # {평가손익} 
            },
            "OutBlock1": {
                # "expcode": "expcode`char",  # {종목번호} 
                # "jangb": "jangb`char",  # {잔고구분} 
                # "janqty": "janqty`long",  # {잔고수량} 
                # "mdposqt": "mdposqt`long",  # {매도가능수량} 
                # "pamt": "pamt`long",  # {평균단가} 
                # "mamt": "mamt`long",  # {매입금액} 
                # "sinamt": "sinamt`long",  # {대출금액} 
                # "lastdt": "lastdt`char",  # {만기일자} 
                # "msat": "msat`long",  # {당일매수금액} 
                # "mpms": "mpms`long",  # {당일매수단가} 
                # "mdat": "mdat`long",  # {당일매도금액} 
                # "mpmd": "mpmd`long",  # {당일매도단가} 
                # "jsat": "jsat`long",  # {전일매수금액} 
                # "jpms": "jpms`long",  # {전일매수단가} 
                # "jdat": "jdat`long",  # {전일매도금액} 
                # "jpmd": "jpmd`long",  # {전일매도단가} 
                # "sysprocseq": "sysprocseq`long",  # {처리순번} 
                # "loandt": "loandt`char",  # {대출일자} 
                # "hname": "hname`char",  # {종목명} 
                # "marketgb": "marketgb`char",  # {시장구분} 
                # "jonggb": "jonggb`char",  # {종목구분} 
                # "janrt": "janrt`float",  # {보유비중} 
                # "price": "price`long",  # {현재가} 
                # "appamt": "appamt`long",  # {평가금액} 
                # "dtsunik": "dtsunik`long",  # {평가손익} 
                # "sunikrt": "sunikrt`float",  # {수익율} 
                # "fee": "fee`long",  # {수수료} 
                # "tax": "tax`long",  # {제세금} 
                # "sininter": "sininter`long"  # {신용이자} 
            }
        }
    },
    "t0425": {  ### 주식체결/미체결
        "inblock": {
            "InBlock": {
                # "accno": " ",  # {계좌번호} 
                # "passwd": " ",  # {비밀번호} 
                # "expcode": " ",  # {종목번호} 
                # "chegb": " ",  # {체결구분} 
                # "medosu": " ",  # {매매구분} 
                # "sortgb": " ",  # {정렬순서} 
                # "cts_ordno": " "  # {주문번호} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "tqty": "tqty`long",  # {총주문수량} 
                # "tcheqty": "tcheqty`long",  # {총체결수량} 
                # "tordrem": "tordrem`long",  # {총미체결수량} 
                # "cmss": "cmss`long",  # {추정수수료} 
                # "tamt": "tamt`long",  # {총주문금액} 
                # "tmdamt": "tmdamt`long",  # {총매도체결금액} 
                # "tmsamt": "tmsamt`long",  # {총매수체결금액} 
                # "tax": "tax`long",  # {추정제세금} 
                # "cts_ordno": "cts_ordno`char"  # {주문번호} 
            },
            "OutBlock1": {
                # "ordno": "ordno`long",  # {주문번호} 
                # "expcode": "expcode`char",  # {종목번호} 
                # "medosu": "medosu`char",  # {구분} 
                # "qty": "qty`long",  # {주문수량} 
                # "price": "price`long",  # {주문가격} 
                # "cheqty": "cheqty`long",  # {체결수량} 
                # "cheprice": "cheprice`long",  # {체결가격} 
                # "ordrem": "ordrem`long",  # {미체결잔량} 
                # "cfmqty": "cfmqty`long",  # {확인수량} 
                # "status": "status`char",  # {상태} 
                # "orgordno": "orgordno`long",  # {원주문번호} 
                # "ordgb": "ordgb`char",  # {유형} 
                # "ordtime": "ordtime`char",  # {주문시간} 
                # "ordermtd": "ordermtd`char",  # {주문매체} 
                # "sysprocseq": "sysprocseq`long",  # {처리순번} 
                # "hogagb": "hogagb`char",  # {호가유형} 
                # "price1": "price1`long",  # {현재가} 
                # "orggb": "orggb`char",  # {주문구분} 
                # "singb": "singb`char",  # {신용구분} 
                # "loandt": "loandt`char"  # {대출일자} 
            }
        }
    },
    "t1101": {  ### 주식현재가호가조회
        "inblock": {
            "InBlock": {
                # "shcode": " "  # {단축코드} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "hname": "hname`char",  # {한글명} 
                # "price": "price`long",  # {현재가} 
                # "sign": "sign`char",  # {전일대비구분} 
                # "change": "change`long",  # {전일대비} 
                # "diff": "diff`float",  # {등락율} 
                # "volume": "volume`long",  # {누적거래량} 
                # "jnilclose": "jnilclose`long",  # {전일종가} 
                # "offerho1": "offerho1`long",  # {매도호가1} 
                # "bidho1": "bidho1`long",  # {매수호가1} 
                # "offerrem1": "offerrem1`long",  # {매도호가수량1} 
                # "bidrem1": "bidrem1`long",  # {매수호가수량1} 
                # "preoffercha1": "preoffercha1`long",  # {직전매도대비수량1} 
                # "prebidcha1": "prebidcha1`long",  # {직전매수대비수량1} 
                # "offerho2": "offerho2`long",  # {매도호가2} 
                # "bidho2": "bidho2`long",  # {매수호가2} 
                # "offerrem2": "offerrem2`long",  # {매도호가수량2} 
                # "bidrem2": "bidrem2`long",  # {매수호가수량2} 
                # "preoffercha2": "preoffercha2`long",  # {직전매도대비수량2} 
                # "prebidcha2": "prebidcha2`long",  # {직전매수대비수량2} 
                # "offerho3": "offerho3`long",  # {매도호가3} 
                # "bidho3": "bidho3`long",  # {매수호가3} 
                # "offerrem3": "offerrem3`long",  # {매도호가수량3} 
                # "bidrem3": "bidrem3`long",  # {매수호가수량3} 
                # "preoffercha3": "preoffercha3`long",  # {직전매도대비수량3} 
                # "prebidcha3": "prebidcha3`long",  # {직전매수대비수량3} 
                # "offerho4": "offerho4`long",  # {매도호가4} 
                # "bidho4": "bidho4`long",  # {매수호가4} 
                # "offerrem4": "offerrem4`long",  # {매도호가수량4} 
                # "bidrem4": "bidrem4`long",  # {매수호가수량4} 
                # "preoffercha4": "preoffercha4`long",  # {직전매도대비수량4} 
                # "prebidcha4": "prebidcha4`long",  # {직전매수대비수량4} 
                # "offerho5": "offerho5`long",  # {매도호가5} 
                # "bidho5": "bidho5`long",  # {매수호가5} 
                # "offerrem5": "offerrem5`long",  # {매도호가수량5} 
                # "bidrem5": "bidrem5`long",  # {매수호가수량5} 
                # "preoffercha5": "preoffercha5`long",  # {직전매도대비수량5} 
                # "prebidcha5": "prebidcha5`long",  # {직전매수대비수량5} 
                # "offerho6": "offerho6`long",  # {매도호가6} 
                # "bidho6": "bidho6`long",  # {매수호가6} 
                # "offerrem6": "offerrem6`long",  # {매도호가수량6} 
                # "bidrem6": "bidrem6`long",  # {매수호가수량6} 
                # "preoffercha6": "preoffercha6`long",  # {직전매도대비수량6} 
                # "prebidcha6": "prebidcha6`long",  # {직전매수대비수량6} 
                # "offerho7": "offerho7`long",  # {매도호가7} 
                # "bidho7": "bidho7`long",  # {매수호가7} 
                # "offerrem7": "offerrem7`long",  # {매도호가수량7} 
                # "bidrem7": "bidrem7`long",  # {매수호가수량7} 
                # "preoffercha7": "preoffercha7`long",  # {직전매도대비수량7} 
                # "prebidcha7": "prebidcha7`long",  # {직전매수대비수량7} 
                # "offerho8": "offerho8`long",  # {매도호가8} 
                # "bidho8": "bidho8`long",  # {매수호가8} 
                # "offerrem8": "offerrem8`long",  # {매도호가수량8} 
                # "bidrem8": "bidrem8`long",  # {매수호가수량8} 
                # "preoffercha8": "preoffercha8`long",  # {직전매도대비수량8} 
                # "prebidcha8": "prebidcha8`long",  # {직전매수대비수량8} 
                # "offerho9": "offerho9`long",  # {매도호가9} 
                # "bidho9": "bidho9`long",  # {매수호가9} 
                # "offerrem9": "offerrem9`long",  # {매도호가수량9} 
                # "bidrem9": "bidrem9`long",  # {매수호가수량9} 
                # "preoffercha9": "preoffercha9`long",  # {직전매도대비수량9} 
                # "prebidcha9": "prebidcha9`long",  # {직전매수대비수량9} 
                # "offerho10": "offerho10`long",  # {매도호가10} 
                # "bidho10": "bidho10`long",  # {매수호가10} 
                # "offerrem10": "offerrem10`long",  # {매도호가수량10} 
                # "bidrem10": "bidrem10`long",  # {매수호가수량10} 
                # "preoffercha10": "preoffercha10`long",  # {직전매도대비수량10} 
                # "prebidcha10": "prebidcha10`long",  # {직전매수대비수량10} 
                # "offer": "offer`long",  # {매도호가수량합} 
                # "bid": "bid`long",  # {매수호가수량합} 
                # "preoffercha": "preoffercha`long",  # {직전매도대비수량합} 
                # "prebidcha": "prebidcha`long",  # {직전매수대비수량합} 
                # "hotime": "hotime`char",  # {수신시간} 
                # "yeprice": "yeprice`long",  # {예상체결가격} 
                # "yevolume": "yevolume`long",  # {예상체결수량} 
                # "yesign": "yesign`char",  # {예상체결전일구분} 
                # "yechange": "yechange`long",  # {예상체결전일대비} 
                # "yediff": "yediff`float",  # {예상체결등락율} 
                # "tmoffer": "tmoffer`long",  # {시간외매도잔량} 
                # "tmbid": "tmbid`long",  # {시간외매수잔량} 
                # "ho_status": "ho_status`char",  # {동시구분} 
                # "shcode": "shcode`char",  # {단축코드} 
                # "uplmtprice": "uplmtprice`long",  # {상한가} 
                # "dnlmtprice": "dnlmtprice`long",  # {하한가} 
                # "open": "open`long",  # {시가} 
                # "high": "high`long",  # {고가} 
                # "low": "low`long"  # {저가} 
            }
        }
    },
    "t1102": {  ### 주식현재가(시세)조회
        "inblock": {
            "InBlock": {
                # "shcode": " "  # {단축코드} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "hname": "hname`char",  # {한글명} 
                # "price": "price`long",  # {현재가} 
                # "sign": "sign`char",  # {전일대비구분} 
                # "change": "change`long",  # {전일대비} 
                # "diff": "diff`float",  # {등락율} 
                # "volume": "volume`long",  # {누적거래량} 
                # "recprice": "recprice`long",  # {기준가(평가가격)} 
                # "avg": "avg`long",  # {가중평균} 
                # "uplmtprice": "uplmtprice`long",  # {상한가(최고호가가격)} 
                # "dnlmtprice": "dnlmtprice`long",  # {하한가(최저호가가격)} 
                # "jnilvolume": "jnilvolume`long",  # {전일거래량} 
                # "volumediff": "volumediff`long",  # {거래량차} 
                # "open": "open`long",  # {시가} 
                # "opentime": "opentime`char",  # {시가시간} 
                # "high": "high`long",  # {고가} 
                # "hightime": "hightime`char",  # {고가시간} 
                # "low": "low`long",  # {저가} 
                # "lowtime": "lowtime`char",  # {저가시간} 
                # "high52w": "high52w`long",  # {52최고가} 
                # "high52wdate": "high52wdate`char",  # {52최고가일} 
                # "low52w": "low52w`long",  # {52최저가} 
                # "low52wdate": "low52wdate`char",  # {52최저가일} 
                # "exhratio": "exhratio`float",  # {소진율} 
                # "per": "per`float",  # {PER} 
                # "pbrx": "pbrx`float",  # {PBRX} 
                # "listing": "listing`long",  # {상장주식수(천)} 
                # "jkrate": "jkrate`long",  # {증거금율} 
                # "memedan": "memedan`char",  # {수량단위} 
                # "offernocd1": "offernocd1`char",  # {매도증권사코드1} 
                # "bidnocd1": "bidnocd1`char",  # {매수증권사코드1} 
                # "offerno1": "offerno1`char",  # {매도증권사명1} 
                # "bidno1": "bidno1`char",  # {매수증권사명1} 
                # "dvol1": "dvol1`long",  # {총매도수량1} 
                # "svol1": "svol1`long",  # {총매수수량1} 
                # "dcha1": "dcha1`long",  # {매도증감1} 
                # "scha1": "scha1`long",  # {매수증감1} 
                # "ddiff1": "ddiff1`float",  # {매도비율1} 
                # "sdiff1": "sdiff1`float",  # {매수비율1} 
                # "offernocd2": "offernocd2`char",  # {매도증권사코드2} 
                # "bidnocd2": "bidnocd2`char",  # {매수증권사코드2} 
                # "offerno2": "offerno2`char",  # {매도증권사명2} 
                # "bidno2": "bidno2`char",  # {매수증권사명2} 
                # "dvol2": "dvol2`long",  # {총매도수량2} 
                # "svol2": "svol2`long",  # {총매수수량2} 
                # "dcha2": "dcha2`long",  # {매도증감2} 
                # "scha2": "scha2`long",  # {매수증감2} 
                # "ddiff2": "ddiff2`float",  # {매도비율2} 
                # "sdiff2": "sdiff2`float",  # {매수비율2} 
                # "offernocd3": "offernocd3`char",  # {매도증권사코드3} 
                # "bidnocd3": "bidnocd3`char",  # {매수증권사코드3} 
                # "offerno3": "offerno3`char",  # {매도증권사명3} 
                # "bidno3": "bidno3`char",  # {매수증권사명3} 
                # "dvol3": "dvol3`long",  # {총매도수량3} 
                # "svol3": "svol3`long",  # {총매수수량3} 
                # "dcha3": "dcha3`long",  # {매도증감3} 
                # "scha3": "scha3`long",  # {매수증감3} 
                # "ddiff3": "ddiff3`float",  # {매도비율3} 
                # "sdiff3": "sdiff3`float",  # {매수비율3} 
                # "offernocd4": "offernocd4`char",  # {매도증권사코드4} 
                # "bidnocd4": "bidnocd4`char",  # {매수증권사코드4} 
                # "offerno4": "offerno4`char",  # {매도증권사명4} 
                # "bidno4": "bidno4`char",  # {매수증권사명4} 
                # "dvol4": "dvol4`long",  # {총매도수량4} 
                # "svol4": "svol4`long",  # {총매수수량4} 
                # "dcha4": "dcha4`long",  # {매도증감4} 
                # "scha4": "scha4`long",  # {매수증감4} 
                # "ddiff4": "ddiff4`float",  # {매도비율4} 
                # "sdiff4": "sdiff4`float",  # {매수비율4} 
                # "offernocd5": "offernocd5`char",  # {매도증권사코드5} 
                # "bidnocd5": "bidnocd5`char",  # {매수증권사코드5} 
                # "offerno5": "offerno5`char",  # {매도증권사명5} 
                # "bidno5": "bidno5`char",  # {매수증권사명5} 
                # "dvol5": "dvol5`long",  # {총매도수량5} 
                # "svol5": "svol5`long",  # {총매수수량5} 
                # "dcha5": "dcha5`long",  # {매도증감5} 
                # "scha5": "scha5`long",  # {매수증감5} 
                # "ddiff5": "ddiff5`float",  # {매도비율5} 
                # "sdiff5": "sdiff5`float",  # {매수비율5} 
                # "fwdvl": "fwdvl`long",  # {외국계매도합계수량} 
                # "ftradmdcha": "ftradmdcha`long",  # {외국계매도직전대비} 
                # "ftradmddiff": "ftradmddiff`float",  # {외국계매도비율} 
                # "fwsvl": "fwsvl`long",  # {외국계매수합계수량} 
                # "ftradmscha": "ftradmscha`long",  # {외국계매수직전대비} 
                # "ftradmsdiff": "ftradmsdiff`float",  # {외국계매수비율} 
                # "vol": "vol`float",  # {회전율} 
                # "shcode": "shcode`char",  # {단축코드} 
                # "value": "value`long",  # {누적거래대금} 
                # "jvolume": "jvolume`long",  # {전일동시간거래량} 
                # "highyear": "highyear`long",  # {연중최고가} 
                # "highyeardate": "highyeardate`char",  # {연중최고일자} 
                # "lowyear": "lowyear`long",  # {연중최저가} 
                # "lowyeardate": "lowyeardate`char",  # {연중최저일자} 
                # "target": "target`long",  # {목표가} 
                # "capital": "capital`long",  # {자본금} 
                # "abscnt": "abscnt`long",  # {유동주식수} 
                # "parprice": "parprice`long",  # {액면가} 
                # "gsmm": "gsmm`char",  # {결산월} 
                # "subprice": "subprice`long",  # {대용가} 
                # "total": "total`long",  # {시가총액} 
                # "listdate": "listdate`char",  # {상장일} 
                # "name": "name`char",  # {전분기명} 
                # "bfsales": "bfsales`long",  # {전분기매출액} 
                # "bfoperatingincome": "bfoperatingincome`long",  # {전분기영업이익} 
                # "bfordinaryincome": "bfordinaryincome`long",  # {전분기경상이익} 
                # "bfnetincome": "bfnetincome`long",  # {전분기순이익} 
                # "bfeps": "bfeps`float",  # {전분기EPS} 
                # "name2": "name2`char",  # {전전분기명} 
                # "bfsales2": "bfsales2`long",  # {전전분기매출액} 
                # "bfoperatingincome2": "bfoperatingincome2`long",  # {전전분기영업이익} 
                # "bfordinaryincome2": "bfordinaryincome2`long",  # {전전분기경상이익} 
                # "bfnetincome2": "bfnetincome2`long",  # {전전분기순이익} 
                # "bfeps2": "bfeps2`float",  # {전전분기EPS} 
                # "salert": "salert`float",  # {전년대비매출액} 
                # "opert": "opert`float",  # {전년대비영업이익} 
                # "ordrt": "ordrt`float",  # {전년대비경상이익} 
                # "netrt": "netrt`float",  # {전년대비순이익} 
                # "epsrt": "epsrt`float",  # {전년대비EPS} 
                # "info1": "info1`char",  # {락구분} 
                # "info2": "info2`char",  # {관리/급등구분} 
                # "info3": "info3`char",  # {정지/연장구분} 
                # "info4": "info4`char",  # {투자/불성실구분} 
                # "janginfo": "janginfo`char",  # {장구분} 
                # "t_per": "t_per`float",  # {T.PER} 
                # "tonghwa": "tonghwa`char",  # {통화ISO코드} 
                # "dval1": "dval1`long",  # {총매도대금1} 
                # "sval1": "sval1`long",  # {총매수대금1} 
                # "dval2": "dval2`long",  # {총매도대금2} 
                # "sval2": "sval2`long",  # {총매수대금2} 
                # "dval3": "dval3`long",  # {총매도대금3} 
                # "sval3": "sval3`long",  # {총매수대금3} 
                # "dval4": "dval4`long",  # {총매도대금4} 
                # "sval4": "sval4`long",  # {총매수대금4} 
                # "dval5": "dval5`long",  # {총매도대금5} 
                # "sval5": "sval5`long",  # {총매수대금5} 
                # "davg1": "davg1`long",  # {총매도평단가1} 
                # "savg1": "savg1`long",  # {총매수평단가1} 
                # "davg2": "davg2`long",  # {총매도평단가2} 
                # "savg2": "savg2`long",  # {총매수평단가2} 
                # "davg3": "davg3`long",  # {총매도평단가3} 
                # "savg3": "savg3`long",  # {총매수평단가3} 
                # "davg4": "davg4`long",  # {총매도평단가4} 
                # "savg4": "savg4`long",  # {총매수평단가4} 
                # "davg5": "davg5`long",  # {총매도평단가5} 
                # "savg5": "savg5`long",  # {총매수평단가5} 
                # "ftradmdval": "ftradmdval`long",  # {외국계매도대금} 
                # "ftradmsval": "ftradmsval`long",  # {외국계매수대금} 
                # "ftradmdvag": "ftradmdvag`long",  # {외국계매도평단가} 
                # "ftradmsvag": "ftradmsvag`long",  # {외국계매수평단가} 
                # "info5": "info5`char",  # {투자주의환기} 
                # "spac_gubun": "spac_gubun`char",  # {기업인수목적회사여부} 
                # "issueprice": "issueprice`long",  # {발행가격} 
                # "alloc_gubun": "alloc_gubun`char",  # {배분적용구분코드} 1:배분발생2:배분해제그외:미발생
                # "alloc_text": "alloc_text`char",  # {배분적용구분} 
                # "shterm_text": "shterm_text`char",  # {단기과열/VI발동} 
                # "svi_uplmtprice": "svi_uplmtprice`long",  # {정적VI상한가} 
                # "svi_dnlmtprice": "svi_dnlmtprice`long",  # {정적VI하한가} 
                # "low_lqdt_gu": "low_lqdt_gu`char",  # {저유동성종목여부} 
                # "abnormal_rise_gu": "abnormal_rise_gu`char",  # {이상급등종목여부} 
                # "lend_text": "lend_text`char",  # {대차불가표시} 
                # "ty_text": "ty_text`char"  # {ETF/ETN투자유의} 
            }
        }
    },
    "t1104": {  ### 주식현재가시세메모
        "inblock": {
            "InBlock": {
                # "code": " ",  # {종목코드} 
                # "nrec": " "  # {건수} 
            },
            "InBlock1": {
                # "indx": " ",  # {인덱스} 
                # "gubn": " ",  # {조건구분} 
                # "dat1": " ",  # {데이타1} 
                # "dat2": " "  # {데이타2} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "nrec": "nrec`char"  # {출력건수} 
            },
            "OutBlock1": {
                # "indx": "indx`char",  # {인덱스} 
                # "gubn": "gubn`char",  # {조건구분} 
                # "vals": "vals`char"  # {출력값} 
            }
        }
    },
    "t1105": {  ### 주식피못/디마크조회
        "inblock": {
            "InBlock": {
                # "shcode": " "  # {단축코드} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "shcode": "shcode`char",  # {단축코드} 
                # "pbot": "pbot`long",  # {피봇} 
                # "offer1": "offer1`long",  # {1차저항} 
                # "supp1": "supp1`long",  # {1차지지} 
                # "offer2": "offer2`long",  # {2차저항} 
                # "supp2": "supp2`long",  # {2차지지} 
                # "stdprc": "stdprc`long",  # {기준가격} 
                # "offerd": "offerd`long",  # {D저항} 
                # "suppd": "suppd`long"  # {D지지} 
            }
        }
    },
    "t1301": {  ### 주식시간대별체결조회
        "inblock": {
            "InBlock": {
                # "shcode": " ",  # {단축코드} 
                # "cvolume": 0,  # {특이거래량} 
                # "starttime": " ",  # {시작시간} 
                # "endtime": " ",  # {종료시간} 
                # "cts_time": " "  # {시간CTS} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "cts_time": "cts_time`char"  # {시간CTS} 
            },
            "OutBlock1": {
                # "chetime": "chetime`char",  # {시간} 
                # "price": "price`long",  # {현재가} 
                # "sign": "sign`char",  # {전일대비구분} 
                # "change": "change`long",  # {전일대비} 
                # "diff": "diff`float",  # {등락율} 
                # "cvolume": "cvolume`long",  # {체결수량} 
                # "chdegree": "chdegree`float",  # {체결강도} 
                # "volume": "volume`long",  # {거래량} 
                # "mdvolume": "mdvolume`long",  # {매도체결수량} 
                # "mdchecnt": "mdchecnt`long",  # {매도체결건수} 
                # "msvolume": "msvolume`long",  # {매수체결수량} 
                # "mschecnt": "mschecnt`long",  # {매수체결건수} 
                # "revolume": "revolume`long",  # {순체결량} 
                # "rechecnt": "rechecnt`long"  # {순체결건수} 
            }
        }
    },
    "t1302": {  ### 주식분별주가조회
        "inblock": {
            "InBlock": {
                # "shcode": " ",  # {단축코드} 
                # "gubun": " ",  # {작업구분} 
                # "time": " ",  # {시간} 
                # "cnt": 0  # {건수} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "cts_time": "cts_time`char"  # {시간CTS} 
            },
            "OutBlock1": {
                # "chetime": "chetime`char",  # {시간} 
                # "close": "close`long",  # {종가} 
                # "sign": "sign`char",  # {전일대비구분} 
                # "change": "change`long",  # {전일대비} 
                # "diff": "diff`float",  # {등락율} 
                # "chdegree": "chdegree`float",  # {체결강도} 
                # "mdvolume": "mdvolume`long",  # {매도체결수량} 
                # "msvolume": "msvolume`long",  # {매수체결수량} 
                # "revolume": "revolume`long",  # {순매수체결량} 
                # "mdchecnt": "mdchecnt`long",  # {매도체결건수} 
                # "mschecnt": "mschecnt`long",  # {매수체결건수} 
                # "rechecnt": "rechecnt`long",  # {순체결건수} 
                # "volume": "volume`long",  # {거래량} 
                # "open": "open`long",  # {시가} 
                # "high": "high`long",  # {고가} 
                # "low": "low`long",  # {저가} 
                # "cvolume": "cvolume`long",  # {체결량} 
                # "mdchecnttm": "mdchecnttm`long",  # {매도체결건수(시간)} 
                # "mschecnttm": "mschecnttm`long",  # {매수체결건수(시간)} 
                # "totofferrem": "totofferrem`long",  # {매도잔량} 
                # "totbidrem": "totbidrem`long",  # {매수잔량} 
                # "mdvolumetm": "mdvolumetm`long",  # {시간별매도체결량} 
                # "msvolumetm": "msvolumetm`long"  # {시간별매수체결량} 
            }
        }
    },
    "t1305": {  ### 기간별주가
        "inblock": {
            "InBlock": {
                # "shcode": " ",  # {단축코드} 
                # "dwmcode": 0,  # {일주월구분} 
                # "date": " ",  # {날짜} 
                # "idx": 0,  # {IDX} 
                # "cnt": 0  # {건수} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "cnt": "cnt`long",  # {CNT} 
                # "date": "date`char",  # {날짜} 
                # "idx": "idx`long"  # {IDX} 
            },
            "OutBlock1": {
                # "date": "date`char",  # {날짜} 
                # "open": "open`long",  # {시가} 
                # "high": "high`long",  # {고가} 
                # "low": "low`long",  # {저가} 
                # "close": "close`long",  # {종가} 
                # "sign": "sign`char",  # {전일대비구분} 
                # "change": "change`long",  # {전일대비} 
                # "diff": "diff`float",  # {등락율} 
                # "volume": "volume`long",  # {누적거래량} 
                # "diff_vol": "diff_vol`float",  # {거래증가율} 
                # "chdegree": "chdegree`float",  # {체결강도} 
                # "sojinrate": "sojinrate`float",  # {소진율} 
                # "changerate": "changerate`float",  # {회전율} 
                # "fpvolume": "fpvolume`long",  # {외인순매수} 
                # "covolume": "covolume`long",  # {기관순매수} 
                # "shcode": "shcode`char",  # {종목코드} 
                # "value": "value`long",  # {누적거래대금} 단위:백만
                # "ppvolume": "ppvolume`long",  # {개인순매수} 
                # "o_sign": "o_sign`char",  # {시가대비구분} 
                # "o_change": "o_change`long",  # {시가대비} 
                # "o_diff": "o_diff`float",  # {시가기준등락율} 
                # "h_sign": "h_sign`char",  # {고가대비구분} 
                # "h_change": "h_change`long",  # {고가대비} 
                # "h_diff": "h_diff`float",  # {고가기준등락율} 
                # "l_sign": "l_sign`char",  # {저가대비구분} 
                # "l_change": "l_change`long",  # {저가대비} 
                # "l_diff": "l_diff`float",  # {저가기준등락율} 
                # "marketcap": "marketcap`long"  # {시가총액} 단위:백만
            }
        }
    },
    "t1308": {  ### 주식시간대별체결조회챠트
        "inblock": {
            "InBlock": {
                # "shcode": " ",  # {단축코드} 
                # "starttime": " ",  # {시작시간} 
                # "endtime": " ",  # {종료시간} 
                # "bun_term": " "  # {분간격} 
            }
        },
        "outblock": {
            "OutBlock1": {
                # "chetime": "chetime`char",  # {시간} 
                # "price": "price`long",  # {현재가} 
                # "sign": "sign`char",  # {전일대비구분} 
                # "change": "change`long",  # {전일대비} 
                # "diff": "diff`float",  # {등락율} 
                # "cvolume": "cvolume`long",  # {체결수량} 
                # "chdegvol": "chdegvol`float",  # {체결강도(거래량)} 
                # "chdegcnt": "chdegcnt`float",  # {체결강도(건수)} 
                # "volume": "volume`long",  # {거래량} 
                # "mdvolume": "mdvolume`long",  # {매도체결수량} 
                # "mdchecnt": "mdchecnt`long",  # {매도체결건수} 
                # "msvolume": "msvolume`long",  # {매수체결수량} 
                # "mschecnt": "mschecnt`long",  # {매수체결건수} 
                # "open": "open`long",  # {시가} 
                # "high": "high`long",  # {고가} 
                # "low": "low`long"  # {저가} 
            }
        }
    },
    "t1310": {  ### 주식당일전일분틱조회
        "inblock": {
            "InBlock": {
                # "daygb": " ",  # {당일전일구분} 
                # "timegb": " ",  # {분틱구분} 
                # "shcode": " ",  # {단축코드} 
                # "endtime": " ",  # {종료시간} 
                # "cts_time": " "  # {시간CTS} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "cts_time": "cts_time`char"  # {시간CTS} 
            },
            "OutBlock1": {
                # "chetime": "chetime`char",  # {시간} 
                # "price": "price`long",  # {현재가} 
                # "sign": "sign`char",  # {전일대비구분} 
                # "change": "change`long",  # {전일대비} 
                # "diff": "diff`float",  # {등락율} 
                # "cvolume": "cvolume`long",  # {체결수량} 
                # "chdegree": "chdegree`float",  # {체결강도} 
                # "volume": "volume`long",  # {거래량} 
                # "mdvolume": "mdvolume`long",  # {매도체결수량} 
                # "mdchecnt": "mdchecnt`long",  # {매도체결건수} 
                # "msvolume": "msvolume`long",  # {매수체결수량} 
                # "mschecnt": "mschecnt`long",  # {매수체결건수} 
                # "revolume": "revolume`long",  # {순체결량} 
                # "rechecnt": "rechecnt`long"  # {순체결건수} 
            }
        }
    },
    "t1403": {  ### 신규상장종목조회
        "inblock": {
            "InBlock": {
                # "gubun": " ",  # {구분} 
                # "styymm": " ",  # {시작상장월} 
                # "enyymm": " ",  # {종료상장월} 
                # "idx": 0  # {IDX} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "idx": "idx`long"  # {IDX} 
            },
            "OutBlock1": {
                # "hname": "hname`char",  # {한글명} 
                # "price": "price`long",  # {현재가} 
                # "sign": "sign`char",  # {전일대비구분} 
                # "change": "change`long",  # {전일대비} 
                # "diff": "diff`float",  # {등락율} 
                # "volume": "volume`long",  # {누적거래량} 
                # "kmprice": "kmprice`long",  # {공모가} 
                # "date": "date`char",  # {등록일} 
                # "recprice": "recprice`long",  # {등록일기준가} 
                # "kmdiff": "kmdiff`float",  # {기준가등락율} 
                # "close": "close`long",  # {등록일종가} 
                # "recdiff": "recdiff`float",  # {등록일등락율} 
                # "shcode": "shcode`char"  # {종목코드} 
            }
        }
    },
    "t1404": {  ### 관리/불성실/투자유의조회
        "inblock": {
            "InBlock": {
                # "gubun": " ",  # {구분} 
                # "jongchk": " ",  # {종목체크} 
                # "cts_shcode": " "  # {종목코드_CTS} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "cts_shcode": "cts_shcode`char"  # {종목코드_CTS} 
            },
            "OutBlock1": {
                # "hname": "hname`char",  # {한글명} 
                # "price": "price`long",  # {현재가} 
                # "sign": "sign`char",  # {전일대비구분} 
                # "change": "change`long",  # {전일대비} 
                # "diff": "diff`float",  # {등락율} 
                # "volume": "volume`long",  # {누적거래량} 
                # "date": "date`char",  # {지정일} 
                # "tprice": "tprice`long",  # {지정일주가} 
                # "tchange": "tchange`long",  # {지정일대비} 
                # "tdiff": "tdiff`float",  # {대비율} 
                # "reason": "reason`char",  # {사유} 
                # "shcode": "shcode`char",  # {종목코드} 
                # "edate": "edate`char"  # {해제일} 
            }
        }
    },
    "t1405": {  ### 투자경고/매매정지/정리매매조회
        "inblock": {
            "InBlock": {
                # "gubun": " ",  # {구분} 
                # "jongchk": " ",  # {종목체크} 
                # "cts_shcode": " "  # {종목코드_CTS} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "cts_shcode": "cts_shcode`char"  # {종목코드_CTS} 
            },
            "OutBlock1": {
                # "hname": "hname`char",  # {한글명} 
                # "price": "price`long",  # {현재가} 
                # "sign": "sign`char",  # {전일대비구분} 
                # "change": "change`long",  # {전일대비} 
                # "diff": "diff`float",  # {등락율} 
                # "volume": "volume`long",  # {누적거래량} 
                # "date": "date`char",  # {지정일} 
                # "edate": "edate`char",  # {해제일} 
                # "shcode": "shcode`char"  # {종목코드} 
            }
        }
    },
    "t1410": {  ### 초저유동성조회
        "inblock": {
            "InBlock": {
                # "gubun": " ",  # {구분} 
                # "cts_shcode": " "  # {종목코드_CTS} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "cts_shcode": "cts_shcode`char"  # {종목코드_CTS} 
            },
            "OutBlock1": {
                # "hname": "hname`char",  # {한글명} 
                # "price": "price`long",  # {현재가} 
                # "sign": "sign`char",  # {전일대비구분} 
                # "change": "change`long",  # {전일대비} 
                # "diff": "diff`float",  # {등락율} 
                # "volume": "volume`long",  # {누적거래량} 
                # "shcode": "shcode`char"  # {종목코드} 
            }
        }
    },
    "t1411": {  ### 증거금율별종목조회
        "inblock": {
            "InBlock": {
                # "gubun": " ",  # {시장구분} 
                # "jongchk": " ",  # {위탁신용구분} 
                # "jkrate": " ",  # {증거금율구분} 
                # "shcode": " ",  # {종목코드} 
                # "idx": 0  # {IDX} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "jkrate": "jkrate`long",  # {위탁증거금율} 
                # "sjkrate": "sjkrate`long",  # {신용증거금율} 
                # "idx": "idx`long"  # {IDX} 
            },
            "OutBlock1": {
                # "shcode": "shcode`char",  # {종목코드} 
                # "hname": "hname`char",  # {종목명} 
                # "jkrate": "jkrate`long",  # {위탁증거금율} 
                # "sjkrate": "sjkrate`long",  # {신용증거금율} 
                # "subprice": "subprice`long",  # {대용가} 
                # "recprice": "recprice`long",  # {전일종가} 
                # "price": "price`long",  # {현재가} 
                # "sign": "sign`char",  # {전일대비구분} 
                # "change": "change`long",  # {전일대비} 
                # "diff": "diff`float",  # {등락율} 
                # "volume": "volume`long"  # {누적거래량} 
            }
        }
    },
    "t1422": {  ### 상/하한
        "inblock": {
            "InBlock": {
                # "qrygb": " ",  # {조회구분} 
                # "gubun": " ",  # {구분} 
                # "jnilgubun": " ",  # {전일구분} 
                # "sign": " ",  # {상하한구분} 
                # "jc_num": 0,  # {대상제외} 
                # "sprice": 0,  # {시작가격} 
                # "eprice": 0,  # {종료가격} 
                # "volume": 0,  # {거래량} 
                # "idx": 0  # {IDX} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "cnt": "cnt`long",  # {CNT} 
                # "idx": "idx`long"  # {IDX} 
            },
            "OutBlock1": {
                # "hname": "hname`char",  # {한글명} 
                # "price": "price`long",  # {현재가} 
                # "sign": "sign`char",  # {전일대비구분} 
                # "change": "change`long",  # {전일대비} 
                # "diff": "diff`float",  # {등락율} 
                # "volume": "volume`long",  # {누적거래량} 
                # "diff_vol": "diff_vol`float",  # {거래증가율} 
                # "offerrem1": "offerrem1`long",  # {매도잔량} 
                # "bidrem1": "bidrem1`long",  # {매수잔량} 
                # "last": "last`char",  # {최종진입} 
                # "lmtdaycnt": "lmtdaycnt`long",  # {연속} 
                # "jnilvolume": "jnilvolume`long",  # {전일거래량} 
                # "shcode": "shcode`char"  # {종목코드} 
            }
        }
    },
    "t1427": {  ### 상/하한가직전
        "inblock": {
            "InBlock": {
                # "qrygb": " ",  # {조회구분} 
                # "gubun": " ",  # {구분} 
                # "signgubun": " ",  # {상하한가구분} 
                # "diff": 0,  # {등락율} 
                # "jc_num": 0,  # {대상제외} 
                # "sprice": 0,  # {시작가격} 
                # "eprice": 0,  # {종료가격} 
                # "volume": 0,  # {거래량} 
                # "idx": 0,  # {IDX} 
                # "jshex": " "  # {전일상하한제외} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "cnt": "cnt`long",  # {CNT} 
                # "idx": "idx`long"  # {IDX} 
            },
            "OutBlock1": {
                # "hname": "hname`char",  # {한글명} 
                # "price": "price`long",  # {현재가} 
                # "sign": "sign`char",  # {전일대비구분} 
                # "change": "change`long",  # {전일대비} 
                # "diff": "diff`float",  # {등락율} 
                # "volume": "volume`long",  # {누적거래량} 
                # "diff_vol": "diff_vol`float",  # {거래증가율} 
                # "lmtprice": "lmtprice`long",  # {상한가/하한가} 
                # "rate": "rate`float",  # {대비율} 
                # "shcode": "shcode`char",  # {종목코드} 
                # "jnilvolume": "jnilvolume`long",  # {전일거래량} 
                # "open": "open`long",  # {시가} 
                # "high": "high`long",  # {고가} 
                # "low": "low`long",  # {저가} 
                # "lmtdaycnt": "lmtdaycnt`long",  # {연속} 
                # "value": "value`long",  # {거래대금} 
                # "total": "total`long"  # {시가총액} 
            }
        }
    },
    "t1442": {  ### 신고/신저가
        "inblock": {
            "InBlock": {
                # "gubun": " ",  # {구분} 
                # "type1": " ",  # {신고신저} 
                # "type2": " ",  # {기간} 
                # "type3": " ",  # {유지여부} 
                # "jc_num": 0,  # {대상제외} 
                # "sprice": 0,  # {시작가격} 
                # "eprice": 0,  # {종료가격} 
                # "volume": 0,  # {거래량} 
                # "idx": 0,  # {IDX} 
                # "jc_num2": 0  # {대상제외2} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "idx": "idx`long"  # {IDX} 
            },
            "OutBlock1": {
                # "shcode": "shcode`char",  # {종목코드} 
                # "hname": "hname`char",  # {종목명} 
                # "price": "price`long",  # {현재가} 
                # "sign": "sign`char",  # {전일대비구분} 
                # "change": "change`long",  # {전일대비} 
                # "diff": "diff`float",  # {등락율} 
                # "volume": "volume`long",  # {거래량} 
                # "pastprice": "pastprice`long",  # {이전가} 
                # "pastsign": "pastsign`char",  # {이전가대비구분} 
                # "pastchange": "pastchange`long",  # {이전가대비} 
                # "pastdiff": "pastdiff`float"  # {이전가대비율} 
            }
        }
    },
    "t1444": {  ### 시가총액상위
        "inblock": {
            "InBlock": {
                # "upcode": " ",  # {업종코드} 
                # "idx": 0  # {IDX} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "idx": "idx`long"  # {IDX} 
            },
            "OutBlock1": {
                # "shcode": "shcode`char",  # {종목코드} 
                # "hname": "hname`char",  # {종목명} 
                # "price": "price`long",  # {현재가} 
                # "sign": "sign`char",  # {전일대비구분} 
                # "change": "change`long",  # {전일대비} 
                # "diff": "diff`float",  # {등락율} 
                # "volume": "volume`long",  # {거래량} 
                # "vol_rate": "vol_rate`float",  # {거래비중} 
                # "total": "total`long",  # {시가총액} 
                # "rate": "rate`float",  # {비중} 
                # "for_rate": "for_rate`float"  # {외인비중} 
            }
        }
    },
    "t1449": {  ### 가격대별매매비중조회
        "inblock": {
            "InBlock": {
                # "shcode": " ",  # {단축코드} 
                # "dategb": " "  # {일자구분} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "price": "price`long",  # {현재가} 
                # "sign": "sign`char",  # {전일대비구분} 
                # "change": "change`long",  # {전일대비} 
                # "diff": "diff`float",  # {등락율} 
                # "volume": "volume`long",  # {거래량} 
                # "msvolume": "msvolume`long",  # {매수체결량} 
                # "mdvolume": "mdvolume`long"  # {매도체결량} 
            },
            "OutBlock1": {
                # "price": "price`long",  # {체결가} 
                # "sign": "sign`char",  # {전일대비구분} 
                # "change": "change`long",  # {전일대비} 
                # "tickdiff": "tickdiff`float",  # {등락율} 
                # "cvolume": "cvolume`long",  # {체결수량} 
                # "diff": "diff`float",  # {비중} 
                # "mdvolume": "mdvolume`long",  # {매도체결량} 
                # "msvolume": "msvolume`long",  # {매수체결량} 
                # "msdiff": "msdiff`float"  # {매수비율} 
            }
        }
    },
    "t1452": {  ### 거래량상위
        "inblock": {
            "InBlock": {
                # "gubun": " ",  # {구분} 
                # "jnilgubun": " ",  # {전일구분} 
                # "sdiff": 0,  # {시작등락율} 
                # "ediff": 0,  # {종료등락율} 
                # "jc_num": 0,  # {대상제외} 
                # "sprice": 0,  # {시작가격} 
                # "eprice": 0,  # {종료가격} 
                # "volume": 0,  # {거래량} 
                # "idx": 0  # {IDX} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "idx": "idx`long"  # {IDX} 
            },
            "OutBlock1": {
                # "hname": "hname`char",  # {종목명} 
                # "price": "price`long",  # {현재가} 
                # "sign": "sign`char",  # {전일대비구분} 
                # "change": "change`long",  # {전일대비} 
                # "diff": "diff`float",  # {등락율} 
                # "volume": "volume`long",  # {누적거래량} 
                # "vol": "vol`float",  # {회전율} 
                # "jnilvolume": "jnilvolume`long",  # {전일거래량} 
                # "bef_diff": "bef_diff`float",  # {전일비} 
                # "shcode": "shcode`char"  # {종목코드} 
            }
        }
    },
    "t1463": {  ### 거래대금상위
        "inblock": {
            "InBlock": {
                # "gubun": " ",  # {구분} 
                # "jnilgubun": " ",  # {전일구분} 
                # "jc_num": 0,  # {대상제외} 
                # "sprice": 0,  # {시작가격} 
                # "eprice": 0,  # {종료가격} 
                # "volume": 0,  # {거래량} 
                # "idx": 0,  # {IDX} 
                # "jc_num2": 0  # {대상제외2} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "idx": "idx`long"  # {IDX} 
            },
            "OutBlock1": {
                # "hname": "hname`char",  # {한글명} 
                # "price": "price`long",  # {현재가} 
                # "sign": "sign`char",  # {전일대비구분} 
                # "change": "change`long",  # {전일대비} 
                # "diff": "diff`float",  # {등락율} 
                # "volume": "volume`long",  # {누적거래량} 
                # "value": "value`long",  # {거래대금} 
                # "jnilvalue": "jnilvalue`long",  # {전일거래대금} 
                # "bef_diff": "bef_diff`float",  # {전일비} 
                # "shcode": "shcode`char",  # {종목코드} 
                # "filler": "filler`char",  # {filler} 
                # "jnilvolume": "jnilvolume`long"  # {전일거래량} 
            }
        }
    },
    "t1471": {  ### 시간대별호가잔량추이
        "inblock": {
            "InBlock": {
                # "shcode": " ",  # {종목코드} 
                # "gubun": " ",  # {분구분} 
                # "time": " ",  # {시간} 
                # "cnt": " "  # {자료개수} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "time": "time`char",  # {시간CTS} 
                # "price": "price`long",  # {현재가} 
                # "sign": "sign`char",  # {전일대비구분} 
                # "change": "change`long",  # {전일대비} 
                # "diff": "diff`float",  # {등락율} 
                # "volume": "volume`long"  # {누적거래량} 
            },
            "OutBlock1": {
                # "time": "time`char",  # {체결시간} 
                # "preoffercha1": "preoffercha1`long",  # {메도증감} 
                # "offerrem1": "offerrem1`long",  # {매도우선잔량} 
                # "offerho1": "offerho1`long",  # {매도우선호가} 
                # "bidho1": "bidho1`long",  # {매수우선호가} 
                # "bidrem1": "bidrem1`long",  # {매수우선잔량} 
                # "prebidcha1": "prebidcha1`long",  # {매수증감} 
                # "totofferrem": "totofferrem`long",  # {총매도} 
                # "totbidrem": "totbidrem`long",  # {총매수} 
                # "totsun": "totsun`long",  # {순매수} 
                # "msrate": "msrate`float",  # {매수비율} 
                # "close": "close`long"  # {종가} 
            }
        }
    },
    "t1475": {  ### 체결강도추이
        "inblock": {
            "InBlock": {
                # "shcode": " ",  # {종목코드} 
                # "vptype": " ",  # {상승하락} 
                # "datacnt": 0,  # {데이터개수} 
                # "date": 0,  # {기준일자} 
                # "time": 0,  # {기준시간} 
                # "rankcnt": 0,  # {랭크카운터} 
                # "gubun": " "  # {조회구분} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "date": "date`long",  # {기준일자} 
                # "time": "time`long",  # {기준시간} 
                # "rankcnt": "rankcnt`long"  # {랭크카운터} 
            },
            "OutBlock1": {
                # "datetime": "datetime`char",  # {일자} 
                # "price": "price`long",  # {현재가} 
                # "sign": "sign`char",  # {전일대비구분} 
                # "change": "change`long",  # {전일대비} 
                # "diff": "diff`float",  # {등락율} 
                # "volume": "volume`long",  # {거래량} 
                # "todayvp": "todayvp`float",  # {당일VP} 
                # "ma5vp": "ma5vp`float",  # {5일MAVP} 
                # "ma20vp": "ma20vp`float",  # {20일MAVP} 
                # "ma60vp": "ma60vp`float"  # {60일MAVP} 
            }
        }
    },
    "t1485": {  ### 예상지수
        "inblock": {
            "InBlock": {
                # "upcode": " ",  # {업종코드} 
                # "gubun": " "  # {조회구분} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "pricejisu": "pricejisu`float",  # {현재지수} 
                # "sign": "sign`char",  # {지수전일대비구분} 
                # "change": "change`float",  # {전일대비} 
                # "volume": "volume`long",  # {거래량} 
                # "yhighjo": "yhighjo`long",  # {상승종목수} 
                # "yupjo": "yupjo`long",  # {상한종목수} 
                # "yunchgjo": "yunchgjo`long",  # {보합종목수} 
                # "ylowjo": "ylowjo`long",  # {하락종목수} 
                # "ydownjo": "ydownjo`long",  # {하한종목수} 
                # "ytrajo": "ytrajo`long"  # {거래형성수} 
            },
            "OutBlock1": {
                # "chetime": "chetime`char",  # {시간} 
                # "jisu": "jisu`float",  # {예상지수} 
                # "sign": "sign`char",  # {전일대비구분} 
                # "change": "change`float",  # {전일대비} 
                # "volume": "volume`long",  # {예상체결량} 
                # "volcha": "volcha`long"  # {예상체결량직전대비} 
            }
        }
    },
    "t1486": {  ### 시간별예상체결가
        "inblock": {
            "InBlock": {
                # "shcode": " ",  # {단축코드} 
                # "cts_time": " ",  # {시간CTS} 
                # "cnt": 0  # {조회건수} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "cts_time": "cts_time`char"  # {시간CTS} 
            },
            "OutBlock1": {
                # "chetime": "chetime`char",  # {시간} 
                # "price": "price`long",  # {예상체결가} 
                # "sign": "sign`char",  # {전일대비구분} 
                # "change": "change`long",  # {전일대비} 
                # "diff": "diff`float",  # {등락율} 
                # "cvolume": "cvolume`long",  # {예상체결량} 
                # "offerho1": "offerho1`long",  # {매도호가} 
                # "bidho1": "bidho1`long",  # {매수호가} 
                # "offerrem1": "offerrem1`long",  # {매도잔량} 
                # "bidrem1": "bidrem1`long"  # {매수잔량} 
            }
        }
    },
    "t1488": {  ### 예상체결가등락율상위조회
        "inblock": {
            "InBlock": {
                # "gubun": " ",  # {거래소구분} 
                # "sign": " ",  # {상하락구분} 
                # "jgubun": " ",  # {장구분} 
                # "jongchk": " ",  # {종목체크} 
                # "idx": 0,  # {IDX} 
                # "volume": " ",  # {거래량} 
                # "yesprice": 0,  # {예상체결시작가격} 
                # "yeeprice": 0,  # {예상체결종료가격} 
                # "yevolume": 0  # {예상체결량} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "idx": "idx`long"  # {IDX} 
            },
            "OutBlock1": {
                # "hname": "hname`char",  # {한글명} 
                # "price": "price`long",  # {현재가} 
                # "sign": "sign`char",  # {전일대비구분} 
                # "change": "change`long",  # {전일대비} 
                # "diff": "diff`float",  # {등락율} 
                # "volume": "volume`long",  # {누적거래량} 
                # "offerrem": "offerrem`long",  # {매도잔량} 
                # "offerho": "offerho`long",  # {매도호가} 
                # "bidho": "bidho`long",  # {매수호가} 
                # "bidrem": "bidrem`long",  # {매수잔량} 
                # "cnt": "cnt`long",  # {연속일수} 
                # "shcode": "shcode`char",  # {종목코드} 
                # "jkrate": "jkrate`char",  # {증거금율} 
                # "jnilvolume": "jnilvolume`long"  # {전일거래량} 
            }
        }
    },
    "t1489": {  ### 예상체결량상위조회
        "inblock": {
            "InBlock": {
                # "gubun": " ",  # {거래소구분} 
                # "jgubun": " ",  # {장구분} 
                # "jongchk": " ",  # {종목체크} 
                # "idx": 0,  # {IDX} 
                # "yesprice": 0,  # {예상체결시작가격} 
                # "yeeprice": 0,  # {예상체결종료가격} 
                # "yevolume": 0  # {예상체결량} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "idx": "idx`long"  # {IDX} 
            },
            "OutBlock1": {
                # "hname": "hname`char",  # {한글명} 
                # "price": "price`long",  # {현재가} 
                # "sign": "sign`char",  # {전일대비구분} 
                # "change": "change`long",  # {전일대비} 
                # "diff": "diff`float",  # {등락율} 
                # "volume": "volume`long",  # {예상거래량} 
                # "offerho": "offerho`long",  # {매도호가} 
                # "bidho": "bidho`long",  # {매수호가} 
                # "shcode": "shcode`char",  # {종목코드} 
                # "jnilvolume": "jnilvolume`long"  # {전일거래량} 
            }
        }
    },
    "t1511": {  ### 업종현재가
        "inblock": {
            "InBlock": {
                # "upcode": " "  # {업종코드} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "gubun": "gubun`char",  # {업종구분} 
                # "hname": "hname`char",  # {업종명} 
                # "pricejisu": "pricejisu`float",  # {현재지수} 
                # "jniljisu": "jniljisu`float",  # {전일지수} 
                # "sign": "sign`char",  # {전일대비구분} 
                # "change": "change`float",  # {전일대비} 
                # "diffjisu": "diffjisu`float",  # {지수등락율} 
                # "jnilvolume": "jnilvolume`long",  # {전일거래량} 
                # "volume": "volume`long",  # {당일거래량} 
                # "volumechange": "volumechange`long",  # {거래량전일대비} 
                # "volumerate": "volumerate`float",  # {거래량비율} 
                # "jnilvalue": "jnilvalue`long",  # {전일거래대금} 
                # "value": "value`long",  # {당일거래대금} 
                # "valuechange": "valuechange`long",  # {거래대금전일대비} 
                # "valuerate": "valuerate`float",  # {거래대금비율} 
                # "openjisu": "openjisu`float",  # {시가지수} 
                # "opendiff": "opendiff`float",  # {시가등락율} 
                # "opentime": "opentime`char",  # {시가시간} 
                # "highjisu": "highjisu`float",  # {고가지수} 
                # "highdiff": "highdiff`float",  # {고가등락율} 
                # "hightime": "hightime`char",  # {고가시간} 
                # "lowjisu": "lowjisu`float",  # {저가지수} 
                # "lowdiff": "lowdiff`float",  # {저가등락율} 
                # "lowtime": "lowtime`char",  # {저가시간} 
                # "whjisu": "whjisu`float",  # {52주최고지수} 
                # "whchange": "whchange`float",  # {52주최고현재가대비} 
                # "whjday": "whjday`char",  # {52주최고지수일자} 
                # "wljisu": "wljisu`float",  # {52주최저지수} 
                # "wlchange": "wlchange`float",  # {52주최저현재가대비} 
                # "wljday": "wljday`char",  # {52주최저지수일자} 
                # "yhjisu": "yhjisu`float",  # {연중최고지수} 
                # "yhchange": "yhchange`float",  # {연중최고현재가대비} 
                # "yhjday": "yhjday`char",  # {연중최고지수일자} 
                # "yljisu": "yljisu`float",  # {연중최저지수} 
                # "ylchange": "ylchange`float",  # {연중최저현재가대비} 
                # "yljday": "yljday`char",  # {연중최저지수일자} 
                # "firstjcode": "firstjcode`char",  # {첫번째지수코드} 
                # "firstjname": "firstjname`char",  # {첫번째지수명} 
                # "firstjisu": "firstjisu`float",  # {첫번째지수} 
                # "firsign": "firsign`char",  # {첫번째대비구분} 
                # "firchange": "firchange`float",  # {첫번째전일대비} 
                # "firdiff": "firdiff`float",  # {첫번째등락율} 
                # "secondjcode": "secondjcode`char",  # {두번째지수코드} 
                # "secondjname": "secondjname`char",  # {두번째지수명} 
                # "secondjisu": "secondjisu`float",  # {두번째지수} 
                # "secsign": "secsign`char",  # {두번째대비구분} 
                # "secchange": "secchange`float",  # {두번째전일대비} 
                # "secdiff": "secdiff`float",  # {두번째등락율} 
                # "thirdjcode": "thirdjcode`char",  # {세번째지수코드} 
                # "thirdjname": "thirdjname`char",  # {세번째지수명} 
                # "thirdjisu": "thirdjisu`float",  # {세번째지수} 
                # "thrsign": "thrsign`char",  # {세번째대비구분} 
                # "thrchange": "thrchange`float",  # {세번째전일대비} 
                # "thrdiff": "thrdiff`float",  # {세번째등락율} 
                # "fourthjcode": "fourthjcode`char",  # {네번째지수코드} 
                # "fourthjname": "fourthjname`char",  # {네번째지수명} 
                # "fourthjisu": "fourthjisu`float",  # {네번째지수} 
                # "forsign": "forsign`char",  # {네번째대비구분} 
                # "forchange": "forchange`float",  # {네번째전일대비} 
                # "fordiff": "fordiff`float",  # {네번째등락율} 
                # "highjo": "highjo`long",  # {상승종목수} 
                # "upjo": "upjo`long",  # {상한종목수} 
                # "unchgjo": "unchgjo`long",  # {보합종목수} 
                # "lowjo": "lowjo`long",  # {하락종목수} 
                # "downjo": "downjo`long"  # {하한종목수} 
            }
        }
    },
    "t1514": {  ### 업종기간별추이
        "inblock": {
            "InBlock": {
                # "upcode": " ",  # {업종코드} 
                # "gubun1": " ",  # {구분1} 
                # "gubun2": " ",  # {구분2} 
                # "cts_date": " ",  # {CTS_일자} 
                # "cnt": 0,  # {조회건수} 
                # "rate_gbn": " "  # {비중구분} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "cts_date": "cts_date`char"  # {CTS_일자} 
            },
            "OutBlock1": {
                # "date": "date`char",  # {일자} 
                # "jisu": "jisu`float",  # {지수} 
                # "sign": "sign`char",  # {전일대비구분} 
                # "change": "change`float",  # {전일대비} 
                # "diff": "diff`float",  # {등락율} 
                # "volume": "volume`long",  # {거래량} 
                # "diff_vol": "diff_vol`float",  # {거래증가율} 
                # "value1": "value1`long",  # {거래대금1} 
                # "high": "high`long",  # {상승} 
                # "unchg": "unchg`long",  # {보합} 
                # "low": "low`long",  # {하락} 
                # "uprate": "uprate`float",  # {상승종목비율} 
                # "frgsvolume": "frgsvolume`long",  # {외인순매수} 
                # "openjisu": "openjisu`float",  # {시가} 
                # "highjisu": "highjisu`float",  # {고가} 
                # "lowjisu": "lowjisu`float",  # {저가} 
                # "value2": "value2`long",  # {거래대금2} 
                # "up": "up`long",  # {상한} 
                # "down": "down`long",  # {하한} 
                # "totjo": "totjo`long",  # {종목수} 
                # "orgsvolume": "orgsvolume`long",  # {기관순매수} 
                # "upcode": "upcode`char",  # {업종코드} 
                # "rate": "rate`float",  # {거래비중} 
                # "divrate": "divrate`float"  # {업종배당수익률} 
            }
        }
    },
    "t1516": {  ### 업종별종목시세
        "inblock": {
            "InBlock": {
                # "upcode": " ",  # {업종코드} 
                # "gubun": " ",  # {구분} 
                # "shcode": " "  # {종목코드} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "shcode": "shcode`char",  # {종목코드} 
                # "pricejisu": "pricejisu`float",  # {지수} 
                # "sign": "sign`char",  # {전일대비구분} 
                # "change": "change`float",  # {전일대비} 
                # "jdiff": "jdiff`float"  # {등락율} 
            },
            "OutBlock1": {
                # "hname": "hname`char",  # {종목명} 
                # "price": "price`long",  # {현재가} 
                # "sign": "sign`char",  # {전일대비구분} 
                # "change": "change`long",  # {전일대비} 
                # "diff": "diff`float",  # {등락율} 
                # "volume": "volume`long",  # {누적거래량} 
                # "open": "open`long",  # {시가} 
                # "high": "high`long",  # {고가} 
                # "low": "low`long",  # {저가} 
                # "sojinrate": "sojinrate`float",  # {소진율} 
                # "beta": "beta`float",  # {베타계수} 
                # "perx": "perx`float",  # {PER} 
                # "frgsvolume": "frgsvolume`long",  # {외인순매수} 
                # "orgsvolume": "orgsvolume`long",  # {기관순매수} 
                # "diff_vol": "diff_vol`float",  # {거래증가율} 
                # "shcode": "shcode`char",  # {종목코드} 
                # "total": "total`long",  # {시가총액} 
                # "value": "value`long"  # {거래대금} 
            }
        }
    },
    "t1531": {  ### 테마별종목
        "inblock": {
            "InBlock": {
                # "tmname": " ",  # {테마명} 
                # "tmcode": " "  # {테마코드} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "tmname": "tmname`char",  # {테마명} 
                # "avgdiff": "avgdiff`float",  # {평균등락율} 
                # "tmcode": "tmcode`char"  # {테마코드} 
            }
        }
    },
    "t1532": {  ### 종목별테마
        "inblock": {
            "InBlock": {
                # "shcode": " "  # {종목코드} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "tmname": "tmname`char",  # {테마명} 
                # "avgdiff": "avgdiff`float",  # {평균등락율} 
                # "tmcode": "tmcode`char"  # {테마코드} 
            }
        }
    },
    "t1533": {  ### 특이테마
        "inblock": {
            "InBlock": {
                # "gubun": " ",  # {구분} 
                # "chgdate": 0  # {대비일자} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "bdate": "bdate`char"  # {일자} 
            },
            "OutBlock1": {
                # "tmname": "tmname`char",  # {테마명} 
                # "totcnt": "totcnt`long",  # {전체} 
                # "upcnt": "upcnt`long",  # {상승} 
                # "dncnt": "dncnt`long",  # {하락} 
                # "uprate": "uprate`float",  # {상승비율} 
                # "diff_vol": "diff_vol`float",  # {거래증가율} 
                # "avgdiff": "avgdiff`float",  # {평균등락율} 
                # "chgdiff": "chgdiff`float",  # {대비등락율} 
                # "tmcode": "tmcode`char"  # {테마코드} 
            }
        }
    },
    "t1537": {  ### 테마종목별시세조회
        "inblock": {
            "InBlock": {
                # "tmcode": " "  # {테마코드} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "upcnt": "upcnt`long",  # {상승종목수} 
                # "tmcnt": "tmcnt`long",  # {테마종목수} 
                # "uprate": "uprate`long",  # {상승종목비율} 
                # "tmname": "tmname`char"  # {테마명} 
            },
            "OutBlock1": {
                # "hname": "hname`char",  # {종목명} 
                # "price": "price`long",  # {현재가} 
                # "sign": "sign`char",  # {전일대비구분} 
                # "change": "change`long",  # {전일대비} 
                # "diff": "diff`float",  # {등락율} 
                # "volume": "volume`long",  # {누적거래량} 
                # "jniltime": "jniltime`float",  # {전일동시간} 
                # "shcode": "shcode`char",  # {종목코드} 
                # "yeprice": "yeprice`long",  # {예상체결가} 
                # "open": "open`long",  # {시가} 
                # "high": "high`long",  # {고가} 
                # "low": "low`long",  # {저가} 
                # "value": "value`long",  # {누적거래대금} 단위:백만
                # "marketcap": "marketcap`long"  # {시가총액} 단위:백만
            }
        }
    },
    "t1601": {  ### 투자자별종합
        "inblock": {
            "InBlock": {
                # "gubun1": " ",  # {주식금액수량구분1} 
                # "gubun2": " ",  # {옵션금액수량구분2} 
                # "gubun3": " ",  # {금액단위} 
                # "gubun4": " "  # {선물금액수량구분4} 
            }
        },
        "outblock": {
            "OutBlock1": {
                # "tjjcode_08": "tjjcode_08`char",  # {개인투자자코드} 
                # "ms_08": "ms_08`long",  # {개인매수} 
                # "md_08": "md_08`long",  # {개인매도} 
                # "rate_08": "rate_08`long",  # {개인증감} 
                # "svolume_08": "svolume_08`long",  # {개인순매수} 
                # "jjcode_17": "jjcode_17`char",  # {외국인투자자코드} 
                # "ms_17": "ms_17`long",  # {외국인매수} 
                # "md_17": "md_17`long",  # {외국인매도} 
                # "rate_17": "rate_17`long",  # {외국인증감} 
                # "svolume_17": "svolume_17`long",  # {외국인순매수} 
                # "jjcode_18": "jjcode_18`char",  # {기관계투자자코드} 
                # "ms_18": "ms_18`long",  # {기관계매수} 
                # "md_18": "md_18`long",  # {기관계매도} 
                # "rate_18": "rate_18`long",  # {기관계증감} 
                # "svolume_18": "svolume_18`long",  # {기관계순매수} 
                # "jjcode_01": "jjcode_01`char",  # {증권투자자코드} 
                # "ms_01": "ms_01`long",  # {증권매수} 
                # "md_01": "md_01`long",  # {증권매도} 
                # "rate_01": "rate_01`long",  # {증권증감} 
                # "svolume_01": "svolume_01`long",  # {증권순매수} 
                # "jjcode_03": "jjcode_03`char",  # {투신투자자코드} 
                # "ms_03": "ms_03`long",  # {투신매수} 
                # "md_03": "md_03`long",  # {투신매도} 
                # "rate_03": "rate_03`long",  # {투신증감} 
                # "svolume_03": "svolume_03`long",  # {투신순매수} 
                # "jjcode_04": "jjcode_04`char",  # {은행투자자코드} 
                # "ms_04": "ms_04`long",  # {은행매수} 
                # "md_04": "md_04`long",  # {은행매도} 
                # "rate_04": "rate_04`long",  # {은행증감} 
                # "svolume_04": "svolume_04`long",  # {은행순매수} 
                # "jjcode_02": "jjcode_02`char",  # {보험투자자코드} 
                # "ms_02": "ms_02`long",  # {보험매수} 
                # "md_02": "md_02`long",  # {보험매도} 
                # "rate_02": "rate_02`long",  # {보험증감} 
                # "svolume_02": "svolume_02`long",  # {보험순매수} 
                # "jjcode_05": "jjcode_05`char",  # {종금투자자코드} 
                # "ms_05": "ms_05`long",  # {종금매수} 
                # "md_05": "md_05`long",  # {종금매도} 
                # "rate_05": "rate_05`long",  # {종금증감} 
                # "svolume_05": "svolume_05`long",  # {종금순매수} 
                # "jjcode_06": "jjcode_06`char",  # {기금투자자코드} 
                # "ms_06": "ms_06`long",  # {기금매수} 
                # "md_06": "md_06`long",  # {기금매도} 
                # "rate_06": "rate_06`long",  # {기금증감} 
                # "svolume_06": "svolume_06`long",  # {기금순매수} 
                # "jjcode_11": "jjcode_11`char",  # {국가투자코드} 
                # "ms_11": "ms_11`long",  # {국가매수} 
                # "md_11": "md_11`long",  # {국가매도} 
                # "rate_11": "rate_11`long",  # {국가증감} 
                # "svolume_11": "svolume_11`long",  # {국가순매수} 
                # "jjcode_07": "jjcode_07`char",  # {기타투자자코드} 
                # "ms_07": "ms_07`long",  # {기타매수} 
                # "md_07": "md_07`long",  # {기타매도} 
                # "rate_07": "rate_07`long",  # {기타증감} 
                # "svolume_07": "svolume_07`long",  # {기타순매수} 
                # "jjcode_00": "jjcode_00`char",  # {사모펀드투자자코드} 
                # "ms_00": "ms_00`long",  # {사모펀드매수} 
                # "md_00": "md_00`long",  # {사모펀드매도} 
                # "rate_00": "rate_00`long",  # {사모펀드증감} 
                # "svolume_00": "svolume_00`long"  # {사모펀드순매수} 
            },
            "OutBlock2": {
                # "tjjcode_08": "tjjcode_08`char",  # {개인투자자코드} 
                # "ms_08": "ms_08`long",  # {개인매수} 
                # "md_08": "md_08`long",  # {개인매도} 
                # "rate_08": "rate_08`long",  # {개인증감} 
                # "svolume_08": "svolume_08`long",  # {개인순매수} 
                # "jjcode_17": "jjcode_17`char",  # {외국인투자자코드} 
                # "ms_17": "ms_17`long",  # {외국인매수} 
                # "md_17": "md_17`long",  # {외국인매도} 
                # "rate_17": "rate_17`long",  # {외국인증감} 
                # "svolume_17": "svolume_17`long",  # {외국인순매수} 
                # "jjcode_18": "jjcode_18`char",  # {기관계투자자코드} 
                # "ms_18": "ms_18`long",  # {기관계매수} 
                # "md_18": "md_18`long",  # {기관계매도} 
                # "rate_18": "rate_18`long",  # {기관계증감} 
                # "svolume_18": "svolume_18`long",  # {기관계순매수} 
                # "jjcode_01": "jjcode_01`char",  # {증권투자자코드} 
                # "ms_01": "ms_01`long",  # {증권매수} 
                # "md_01": "md_01`long",  # {증권매도} 
                # "rate_01": "rate_01`long",  # {증권증감} 
                # "svolume_01": "svolume_01`long",  # {증권순매수} 
                # "jjcode_03": "jjcode_03`char",  # {투신투자자코드} 
                # "ms_03": "ms_03`long",  # {투신매수} 
                # "md_03": "md_03`long",  # {투신매도} 
                # "rate_03": "rate_03`long",  # {투신증감} 
                # "svolume_03": "svolume_03`long",  # {투신순매수} 
                # "jjcode_04": "jjcode_04`char",  # {은행투자자코드} 
                # "ms_04": "ms_04`long",  # {은행매수} 
                # "md_04": "md_04`long",  # {은행매도} 
                # "rate_04": "rate_04`long",  # {은행증감} 
                # "svolume_04": "svolume_04`long",  # {은행순매수} 
                # "jjcode_02": "jjcode_02`char",  # {보험투자자코드} 
                # "ms_02": "ms_02`long",  # {보험매수} 
                # "md_02": "md_02`long",  # {보험매도} 
                # "rate_02": "rate_02`long",  # {보험증감} 
                # "svolume_02": "svolume_02`long",  # {보험순매수} 
                # "jjcode_05": "jjcode_05`char",  # {종금투자자코드} 
                # "ms_05": "ms_05`long",  # {종금매수} 
                # "md_05": "md_05`long",  # {종금매도} 
                # "rate_05": "rate_05`long",  # {종금증감} 
                # "svolume_05": "svolume_05`long",  # {종금순매수} 
                # "jjcode_06": "jjcode_06`char",  # {기금투자자코드} 
                # "ms_06": "ms_06`long",  # {기금매수} 
                # "md_06": "md_06`long",  # {기금매도} 
                # "rate_06": "rate_06`long",  # {기금증감} 
                # "svolume_06": "svolume_06`long",  # {기금순매수} 
                # "jjcode_11": "jjcode_11`char",  # {국가투자코드} 
                # "ms_11": "ms_11`long",  # {국가매수} 
                # "md_11": "md_11`long",  # {국가매도} 
                # "rate_11": "rate_11`long",  # {국가증감} 
                # "svolume_11": "svolume_11`long",  # {국가순매수} 
                # "jjcode_07": "jjcode_07`char",  # {기타투자자코드} 
                # "ms_07": "ms_07`long",  # {기타매수} 
                # "md_07": "md_07`long",  # {기타매도} 
                # "rate_07": "rate_07`long",  # {기타증감} 
                # "svolume_07": "svolume_07`long",  # {기타순매수} 
                # "jjcode_00": "jjcode_00`char",  # {사모펀드투자자코드} 
                # "ms_00": "ms_00`long",  # {사모펀드매수} 
                # "md_00": "md_00`long",  # {사모펀드매도} 
                # "rate_00": "rate_00`long",  # {사모펀드증감} 
                # "svolume_00": "svolume_00`long"  # {사모펀드순매수} 
            },
            "OutBlock3": {
                # "tjjcode_08": "tjjcode_08`char",  # {개인투자자코드} 
                # "ms_08": "ms_08`long",  # {개인매수} 
                # "md_08": "md_08`long",  # {개인매도} 
                # "rate_08": "rate_08`long",  # {개인증감} 
                # "svolume_08": "svolume_08`long",  # {개인순매수} 
                # "jjcode_17": "jjcode_17`char",  # {외국인투자자코드} 
                # "ms_17": "ms_17`long",  # {외국인매수} 
                # "md_17": "md_17`long",  # {외국인매도} 
                # "rate_17": "rate_17`long",  # {외국인증감} 
                # "svolume_17": "svolume_17`long",  # {외국인순매수} 
                # "jjcode_18": "jjcode_18`char",  # {기관계투자자코드} 
                # "ms_18": "ms_18`long",  # {기관계매수} 
                # "md_18": "md_18`long",  # {기관계매도} 
                # "rate_18": "rate_18`long",  # {기관계증감} 
                # "svolume_18": "svolume_18`long",  # {기관계순매수} 
                # "jjcode_01": "jjcode_01`char",  # {증권투자자코드} 
                # "ms_01": "ms_01`long",  # {증권매수} 
                # "md_01": "md_01`long",  # {증권매도} 
                # "rate_01": "rate_01`long",  # {증권증감} 
                # "svolume_01": "svolume_01`long",  # {증권순매수} 
                # "jjcode_03": "jjcode_03`char",  # {투신투자자코드} 
                # "ms_03": "ms_03`long",  # {투신매수} 
                # "md_03": "md_03`long",  # {투신매도} 
                # "rate_03": "rate_03`long",  # {투신증감} 
                # "svolume_03": "svolume_03`long",  # {투신순매수} 
                # "jjcode_04": "jjcode_04`char",  # {은행투자자코드} 
                # "ms_04": "ms_04`long",  # {은행매수} 
                # "md_04": "md_04`long",  # {은행매도} 
                # "rate_04": "rate_04`long",  # {은행증감} 
                # "svolume_04": "svolume_04`long",  # {은행순매수} 
                # "jjcode_02": "jjcode_02`char",  # {보험투자자코드} 
                # "ms_02": "ms_02`long",  # {보험매수} 
                # "md_02": "md_02`long",  # {보험매도} 
                # "rate_02": "rate_02`long",  # {보험증감} 
                # "svolume_02": "svolume_02`long",  # {보험순매수} 
                # "jjcode_05": "jjcode_05`char",  # {종금투자자코드} 
                # "ms_05": "ms_05`long",  # {종금매수} 
                # "md_05": "md_05`long",  # {종금매도} 
                # "rate_05": "rate_05`long",  # {종금증감} 
                # "svolume_05": "svolume_05`long",  # {종금순매수} 
                # "jjcode_06": "jjcode_06`char",  # {기금투자자코드} 
                # "ms_06": "ms_06`long",  # {기금매수} 
                # "md_06": "md_06`long",  # {기금매도} 
                # "rate_06": "rate_06`long",  # {기금증감} 
                # "svolume_06": "svolume_06`long",  # {기금순매수} 
                # "jjcode_11": "jjcode_11`char",  # {국가투자코드} 
                # "ms_11": "ms_11`long",  # {국가매수} 
                # "md_11": "md_11`long",  # {국가매도} 
                # "rate_11": "rate_11`long",  # {국가증감} 
                # "svolume_11": "svolume_11`long",  # {국가순매수} 
                # "jjcode_07": "jjcode_07`char",  # {기타투자자코드} 
                # "ms_07": "ms_07`long",  # {기타매수} 
                # "md_07": "md_07`long",  # {기타매도} 
                # "rate_07": "rate_07`long",  # {기타증감} 
                # "svolume_07": "svolume_07`long",  # {기타순매수} 
                # "jjcode_00": "jjcode_00`char",  # {사모펀드투자자코드} 
                # "ms_00": "ms_00`long",  # {사모펀드매수} 
                # "md_00": "md_00`long",  # {사모펀드매도} 
                # "rate_00": "rate_00`long",  # {사모펀드증감} 
                # "svolume_00": "svolume_00`long"  # {사모펀드순매수} 
            },
            "OutBlock4": {
                # "tjjcode_08": "tjjcode_08`char",  # {개인투자자코드} 
                # "ms_08": "ms_08`long",  # {개인매수} 
                # "md_08": "md_08`long",  # {개인매도} 
                # "rate_08": "rate_08`long",  # {개인증감} 
                # "svolume_08": "svolume_08`long",  # {개인순매수} 
                # "jjcode_17": "jjcode_17`char",  # {외국인투자자코드} 
                # "ms_17": "ms_17`long",  # {외국인매수} 
                # "md_17": "md_17`long",  # {외국인매도} 
                # "rate_17": "rate_17`long",  # {외국인증감} 
                # "svolume_17": "svolume_17`long",  # {외국인순매수} 
                # "jjcode_18": "jjcode_18`char",  # {기관계투자자코드} 
                # "ms_18": "ms_18`long",  # {기관계매수} 
                # "md_18": "md_18`long",  # {기관계매도} 
                # "rate_18": "rate_18`long",  # {기관계증감} 
                # "svolume_18": "svolume_18`long",  # {기관계순매수} 
                # "jjcode_01": "jjcode_01`char",  # {증권투자자코드} 
                # "ms_01": "ms_01`long",  # {증권매수} 
                # "md_01": "md_01`long",  # {증권매도} 
                # "rate_01": "rate_01`long",  # {증권증감} 
                # "svolume_01": "svolume_01`long",  # {증권순매수} 
                # "jjcode_03": "jjcode_03`char",  # {투신투자자코드} 
                # "ms_03": "ms_03`long",  # {투신매수} 
                # "md_03": "md_03`long",  # {투신매도} 
                # "rate_03": "rate_03`long",  # {투신증감} 
                # "svolume_03": "svolume_03`long",  # {투신순매수} 
                # "jjcode_04": "jjcode_04`char",  # {은행투자자코드} 
                # "ms_04": "ms_04`long",  # {은행매수} 
                # "md_04": "md_04`long",  # {은행매도} 
                # "rate_04": "rate_04`long",  # {은행증감} 
                # "svolume_04": "svolume_04`long",  # {은행순매수} 
                # "jjcode_02": "jjcode_02`char",  # {보험투자자코드} 
                # "ms_02": "ms_02`long",  # {보험매수} 
                # "md_02": "md_02`long",  # {보험매도} 
                # "rate_02": "rate_02`long",  # {보험증감} 
                # "svolume_02": "svolume_02`long",  # {보험순매수} 
                # "jjcode_05": "jjcode_05`char",  # {종금투자자코드} 
                # "ms_05": "ms_05`long",  # {종금매수} 
                # "md_05": "md_05`long",  # {종금매도} 
                # "rate_05": "rate_05`long",  # {종금증감} 
                # "svolume_05": "svolume_05`long",  # {종금순매수} 
                # "jjcode_06": "jjcode_06`char",  # {기금투자자코드} 
                # "ms_06": "ms_06`long",  # {기금매수} 
                # "md_06": "md_06`long",  # {기금매도} 
                # "rate_06": "rate_06`long",  # {기금증감} 
                # "svolume_06": "svolume_06`long",  # {기금순매수} 
                # "jjcode_11": "jjcode_11`char",  # {국가투자코드} 
                # "ms_11": "ms_11`long",  # {국가매수} 
                # "md_11": "md_11`long",  # {국가매도} 
                # "rate_11": "rate_11`long",  # {국가증감} 
                # "svolume_11": "svolume_11`long",  # {국가순매수} 
                # "jjcode_07": "jjcode_07`char",  # {기타투자자코드} 
                # "ms_07": "ms_07`long",  # {기타매수} 
                # "md_07": "md_07`long",  # {기타매도} 
                # "rate_07": "rate_07`long",  # {기타증감} 
                # "svolume_07": "svolume_07`long",  # {기타순매수} 
                # "jjcode_00": "jjcode_00`char",  # {사모펀드투자자코드} 
                # "ms_00": "ms_00`long",  # {사모펀드매수} 
                # "md_00": "md_00`long",  # {사모펀드매도} 
                # "rate_00": "rate_00`long",  # {사모펀드증감} 
                # "svolume_00": "svolume_00`long"  # {사모펀드순매수} 
            },
            "OutBlock5": {
                # "tjjcode_08": "tjjcode_08`char",  # {개인투자자코드} 
                # "ms_08": "ms_08`long",  # {개인매수} 
                # "md_08": "md_08`long",  # {개인매도} 
                # "rate_08": "rate_08`long",  # {개인증감} 
                # "svolume_08": "svolume_08`long",  # {개인순매수} 
                # "jjcode_17": "jjcode_17`char",  # {외국인투자자코드} 
                # "ms_17": "ms_17`long",  # {외국인매수} 
                # "md_17": "md_17`long",  # {외국인매도} 
                # "rate_17": "rate_17`long",  # {외국인증감} 
                # "svolume_17": "svolume_17`long",  # {외국인순매수} 
                # "jjcode_18": "jjcode_18`char",  # {기관계투자자코드} 
                # "ms_18": "ms_18`long",  # {기관계매수} 
                # "md_18": "md_18`long",  # {기관계매도} 
                # "rate_18": "rate_18`long",  # {기관계증감} 
                # "svolume_18": "svolume_18`long",  # {기관계순매수} 
                # "jjcode_01": "jjcode_01`char",  # {증권투자자코드} 
                # "ms_01": "ms_01`long",  # {증권매수} 
                # "md_01": "md_01`long",  # {증권매도} 
                # "rate_01": "rate_01`long",  # {증권증감} 
                # "svolume_01": "svolume_01`long",  # {증권순매수} 
                # "jjcode_03": "jjcode_03`char",  # {투신투자자코드} 
                # "ms_03": "ms_03`long",  # {투신매수} 
                # "md_03": "md_03`long",  # {투신매도} 
                # "rate_03": "rate_03`long",  # {투신증감} 
                # "svolume_03": "svolume_03`long",  # {투신순매수} 
                # "jjcode_04": "jjcode_04`char",  # {은행투자자코드} 
                # "ms_04": "ms_04`long",  # {은행매수} 
                # "md_04": "md_04`long",  # {은행매도} 
                # "rate_04": "rate_04`long",  # {은행증감} 
                # "svolume_04": "svolume_04`long",  # {은행순매수} 
                # "jjcode_02": "jjcode_02`char",  # {보험투자자코드} 
                # "ms_02": "ms_02`long",  # {보험매수} 
                # "md_02": "md_02`long",  # {보험매도} 
                # "rate_02": "rate_02`long",  # {보험증감} 
                # "svolume_02": "svolume_02`long",  # {보험순매수} 
                # "jjcode_05": "jjcode_05`char",  # {종금투자자코드} 
                # "ms_05": "ms_05`long",  # {종금매수} 
                # "md_05": "md_05`long",  # {종금매도} 
                # "rate_05": "rate_05`long",  # {종금증감} 
                # "svolume_05": "svolume_05`long",  # {종금순매수} 
                # "jjcode_06": "jjcode_06`char",  # {기금투자자코드} 
                # "ms_06": "ms_06`long",  # {기금매수} 
                # "md_06": "md_06`long",  # {기금매도} 
                # "rate_06": "rate_06`long",  # {기금증감} 
                # "svolume_06": "svolume_06`long",  # {기금순매수} 
                # "jjcode_11": "jjcode_11`char",  # {국가투자코드} 
                # "ms_11": "ms_11`long",  # {국가매수} 
                # "md_11": "md_11`long",  # {국가매도} 
                # "rate_11": "rate_11`long",  # {국가증감} 
                # "svolume_11": "svolume_11`long",  # {국가순매수} 
                # "jjcode_07": "jjcode_07`char",  # {기타투자자코드} 
                # "ms_07": "ms_07`long",  # {기타매수} 
                # "md_07": "md_07`long",  # {기타매도} 
                # "rate_07": "rate_07`long",  # {기타증감} 
                # "svolume_07": "svolume_07`long",  # {기타순매수} 
                # "jjcode_00": "jjcode_00`char",  # {사모펀드투자자코드} 
                # "ms_00": "ms_00`long",  # {사모펀드매수} 
                # "md_00": "md_00`long",  # {사모펀드매도} 
                # "rate_00": "rate_00`long",  # {사모펀드증감} 
                # "svolume_00": "svolume_00`long"  # {사모펀드순매수} 
            },
            "OutBlock6": {
                # "tjjcode_08": "tjjcode_08`char",  # {개인투자자코드} 
                # "ms_08": "ms_08`long",  # {개인매수} 
                # "md_08": "md_08`long",  # {개인매도} 
                # "rate_08": "rate_08`long",  # {개인증감} 
                # "svolume_08": "svolume_08`long",  # {개인순매수} 
                # "jjcode_17": "jjcode_17`char",  # {외국인투자자코드} 
                # "ms_17": "ms_17`long",  # {외국인매수} 
                # "md_17": "md_17`long",  # {외국인매도} 
                # "rate_17": "rate_17`long",  # {외국인증감} 
                # "svolume_17": "svolume_17`long",  # {외국인순매수} 
                # "jjcode_18": "jjcode_18`char",  # {기관계투자자코드} 
                # "ms_18": "ms_18`long",  # {기관계매수} 
                # "md_18": "md_18`long",  # {기관계매도} 
                # "rate_18": "rate_18`long",  # {기관계증감} 
                # "svolume_18": "svolume_18`long",  # {기관계순매수} 
                # "jjcode_01": "jjcode_01`char",  # {증권투자자코드} 
                # "ms_01": "ms_01`long",  # {증권매수} 
                # "md_01": "md_01`long",  # {증권매도} 
                # "rate_01": "rate_01`long",  # {증권증감} 
                # "svolume_01": "svolume_01`long",  # {증권순매수} 
                # "jjcode_03": "jjcode_03`char",  # {투신투자자코드} 
                # "ms_03": "ms_03`long",  # {투신매수} 
                # "md_03": "md_03`long",  # {투신매도} 
                # "rate_03": "rate_03`long",  # {투신증감} 
                # "svolume_03": "svolume_03`long",  # {투신순매수} 
                # "jjcode_04": "jjcode_04`char",  # {은행투자자코드} 
                # "ms_04": "ms_04`long",  # {은행매수} 
                # "md_04": "md_04`long",  # {은행매도} 
                # "rate_04": "rate_04`long",  # {은행증감} 
                # "svolume_04": "svolume_04`long",  # {은행순매수} 
                # "jjcode_02": "jjcode_02`char",  # {보험투자자코드} 
                # "ms_02": "ms_02`long",  # {보험매수} 
                # "md_02": "md_02`long",  # {보험매도} 
                # "rate_02": "rate_02`long",  # {보험증감} 
                # "svolume_02": "svolume_02`long",  # {보험순매수} 
                # "jjcode_05": "jjcode_05`char",  # {종금투자자코드} 
                # "ms_05": "ms_05`long",  # {종금매수} 
                # "md_05": "md_05`long",  # {종금매도} 
                # "rate_05": "rate_05`long",  # {종금증감} 
                # "svolume_05": "svolume_05`long",  # {종금순매수} 
                # "jjcode_06": "jjcode_06`char",  # {기금투자자코드} 
                # "ms_06": "ms_06`long",  # {기금매수} 
                # "md_06": "md_06`long",  # {기금매도} 
                # "rate_06": "rate_06`long",  # {기금증감} 
                # "svolume_06": "svolume_06`long",  # {기금순매수} 
                # "jjcode_11": "jjcode_11`char",  # {국가투자코드} 
                # "ms_11": "ms_11`long",  # {국가매수} 
                # "md_11": "md_11`long",  # {국가매도} 
                # "rate_11": "rate_11`long",  # {국가증감} 
                # "svolume_11": "svolume_11`long",  # {국가순매수} 
                # "jjcode_07": "jjcode_07`char",  # {기타투자자코드} 
                # "ms_07": "ms_07`long",  # {기타매수} 
                # "md_07": "md_07`long",  # {기타매도} 
                # "rate_07": "rate_07`long",  # {기타증감} 
                # "svolume_07": "svolume_07`long",  # {기타순매수} 
                # "jjcode_00": "jjcode_00`char",  # {사모펀드투자자코드} 
                # "ms_00": "ms_00`long",  # {사모펀드매수} 
                # "md_00": "md_00`long",  # {사모펀드매도} 
                # "rate_00": "rate_00`long",  # {사모펀드증감} 
                # "svolume_00": "svolume_00`long"  # {사모펀드순매수} 
            }
        }
    },
    "t1602": {  ### 시간대별투자자매매추이
        "inblock": {
            "InBlock": {
                # "market": " ",  # {시장구분} 
                # "upcode": " ",  # {업종코드} 
                # "gubun1": " ",  # {수량구분} 
                # "gubun2": " ",  # {전일분구분} 
                # "cts_time": " ",  # {CTSTIME} 
                # "cts_idx": 0,  # {CTSIDX} 
                # "cnt": 0,  # {조회건수} 
                # "gubun3": " "  # {직전대비구분} C:직전대비
            }
        },
        "outblock": {
            "OutBlock": {
                # "cts_time": "cts_time`char",  # {CTSTIME} 
                # "tjjcode_08": "tjjcode_08`char",  # {개인투자자코드} 
                # "ms_08": "ms_08`long",  # {개인매수} 
                # "md_08": "md_08`long",  # {개인매도} 
                # "rate_08": "rate_08`long",  # {개인증감} 
                # "svolume_08": "svolume_08`long",  # {개인순매수} 
                # "jjcode_17": "jjcode_17`char",  # {외국인투자자코드} 
                # "ms_17": "ms_17`long",  # {외국인매수} 
                # "md_17": "md_17`long",  # {외국인매도} 
                # "rate_17": "rate_17`long",  # {외국인증감} 
                # "svolume_17": "svolume_17`long",  # {외국인순매수} 
                # "jjcode_18": "jjcode_18`char",  # {기관계투자자코드} 
                # "ms_18": "ms_18`long",  # {기관계매수} 
                # "md_18": "md_18`long",  # {기관계매도} 
                # "rate_18": "rate_18`long",  # {기관계증감} 
                # "svolume_18": "svolume_18`long",  # {기관계순매수} 
                # "jjcode_01": "jjcode_01`char",  # {증권투자자코드} 
                # "ms_01": "ms_01`long",  # {증권매수} 
                # "md_01": "md_01`long",  # {증권매도} 
                # "rate_01": "rate_01`long",  # {증권증감} 
                # "svolume_01": "svolume_01`long",  # {증권순매수} 
                # "jjcode_03": "jjcode_03`char",  # {투신투자자코드} 
                # "ms_03": "ms_03`long",  # {투신매수} 
                # "md_03": "md_03`long",  # {투신매도} 
                # "rate_03": "rate_03`long",  # {투신증감} 
                # "svolume_03": "svolume_03`long",  # {투신순매수} 
                # "jjcode_04": "jjcode_04`char",  # {은행투자자코드} 
                # "ms_04": "ms_04`long",  # {은행매수} 
                # "md_04": "md_04`long",  # {은행매도} 
                # "rate_04": "rate_04`long",  # {은행증감} 
                # "svolume_04": "svolume_04`long",  # {은행순매수} 
                # "jjcode_02": "jjcode_02`char",  # {보험투자자코드} 
                # "ms_02": "ms_02`long",  # {보험매수} 
                # "md_02": "md_02`long",  # {보험매도} 
                # "rate_02": "rate_02`long",  # {보험증감} 
                # "svolume_02": "svolume_02`long",  # {보험순매수} 
                # "jjcode_05": "jjcode_05`char",  # {종금투자자코드} 
                # "ms_05": "ms_05`long",  # {종금매수} 
                # "md_05": "md_05`long",  # {종금매도} 
                # "rate_05": "rate_05`long",  # {종금증감} 
                # "svolume_05": "svolume_05`long",  # {종금순매수} 
                # "jjcode_06": "jjcode_06`char",  # {기금투자자코드} 
                # "ms_06": "ms_06`long",  # {기금매수} 
                # "md_06": "md_06`long",  # {기금매도} 
                # "rate_06": "rate_06`long",  # {기금증감} 
                # "svolume_06": "svolume_06`long",  # {기금순매수} 
                # "jjcode_07": "jjcode_07`char",  # {기타투자자코드} 
                # "ms_07": "ms_07`long",  # {기타매수} 
                # "md_07": "md_07`long",  # {기타매도} 
                # "rate_07": "rate_07`long",  # {기타증감} 
                # "svolume_07": "svolume_07`long",  # {기타순매수} 
                # "jjcode_11": "jjcode_11`char",  # {국가투자자코드} 
                # "ms_11": "ms_11`long",  # {국가매수} 
                # "md_11": "md_11`long",  # {국가매도} 
                # "rate_11": "rate_11`long",  # {국가증감} 
                # "svolume_11": "svolume_11`long",  # {국가순매수} 
                # "jjcode_00": "jjcode_00`char",  # {사모펀드코드} 
                # "ms_00": "ms_00`long",  # {사모펀드매수} 
                # "md_00": "md_00`long",  # {사모펀드매도} 
                # "rate_00": "rate_00`long",  # {사모펀드증감} 
                # "svolume_00": "svolume_00`long"  # {사모펀드순매수} 
            },
            "OutBlock1": {
                # "time": "time`char",  # {시간} 
                # "sv_08": "sv_08`long",  # {개인순매수} 
                # "sv_17": "sv_17`long",  # {외국인순매수} 
                # "sv_18": "sv_18`long",  # {기관계순매수} 
                # "sv_01": "sv_01`long",  # {증권순매수} 
                # "sv_03": "sv_03`long",  # {투신순매수} 
                # "sv_04": "sv_04`long",  # {은행순매수} 
                # "sv_02": "sv_02`long",  # {보험순매수} 
                # "sv_05": "sv_05`long",  # {종금순매수} 
                # "sv_06": "sv_06`long",  # {기금순매수} 
                # "sv_07": "sv_07`long",  # {기타순매수} 
                # "sv_11": "sv_11`long",  # {국가순매수} 
                # "sv_00": "sv_00`long"  # {사모펀드순매수} 
            }
        }
    },
    "t1603": {  ### 시간대별투자자매매추이상세
        "inblock": {
            "InBlock": {
                # "market": " ",  # {시장구분} 
                # "gubun1": " ",  # {투자자구분} 
                # "gubun2": " ",  # {전일분구분} 
                # "cts_time": " ",  # {CTSTIME} 
                # "cts_idx": 0,  # {CTSIDX} 
                # "cnt": 0,  # {조회건수} 
                # "upcode": " "  # {업종코드} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "cts_idx": "cts_idx`long",  # {CTSIDX} 
                # "cts_time": "cts_time`char"  # {CTSTIME} 
            },
            "OutBlock1": {
                # "time": "time`char",  # {시간} 
                # "tjjcode": "tjjcode`char",  # {투자자구분} 
                # "msvolume": "msvolume`long",  # {매수수량} 
                # "mdvolume": "mdvolume`long",  # {매도수량} 
                # "msvalue": "msvalue`long",  # {매수금액} 
                # "mdvalue": "mdvalue`long",  # {매도금액} 
                # "svolume": "svolume`long",  # {순매수수량} 
                # "svalue": "svalue`long"  # {순매수금액} 
            }
        }
    },
    "t1615": {  ### 투자자매매종합1
        "inblock": {
            "InBlock": {
                # "gubun1": " ",  # {주식구분} 
                # "gubun2": " "  # {옵션구분} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "dwvolume": "dwvolume`long",  # {위탁매도수량} 
                # "dwvalue": "dwvalue`long",  # {위탁매도금액} 
                # "djvolume": "djvolume`long",  # {자기매도수량} 
                # "djvalue": "djvalue`long",  # {자기매도금액} 
                # "sum_volume": "sum_volume`long",  # {합계수량} 
                # "sum_value": "sum_value`long"  # {합계금액} 
            },
            "OutBlock1": {
                # "hname": "hname`char",  # {시장명} 
                # "sv_08": "sv_08`long",  # {개인} 
                # "sv_17": "sv_17`long",  # {외국인} 
                # "sv_18": "sv_18`long",  # {기관계} 
                # "sv_07": "sv_07`long"  # {증권} 
            }
        }
    },
    "t1617": {  ### 투자자매매종합2
        "inblock": {
            "InBlock": {
                # "gubun1": " ",  # {시장구분} 1:코스피2:코스닥3:선물4:콜옵션5:풋옵션6:주식선물
                # "gubun2": " ",  # {수량금액구분} 1:수량2:금액
                # "gubun3": " ",  # {일자구분} 1:시간대별2:일별
                # "cts_date": " ",  # {CTSDATE(연속키값-일자)} 
                # "cts_time": " "  # {CTSTIME(연속키값-시간)} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "cts_date": "cts_date`char",  # {CTSDATE} 
                # "cts_time": "cts_time`char",  # {CTSTIME} 
                # "ms_08": "ms_08`long",  # {개인매수} 
                # "md_08": "md_08`long",  # {개인매도} 
                # "sv_08": "sv_08`long",  # {개인순매수} 
                # "ms_17": "ms_17`long",  # {외국인매수} 
                # "md_17": "md_17`long",  # {외국인매도} 
                # "sv_17": "sv_17`long",  # {외국인순매수} 
                # "ms_18": "ms_18`long",  # {기관계매수} 
                # "md_18": "md_18`long",  # {기관계매도} 
                # "sv_18": "sv_18`long",  # {기관계순매수} 
                # "ms_01": "ms_01`long",  # {증권매수} 
                # "md_01": "md_01`long",  # {증권매도} 
                # "sv_01": "sv_01`long"  # {증권순매수} 
            },
            "OutBlock1": {
                # "date": "date`char",  # {날짜} 
                # "time": "time`char",  # {시간} 
                # "sv_08": "sv_08`long",  # {개인} 
                # "sv_17": "sv_17`long",  # {외국인} 
                # "sv_18": "sv_18`long",  # {기관계} 
                # "sv_01": "sv_01`long"  # {증권} 
            }
        }
    },
    "t1621": {  ### 업종별분별투자자매매동향(챠트용)
        "inblock": {
            "InBlock": {
                # "upcode": " ",  # {업종코드} 
                # "nmin": 0,  # {N분} 
                # "cnt": 0,  # {조회건수} 
                # "bgubun": " "  # {전일분} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "indcode": "indcode`char",  # {개인투자자코드} 
                # "forcode": "forcode`char",  # {외국인투자자코드} 
                # "syscode": "syscode`char",  # {기관계투자자코드} 
                # "stocode": "stocode`char",  # {증권투자자코드} 
                # "invcode": "invcode`char",  # {투신투자자코드} 
                # "bancode": "bancode`char",  # {은행투자자코드} 
                # "inscode": "inscode`char",  # {보험투자자코드} 
                # "fincode": "fincode`char",  # {종금투자자코드} 
                # "moncode": "moncode`char",  # {기금투자자코드} 
                # "etccode": "etccode`char",  # {기타투자자코드} 
                # "natcode": "natcode`char",  # {국가투자자코드} 
                # "pefcode": "pefcode`char",  # {사모펀드투자자코드} 
                # "jisucd": "jisucd`char",  # {기준지수코드} 
                # "jisunm": "jisunm`char"  # {기준지수명} 
            },
            "OutBlock1": {
                # "date": "date`char",  # {일자} 
                # "time": "time`char",  # {시간} 
                # "datetime": "datetime`char",  # {일자시간} 
                # "indmsvol": "indmsvol`long",  # {개인순매수거래량} 
                # "indmsamt": "indmsamt`double",  # {개인순매수거래대금} 
                # "formsvol": "formsvol`long",  # {외국인순매수거래량} 
                # "formsamt": "formsamt`double",  # {외국인순매수거래대금} 
                # "sysmsvol": "sysmsvol`long",  # {기관계순매수거래량} 
                # "sysmsamt": "sysmsamt`double",  # {기관계순매수거래대금} 
                # "stomsvol": "stomsvol`long",  # {증권순매수거래량} 
                # "stomsamt": "stomsamt`double",  # {증권순매수거래대금} 
                # "invmsvol": "invmsvol`long",  # {투신순매수거래량} 
                # "invmsamt": "invmsamt`double",  # {투신순매수거래대금} 
                # "banmsvol": "banmsvol`long",  # {은행순매수거래량} 
                # "banmsamt": "banmsamt`double",  # {은행순매수거래대금} 
                # "insmsvol": "insmsvol`long",  # {보험순매수거래량} 
                # "insmsamt": "insmsamt`double",  # {보험순매수거래대금} 
                # "finmsvol": "finmsvol`long",  # {종금순매수거래량} 
                # "finmsamt": "finmsamt`double",  # {종금순매수거래대금} 
                # "monmsvol": "monmsvol`long",  # {기금순매수거래량} 
                # "monmsamt": "monmsamt`double",  # {기금순매수거래대금} 
                # "etcmsvol": "etcmsvol`long",  # {기타순매수거래량} 
                # "etcmsamt": "etcmsamt`double",  # {기타순매수거래대금} 
                # "natmsvol": "natmsvol`long",  # {국가순매수거래량} 
                # "natmsamt": "natmsamt`double",  # {국가순매수거래대금} 
                # "pefmsvol": "pefmsvol`long",  # {사모펀드순매수거래량} 
                # "pefmsamt": "pefmsamt`double",  # {사모펀드순매수거래대금} 
                # "upclose": "upclose`float",  # {기준지수} 
                # "upcvolume": "upcvolume`long",  # {기준체결거래량} 
                # "upvolume": "upvolume`double",  # {기준누적거래량} 
                # "upvalue": "upvalue`double"  # {기준거래대금} 
            }
        }
    },
    "t1631": {  ### 프로그램매매종합조회
        "inblock": {
            "InBlock": {
                # "gubun": " ",  # {구분} 
                # "dgubun": " ",  # {일자구분} 
                # "sdate": " ",  # {시작일자} 
                # "edate": " "  # {종료일자} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "cdhrem": "cdhrem`long",  # {매도차익미체결잔량} 
                # "bdhrem": "bdhrem`long",  # {매도비차익미체결잔량} 
                # "tcdrem": "tcdrem`long",  # {매도차익주문수량} 
                # "tbdrem": "tbdrem`long",  # {매도비차익주문수량} 
                # "cshrem": "cshrem`long",  # {매수차익미체결잔량} 
                # "bshrem": "bshrem`long",  # {매수비차익미체결잔량} 
                # "tcsrem": "tcsrem`long",  # {매수차익주문수량} 
                # "tbsrem": "tbsrem`long"  # {매수비차익주문수량} 
            },
            "OutBlock1": {
                # "offervolume": "offervolume`long",  # {매도수량} 
                # "offervalue": "offervalue`long",  # {매도금액} 
                # "bidvolume": "bidvolume`long",  # {매수수량} 
                # "bidvalue": "bidvalue`long",  # {매수금액} 
                # "volume": "volume`long",  # {순매수수량} 
                # "value": "value`long"  # {순매수금액} 
            }
        }
    },
    "t1632": {  ### 시간대별프로그램매매추이
        "inblock": {
            "InBlock": {
                # "gubun": " ",  # {구분} 
                # "gubun1": " ",  # {금액수량구분} 
                # "gubun2": " ",  # {직전대비증감} 
                # "gubun3": " ",  # {전일구분} 
                # "date": " ",  # {일자} 
                # "time": " "  # {시간} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "date": "date`char",  # {날짜CTS} 
                # "time": "time`char",  # {시간CTS} 
                # "idx": "idx`long"  # {IDX} 
            },
            "OutBlock1": {
                # "time": "time`char",  # {시간} 
                # "k200jisu": "k200jisu`float",  # {KP200} 
                # "sign": "sign`char",  # {대비구분} 
                # "change": "change`float",  # {대비} 
                # "k200basis": "k200basis`float",  # {BASIS} 
                # "tot3": "tot3`long",  # {전체순매수} 
                # "tot1": "tot1`long",  # {전체매수} 
                # "tot2": "tot2`long",  # {전체매도} 
                # "cha3": "cha3`long",  # {차익순매수} 
                # "cha1": "cha1`long",  # {차익매수} 
                # "cha2": "cha2`long",  # {차익매도} 
                # "bcha3": "bcha3`long",  # {비차익순매수} 
                # "bcha1": "bcha1`long",  # {비차익매수} 
                # "bcha2": "bcha2`long"  # {비차익매도} 
            }
        }
    },
    "t1633": {  ### 기간별프로그램매매추이
        "inblock": {
            "InBlock": {
                # "gubun": " ",  # {시장구분} 
                # "gubun1": " ",  # {금액수량구분} 
                # "gubun2": " ",  # {수치누적구분} 
                # "gubun3": " ",  # {일주월구분} 
                # "fdate": " ",  # {from일자} 
                # "tdate": " ",  # {to일자} 
                # "gubun4": " ",  # {직전대비증감구분} 
                # "date": " "  # {날짜} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "date": "date`char",  # {날짜} 
                # "idx": "idx`long"  # {IDX} 
            },
            "OutBlock1": {
                # "date": "date`char",  # {일자} 
                # "jisu": "jisu`float",  # {KP200} 
                # "sign": "sign`char",  # {대비구분} 
                # "change": "change`float",  # {대비} 
                # "tot3": "tot3`long",  # {전체순매수} 
                # "tot1": "tot1`long",  # {전체매수} 
                # "tot2": "tot2`long",  # {전체매도} 
                # "cha3": "cha3`long",  # {차익순매수} 
                # "cha1": "cha1`long",  # {차익매수} 
                # "cha2": "cha2`long",  # {차익매도} 
                # "bcha3": "bcha3`long",  # {비차익순매수} 
                # "bcha1": "bcha1`long",  # {비차익매수} 
                # "bcha2": "bcha2`long",  # {비차익매도} 
                # "volume": "volume`long"  # {거래량} 
            }
        }
    },
    "t1636": {  ### 종목별프로그램매매동향
        "inblock": {
            "InBlock": {
                # "gubun": " ",  # {구분} 
                # "gubun1": " ",  # {금액수량구분} 
                # "gubun2": " ",  # {정렬기준} 
                # "shcode": " ",  # {종목코드} 
                # "cts_idx": 0  # {IDXCTS} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "cts_idx": "cts_idx`long"  # {IDXCTS} 
            },
            "OutBlock1": {
                # "rank": "rank`long",  # {순위} 
                # "hname": "hname`char",  # {종목명} 
                # "price": "price`long",  # {현재가} 
                # "sign": "sign`char",  # {대비구분} 
                # "change": "change`long",  # {대비} 
                # "diff": "diff`float",  # {등락율} 
                # "volume": "volume`long",  # {거래량} 
                # "svalue": "svalue`long",  # {순매수금액} 
                # "offervalue": "offervalue`long",  # {매도금액} 
                # "stksvalue": "stksvalue`long",  # {매수금액} 
                # "svolume": "svolume`long",  # {순매수수량} 
                # "offervolume": "offervolume`long",  # {매도수량} 
                # "stksvolume": "stksvolume`long",  # {매수수량} 
                # "sgta": "sgta`long",  # {시가총액} 
                # "rate": "rate`float",  # {비중} 
                # "shcode": "shcode`char"  # {종목코드} 
            }
        }
    },
    "t1637": {  ### 종목별프로그램매매추이
        "inblock": {
            "InBlock": {
                # "gubun1": " ",  # {수량금액구분} 0:수량1:금액
                # "gubun2": " ",  # {시간일별구분} 0:시간1:일자
                # "shcode": " ",  # {종목코드} 
                # "date": " ",  # {일자} 
                # "time": " ",  # {시간} 
                # "cts_idx": 0  # {IDXCTS} 9999:차트
            }
        },
        "outblock": {
            "OutBlock": {
                # "cts_idx": "cts_idx`long"  # {IDXCTS} 
            },
            "OutBlock1": {
                # "date": "date`char",  # {일자} 
                # "time": "time`char",  # {시간} 
                # "price": "price`long",  # {현재가} 
                # "sign": "sign`char",  # {대비구분} 
                # "change": "change`long",  # {대비} 
                # "diff": "diff`float",  # {등락율} 
                # "volume": "volume`long",  # {거래량} 
                # "svalue": "svalue`long",  # {순매수금액} 
                # "offervalue": "offervalue`long",  # {매도금액} 
                # "stksvalue": "stksvalue`long",  # {매수금액} 
                # "svolume": "svolume`long",  # {순매수수량} 
                # "offervolume": "offervolume`long",  # {매도수량} 
                # "stksvolume": "stksvolume`long",  # {매수수량} 
                # "shcode": "shcode`char"  # {종목코드} 
            }
        }
    },
    "t1638": {  ### 종목별잔량/사전공시
        "inblock": {
            "InBlock": {
                # "gubun1": " ",  # {구분} 
                # "shcode": " ",  # {종목코드} 
                # "gubun2": " "  # {정렬} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "rank": "rank`long",  # {순위} 
                # "hname": "hname`char",  # {한글명} 
                # "price": "price`long",  # {현재가} 
                # "sign": "sign`char",  # {전일대비구분} 
                # "change": "change`long",  # {전일대비} 
                # "diff": "diff`float",  # {등락율} 
                # "sigatotrt": "sigatotrt`float",  # {시총비중} 
                # "obuyvol": "obuyvol`long",  # {순매수잔량} 
                # "buyrem": "buyrem`long",  # {매수잔량} 
                # "psgvolume": "psgvolume`long",  # {매수공시수량} 
                # "sellrem": "sellrem`long",  # {매도잔량} 
                # "pdgvolume": "pdgvolume`long",  # {매도공시수량} 
                # "sigatot": "sigatot`long",  # {시가총액} 
                # "shcode": "shcode`char"  # {종목코드} 
            }
        }
    },
    "t1640": {  ### 프로그램매매종합조회(미니)
        "inblock": {
            "InBlock": {
                # "gubun": " "  # {구분} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "offervolume": "offervolume`long",  # {매도수량} 
                # "bidvolume": "bidvolume`long",  # {매수수량} 
                # "volume": "volume`long",  # {순매수수량} 
                # "offerdiff": "offerdiff`long",  # {매도증감} 
                # "biddiff": "biddiff`long",  # {매수증감} 
                # "sundiff": "sundiff`long",  # {순매수증감} 
                # "basis": "basis`float",  # {베이시스} 
                # "offervalue": "offervalue`double",  # {매도금액} 
                # "bidvalue": "bidvalue`double",  # {매수금액} 
                # "value": "value`double",  # {순매수금액} 
                # "offervaldiff": "offervaldiff`double",  # {매도금액증감} 
                # "bidvaldiff": "bidvaldiff`double",  # {매수금액증감} 
                # "sunvaldiff": "sunvaldiff`double"  # {순매수증감} 
            }
        }
    },
    "t1662": {  ### 시간대별프로그램매매추이(차트)
        "inblock": {
            "InBlock": {
                # "gubun": " ",  # {구분} 
                # "gubun1": " ",  # {금액수량구분} 
                # "gubun3": " "  # {전일구분} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "time": "time`char",  # {시간} 
                # "k200jisu": "k200jisu`float",  # {KP200} 
                # "sign": "sign`char",  # {대비구분} 
                # "change": "change`float",  # {대비} 
                # "k200basis": "k200basis`float",  # {BASIS} 
                # "tot3": "tot3`long",  # {전체순매수} 
                # "tot1": "tot1`long",  # {전체매수} 
                # "tot2": "tot2`long",  # {전체매도} 
                # "cha3": "cha3`long",  # {차익순매수} 
                # "cha1": "cha1`long",  # {차익매수} 
                # "cha2": "cha2`long",  # {차익매도} 
                # "bcha3": "bcha3`long",  # {비차익순매수} 
                # "bcha1": "bcha1`long",  # {비차익매수} 
                # "bcha2": "bcha2`long",  # {비차익매도} 
                # "volume": "volume`long"  # {거래량} 
            }
        }
    },
    "t1664": {  ### 투자자매매종합(챠트)
        "inblock": {
            "InBlock": {
                # "mgubun": " ",  # {시장구분} 
                # "vagubun": " ",  # {금액수량구분} 
                # "bdgubun": " ",  # {시간일별구분} 
                # "cnt": 0  # {조회건수} 
            }
        },
        "outblock": {
            "OutBlock1": {
                # "dt": "dt`char",  # {일자시간} 
                # "tjj01": "tjj01`double",  # {증권순매수} 
                # "tjj02": "tjj02`double",  # {보험순매수} 
                # "tjj03": "tjj03`double",  # {투신순매수} 
                # "tjj04": "tjj04`double",  # {은행순매수} 
                # "tjj05": "tjj05`double",  # {종금순매수} 
                # "tjj06": "tjj06`double",  # {기금순매수} 
                # "tjj07": "tjj07`double",  # {기타순매수} 
                # "tjj08": "tjj08`double",  # {개인순매수} 
                # "tjj17": "tjj17`double",  # {외국인순매수} 
                # "tjj18": "tjj18`double",  # {기관순매수} 
                # "cha": "cha`double",  # {차익순매수} 
                # "bicha": "bicha`double",  # {비차익순매수} 
                # "totcha": "totcha`double",  # {종합순매수} 
                # "basis": "basis`float"  # {베이시스} 
            }
        }
    },
    "t1665": {  ### 기간별투자자매매추이(챠트)
        "inblock": {
            "InBlock": {
                # "market": " ",  # {시장구분} 1:kospi2:kp2003:kosdaq4:선물5:풋옵션6:콜옵션
                # "upcode": " ",  # {업종코드} 
                # "gubun2": " ",  # {수치구분} 1:수치2:누적
                # "gubun3": " ",  # {단위구분} 1:일2:주3:월
                # "from_date": " ",  # {시작날짜} 
                # "to_date": " "  # {종료날짜} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "mcode": "mcode`char",  # {시장코드} 
                # "mname": "mname`char"  # {시장명} 
            },
            "OutBlock1": {
                # "date": "date`char",  # {일자} 
                # "sv_08": "sv_08`long",  # {개인수량} 
                # "sv_17": "sv_17`long",  # {외인계수량(등록+미등록)} 
                # "sv_18": "sv_18`long",  # {기관계수량} 
                # "sv_01": "sv_01`long",  # {증권수량} 
                # "sv_03": "sv_03`long",  # {투신수량} 
                # "sv_04": "sv_04`long",  # {은행수량} 
                # "sv_02": "sv_02`long",  # {보험수량} 
                # "sv_05": "sv_05`long",  # {종금수량} 
                # "sv_06": "sv_06`long",  # {기금수량} 
                # "sv_07": "sv_07`long",  # {기타수량} 
                # "sv_00": "sv_00`long",  # {사모펀드수량} 
                # "sv_09": "sv_09`long",  # {등록외국인수량} 
                # "sv_10": "sv_10`long",  # {미등록외국인수량} 
                # "sv_11": "sv_11`long",  # {국가수량} 
                # "sv_99": "sv_99`long",  # {기타계수량(기타+국가)} 
                # "sa_08": "sa_08`double",  # {개인금액} 
                # "sa_17": "sa_17`double",  # {외인계금액(등록+미등록)} 
                # "sa_18": "sa_18`double",  # {기관계금액} 
                # "sa_01": "sa_01`double",  # {증권금액} 
                # "sa_03": "sa_03`double",  # {투신금액} 
                # "sa_04": "sa_04`double",  # {은행금액} 
                # "sa_02": "sa_02`double",  # {보험금액} 
                # "sa_05": "sa_05`double",  # {종금금액} 
                # "sa_06": "sa_06`double",  # {기금금액} 
                # "sa_07": "sa_07`double",  # {기타금액} 
                # "sa_00": "sa_00`double",  # {사모펀드금액} 
                # "sa_09": "sa_09`double",  # {등록외국인금액} 
                # "sa_10": "sa_10`double",  # {미등록외국인금액} 
                # "sa_11": "sa_11`double",  # {국가금액} 
                # "sa_99": "sa_99`double",  # {기타계금액(기타+국가)} 
                # "jisu": "jisu`float"  # {시장지수} 
            }
        }
    },
    "t1701": {  ### 외인기관종목별동향
        "inblock": {
            "InBlock": {
                # "shcode": " ",  # {종목코드} 
                # "gubun": " ",  # {구분} 
                # "fromdt": " ",  # {시작일자} 
                # "todt": " ",  # {종료일자} 
                # "prapp": 0,  # {PR적용} 
                # "prgubun": " ",  # {PR적용구분} 
                # "orggubun": " ",  # {기관적용} 
                # "frggubun": " "  # {외인적용} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "date": "date`char",  # {일자} 
                # "close": "close`long",  # {종가} 
                # "sign": "sign`char",  # {전일대비구분} 
                # "change": "change`long",  # {전일대비} 
                # "diff": "diff`float",  # {등락율} 
                # "volume": "volume`long",  # {누적거래량} 
                # "psnvolume": "psnvolume`long",  # {개인} 
                # "orgvolume": "orgvolume`long",  # {기관} 
                # "frgvolume": "frgvolume`long",  # {외국인} 
                # "frgvolumesum": "frgvolumesum`long",  # {외국계} 
                # "pgmvolume": "pgmvolume`long",  # {프로그램} 
                # "listing": "listing`long",  # {보유주식수} 
                # "listupdn": "listupdn`long",  # {발행증감} 
                # "sjrate": "sjrate`float"  # {소진율} 
            }
        }
    },
    "t1702": {  ### 외인기관종목별동향
        "inblock": {
            "InBlock": {
                # "shcode": " ",  # {종목코드} 
                # "todt": " ",  # {종료일자} 
                # "volvalgb": " ",  # {금액수량구분} 0:금액1:수량2:단가
                # "msmdgb": " ",  # {매수매도구분} 0:순매수1:매수2:매도
                # "cumulgb": " ",  # {누적구분} 0:일간1:누적
                # "cts_date": " ",  # {CTSDATE} 
                # "cts_idx": 0  # {CTSIDX} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "cts_idx": "cts_idx`long",  # {CTSIDX} 
                # "cts_date": "cts_date`char"  # {CTSDATE} 
            },
            "OutBlock1": {
                # "date": "date`char",  # {일자} 
                # "close": "close`long",  # {종가} 
                # "sign": "sign`char",  # {전일대비구분} 
                # "change": "change`long",  # {전일대비} 
                # "diff": "diff`float",  # {등락율} 
                # "volume": "volume`long",  # {누적거래량} 
                # "amt0000": "amt0000`long",  # {사모펀드} 
                # "amt0001": "amt0001`long",  # {증권} 
                # "amt0002": "amt0002`long",  # {보험} 
                # "amt0003": "amt0003`long",  # {투신} 
                # "amt0004": "amt0004`long",  # {은행} 
                # "amt0005": "amt0005`long",  # {종금} 
                # "amt0006": "amt0006`long",  # {기금} 
                # "amt0007": "amt0007`long",  # {기타법인} 
                # "amt0008": "amt0008`long",  # {개인} 
                # "amt0009": "amt0009`long",  # {등록외국인} 
                # "amt0010": "amt0010`long",  # {미등록외국인} 
                # "amt0011": "amt0011`long",  # {국가외} 
                # "amt0018": "amt0018`long",  # {기관} 
                # "amt0088": "amt0088`long",  # {외인계(등록+미등록)} 
                # "amt0099": "amt0099`long"  # {기타계(기타+국가)} 
            }
        }
    },
    "t1717": {  ### 외인기관종목별동향
        "inblock": {
            "InBlock": {
                # "shcode": " ",  # {종목코드} 
                # "gubun": " ",  # {구분} 0:일간순매수1:기간누적순매수
                # "fromdt": " ",  # {시작일자(일간조회일경우는space)} 
                # "todt": " "  # {종료일자} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "date": "date`char",  # {일자} 
                # "close": "close`long",  # {종가} 
                # "sign": "sign`char",  # {전일대비구분} 
                # "change": "change`long",  # {전일대비} 
                # "diff": "diff`float",  # {등락율} 
                # "volume": "volume`long",  # {누적거래량} 
                # "tjj0000_vol": "tjj0000_vol`long",  # {사모펀드(순매수량)} 
                # "tjj0001_vol": "tjj0001_vol`long",  # {증권(순매수량)} 
                # "tjj0002_vol": "tjj0002_vol`long",  # {보험(순매수량)} 
                # "tjj0003_vol": "tjj0003_vol`long",  # {투신(순매수량)} 
                # "tjj0004_vol": "tjj0004_vol`long",  # {은행(순매수량)} 
                # "tjj0005_vol": "tjj0005_vol`long",  # {종금(순매수량)} 
                # "tjj0006_vol": "tjj0006_vol`long",  # {기금(순매수량)} 
                # "tjj0007_vol": "tjj0007_vol`long",  # {기타법인(순매수량)} 
                # "tjj0008_vol": "tjj0008_vol`long",  # {개인(순매수량)} 
                # "tjj0009_vol": "tjj0009_vol`long",  # {등록외국인(순매수량)} 
                # "tjj0010_vol": "tjj0010_vol`long",  # {미등록외국인(순매수량)} 
                # "tjj0011_vol": "tjj0011_vol`long",  # {국가외(순매수량)} 
                # "tjj0018_vol": "tjj0018_vol`long",  # {기관(순매수량)} 
                # "tjj0016_vol": "tjj0016_vol`long",  # {외인계(순매수량)(등록+미등록)} 
                # "tjj0017_vol": "tjj0017_vol`long",  # {기타계(순매수량)(기타+국가)} 
                # "tjj0000_dan": "tjj0000_dan`long",  # {사모펀드(단가)} 
                # "tjj0001_dan": "tjj0001_dan`long",  # {증권(단가)} 
                # "tjj0002_dan": "tjj0002_dan`long",  # {보험(단가)} 
                # "tjj0003_dan": "tjj0003_dan`long",  # {투신(단가)} 
                # "tjj0004_dan": "tjj0004_dan`long",  # {은행(단가)} 
                # "tjj0005_dan": "tjj0005_dan`long",  # {종금(단가)} 
                # "tjj0006_dan": "tjj0006_dan`long",  # {기금(단가)} 
                # "tjj0007_dan": "tjj0007_dan`long",  # {기타법인(단가)} 
                # "tjj0008_dan": "tjj0008_dan`long",  # {개인(단가)} 
                # "tjj0009_dan": "tjj0009_dan`long",  # {등록외국인(단가)} 
                # "tjj0010_dan": "tjj0010_dan`long",  # {미등록외국인(단가)} 
                # "tjj0011_dan": "tjj0011_dan`long",  # {국가외(단가)} 
                # "tjj0018_dan": "tjj0018_dan`long",  # {기관(단가)} 
                # "tjj0016_dan": "tjj0016_dan`long",  # {외인계(단가)(등록+미등록)} 
                # "tjj0017_dan": "tjj0017_dan`long"  # {기타계(단가)(기타+국가)} 
            }
        }
    },
    "t1752": {  ### 종목별상위회원사
        "inblock": {
            "InBlock": {
                # "shcode": " ",  # {종목코드} 
                # "traddate1": " ",  # {조회날짜1} 
                # "traddate2": " ",  # {조회날짜2} 
                # "fwgubun1": " ",  # {외국계구분} 
                # "cts_idx": 0  # {CTSIDX} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "fwdvl": "fwdvl`long",  # {외국계매도} 
                # "fwsvl": "fwsvl`long",  # {외국계매수} 
                # "cts_idx": "cts_idx`long"  # {CTSIDX} 
            },
            "OutBlock1": {
                # "tradname": "tradname`char",  # {회원사} 
                # "tradmdvol": "tradmdvol`long",  # {매도수량} 
                # "tradmsvol": "tradmsvol`long",  # {매수수량} 
                # "tradmssvol": "tradmssvol`long",  # {순매수} 
                # "wintrd": "wintrd`long",  # {창구거래} 
                # "winrat": "winrat`float",  # {비중} 
                # "tradno": "tradno`char",  # {회원사코드} 
                # "wgubun": "wgubun`char",  # {외국계여부} 
                # "swinrat": "swinrat`float"  # {순비중} 
            }
        }
    },
    "t1764": {  ### 회원사리스트
        "inblock": {
            "InBlock": {
                # "shcode": " ",  # {종목코드} 
                # "gubun1": " "  # {구분1} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "rank": "rank`long",  # {순위} 
                # "tradno": "tradno`char",  # {거래원번호} 
                # "tradname": "tradname`char"  # {거래원이름} 
            }
        }
    },
    "t1771": {  ### 종목별회원사추이
        "inblock": {
            "InBlock": {
                # "shcode": " ",  # {종목코드} 
                # "tradno": " ",  # {거래원코드} 
                # "gubun1": " ",  # {구분1} 
                # "traddate1": " ",  # {거래원날짜1} 
                # "traddate2": " ",  # {거래원날짜2} 
                # "cts_idx": 0,  # {CTSIDX} 
                # "cnt": 0  # {요청건수} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "cts_idx": "cts_idx`long"  # {CTSIDX} 
            },
            "OutBlock2": {
                # "traddate": "traddate`char",  # {날짜} 
                # "tradtime": "tradtime`char",  # {시간} 
                # "price": "price`long",  # {현재가} 
                # "sign": "sign`char",  # {대비구분} 
                # "change": "change`long",  # {대비} 
                # "diff": "diff`float",  # {등락율} 
                # "volume": "volume`long",  # {거래량} 
                # "tradmdcha": "tradmdcha`long",  # {매도} 
                # "tradmscha": "tradmscha`long",  # {매수} 
                # "tradmdval": "tradmdval`long",  # {매도대금} 
                # "tradmsval": "tradmsval`long",  # {매수대금} 
                # "tradmsscha": "tradmsscha`long",  # {순매수} 
                # "tradmttvolume": "tradmttvolume`long",  # {누적순매수} 
                # "tradavg": "tradavg`long",  # {평균단가} 
                # "tradmttavg": "tradmttavg`long"  # {누적평균단가} 
            }
        }
    },
    "t1809": {  ### 신호조회
        "inblock": {
            "InBlock": {
                # "gubun": " ",  # {신호구분} 
                # "jmGb": " ",  # {종목구분} 
                # "jmcode": " ",  # {종목코드} 
                # "cts": " "  # {NEXTKEY} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "cts": "cts`char"  # {NEXTKEY} 
            },
            "OutBlock1": {
                # "date": "date`char",  # {일자} 
                # "time": "time`char",  # {시간} 
                # "signal_id": "signal_id`char",  # {신호ID} 
                # "signal_desc": "signal_desc`char",  # {신호명} 
                # "point": "point`char",  # {신호강도} 
                # "keyword": "keyword`char",  # {뉴스신호키워드} 
                # "seq": "seq`char",  # {신호별구분} 
                # "gubun": "gubun`char",  # {신호구분} 
                # "jmcode": "jmcode`char",  # {신호종목} 
                # "price": "price`long",  # {종목가격} 
                # "sign": "sign`char",  # {종목등락부호} 
                # "chgrate": "chgrate`float",  # {대비등락율} 
                # "volume": "volume`long",  # {거래량} 
                # "datetime": "datetime`char"  # {신호일시} 
            }
        }
    },
    "t1825": {  ### 종목Q클릭검색(씽큐스마트)
        "inblock": {
            "InBlock": {
                # "search_cd": " ",  # {검색코드} 
                # "gubun": " "  # {구분} 0:전체1:코스피2:코스닥
            }
        },
        "outblock": {
            "OutBlock": {
                # "JongCnt": "JongCnt`long"  # {검색종목수} 
            },
            "OutBlock1": {
                # "shcode": "shcode`char",  # {종목코드} 
                # "hname": "hname`char",  # {종목명} 
                # "sign": "sign`char",  # {전일대비구분} 
                # "signcnt": "signcnt`long",  # {연속봉수} 
                # "close": "close`long",  # {현재가} 
                # "change": "change`long",  # {전일대비} 
                # "diff": "diff`float",  # {등락율} 
                # "volume": "volume`long",  # {거래량} 
                # "volumerate": "volumerate`float"  # {거래량전일대비율} 
            }
        }
    },
    "t1826": {  ### 종목Q클릭검색리스트조회(씽큐스마트)
        "inblock": {
            "InBlock": {
                # "search_gb": " "  # {검색구분} 0:핵심검색1:지표검색2:시세동향3:투자자동향
            }
        },
        "outblock": {
            "OutBlock": {
                # "search_cd": "search_cd`char",  # {검색코드} 
                # "search_nm": "search_nm`char"  # {검색명} 
            }
        }
    },
    "t1857": {  ### e종목검색(신버전API용)
        "inblock": {
            "InBlock": {
                # "sRealFlag": " ",  # {실시간구분} 0:조회 1:실시간
                # "sSearchFlag": " ",  # {종목검색구분} F:파일 S:서버
                # "query_index": " "  # {종목검색입력값} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "result_count": "result_count`long",  # {검색종목수} 
                # "result_time": "result_time`char",  # {포착시간} 
                # "AlertNum": "AlertNum`char"  # {실시간키} 
            },
            "OutBlock1": {
                # "shcode": "shcode`char",  # {종목코드} 
                # "hname": "hname`char",  # {종목명} 
                # "price": "price`long",  # {현재가} 
                # "sign": "sign`char",  # {전일대비구분} 
                # "change": "change`long",  # {전일대비} 
                # "diff": "diff`float",  # {등락율} 
                # "volume": "volume`long",  # {거래량} 
                # "JobFlag": "JobFlag`char"  # {종목상태} N:진입 R:재진입 O:이탈
            }
        }
    },
    "t1866": {  ### 서버저장조건리스트조회(API)
        "inblock": {
            "InBlock": {
                # "user_id": " ",  # {로그인ID} 
                # "gb": " ",  # {조회구분} 
                # "group_name": " ",  # {그룹명} 
                # "cont": " ",  # {연속여부} 
                # "contkey": " "  # {연속키} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "result_count": "result_count`long",  # {저장조건수} 
                # "cont": "cont`char",  # {연속여부} 
                # "contkey": "contkey`char"  # {연속키} 
            },
            "OutBlock1": {
                # "query_index": "query_index`char",  # {서버저장인덱스} 
                # "group_name": "group_name`char",  # {그룹명} 
                # "query_name": "query_name`char"  # {조건저장명} 
            }
        }
    },
    "t1921": {  ### 신용거래동향
        "inblock": {
            "InBlock": {
                # "shcode": " ",  # {종목코드} 
                # "gubun": " ",  # {융자대주구분} 
                # "date": " ",  # {날짜} 
                # "idx": 0  # {IDX} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "cnt": "cnt`long",  # {CNT} 
                # "date": "date`char",  # {날짜} 
                # "idx": "idx`long"  # {IDX} 
            },
            "OutBlock1": {
                # "mmdate": "mmdate`char",  # {날짜} 
                # "close": "close`long",  # {종가} 
                # "sign": "sign`char",  # {전일대비구분} 
                # "jchange": "jchange`long",  # {전일대비} 
                # "diff": "diff`float",  # {등락율} 
                # "nvolume": "nvolume`long",  # {신규} 
                # "svolume": "svolume`long",  # {상환} 
                # "jvolume": "jvolume`long",  # {잔고} 
                # "price": "price`long",  # {금액} 
                # "change": "change`long",  # {대비} 
                # "gyrate": "gyrate`float",  # {공여율} 
                # "jkrate": "jkrate`float",  # {잔고율} 
                # "shcode": "shcode`char"  # {종목코드} 
            }
        }
    },
    "t1926": {  ### 종목별신용정보
        "inblock": {
            "InBlock": {
                # "shcode": " "  # {종목코드} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "ynvolume": "ynvolume`long",  # {융자신규수량} 
                # "ysvolume": "ysvolume`long",  # {융자상환수량} 
                # "yjvolume": "yjvolume`long",  # {융자잔고수량} 
                # "yvchange": "yvchange`long",  # {융자수량대비} 
                # "ygrate": "ygrate`float",  # {융자공여율} 
                # "yjrate": "yjrate`float",  # {융자잔고율} 
                # "ynprice": "ynprice`long",  # {융자신규금액} 
                # "ysprice": "ysprice`long",  # {융자상환금액} 
                # "yjprice": "yjprice`long",  # {융자잔고금액} 
                # "yachange": "yachange`long",  # {융자금액대비} 
                # "dnvolume": "dnvolume`long",  # {대주신규수량} 
                # "dsvolume": "dsvolume`long",  # {대주상환수량} 
                # "djvolume": "djvolume`long",  # {대주잔고수량} 
                # "dvchange": "dvchange`long",  # {대주수량대비} 
                # "dgrate": "dgrate`float",  # {대주공여율} 
                # "djrate": "djrate`float",  # {대주잔고율} 
                # "dnprice": "dnprice`long",  # {대주신규금액} 
                # "dsprice": "dsprice`long",  # {대주상환금액} 
                # "djprice": "djprice`long",  # {대주잔고금액} 
                # "dachange": "dachange`long",  # {대주금액대비} 
                # "mmdate": "mmdate`char",  # {결제일} 
                # "close": "close`long",  # {결제일종가} 
                # "volume": "volume`long",  # {결제일거래량} 
                # "value": "value`long",  # {결제일거래대금} 
                # "pr5days": "pr5days`float",  # {주가5일증가율} 
                # "pr20days": "pr20days`float",  # {주가20일증가율} 
                # "yj5days": "yj5days`float",  # {융자5일증가율} 
                # "yj20days": "yj20days`float",  # {융자20일증가율} 
                # "dj5days": "dj5days`float",  # {대주5일증가율} 
                # "dj20days": "dj20days`float"  # {대주20일증가율} 
            }
        }
    },
    "t1927": {  ### 공매도일별추이
        "inblock": {
            "InBlock": {
                # "shcode": " ",  # {종목코드} 
                # "date": " ",  # {일자} 
                # "sdate": " ",  # {시작일자} 
                # "edate": " "  # {종료일자} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "date": "date`char"  # {일자CTS} 
            },
            "OutBlock1": {
                # "date": "date`char",  # {일자} 
                # "price": "price`long",  # {현재가} 
                # "sign": "sign`char",  # {전일대비구분} 
                # "change": "change`long",  # {전일대비} 
                # "diff": "diff`float",  # {등락율} 
                # "volume": "volume`long",  # {거래량} 
                # "value": "value`long",  # {거래대금} 
                # "gm_vo": "gm_vo`long",  # {공매도수량} 
                # "gm_va": "gm_va`long",  # {공매도대금} 
                # "gm_per": "gm_per`float",  # {공매도거래비중} 
                # "gm_avg": "gm_avg`long",  # {평균공매도단가} 
                # "gm_vo_sum": "gm_vo_sum`long",  # {누적공매도수량} 
                # "gm_vo1": "gm_vo1`long",  # {업틱룰적용공매도수량} 
                # "gm_va1": "gm_va1`long",  # {업틱룰적용공매도대금} 
                # "gm_vo2": "gm_vo2`long",  # {업틱룰예외공매도수량} 
                # "gm_va2": "gm_va2`long"  # {업틱룰예외공매도대금} 
            }
        }
    },
    "t1941": {  ### 종목별대차거래일간추이
        "inblock": {
            "InBlock": {
                # "shcode": " ",  # {종목코드} 
                # "sdate": " ",  # {시작일자} 
                # "edate": " "  # {종료일자} 
            }
        },
        "outblock": {
            "OutBlock1": {
                # "date": "date`char",  # {일자} 
                # "price": "price`long",  # {종가} 
                # "sign": "sign`char",  # {대비구분} 
                # "change": "change`long",  # {대비} 
                # "diff": "diff`float",  # {등락율} 
                # "volume": "volume`long",  # {거래량} 
                # "upvolume": "upvolume`long",  # {당일체결} 
                # "dnvolume": "dnvolume`long",  # {당일상환} 
                # "tovolume": "tovolume`long",  # {당일잔고} 
                # "tovalue": "tovalue`long",  # {잔고금액} 
                # "shcode": "shcode`char",  # {종목코드} 
                # "tovoldif": "tovoldif`long"  # {대차증감} 
            }
        }
    },
    "t1959": {  ### LP대상종목정보조회
        "inblock": {
            "InBlock": {
                # "shcode": " "  # {종목코드} 
            }
        },
        "outblock": {
            "OutBlock1": {
                # "shcode": "shcode`char",  # {종목코드} 
                # "hname": "hname`char",  # {종목명} 
                # "price": "price`char",  # {현재가} 
                # "sign": "sign`char",  # {부호} 
                # "change": "change`char",  # {대비} 
                # "rate": "rate`float",  # {등락율} 
                # "volume": "volume`char",  # {누적거래량} 
                # "value": "value`char",  # {누적거래대금} 
                # "lp_gb": "lp_gb`char",  # {LP주문가능여부} 
                # "lp_mem_nm1": "lp_mem_nm1`char",  # {LP회원사명1} 
                # "lp_mem_nm2": "lp_mem_nm2`char",  # {LP회원사명2} 
                # "lp_mem_nm3": "lp_mem_nm3`char",  # {LP회원사명3} 
                # "lp_mem_nm4": "lp_mem_nm4`char",  # {LP회원사명4} 
                # "lp_mem_nm5": "lp_mem_nm5`char",  # {LP회원사명5} 
                # "lp_min_qty": "lp_min_qty`char",  # {LP최소호가수량} 
                # "lp_st_date": "lp_st_date`char",  # {LP시작일} 
                # "lp_end_date": "lp_end_date`char",  # {LP종료일} 
                # "lp_spread": "lp_spread`float"  # {LP스프레드} 
            }
        }
    },
    "t1981": {  ### 기초자산리스트조회
        "inblock": {
            "InBlock": {
                # "mkt_gb": " "  # {시장구분} 0:전체1:코스피2:코스닥
            }
        },
        "outblock": {
            "OutBlock": {
                # "ksp_cnt": "ksp_cnt`char",  # {코스피종목건수} 
                # "ksd_cnt": "ksd_cnt`char"  # {코스닥종목건수} 
            },
            "OutBlock1": {
                # "shcode": "shcode`char",  # {단축코드} 
                # "expcode": "expcode`char",  # {표준코드} 
                # "hname": "hname`char",  # {종목명} 
                # "price": "price`char",  # {현재가} 
                # "sign": "sign`char",  # {부호} 
                # "change": "change`char",  # {대비} 
                # "rate": "rate`float",  # {등락율} 
                # "volume": "volume`char",  # {누적거래량(주)} 
                # "value": "value`char",  # {누적거래대금(백만)} 
                # "mkt_gb": "mkt_gb`char"  # {시장구분} 
            }
        }
    },
    "t3102": {  ### 뉴스본문
        "inblock": {
            "InBlock": {
                # "sNewsno": " "  # {뉴스번호} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "sJongcode": "sJongcode`char"  # {뉴스종목} 
            },
            "OutBlock1": {
                # "sBody": "sBody`char"  # {뉴스본문} 
            },
            "OutBlock2": {
                # "sTitle": "sTitle`char"  # {뉴스타이틀} 
            }
        }
    },
    "t3202": {  ### 종목별증시일정
        "inblock": {
            "InBlock": {
                # "shcode": " ",  # {종목코드} 
                # "date": " "  # {조회일자} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "recdt": "recdt`char",  # {기준일} 
                # "tableid": "tableid`char",  # {테이블아이디} 
                # "upgu": "upgu`char",  # {업무구분} 
                # "custno": "custno`char",  # {발행체번호} 
                # "custnm": "custnm`char",  # {발행회사명} 
                # "shcode": "shcode`char",  # {종목코드} 
                # "upunm": "upunm`char"  # {업무명} 
            }
        }
    },
    "t3320": {  ### FNG_요약
        "inblock": {
            "InBlock": {
                # "gicode": " "  # {종목코드} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "upgubunnm": "upgubunnm`char",  # {업종구분명} 
                # "sijangcd": "sijangcd`char",  # {시장구분} 
                # "marketnm": "marketnm`char",  # {시장구분명} 
                # "company": "company`char",  # {한글기업명} 
                # "baddress": "baddress`char",  # {본사주소} 
                # "btelno": "btelno`char",  # {본사전화번호} 
                # "gsyyyy": "gsyyyy`char",  # {최근결산년도} 
                # "gsmm": "gsmm`char",  # {결산월} 
                # "gsym": "gsym`char",  # {최근결산년월} 
                # "lstprice": "lstprice`long",  # {주당액면가} 
                # "gstock": "gstock`long",  # {주식수} 
                # "homeurl": "homeurl`char",  # {Homepage} 
                # "grdnm": "grdnm`char",  # {그룹명} 
                # "foreignratio": "foreignratio`float",  # {외국인} 
                # "irtel": "irtel`char",  # {주담전화} 
                # "capital": "capital`float",  # {자본금} 
                # "sigavalue": "sigavalue`float",  # {시가총액} 
                # "cashsis": "cashsis`float",  # {배당금} 
                # "cashrate": "cashrate`float",  # {배당수익율} 
                # "price": "price`long",  # {현재가} 
                # "jnilclose": "jnilclose`long",  # {전일종가} 
                # "notice1": "notice1`char",  # {위험고지구분1_정리매매} 
                # "notice2": "notice2`char",  # {위험고지구분2_투자위험} 
                # "notice3": "notice3`char"  # {위험고지구분3_단기과열} 
            },
            "OutBlock1": {
                # "gicode": "gicode`char",  # {기업코드} 
                # "gsym": "gsym`char",  # {결산년월} 
                # "gsgb": "gsgb`char",  # {결산구분} 
                # "per": "per`float",  # {PER} 
                # "eps": "eps`float",  # {EPS} 
                # "pbr": "pbr`float",  # {PBR} 
                # "roa": "roa`float",  # {ROA} 
                # "roe": "roe`float",  # {ROE} 
                # "ebitda": "ebitda`float",  # {EBITDA} 
                # "evebitda": "evebitda`float",  # {EVEBITDA} 
                # "par": "par`float",  # {액면가} 
                # "sps": "sps`float",  # {SPS} 
                # "cps": "cps`float",  # {CPS} 
                # "bps": "bps`float",  # {BPS} 
                # "t_per": "t_per`float",  # {T.PER} 
                # "t_eps": "t_eps`float",  # {T.EPS} 
                # "peg": "peg`float",  # {PEG} 
                # "t_peg": "t_peg`float",  # {T.PEG} 
                # "t_gsym": "t_gsym`char"  # {최근분기년도} 
            }
        }
    },
    "t3341": {  ### 재무순위종합
        "inblock": {
            "InBlock": {
                # "gubun": " ",  # {시장구분} 
                # "gubun1": " ",  # {순위구분} 1:매출액증가율2:영업이익증가율3:세전계속이익증가율4:부채비율5:유보율6:EPS7:BPS8:ROE9:PERa:PBRb:PEG
                # "gubun2": " ",  # {대비구분} 
                # "idx": 0  # {IDX} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "cnt": "cnt`long",  # {CNT} 
                # "idx": "idx`long"  # {IDX} 
            },
            "OutBlock1": {
                # "rank": "rank`long",  # {순위} 
                # "hname": "hname`char",  # {기업명} 
                # "salesgrowth": "salesgrowth`long",  # {매출액증가율} 
                # "operatingincomegrowt": "operatingincomegrowt`long",  # {영업이익증가율} 
                # "ordinaryincomegrowth": "ordinaryincomegrowth`long",  # {경상이익증가율} 
                # "liabilitytoequity": "liabilitytoequity`long",  # {부채비율} 
                # "enterpriseratio": "enterpriseratio`long",  # {유보율} 
                # "eps": "eps`long",  # {EPS} 
                # "bps": "bps`long",  # {BPS} 
                # "roe": "roe`long",  # {ROE} 
                # "shcode": "shcode`char",  # {종목코드} 
                # "per": "per`float",  # {PER} 
                # "pbr": "pbr`float",  # {PBR} 
                # "peg": "peg`float"  # {PEG} 
            }
        }
    },
    "t3401": {  ### 투자의견
        "inblock": {
            "InBlock": {
                # "shcode": " ",  # {종목코드} 
                # "gubun1": " ",  # {구분} 
                # "tradno": " ",  # {회원사코드} 
                # "cts_date": " "  # {IDXDATE} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "cts_date": "cts_date`char",  # {IDXDATE} 
                # "price": "price`long",  # {현재가} 
                # "sign": "sign`char",  # {대비속성} 
                # "change": "change`long",  # {대비} 
                # "diff": "diff`float",  # {등락율} 
                # "volume": "volume`long",  # {거래량} 
                # "value": "value`long"  # {거래대금} 
            },
            "OutBlock1": {
                # "shcode": "shcode`char",  # {종목코드} 
                # "tradno": "tradno`char",  # {회원사코드} 
                # "date": "date`char",  # {의견일자} 
                # "tradname": "tradname`char",  # {회원사명} 
                # "bopn": "bopn`char",  # {투자의견변경후} 
                # "nopn": "nopn`char",  # {투자의견변경전} 
                # "boga": "boga`long",  # {목표가변경전} 
                # "noga": "noga`long",  # {목표가변경후} 
                # "close": "close`long"  # {의견일종가} 
            }
        }
    },
    "t4201": {  ### 주식챠트(종합)
        "inblock": {
            "InBlock": {
                # "shcode": " ",  # {단축코드} 
                # "gubun": " ",  # {주기구분} 0:틱1:분2:일3:주4:월
                # "ncnt": 0,  # {틱개수} 
                # "qrycnt": 0,  # {건수(500건이하)} 
                # "tdgb": " ",  # {당일구분} 0:전체1:당일만
                # "sdate": " ",  # {시작일자} 
                # "edate": " ",  # {종료일자} 
                # "cts_date": " ",  # {연속일자} 
                # "cts_time": " ",  # {연속시간} 
                # "cts_daygb": " "  # {연속당일구분} 0:연속전체1:연속당일만2:연속전일만
            }
        },
        "outblock": {
            "OutBlock": {
                # "shcode": "shcode`char",  # {단축코드} 
                # "jisiga": "jisiga`long",  # {전일시가} 
                # "jihigh": "jihigh`long",  # {전일고가} 
                # "jilow": "jilow`long",  # {전일저가} 
                # "jiclose": "jiclose`long",  # {전일종가} 
                # "jivolume": "jivolume`long",  # {전일거래량} 
                # "disiga": "disiga`long",  # {당일시가} 
                # "dihigh": "dihigh`long",  # {당일고가} 
                # "dilow": "dilow`long",  # {당일저가} 
                # "diclose": "diclose`long",  # {당일종가} 
                # "highend": "highend`long",  # {상한가} 
                # "lowend": "lowend`long",  # {하한가} 
                # "cts_date": "cts_date`char",  # {연속일자} 
                # "cts_time": "cts_time`char",  # {연속시간} 
                # "cts_daygb": "cts_daygb`char"  # {연속당일구분} 
            },
            "OutBlock1": {
                # "date": "date`char",  # {날짜} 
                # "time": "time`char",  # {시간} 
                # "open": "open`long",  # {시가} 
                # "high": "high`long",  # {고가} 
                # "low": "low`long",  # {저가} 
                # "close": "close`long",  # {종가} 
                # "jdiff_vol": "jdiff_vol`long",  # {거래량} 
                # "value": "value`long",  # {거래대금} 
                # "jongchk": "jongchk`long",  # {수정구분} 
                # "rate": "rate`double",  # {수정비율} 
                # "pricechk": "pricechk`long",  # {수정주가반영항목} 
                # "ratevalue": "ratevalue`long"  # {수정비율반영거래대금} 
            }
        }
    },
    "t4203": {  ### 업종챠트(종합)
        "inblock": {
            "InBlock": {
                # "shcode": " ",  # {단축코드} 
                # "gubun": " ",  # {주기구분} 0:틱1:분2:일3:주4:월
                # "ncnt": 0,  # {틱개수} 
                # "qrycnt": 0,  # {건수} 
                # "tdgb": " ",  # {당일구분} 0:전체1:당일만
                # "sdate": " ",  # {시작일자} 
                # "edate": " ",  # {종료일자} 
                # "cts_date": " ",  # {연속일자} 
                # "cts_time": " ",  # {연속시간} 
                # "cts_daygb": " "  # {연속당일구분} 0:연속전체1:연속당일만2:연속전일만
            }
        },
        "outblock": {
            "OutBlock": {
                # "shcode": "shcode`char",  # {단축코드} 
                # "jisiga": "jisiga`float",  # {전일시가} 
                # "jihigh": "jihigh`float",  # {전일고가} 
                # "jilow": "jilow`float",  # {전일저가} 
                # "jiclose": "jiclose`float",  # {전일종가} 
                # "jivolume": "jivolume`long",  # {전일거래량} 
                # "disiga": "disiga`float",  # {당일시가} 
                # "dihigh": "dihigh`float",  # {당일고가} 
                # "dilow": "dilow`float",  # {당일저가} 
                # "diclose": "diclose`float",  # {당일종가} 
                # "disvalue": "disvalue`long",  # {당일거래대금} 
                # "cts_date": "cts_date`char",  # {연속일자} 
                # "cts_time": "cts_time`char",  # {연속시간} 
                # "cts_daygb": "cts_daygb`char"  # {연속당일구분} 
            },
            "OutBlock1": {
                # "date": "date`char",  # {날짜} 
                # "time": "time`char",  # {시간} 
                # "open": "open`float",  # {시가} 
                # "high": "high`float",  # {고가} 
                # "low": "low`float",  # {저가} 
                # "close": "close`float",  # {종가} 
                # "jdiff_vol": "jdiff_vol`long",  # {거래량} 
                # "value": "value`long"  # {거래대금} 
            }
        }
    },
    "t8407": {  ### API용주식멀티현재가조회
        "inblock": {
            "InBlock": {
                # "nrec": 0,  # {건수} 
                # "shcode": " "  # {종목코드} 
            }
        },
        "outblock": {
            "OutBlock1": {
                # "shcode": "shcode`char",  # {종목코드} 
                # "hname": "hname`char",  # {종목명} 
                # "price": "price`long",  # {현재가} 
                # "sign": "sign`char",  # {전일대비구분} 
                # "change": "change`long",  # {전일대비} 
                # "diff": "diff`float",  # {등락율} 
                # "volume": "volume`long",  # {누적거래량} 
                # "offerho": "offerho`long",  # {매도호가} 
                # "bidho": "bidho`long",  # {매수호가} 
                # "cvolume": "cvolume`long",  # {체결수량} 
                # "chdegree": "chdegree`float",  # {체결강도} 
                # "open": "open`long",  # {시가} 
                # "high": "high`long",  # {고가} 
                # "low": "low`long",  # {저가} 
                # "value": "value`long",  # {거래대금(백만)} 
                # "offerrem": "offerrem`long",  # {우선매도잔량} 
                # "bidrem": "bidrem`long",  # {우선매수잔량} 
                # "totofferrem": "totofferrem`long",  # {총매도잔량} 
                # "totbidrem": "totbidrem`long",  # {총매수잔량} 
                # "jnilclose": "jnilclose`long",  # {전일종가} 
                # "uplmtprice": "uplmtprice`long",  # {상한가} 
                # "dnlmtprice": "dnlmtprice`long"  # {하한가} 
            }
        }
    },
    "t8411": {  ### 주식챠트(틱/n틱)
        "inblock": {
            "InBlock": {
                # "shcode": " ",  # {단축코드} 
                # "ncnt": 0,  # {단위(n틱)} 
                # "qrycnt": 0,  # {요청건수} 최대-압축:2000비압축:500
                # "nday": " ",  # {조회영업일수} 0:미사용1>=사용
                # "sdate": " ",  # {시작일자} 
                # "stime": " ",  # {시작시간(현재미사용)} 
                # "edate": " ",  # {종료일자} 
                # "etime": " ",  # {종료시간(현재미사용)} 
                # "cts_date": " ",  # {연속일자} 
                # "cts_time": " ",  # {연속시간} 
                # "comp_yn": " "  # {압축여부} Y:압축N:비압축
            }
        },
        "outblock": {
            "OutBlock": {
                # "shcode": "shcode`char",  # {단축코드} 
                # "jisiga": "jisiga`long",  # {전일시가} 
                # "jihigh": "jihigh`long",  # {전일고가} 
                # "jilow": "jilow`long",  # {전일저가} 
                # "jiclose": "jiclose`long",  # {전일종가} 
                # "jivolume": "jivolume`long",  # {전일거래량} 
                # "disiga": "disiga`long",  # {당일시가} 
                # "dihigh": "dihigh`long",  # {당일고가} 
                # "dilow": "dilow`long",  # {당일저가} 
                # "diclose": "diclose`long",  # {당일종가} 
                # "highend": "highend`long",  # {상한가} 
                # "lowend": "lowend`long",  # {하한가} 
                # "cts_date": "cts_date`char",  # {연속일자} 
                # "cts_time": "cts_time`char",  # {연속시간} 
                # "s_time": "s_time`char",  # {장시작시간(HHMMSS)} 
                # "e_time": "e_time`char",  # {장종료시간(HHMMSS)} 
                # "dshmin": "dshmin`char",  # {동시호가처리시간} MM:분
                # "rec_count": "rec_count`long"  # {레코드카운트} 
            },
            "OutBlock1": {
                # "date": "date`char",  # {날짜} 
                # "time": "time`char",  # {시간} 
                # "open": "open`long",  # {시가} 
                # "high": "high`long",  # {고가} 
                # "low": "low`long",  # {저가} 
                # "close": "close`long",  # {종가} 
                # "jdiff_vol": "jdiff_vol`long",  # {거래량} 
                # "jongchk": "jongchk`long",  # {수정구분} 
                # "rate": "rate`double",  # {수정비율} 
                # "pricechk": "pricechk`long"  # {수정주가반영항목} 
            }
        }
    },
    "t8412": {  ### 주식챠트(N분)
        "inblock": {
            "InBlock": {
                # "shcode": " ",  # {단축코드} 
                # "ncnt": 0,  # {단위(n분)} 
                # "qrycnt": 0,  # {요청건수} 최대-압축:2000비압축:500
                # "nday": " ",  # {조회영업일수} 0:미사용1>=사용
                # "sdate": " ",  # {시작일자} 
                # "stime": " ",  # {시작시간(현재미사용)} 
                # "edate": " ",  # {종료일자} 
                # "etime": " ",  # {종료시간(현재미사용)} 
                # "cts_date": " ",  # {연속일자} 
                # "cts_time": " ",  # {연속시간} 
                # "comp_yn": " "  # {압축여부} Y:압축N:비압축
            }
        },
        "outblock": {
            "OutBlock": {
                # "shcode": "shcode`char",  # {단축코드} 
                # "jisiga": "jisiga`long",  # {전일시가} 
                # "jihigh": "jihigh`long",  # {전일고가} 
                # "jilow": "jilow`long",  # {전일저가} 
                # "jiclose": "jiclose`long",  # {전일종가} 
                # "jivolume": "jivolume`long",  # {전일거래량} 
                # "disiga": "disiga`long",  # {당일시가} 
                # "dihigh": "dihigh`long",  # {당일고가} 
                # "dilow": "dilow`long",  # {당일저가} 
                # "diclose": "diclose`long",  # {당일종가} 
                # "highend": "highend`long",  # {상한가} 
                # "lowend": "lowend`long",  # {하한가} 
                # "cts_date": "cts_date`char",  # {연속일자} 
                # "cts_time": "cts_time`char",  # {연속시간} 
                # "s_time": "s_time`char",  # {장시작시간(HHMMSS)} 
                # "e_time": "e_time`char",  # {장종료시간(HHMMSS)} 
                # "dshmin": "dshmin`char",  # {동시호가처리시간} MM:분
                # "rec_count": "rec_count`long"  # {레코드카운트} 
            },
            "OutBlock1": {
                # "date": "date`char",  # {날짜} 
                # "time": "time`char",  # {시간} 
                # "open": "open`long",  # {시가} 
                # "high": "high`long",  # {고가} 
                # "low": "low`long",  # {저가} 
                # "close": "close`long",  # {종가} 
                # "jdiff_vol": "jdiff_vol`long",  # {거래량} 
                # "value": "value`long",  # {거래대금} 
                # "jongchk": "jongchk`long",  # {수정구분} 
                # "rate": "rate`double",  # {수정비율} 
                # "sign": "sign`char"  # {종가등락구분} 1:상한2:상승3:보합4:하한5:하락
            }
        }
    },
    "t8413": {  ### 주식챠트(일주월)
        "inblock": {
            "InBlock": {
                # "shcode": " ",  # {단축코드} 
                # "gubun": " ",  # {주기구분} 2:일3:주4:월
                # "qrycnt": 0,  # {요청건수} 최대-압축:2000비압축:500
                # "sdate": " ",  # {시작일자} 
                # "edate": " ",  # {종료일자} 
                # "cts_date": " ",  # {연속일자} 
                # "comp_yn": " "  # {압축여부} Y:압축N:비압축
            }
        },
        "outblock": {
            "OutBlock": {
                # "shcode": "shcode`char",  # {단축코드} 
                # "jisiga": "jisiga`long",  # {전일시가} 
                # "jihigh": "jihigh`long",  # {전일고가} 
                # "jilow": "jilow`long",  # {전일저가} 
                # "jiclose": "jiclose`long",  # {전일종가} 
                # "jivolume": "jivolume`long",  # {전일거래량} 
                # "disiga": "disiga`long",  # {당일시가} 
                # "dihigh": "dihigh`long",  # {당일고가} 
                # "dilow": "dilow`long",  # {당일저가} 
                # "diclose": "diclose`long",  # {당일종가} 
                # "highend": "highend`long",  # {상한가} 
                # "lowend": "lowend`long",  # {하한가} 
                # "cts_date": "cts_date`char",  # {연속일자} 
                # "s_time": "s_time`char",  # {장시작시간(HHMMSS)} 
                # "e_time": "e_time`char",  # {장종료시간(HHMMSS)} 
                # "dshmin": "dshmin`char",  # {동시호가처리시간} MM:분
                # "rec_count": "rec_count`long"  # {레코드카운트} 
            },
            "OutBlock1": {
                # "date": "date`char",  # {날짜} 
                # "open": "open`long",  # {시가} 
                # "high": "high`long",  # {고가} 
                # "low": "low`long",  # {저가} 
                # "close": "close`long",  # {종가} 
                # "jdiff_vol": "jdiff_vol`long",  # {거래량} 
                # "value": "value`long",  # {거래대금} 
                # "jongchk": "jongchk`long",  # {수정구분} 
                # "rate": "rate`double",  # {수정비율} 
                # "pricechk": "pricechk`long",  # {수정주가반영항목} 
                # "ratevalue": "ratevalue`long",  # {수정비율반영거래대금} 
                # "sign": "sign`char"  # {종가등락구분} 1:상한2:상승3:보합4:하한5:하락주식일만사용
            }
        }
    },
    "t8417": {  ### 업종차트(틱/n틱)
        "inblock": {
            "InBlock": {
                # "shcode": " ",  # {단축코드} 
                # "ncnt": 0,  # {단위(n틱)} 
                # "qrycnt": 0,  # {요청건수} 최대-압축:2000비압축:500
                # "nday": " ",  # {조회영업일수} 0:미사용1>=사용
                # "sdate": " ",  # {시작일자} 
                # "stime": " ",  # {시작시간(현재미사용)} 
                # "edate": " ",  # {종료일자} 
                # "etime": " ",  # {종료시간(현재미사용)} 
                # "cts_date": " ",  # {연속일자} 
                # "cts_time": " ",  # {연속시간} 
                # "comp_yn": " "  # {압축여부} Y:압축N:비압축
            }
        },
        "outblock": {
            "OutBlock": {
                # "shcode": "shcode`char",  # {단축코드} 
                # "jisiga": "jisiga`float",  # {전일시가} 
                # "jihigh": "jihigh`float",  # {전일고가} 
                # "jilow": "jilow`float",  # {전일저가} 
                # "jiclose": "jiclose`float",  # {전일종가} 
                # "jivolume": "jivolume`long",  # {전일거래량} 
                # "disiga": "disiga`float",  # {당일시가} 
                # "dihigh": "dihigh`float",  # {당일고가} 
                # "dilow": "dilow`float",  # {당일저가} 
                # "diclose": "diclose`float",  # {당일종가} 
                # "cts_date": "cts_date`char",  # {연속일자} 
                # "cts_time": "cts_time`char",  # {연속시간} 
                # "s_time": "s_time`char",  # {장시작시간(HHMMSS)} 
                # "e_time": "e_time`char",  # {장종료시간(HHMMSS)} 
                # "dshmin": "dshmin`char",  # {동시호가처리시간} MM:분
                # "rec_count": "rec_count`long"  # {레코드카운트} 
            },
            "OutBlock1": {
                # "date": "date`char",  # {날짜} 
                # "time": "time`char",  # {시간} 
                # "open": "open`float",  # {시가} 
                # "high": "high`float",  # {고가} 
                # "low": "low`float",  # {저가} 
                # "close": "close`float",  # {종가} 
                # "jdiff_vol": "jdiff_vol`long"  # {거래량} 
            }
        }
    },
    "t8418": {  ### 업종챠트(N분)
        "inblock": {
            "InBlock": {
                # "shcode": " ",  # {단축코드} 
                # "ncnt": 0,  # {단위(n분)} 
                # "qrycnt": 0,  # {요청건수} 최대-압축:2000비압축:500
                # "nday": " ",  # {조회영업일수} 0:미사용1>=사용
                # "sdate": " ",  # {시작일자} 
                # "stime": " ",  # {시작시간(현재미사용)} 
                # "edate": " ",  # {종료일자} 
                # "etime": " ",  # {종료시간(현재미사용)} 
                # "cts_date": " ",  # {연속일자} 
                # "cts_time": " ",  # {연속시간} 
                # "comp_yn": " "  # {압축여부} Y:압축N:비압축
            }
        },
        "outblock": {
            "OutBlock": {
                # "shcode": "shcode`char",  # {단축코드} 
                # "jisiga": "jisiga`float",  # {전일시가} 
                # "jihigh": "jihigh`float",  # {전일고가} 
                # "jilow": "jilow`float",  # {전일저가} 
                # "jiclose": "jiclose`float",  # {전일종가} 
                # "jivolume": "jivolume`long",  # {전일거래량} 
                # "disiga": "disiga`float",  # {당일시가} 
                # "dihigh": "dihigh`float",  # {당일고가} 
                # "dilow": "dilow`float",  # {당일저가} 
                # "diclose": "diclose`float",  # {당일종가} 
                # "disvalue": "disvalue`long",  # {당일거래대금} 
                # "cts_date": "cts_date`char",  # {연속일자} 
                # "cts_time": "cts_time`char",  # {연속시간} 
                # "s_time": "s_time`char",  # {업종시작시간(HHMMSS)} 
                # "e_time": "e_time`char",  # {업종종료시간(HHMMSS)} 
                # "dshmin": "dshmin`char",  # {동시호가처리시간} MM:분
                # "rec_count": "rec_count`long"  # {레코드카운트} 
            },
            "OutBlock1": {
                # "date": "date`char",  # {날짜} 
                # "time": "time`char",  # {시간} 
                # "open": "open`float",  # {시가} 
                # "high": "high`float",  # {고가} 
                # "low": "low`float",  # {저가} 
                # "close": "close`float",  # {종가} 
                # "jdiff_vol": "jdiff_vol`long",  # {거래량} 
                # "value": "value`long"  # {거래대금} 
            }
        }
    },
    "t8419": {  ### 업종챠트(일주월)
        "inblock": {
            "InBlock": {
                # "shcode": " ",  # {단축코드} 
                # "gubun": " ",  # {주기구분} 2:일3:주4:월
                # "qrycnt": 0,  # {요청건수} 최대-압축:2000비압축:500
                # "sdate": " ",  # {시작일자} 
                # "edate": " ",  # {종료일자} 
                # "cts_date": " ",  # {연속일자} 
                # "comp_yn": " "  # {압축여부} Y:압축N:비압축
            }
        },
        "outblock": {
            "OutBlock": {
                # "shcode": "shcode`char",  # {단축코드} 
                # "jisiga": "jisiga`float",  # {전일시가} 
                # "jihigh": "jihigh`float",  # {전일고가} 
                # "jilow": "jilow`float",  # {전일저가} 
                # "jiclose": "jiclose`float",  # {전일종가} 
                # "jivolume": "jivolume`long",  # {전일거래량} 
                # "disiga": "disiga`float",  # {당일시가} 
                # "dihigh": "dihigh`float",  # {당일고가} 
                # "dilow": "dilow`float",  # {당일저가} 
                # "diclose": "diclose`float",  # {당일종가} 
                # "disvalue": "disvalue`long",  # {당일거래대금} 
                # "cts_date": "cts_date`char",  # {연속일자} 
                # "s_time": "s_time`char",  # {업종시작시간} 
                # "e_time": "e_time`char",  # {업종종료시간} 
                # "dshmin": "dshmin`char",  # {동시호가처리시간} MM:분
                # "rec_count": "rec_count`long"  # {레코드카운트} 
            },
            "OutBlock1": {
                # "date": "date`char",  # {날짜} 
                # "open": "open`float",  # {시가} 
                # "high": "high`float",  # {고가} 
                # "low": "low`float",  # {저가} 
                # "close": "close`float",  # {종가} 
                # "jdiff_vol": "jdiff_vol`long",  # {거래량} 
                # "value": "value`long"  # {거래대금} 
            }
        }
    },
    "t8424": {  ### 전체업종
        "inblock": {
            "InBlock": {
                # "gubun1": " "  # {구분1} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "hname": "hname`char",  # {업종명} 
                # "upcode": "upcode`char"  # {업종코드} 
            }
        }
    },
    "t8425": {  ### 전체테마
        "inblock": {
            "InBlock": {
                # "dummy": " "  # {Dummy} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "tmname": "tmname`char",  # {테마명} 
                # "tmcode": "tmcode`char"  # {테마코드} 
            }
        }
    },
    "t8427": {  ### 과거데이터시간대별조회
        "inblock": {
            "InBlock": {
                # "fo_gbn": " ",  # {선물옵션구분} 
                # "yyyy": " ",  # {조회년도} 
                # "mm": " ",  # {조회월} 
                # "cp_gbn": " ",  # {옵션콜풋구분} 
                # "actprice": 0.0,  # {옵션행사가} 
                # "focode": " ",  # {선물옵션코드} 
                # "dt_gbn": " ",  # {일분구분} 
                # "min_term": " ",  # {분간격} 
                # "date": " ",  # {날짜} 
                # "time": " "  # {시간} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "focode": "focode`char",  # {선물옵션코드} 
                # "date": "date`char",  # {날짜} 
                # "time": "time`char"  # {시간} 
            },
            "OutBlock1": {
                # "date": "date`char",  # {날짜} 
                # "time": "time`char",  # {시간} 
                # "open": "open`float",  # {시가} 
                # "high": "high`float",  # {고가} 
                # "low": "low`float",  # {저가} 
                # "close": "close`float",  # {종가} 
                # "sign": "sign`char",  # {전일대비구분} 
                # "change": "change`float",  # {전일대비} 
                # "diff": "diff`float",  # {등락율} 
                # "volume": "volume`long",  # {거래량} 
                # "diff_vol": "diff_vol`float",  # {거래증가율} 
                # "openyak": "openyak`long",  # {미결수량} 
                # "openyakupdn": "openyakupdn`long",  # {미결증감} 
                # "value": "value`float"  # {거래대금} 
            }
        }
    },
    "t8428": {  ### 증시주변자금추이
        "inblock": {
            "InBlock": {
                # "fdate": " ",  # {from일자} 
                # "tdate": " ",  # {to일자} 
                # "gubun": " ",  # {구분} 
                # "key_date": " ",  # {날짜} 
                # "upcode": " ",  # {업종코드} 
                # "cnt": 0  # {조회건수} 
            }
        },
        "outblock": {
            "OutBlock": {
                # "date": "date`char",  # {날짜CTS} 
                # "idx": "idx`long"  # {IDX} 
            },
            "OutBlock1": {
                # "date": "date`char",  # {일자} 
                # "jisu": "jisu`float",  # {지수} 
                # "sign": "sign`char",  # {대비구분} 
                # "change": "change`float",  # {대비} 
                # "diff": "diff`float",  # {등락율} 
                # "volume": "volume`long",  # {거래량} 
                # "custmoney": "custmoney`long",  # {고객예탁금_억원} 
                # "yecha": "yecha`long",  # {예탁증감_억원} 
                # "vol": "vol`float",  # {회전율} 
                # "outmoney": "outmoney`long",  # {미수금_억원} 
                # "trjango": "trjango`long",  # {신용잔고_억원} 
                # "futymoney": "futymoney`long",  # {선물예수금_억원} 
                # "stkmoney": "stkmoney`long",  # {주식형_억원} 
                # "mstkmoney": "mstkmoney`long",  # {혼합형_억원(주식)} 
                # "mbndmoney": "mbndmoney`long",  # {혼합형_억원(채권)} 
                # "bndmoney": "bndmoney`long",  # {채권형_억원} 
                # "bndsmoney": "bndsmoney`long",  # {필러(구.단기채권)} 
                # "mmfmoney": "mmfmoney`long"  # {MMF_억원(주식)} 
            }
        }
    },
    "t8430": {  ### 주식종목조회
        "inblock": {
            "InBlock": {
                # "gubun": " "  # {구분} 0:전체1:코스피2:코스닥
            }
        },
        "outblock": {
            "OutBlock": {
                # "hname": "hname`char",  # {종목명} 
                # "shcode": "shcode`char",  # {단축코드} 
                # "expcode": "expcode`char",  # {확장코드} 
                # "etfgubun": "etfgubun`char",  # {ETF구분} 1:ETF
                # "uplmtprice": "uplmtprice`long",  # {상한가} 
                # "dnlmtprice": "dnlmtprice`long",  # {하한가} 
                # "jnilclose": "jnilclose`long",  # {전일가} 
                # "memedan": "memedan`char",  # {주문수량단위} 
                # "recprice": "recprice`long",  # {기준가} 
                # "gubun": "gubun`char"  # {구분} 1:코스피2:코스닥
            }
        }
    },
    "t8436": {  ### 주식종목조회 API용
        "inblock": {
            "InBlock": {
                # "gubun": " "  # {구분} 0:전체1:코스피2:코스닥
            }
        },
        "outblock": {
            "OutBlock": {
                # "hname": "hname`char",  # {종목명} 
                # "shcode": "shcode`char",  # {단축코드} 
                # "expcode": "expcode`char",  # {확장코드} 
                # "etfgubun": "etfgubun`char",  # {ETF구분} 1:ETF2:ETN
                # "uplmtprice": "uplmtprice`long",  # {상한가} 
                # "dnlmtprice": "dnlmtprice`long",  # {하한가} 
                # "jnilclose": "jnilclose`long",  # {전일가} 
                # "memedan": "memedan`char",  # {주문수량단위} 
                # "recprice": "recprice`long",  # {기준가} 
                # "gubun": "gubun`char",  # {구분} 1:코스피2:코스닥
                # "bu12gubun": "bu12gubun`char",  # {증권그룹} 
                # "spac_gubun": "spac_gubun`char",  # {기업인수목적회사여부} Y/N
                # "filler": "filler`char"  # {filler(미사용)} 
            }
        }
    },
    "t9905": {  ### 기초자산리스트조회
        "inblock": {
            "InBlock": {
                # "dummy": " "  # {DUMMY} 
            }
        },
        "outblock": {
            "OutBlock1": {
                # "shcode": "shcode`char",  # {단축코드} 
                # "expcode": "expcode`char",  # {표준코드} 
                # "hname": "hname`char"  # {종목명} 
            }
        }
    },
    "t9907": {  ### 만기월조회
        "inblock": {
            "InBlock": {
                # "dummy": " "  # {DUMMY} 
            }
        },
        "outblock": {
            "OutBlock1": {
                # "lastym": "lastym`char",  # {만기월} 
                # "lastnm": "lastnm`char"  # {만기월명} 
            }
        }
    }
}
