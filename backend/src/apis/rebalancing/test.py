import json
class returnListObj:
    INDICATOR_LIST= []                                          # 지표 리스트
    INDICATOR_MIN_LIST = []                                    # 지표별 최솟값
    INDICATOR_MAX_LIST = []                                    # 지표별 최댓값

def get_indicator_from_json():
    listObj = returnListObj

    # test_indicator.json 내용 : 
    # { "userPER_start":0, "userPER_end":1, "userPBR_start":1, "userPBR_end":3, "userROE_start":0, "userROE_end":0 }
    # json 파일을 가져오는 것이라 그냥 json파일 여는 것으로 해놨는데 이 부분을 받아오는 형식대로 고쳐야할듯?
    with open('./indicator.json') as json_file:
        dic = json.load(json_file)

    for key,value in dic.items():
        # 이상이여야( MAX = 999999를 append한다 ) 하는 값들 ROE , ROA , 매출액대비 순이익률, 매출액 대비 영업이익률, 매출액 증가율
        # 영업이익 증가율, 순이익 증가율, 유동비율
        # 이하이여야 (MIN = -999999를 append한다 부채비율
        # ROE
        if key=="userROE" and value != 0:
            listObj.INDICATOR_LIST.append("ROE")
            listObj.INDICATOR_MIN_LIST.append(value)
            listObj.INDICATOR_MAX_LIST.append(999999)
        #ROA
        elif key=="userROA" and value != 0:
            listObj.INDICATOR_LIST.append("ROA")
            listObj.INDICATOR_MIN_LIST.append(value)
            listObj.INDICATOR_MAX_LIST.append(999999)
        # 매출액 대비 순 이익률,
        elif key=="userSalesPerProfit" and value != 0:
            listObj.INDICATOR_LIST.append("SalesPerProfit")
            listObj.INDICATOR_MIN_LIST.append(value)
            listObj.INDICATOR_MAX_LIST.append(999999)
        # 매출액 대비 영업 이익률
        elif key=="userSalesPerMargin" and value != 0:
            listObj.INDICATOR_LIST.append("SalesPerMargin")
            listObj.INDICATOR_MIN_LIST.append(value)
            listObj.INDICATOR_MAX_LIST.append(999999)
        # 매출액 증가율
        elif key=="userSalesIncrese" and value != 0:
            listObj.INDICATOR_LIST.append("SalesIncrese")
            listObj.INDICATOR_MIN_LIST.append(value)
            listObj.INDICATOR_MAX_LIST.append(999999)
        # 영업이익 증가율
        elif key=="userMarginIncrease" and value != 0:
            listObj.INDICATOR_LIST.append("MarginIncrease")
            listObj.INDICATOR_MIN_LIST.append(value)
            listObj.INDICATOR_MAX_LIST.append(999999)
        # 순이익 증가율
        elif key=="userProfitIncrease" and value != 0:
            listObj.INDICATOR_LIST.append("ProfitIncrease")
            listObj.INDICATOR_MIN_LIST.append(value)
            listObj.INDICATOR_MAX_LIST.append(999999)
        # 유동비율
        elif key=="userCurrentRatio" and value != 0:
            listObj.INDICATOR_LIST.append("CurrentRatio")
            listObj.INDICATOR_MIN_LIST.append(value)
            listObj.INDICATOR_MAX_LIST.append(999999)
        # 부채비율 ( 이하이어야 한다)
        elif key=="userDebtRatio" and value != 0:
            listObj.INDICATOR_LIST.append("DebtRatio")
            listObj.INDICATOR_MIN_LIST.append(-999999)
            listObj.INDICATOR_MAX_LIST.append(value)

        elif key=="userOperatingActivityCashFlow" and value !="0":
            listObj.INDICATOR_LIST.append("Operating_Activity_Cash_Flow")
            # -인 경우
            if value=="1":
                listObj.INDICATOR_MIN_LIST.append(-999999)
                listObj.INDICATOR_MAX_LIST.append(0)
            # +인 경우
            elif value=="2":
                listObj.INDICATOR_MIN_LIST.append(0)
                listObj.INDICATOR_MAX_LIST.append(999999)

        elif key=="userInvestmentActivityCashFlow" and value !="0":
            listObj.INDICATOR_LIST.append("Investment_Activity_Cash_Flow")
            # -+인 경우
            if value=="1":
                listObj.INDICATOR_MIN_LIST.append(-999999)
                listObj.INDICATOR_MAX_LIST.append(0)
            # +인 경우
            elif value=="2":
                listObj.INDICATOR_MIN_LIST.append(0)
                listObj.INDICATOR_MAX_LIST.append(999999)

        elif key=="userFinancialActivityCashFlow" and value !="0":
            listObj.INDICATOR_LIST.append("Financial_Activity_Cash_Flow")
            # -인 경우
            if value=="1":
                listObj.INDICATOR_MIN_LIST.append(-999999)
                listObj.INDICATOR_MAX_LIST.append(0)
            # +인 경우
            elif value=="2":
                listObj.INDICATOR_MIN_LIST.append(0)
                listObj.INDICATOR_MAX_LIST.append(999999)
            
        # EPS
        if key=="userEPS_Start" and value != 0:
            listObj.INDICATOR_LIST.append("EPS_connect")
            listObj.INDICATOR_MIN_LIST.append(value)
        if key=="userEPS_End" and value != 0:
            listObj.INDICATOR_MAX_LIST.append(value)

        if key=="userBPS_Start" and value != 0:
            listObj.INDICATOR_LIST.append("BPS")
            listObj.INDICATOR_MIN_LIST.append(value)
        if key=="userBPS_End" and value != 0:
            listObj.INDICATOR_MAX_LIST.append(value)

        if key=="userCFPS_Start" and value != 0:
            listObj.INDICATOR_LIST.append("CFPS")
            listObj.INDICATOR_MIN_LIST.append(value)
        if key=="userCFPS_End" and value != 0:
            listObj.INDICATOR_MAX_LIST.append(value)

        if key=="userSPS_Start" and value != 0:
            listObj.INDICATOR_LIST.append("SPS")
            listObj.INDICATOR_MIN_LIST.append(value)
        if key=="userSPS_End" and value != 0:
            listObj.INDICATOR_MAX_LIST.append(value)

        if key=="userDPS_Start" and value != 0:
            listObj.INDICATOR_LIST.append("DPS")
            listObj.INDICATOR_MIN_LIST.append(value)
        if key=="userDPS_End" and value != 0:
            listObj.INDICATOR_MAX_LIST.append(value)

        if key=="userPER_Start" and value != 0:
            listObj.INDICATOR_LIST.append("PER")
            listObj.INDICATOR_MIN_LIST.append(value)
        if key=="userPER_End" and value != 0:
            listObj.INDICATOR_MAX_LIST.append(value)

        if key=="userPBR_Start" and value != 0:
            listObj.INDICATOR_LIST.append("PBR")
            listObj.INDICATOR_MIN_LIST.append(value)
        if key=="userPBR_End" and value != 0:
            listObj.INDICATOR_MAX_LIST.append(value)

        if key=="userPCR_Start" and value != 0:
            listObj.INDICATOR_LIST.append("PCR")
            listObj.INDICATOR_MIN_LIST.append(value)
        if key=="userPCR_End" and value != 0:
            listObj.INDICATOR_MAX_LIST.append(value)

        if key=="userPSR_Start" and value != 0:
            listObj.INDICATOR_LIST.append("PSR")
            listObj.INDICATOR_MIN_LIST.append(value)
        if key=="userPSR_End" and value != 0:
            listObj.INDICATOR_MAX_LIST.append(value)

        if key=="userMarketDiviend_Start" and value != 0:
            listObj.INDICATOR_LIST.append("Market_odds")
            listObj.INDICATOR_MIN_LIST.append(value)
        if key=="userMarketDiviend_End" and value != 0:
            listObj.INDICATOR_MAX_LIST.append(value)

        if key=="userEPS_Start" and value != 0:
            listObj.INDICATOR_LIST.append("EPS")
            listObj.INDICATOR_MIN_LIST.append(value)
        if key=="userEPS_End" and value != 0:
            listObj.INDICATOR_MAX_LIST.append(value)

        if key=="userEPS_Start" and value != 0:
            listObj.INDICATOR_LIST.append("EPS")
            listObj.INDICATOR_MIN_LIST.append(value)
        if key=="userEPS_End" and value != 0:
            listObj.INDICATOR_MAX_LIST.append(value)
    return listObj



if __name__ == "__main__":
    listObj1=get_indicator_from_json()
    print(listObj1.INDICATOR_LIST)
    print(listObj1.INDICATOR_MIN_LIST)
    print(listObj1.INDICATOR_MAX_LIST)
