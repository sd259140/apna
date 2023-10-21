import pymongo
url="mongodb://localhost:27017/"
mongoServer=pymongo.MongoClient(url)
db=mongoServer['mydatabase']
collection=db['school']
#data=[{'prodid':800,'proname':"i9",'mf':'apple','price':6000,'category':{'main':'smart','sub':'smartphone'}},{'prodid':900,'proname':"i11",'mf':'ttple','price':9000,'category':{'main':'smart','sub':'smartphone'}}]

#result= collection.find({"$and":[{'category.main':'smart'},{'price':6000}]})
#result=collection .delete_many({"proname":{"$regex":"^i"}})
result=collection.create_index("year":-1)
print(result)







    

