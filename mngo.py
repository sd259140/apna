import pymongo
url='mongodb://localhost:27017'
mongoServer=pymongo.MongoClient(url)
db=mongoServer['stepup']
collection=db['batch']
document=[{'a':1,'name':'shubham'},{'a':2,'name':'ashubham'},{'a':3,'name':'bshubham'}]
query={'name':{'$regex':'^s'}}

x=collection.delete_many(query)
print(x)


































































#my_query={'prodid':700}
#value={'$pop':{'colour':1}}
#
#for x in collection.find({'price':{'$elemMatch':{'$lt':8000,'$gt':100}}}):
    #print(x)
    
#for x in collection.aggregate([{'$limit':2}]):
#x= collection.update_one(my_query,value)
    #print(x)



