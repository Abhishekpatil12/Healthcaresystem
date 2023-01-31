import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017')

mydb = client['Employee']

information = mydb.employeeinformation
str='seth'

record={
    'firstname':str,
    'lastname':'Reigns',
    'dep':'computer'
    }

information.insert_one(record)

print('done')