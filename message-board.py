'''
Created on Oct 28, 2018

@author: sharm
'''
'''
Created on Oct 28, 2018

@author: sharm
'''
import redis
import database_crud
dir(redis)

r = redis.Redis()


subscribing = False;
topic = "";

while True:
    try:
#         if subscribing:
#             print("Sub")
#             for item in p.listen():    
#                 print(item)

        cmd = input('Enter your command: ')
        print(cmd)
        cmd_parts = cmd.split(" ")
        print(cmd_parts)
        if cmd_parts[0] == "select":
            channel= cmd_parts[1];
            if(""==channel):
               print("Enter a message board to select ") 
        elif cmd_parts[0] == "read":
            database_crud.getRecords(channel)
           
        elif cmd_parts[0] == "write":
            to_pub = ' '.join(cmd_parts[1:])
            res = r.publish(channel, to_pub) 
            print(res)
            database_crud.insertRecords(channel, cmd_parts[1:])
        elif cmd_parts[0] == "listen":
            subscribing = True;
            p = r.pubsub()
            res = p.subscribe([channel]) 
            print(res)
        elif cmd_parts[0] == "stop":
            subscribing = False;
            res = p.unsubscribe([channel]) 
            print(res)    
        elif cmd_parts[0] == "quit":
            break;
        else:
            print("Input format wrong");
            
        if subscribing:
            print("Sub")
            for item in p.listen():    
                print(item)
    except KeyboardInterrupt:
        subscribing = False


    