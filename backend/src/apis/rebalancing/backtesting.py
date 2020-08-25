# pymongo 사용 모듈 추출
import pymongo
import json

from backtesting_class_collection import Result, Init_data, User_input_data

# 규칙
# 1. 맨 처음 받고 변하지 않는 변수는 모두 대문자로
# 2. 받는 변수를 한 class로, 보내는 변수를 한 class로 만든다.
# 3. 변수는 사용하는 곳 근처에서 선언하기

# Function1 : rebalancing_date_data
# 함수 설명 : 리벨런싱하는 주기별 날짜 데이터 가공 및 반환
# Parameter : 
# 1) user_input : User_input_data Class 객체
# return : 
# 1) rebalancing_date_list -> 주기별 날짜 데이터
#  ex) 시작날이 20150101 종료일이 20160701이고 rebalancing이 분기별이면 [2014_12, 2015_03, 2015_06, 2015_09, 2015_12, 2016_03, 2016_06] 반환
# clear
def rebalancing_date_data(user_input):
    start_data_year = user_input.DATE_START//10000
    start_data_month = user_input.DATE_START%10000
    if start_data_month<301:
        start_data_month="12"
        start_data_year=start_data_year-1
    elif start_data_month<601:
        start_data_month="03"
    elif start_data_month<901:
        start_data_month="06"
    elif start_data_month<1201:
        start_data_month="09"
    start_data_int=int(str(start_data_year)+start_data_month)
    start_data=str(start_data_year)+"_"+start_data_month
    rebalancing_date_list=[]
    rebalancing_date_list.append(start_data)
    YEAR_LIST= [20100000,20110000,20120000,20130000,20140000,20150000,20160000,20170000,20180000,20190000,20200000]
    MONTH_LIST=[301,601,901,1201]
    # 분기별 데이터 가공
    temp=""
    if user_input.REBALANCING=="0":
        for i in YEAR_LIST:
            for j in MONTH_LIST:
                if user_input.DATE_START<=i+j and i+j<user_input.DATE_END:
                    if j!=1201:
                        temp=str(i//10000)+"_"+"0"+str(j//100)
                        rebalancing_date_list.append(temp)
                    else :
                        temp=str(i//10000)+"_"+str(j//100)
                        rebalancing_date_list.append(temp)
    # 1년 주기별 데이터 가공
    elif user_input.REBALANCING=="1":
        for i in YEAR_LIST:
            if user_input.DATE_START//10000<=i//10000 and i//10000<=user_input.DATE_END//10000:
                temp = str(i//10000)+"_"+start_data_month
                rebalancing_date_list.append(temp)
    print(rebalancing_date_list)
    return rebalancing_date_list

# Function2 : search_rebalanced_enterprise
# explain : 리벨런싱할때 바꿔주는 기업 코드를 리턴하는 함수 
# Parameter :
# 1) db : db (import from pymongo)
# 2) f : Init_data Class`s object
# 3) user_input : User_input_data Class`s object
# 4) count : revalancing count
# return : 
# 1) enterprise_list : enterprise list 
# clear
def search_rebalanced_enterprise(db,f,user_input,count):
    start_data=""
    enterprise_list=[]
    print("count : "+ str(count))
    print("f.rebalancing_date_list : "+f.rebalancing_date_list[count])
    start_data=f.rebalancing_date_list[count]
    for i,indicator in enumerate(user_input.INDICATOR_LIST):
        user_input.INDICATOR_LIST[i]=user_input.INDICATOR_LIST[i]+"."+start_data
    print('MongoDB Connected.')
    # 이 부분은 지표를 3개 받게 했는데, find내부의 doc을 변수 dic으로 저장하려 했으나 쿼리문이 포함되서 dic형식으로 저장할 수가 없었다. 그래서 다른 방법 찾아야함.
    for doc in db.stockparam.find({ "$and":[{user_input.INDICATOR_LIST[0] : { "$gte" : int(user_input.INDICATOR_MIN_LIST[0] ), "$lte": int(user_input.INDICATOR_MAX_LIST[0])}},{ user_input.INDICATOR_LIST[1] : { "$gte" : int(user_input.INDICATOR_MIN_LIST[1] ), "$lte": int(user_input.INDICATOR_MAX_LIST[1])}},{user_input.INDICATOR_LIST[2] : { "$gte" : int(user_input.INDICATOR_MIN_LIST[2] ), "$lte": int(user_input.INDICATOR_MAX_LIST[2])}}]},{"_id":False,"code":True}).sort([("Market_cap",-1)]).limit(20):
        enterprise_list.append(doc["code"])
    for i,indicator in enumerate(user_input.INDICATOR_LIST):
        user_input.INDICATOR_LIST[i]=user_input.INDICATOR_LIST[i][:-8]
    return enterprise_list

# Function3 : make_code_date_clasifyed_list
# explain : 리벨런싱한 기업의 데이터를 리벨런싱 주기별로 바꿔줄 때 사용
# Parameter : 
# 1) db : db (import from pymongo)
# 2) f : Init_data Class`s object
# 3) user_input : User_input_data Class`s object
# return : 
# 1) code_date_clasifyed_list_init.copy() : classifyed data
# 2) count : revalancing count
def make_code_date_clasifyed_list(db,f,user_input):

    date_change=user_input.DATE_START
    REBALANCING_YEAR_GAP=10000
    REBALANCING_QUARTER_GAP=300
    times=0
    try_times=0
    for k in range(0,user_input.THE_NUMBER_OF_MAXIMUM_EVENT):
        code1= f.enterprise_list[k]

        for i in range(len(f.rebalancing_date_list)+5):      # 이건 문제가 아님
            f.code_date_clasifyed_list_init[k].append([])

        for i in db.price_info.find({"code":code1}):
            for index,j in enumerate(i['data']):
                if j['Date']>=user_input.DATE_START and j['Date']<=user_input.DATE_END:
                    #분기별 리벨런싱
                    if user_input.REBALANCING=="0" and (j['Date']-date_change>=REBALANCING_QUARTER_GAP):      # 여기가 문제
                        print("revalancing try : "+ str(try_times))
                        try_times=try_times+1
                        if j['Date']-date_change>=2000:
                            date_change = date_change -1229 + 10000
                        else:   
                            date_change = date_change + REBALANCING_QUARTER_GAP
                        times=times+1
                    #연도별 리벨런싱
                    elif user_input.REBALANCING=="1"and (j['Date']-date_change>=REBALANCING_YEAR_GAP):
                        date_change= date_change + REBALANCING_YEAR_GAP
                        times=times+1
                    #no REBALANCING
                    # elif user_input.REBALANCING=="2":
                    f.code_date_clasifyed_list_init[k][times].append(j)
    print('times'+ str(times))
    return f.code_date_clasifyed_list_init.copy(),times

# Function4 : init_list_condiiton(f,user_input)
# Explain : make list space
# parameter : 
# 1) f : Init_data Class`s object
# 2) user_input : User_input_data Class`s object
def init_list_condiiton(f,user_input):
    for i in range(0,user_input.THE_NUMBER_OF_MAXIMUM_EVENT):
        f.is_buy.append(0)
        f.buy_count.append(0)
    # 최대 기업 수만큼 리스트 공간 만들어줌
    for k in range(0,user_input.THE_NUMBER_OF_MAXIMUM_EVENT+1):
        f.code_date_clasifyed_list.append([])

# Function5 : set_buy_sell_price(user_input,close_price,j)
# Expalin : set buy sell price
# Parameter :
# 1) user_input : User_input_data Class`s object
# 2) close_price : stock`s close price
# 3) k : enterprise index
# 4) j : revalancing index
# return 
# 1) buying_price : close price * buying condition
# 2) sales_profit_price : close price * sales profit condition
# 3) sales_loss_price : close_price * sales loss condition

def set_buy_sell_price(f,user_input,k,j):
    close_price = buying_price = sales_profit_price = sales_loss_price = 0
    for data in f.code_date_clasifyed_list_init[k][j]:
        close_price=int(data['Close'])              #이거 데이터 순서가 날짜 정방향 순서대로인지 확인해야함
        print("========================revalancing========================")
        print("change : close price :"+ str(data['Close']) )
        break
    buying_price = close_price * user_input.BUYING_CONDITION    # 매수 조건
    sales_profit_price = close_price * float(user_input.sales_profit)  # 익절가격
    sales_loss_price = close_price * float(user_input.sales_loss)      # 손절 가격
    print("revalancing try : " + str(j))
    print("buying_price : "+ str(buying_price))
    print("sales_profit_price : "+ str(sales_profit_price))
    print("sales_loss_price : "+ str(sales_loss_price))
    return buying_price,sales_profit_price,sales_loss_price

# Function6 : buying_stock(f,user_input,data,partition_invertment_principal,k,sales_profit_price,sales_loss_price)
# Explain : selling stock
# Parameter : 
# 1) f : Init_data Class`s object
# 2) user_input : User_input_data Class`s object
# 3) partition_invertment_principal : partition investment principal
# 4) k : enterprise index
# 5) sales_profit_price : sales profit price
# 6) sales_loss_price : sales loss price
# return :
# 1) sales_profit_price : adjusted sales loss price
# 2) sales_loss_price : adjusted sales_loss_price
# 3) partition_invertment_principal :  partition_invertment_principal after buy
def buying_stock(f,user_input,data,partition_invertment_principal,k,sales_profit_price,sales_loss_price):
    f.buy_count[k] = partition_invertment_principal[k] // data["Close"]
    partition_invertment_principal[k]-= f.buy_count[k]*data["Close"]
    '''
    print("========================buy=============================")
    print("1. date : "+str(data['Date']))
    print("2. f.buy_count : "+str(f.buy_count[k]))
    print("3. buying_price : "+ str(data["Close"]))
    print("4. buy after rest_investment_principal : "+str(partition_invertment_principal[k]))
    '''
    sales_profit_price = data["Close"] * float(user_input.sales_profit)  # 익절가격
    sales_loss_price = data["Close"] * float(user_input.sales_loss)      # 손절 가격
    f.is_buy[k]=1
    return sales_profit_price,sales_loss_price,partition_invertment_principal

# Function7 : selling_stock(f,user_input,data,partition_invertment_principal,k,buying_price)
# Explain : selling stock
# Parameter : 
# 1) f : Init_data Class`s object
# 2) user_input : User_input_data Class`s object
# 3) data : db.price_info`s stock data dictionary
# 4) partition_invertment_principal : partition invertment principal
# 5) k : enterprise index
# 6) buying_price : buying price
# return :
# 1) partition_invertment_principal : partition invertment principal after sell
# 2) buying_price : adjusted buying price
def selling_stock(f,user_input,data,partition_invertment_principal,k,buying_price):
    partition_invertment_principal[k] += f.buy_count[k]*data["Close"]
    '''
    print("========================sell=============================")
    print("1. date : "+str(data['Date']))
    print("2. sell_count : "+str(f.buy_count[k]))
    print("3. sell_price : "+ str(data["Close"]))
    print("4. sell after rest_investment_principal : "+str(partition_invertment_principal[k]))
    '''
    buying_price = data["Close"] * user_input.BUYING_CONDITION    # 매수 조건
    f.buy_count[k]=0
    f.is_buy[k]=0
    return partition_invertment_principal,buying_price

# Function8 : lastday_sell_all(f,user_input,partition_invertment_principal)
# Parameter :
# 1) f : Init_data Class`s object
# 2) user_input : User_input_data Class`s object
# 3) partition_invertment_principal : partition investment principal
# 4) k : enterprise index
# 5) data : db.price_info`s data
def lastday_sell_all(f,user_input,partition_invertment_principal,k,data):
    partition_invertment_principal[k] += f.buy_count[k]*data["Close"]
    print("====================last day, sell all============================")
    print("1. date : "+str(data['Date']))
    print("2. sell_count : "+str(f.buy_count[k]))
    print("3. lastday close_price : "+ str(data["Close"]))
    print("4. sell after rest_investment_principal : "+str(partition_invertment_principal[k]))
    f.buy_count[k]=0
    f.is_buy[k]=0
    user_input.investment_principal+=partition_invertment_principal[k]
    partition_invertment_principal[k]=0
    #return partition_invertment_principal[k]

# Function9 : set_result(r,user_input)
# Parameter :
# 1) r : Result Class`s object
def set_result(r,user_input):
    r.profit_all = user_input.investment_principal - user_input.INVESTMENT_PRINCIPAL_COPY 
    r.currentAsset = user_input.investment_principal
    r.cagr= r.profit_all/user_input.INVESTMENT_PRINCIPAL_COPY * 100
# function10 :    
def backtesting():
    # 초기 CLASS 세팅
    user_input= User_input_data()
    f = Init_data()
    user_input.strategy1()
    r = Result("dongwoo")
    '''
    user_input.set_indicator_data()
    user_input.set_basic_data()
    user_input.set_backtesting_data()
    '''
    count=0                          # 리벨런싱 횟수 정해주는 변수
    client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.kjrlb.mongodb.net/<test_db_stock>?retryWrites=true&w=majority")    # 파이몽고 사용해서
    db = client.test_db_stock
    # init setting
    f.rebalancing_date_list= rebalancing_date_data(user_input)
    init_list_condiiton(f,user_input)
    f.code_date_clasifyed_list_init=f.code_date_clasifyed_list[:]
    f.enterprise_list=search_rebalanced_enterprise(db,f,user_input,0)

    f.code_date_clasifyed_list_init,count=make_code_date_clasifyed_list(db,f,user_input)
    count2=count
    # count2 = 리벨런싱한 총 횟수
    print("count "+str(count2))
    for j in range(count2):
        if j!=0:
            f.enterprise_list=search_rebalanced_enterprise(db,f,user_input,j)
            f.code_date_clasifyed_list_init,count=make_code_date_clasifyed_list(db,f,user_input)

        partition_invertment_principal=[]
        for ttt in range(0,user_input.THE_NUMBER_OF_MAXIMUM_EVENT):
            partition_invertment_principal.append(user_input.investment_principal//user_input.THE_NUMBER_OF_MAXIMUM_EVENT)
        user_input.investment_principal-=partition_invertment_principal[0]*user_input.THE_NUMBER_OF_MAXIMUM_EVENT

        for k in range(0,user_input.THE_NUMBER_OF_MAXIMUM_EVENT):
            print("change enterprise")
            print("code : "+ f.enterprise_list[k])
            buying_price, sales_profit_price, sales_loss_price = set_buy_sell_price(f,user_input,k,j)
            for i,data in enumerate(f.code_date_clasifyed_list_init[k][j]):
                # 매수 조건
                if f.is_buy[k]==0:
                    if data["Close"]<=buying_price:
                        sales_profit_price,sales_loss_price,partition_invertment_principal=buying_stock(f,user_input,data,partition_invertment_principal,k,sales_profit_price,sales_loss_price)
                # 매도 조건
                elif f.is_buy[k]==1:
                    if data["Close"]>=sales_profit_price or data["Close"] <= sales_loss_price:
                        partition_invertment_principal, buying_price = selling_stock(f,user_input,data,partition_invertment_principal,k,buying_price)
            # 리벨런싱 전에는 가지고 있는 주식을 다 판다.
            lastday_sell_all(f,user_input,partition_invertment_principal,k,data)

    set_result(r,user_input)
    print("profit_all   : " + str(r.profit_all))
    print("cagr         : " + str(r.cagr)+" %")
    print("currentAsset : " +str(r.currentAsset))

if __name__ == "__main__":
    backtesting()