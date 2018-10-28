import mongo_connect
import os
from builtins import str

def getRecords(collection_name):

    
    db = mongo_connect.connectMongo()
    collection = db[collection_name]
    message = collection.find()
    
    for x in message:
        print(x)
                          

                    
  

def insertRecords(collection_name,value):
    try:
       
        db = mongo_connect.connectMongo()
        collection = db[collection_name]
        collection.insert_one(
            {
             "message": value
             }
            )
        print("record written in database") 
     
       
    
    except Exception as e:
        print('Invalid content. One or more parameters not found. Please check the log file')
        print(e)
        

   




