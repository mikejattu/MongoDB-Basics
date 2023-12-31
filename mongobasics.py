# writing a mongoDB test script
from pymongo import MongoClient

# creating a mongo client
client = MongoClient()

# specifiying the host and port
client = MongoClient('localhost', 27017)

# creating or opening a database  
db = client['test-database'] 

# listing the collection names
collection_list = db.list_collection_names()

# creating a collection
collection = db['test-collection']

# inserting a document into the collection
# Dictionaries are used to represent documents
student = {
    "name": "Mark",
    "rollno": 1,
    "branch": "CSE"
}

"""

Inserting Documents

"""
# inserting the document into the collection
collection.insert_one(student)


# inserring multiple documents into the collection
students = [
    {
        "name": "Mark",
        "rollno": 1,
        "branch": "CSE"
    },
    {
        "name": "John",
        "rollno": 2,
        "branch": "CSE"
    },
    {
        "name": "Jane",
        "rollno": 3,
        "branch": "CSE"
    },
    {
        "name": "Doe",
        "rollno": 4,
        "branch": "CSE"
    },
    {
        "name": "Tom",
        "rollno": 5,
        "branch": "CSE"
    }
]
collection.insert_many(students)
# print the ids of the inserted documents:
print(collection.inserted_ids)

"""

finding in a collection

"""
# finding in a collection
# find all documents in the collection
collection.find()

# find documents with a query filter

collection.find({"name": "Mark"}) # equality filter

collection.find({"name": {"$eq": "Mark"}}) # equality filter

collection.find({"name": {"$ne": "Mark"}}) # not equal filter

collection.find({"name": {"$gt": "Mark"}}) # greater than filter

collection.find({"name": {"$gte": "Mark"}}) # greater than or equal to filter

collection.find({"name": {"$lt": "Mark"}}) # less than filter

collection.find({"name": {"$lte": "Mark"}}) # less than or equal to filter

collection.find({"name": {"$in": ["Mark", "John"]}}) # in filter

collection.find({"name": {"$nin": ["Mark", "John"]}}) # not in filter

collection.find({"name": {"$exists": True}}) # exists filter

# limiting the number of documents returned
collection.find().limit(2)

"""

Counting Documents

"""
# find the count of documents in the collection
collection.count_documents({})

# find the count of documents in the collection with a query filter
collection.count_documents({"name": "Mark"})

"""

Updating Documents

"""
# update a single document
collection.update_one({"name": "Mark"}, {"$set": {"branch": "IT"}})

# update multiple documents
collection.update_many({"name": "Mark"}, {"$set": {"branch": "IT"}})



"""

Aggregation Pipeline: Aggregation operations process data records and return computed results. 
                      Aggregation operations group values from multiple documents together, and can perform a variety of operations on the grouped data to return a single result. 
                      MongoDB provides three ways to perform aggregation: the aggregation pipeline, the map-reduce function, and single purpose aggregation methods.

"""

# $group stage
# The $group stage groups documents by some specified expression and outputs to the next stage a document for each distinct grouping.
# The output documents contain an _id field which contains the distinct group by key. The output documents can also contain computed fields that hold the values of some accumulator expression grouped by the $group‘s _id field. 
# $group does not order its output documents.
collection.aggregate([
    {
        "$group": {
            "_id": "$branch",
            "count": {"$sum": 1}
        }
    }
])
# this will group the documents by the branch and count the number of documents in each group

# output will look like this
# { "_id" : "CSE", "count" : 5 }    

# $match stage
# The $match stage filters out documents from the stream that do not match the given expression.
# $match uses standard MongoDB queries. For each input document, outputs either one document (a match) or zero documents (no match).
collection.aggregate([
    {
        "$match": {
            "name": "Mark"
        }
    }
])

# output will look like this
# { "_id" : ObjectId("5f1f7d6a7b1a4c7d2b4e4a1e"), "name" : "Mark", "rollno" : 1, "branch" : "CSE" }

# $project stage
# The $project stage is used to select only the necessary fields from the documents.
# The $project stage can be used to rename fields, add new fields, or to remove fields from the output documents.
collection.aggregate([
    {
        "$project": {
            "name": 1,
            "rollno": 1
        }
    }
])

# output will look like this
# { "_id" : ObjectId("5f1f7d6a7b1a4c7d2b4e4a1e"), "name" : "Mark", "rollno" : 1 }
# { "_id" : ObjectId("5f1f7d6a7b1a4c7d2b4e4a1f"), "name" : "John", "rollno" : 2 }
# { "_id" : ObjectId("5f1f7d6a7b1a4c7d2b4e4a20"), "name" : "Jane", "rollno" : 3 }
# { "_id" : ObjectId("5f1f7d6a7b1a4c7d2b4e4a21"), "name" : "Doe", "rollno" : 4 }
# { "_id" : ObjectId("5f1f7d6a7b1a4c7d2b4e4a22"), "name" : "Tom", "rollno" : 5 }

# $sort stage
# The $sort stage sorts the documents by the specified fields.  
collection.aggregate([
    {
        "$sort": {
            "rollno": 1
        }
    }
])
# output will look like this
# { "_id" : ObjectId("5f1f7d6a7b1a4c7d2b4e4a1e"), "name" : "Mark", "rollno" : 1, "branch" : "CSE" }
# { "_id" : ObjectId("5f1f7d6a7b1a4c7d2b4e4a1f"), "name" : "John", "rollno" : 2, "branch" : "CSE" }
# { "_id" : ObjectId("5f1f7d6a7b1a4c7d2b4e4a20"), "name" : "Jane", "rollno" : 3, "branch" : "CSE" }
# { "_id" : ObjectId("5f1f7d6a7b1a4c7d2b4e4a21"), "name" : "Doe", "rollno" : 4, "branch" : "CSE" }
# { "_id" : ObjectId("5f1f7d6a7b1a4c7d2b4e4a22"), "name" : "Tom", "rollno" : 5, "branch" : "CSE" }

# $lookup stage
# The $lookup stage performs a left outer join to an unsharded collection in the same database to filter in documents from the “joined” collection for processing.
# To each input document, the $lookup stage adds a new array field whose elements are the matching documents from the “joined” collection. The $lookup stage passes these reshaped documents to the next stage.
# The $lookup stage does an equality match between a field from the input documents with a field from the documents of the “joined” collection.

collection.aggregate([
    {
        "$lookup": {
            "from": "test-collection",
            "localField": "rollno",
            "foreignField": "rollno",
            "as": "students"
        }
    }
])

# unwind stage
# The $unwind stage outputs one document for each element in the specified array field.
# The $unwind stage allows you to expand arrays into separate documents, one document for each element of the array.
collection.aggregate([
    {
        "$unwind": "$students"
    }
])

# $regex stage
# The $regex stage matches the documents that satisfy a regular expression.
# this allows string pattern matching
collection.aggregate([
    {
        "$match": {
            "name": {
                "$regex": "^M" # this will match all the names starting with M
            }
        }
    }
])
