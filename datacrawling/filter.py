import pymongo
import traceback
import json

condition = ["PER.2019_12","2015","2020"]

def main():
    try:
        client = pymongo.MongoClient("mongodb+srv://user1:start3we@cluster0.mqlrz.mongodb.net/<TEST2>?retryWrites=true&w=majority")
        db = client.TEST2 ## db name 
        print('MongoDB Connected.')

        #line=json.loads()
        # find()하면 리스트 형식으로 가져옴

        #print(db.platform.find({"code":"005930"}))
        # code가 005930인것 중에 PER의 2019 정보가 2018 보다 크거나 같은 데이터 가져오기
        for doc in db.platform.find({"code":"005930","PER.2019":{"$gte":"2018"}}):
            print(doc)
        print("=======================================")
        # sort사용 
        #cursor.sort(document)
        # document= {key:value}   key는 field이름 , value : 1이면 오름차순 -1이면 내림차순

        for doc in db.platform.find({"code":"005930","PER.2019":{"$gte":"2018", "$lte":"2020"}}).sort([("EPS.2016",1)]):
            print(doc)


        print("=======================================")
        #출력할 조절 개수 3개
        for doc in db.platform.find().limit(3):
            print(doc)

    except Exception as e:
        print(traceback.format_exc())
    finally:
        client.close()
        print('MongoDB Closed.')
 
if __name__ == "__main__":
    main()