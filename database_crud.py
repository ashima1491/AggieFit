import mongo_connect
import os
from builtins import str
from _ast import Str
import string

def getRecords(collection_name):

    try:
        db = mongo_connect.connectMongo()
        collection = db[collection_name]
        message = collection.find()
        
        for x in message:
            print(x)
            
                          
    except Exception as e:
        print(e)        
                    
  

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
        print('Invalid content.')
        print(e)
        

   




