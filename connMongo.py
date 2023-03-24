from pymongo.mongo_client import MongoClient

#configuracion local (windows)
HOST= "localhost"
PORT= 27017


URI = f"mongodb://{HOST}:{PORT}"


client = MongoClient(URI)

def getDbMongo():                   
    try:
        col = client.local

        return col

    except Exception as e:
        print(e)
