from mongo_connect import connectMongo
import constants
import pymongo
import json
import pprint
from _overlapped import NULL


collection = connectMongo()
# print(collection)
##### FIND ALL ENTRIES IN THE DATABASE #####
# Assuming RQ0 is the query to find all entries in the database
# RQ0 = collection.find()
# for data in RQ0:
# 	pprint.pprint(data)
#####################################################################


#####Insert documents of dummy-fitness.json######
#WQ1
# collection.insert_many([{
# 		"uid": 1004,
# 		"age": 45,
# 		"height": "5ft1in",
# 		"weight": "160lbs",
# 		"activityDuration": [67, 48, 56, 15, 57, 20, 57, 15, 60, 10, 4, 3, 89],
# 		"goal": {
# 			"activityGoal": "60min",
# 			"stepGoal": 0,
# 			"weekGoal": 3
# 		},
# 		"tags": ["irregular", "activityOnly"]
# 	},
# 	{
# 		"uid": 1005,
# 		"activityDuration": [56, 62, 48, 54],
# 		"stepCount": [6792, 7832, 5876, 6453],
# 		"age": 50,
# 		"gender": "male",
# 		"goal": {
# 			"activityGoal": "45min",
# 			"stepGoal": 8000,
# 			"weekGoal": 3
# 		},
# 		"tags": ["active"]
# 	},
# 	{
# 		"uid": 1006,
# 		"stepCount": [7694, 4568, 2390, 6738, 1243, 132, 6785],
# 		"goal": {
# 			"activityGoal": "NA",
# 			"stepGoal": 5000,
# 			"weekGoal": 7
# 		},
# 		"tags": ["irregular", "stepOnly"]
# 	},
# 	{
# 		"uid": 1007,
# 		"activityDuration": [23, 14, 32, 12, 19, 32],
# 		"stepCount": [543, 534, 231, 234, 241],
# 		"goal": {
# 			"activityGoal": "30min",
# 			"stepGoal": 1000,
# 			"weekGoal": 7
# 		},
# 		"tags": ["beginner"]
# 	},
# 	{
# 		"uid": 1008,
# 		"activityDuration": [72, 75, 78, 45, 79, 86],
# 		"stepCount": [10439, 10456, 10458, 3423, 10807, 11232],
# 		"gymDuration": [62, 61, 64, 0, 67, 69],
# 		"height": "5ft10in",
# 		"weight": "178lbs",
# 		"goal": {
# 			"activityGoal": "90min",
# 			"stepGoal": 12000,
# 			"weekGoal": 5
# 		},
# 		"competitors": [1009],
# 		"tags": ["regular", "sportsman", "gymGoer", "competitor"]
# 	},
# 	{
# 		"uid": 1009,
# 		"activityDuration": [73, 68, 83, 79, 34, 86],
# 		"stepCount": [10439, 10216, 11342, 11278, 4323, 11762],
# 		"gymDuration": [60, 58, 64, 62, 0, 64],
# 		"height": "5ft8in",
# 		"weight": "183lbs",
# 		"goal": {
# 			"activityGoal": "90min",
# 			"stepGoal": 12000,
# 			"weekGoal": 5
# 		},
# 		"competitors": [1008],
# 		"tags": ["regular", "sportsman", "gymGoer", "competitor"]
# 	}
# ]) 


#########################################################################
#### Update the database with data from user1001-new.json#####
#WQ2
# collection.find_one_and_update({"uid": 1001}, 
#                                  {"$set": { "height": "5ft10in",
#   										 	"weight": "190lbs",
#     										"tags": ["ambitious"]
#     										}
# 								})

#########################################################################

####RQ1. Count the number of employees whose data is in the AggieFit database.

# print(collection.estimated_document_count())

#########################################################################

####RQ2. Retrieve employees who have been tagged as "irregular".
# cur = collection.find({"tags":"irregular"})
# for x in cur:
# 	pprint.pprint(x)


##########################################################################

####RQ3. Retrieve employees that have a goal step count less than or equal to 1500 steps
# cur = collection.find({"goal.stepGoal":{"$lte":15000}})
# for x in cur:
# 	pprint.pprint(x)

##########################################################################

#### RQ4. Aggregate the total activity duration for each employee. If the employee does not
#### have activity duration in their data, you can report their total activity duration as 0. 

cur = collection.find({"activityDuration":{"$gte":0}})
for i in cur:
	sum=0
	for j in i["activityDuration"]:
		sum = sum + j;
	name = i["uid"]	
	print(name)
	print(sum)	
	
cur1 = collection.find({"activityDuration":{"$exists": False}})
for i in cur1:
	sum=0
	
		
	name = i["uid"]	
	print(name)
	print(sum)	
	
# 	pprint.pprint(duration)
		
# pprint.pprint(duration)

######## FIND ENTRIES WITH CONDITION #######
######## collection.find(CONDITION) #######
######## E.g., collection.find({"Name" : "Alice"}) #######

######## UPDATE ENTRIES WITH CONDITION ########
######## collection.update_one(CONDITION, _update_) #######
######## collection.update_many(CONDITION, _update_)
######## E.g., collection.find({"Name" : "Alice"}, {"$inc" : {"age" : 1} })

######## DELETE ENTRIES WITH CONDITION ########
######## collection.delete_one(CONDITION) #######
######## collection.delete_many(CONDITION)
######## E.g., collection.find({"Name" : "Alice"})

######## AGGREGATE ENTRIES WITH PIPELINE ########
######## collection.aggregate(PIPELINE) ########

