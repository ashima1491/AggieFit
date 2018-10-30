import threading
import time
import redis
import database_crud
from time import sleep
dir(redis)

r = redis.Redis()


subscribing = False;
channel="";
while True:
    try:

        cmd = input('Enter your command: ')
        print(cmd)
        cmd_parts = cmd.split(" ")
        print(cmd_parts)
        if cmd_parts[0] == "select":
            channel= cmd_parts[1];
            if(""==channel):
               print("Enter a message board to select ") 
        elif cmd_parts[0] == "read":
            if(""==channel):
                print("Enter a message board to read ") 
            if(channel!=""):    
                database_crud.getRecords(channel)
           
        elif cmd_parts[0] == "write":
            to_pub = ' '.join(cmd_parts[1:])
            if(channel==""):
               print("Enter a message board to write ")
                
            res = r.publish(channel, to_pub) 
            print(res)
            if(channel!=""):
                database_crud.insertRecords(channel, cmd_parts[1:])
        elif cmd_parts[0] == "listen":
            if(""==channel):
                print("Enter a message board to listen ")
            else: 
                subscribing = True;
                p = r.pubsub()
                res = p.subscribe([channel])
                if subscribing:
                    print("Sub")
                    try:    
                        temp = p.listen()
                        for item in temp: 
                            print(item)
                    except KeyboardInterrupt:
                        p.unsubscribe([channel])
                        break;
                print(res)
        elif cmd_parts[0] == "stop":
            if(""==channel):
                print("Enter a message board to stop ")
            elif subscribing == False:
                print("Not listening to any channel")    
            else:    
                subscribing = False;
                p = r.pubsub()
                res = p.unsubscribe([channel]) 
                print(res)    
        elif cmd_parts[0] == "quit":
            break;
        else:
            print("Input format wrong");
                    
           
    except KeyboardInterrupt:
        
        subscribing = False
        break;
        

        