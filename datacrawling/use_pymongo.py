import pymongo
import traceback
import json

def main():
    try:
        client = pymongo.MongoClient("mongodb+srv://user1:start3we@cluster0.mqlrz.mongodb.net/<TEST2>?retryWrites=true&w=majority")
        db = client.TEST2 ## db name 
        print('MongoDB Connected.')
        
        inputfile="./json_file/test1.json"
        f = open(inputfile, 'r',encoding='UTF8')
        lines = f.readlines()

        for line in lines:  
            line=json.loads(line)
            db.platform2.insert_one(line)

    except Exception as e:
        print(traceback.format_exc())
    finally:
        client.close()
        print('MongoDB Closed.')
 
if __name__ == "__main__":
    main()