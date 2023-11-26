
# Basics of MongoDB


This repository demonstrates the usage of MongoDB, a popular NoSQL database.
MongoDB is a document-oriented database that provides high performance, scalability, and flexibility.
It stores data in a flexible, JSON-like format called BSON (Binary JSON), which allows for easy manipulation and querying.

Key concepts related to MongoDB include:

1. **Collections**: MongoDB stores data in collections, which are analogous to tables in relational databases. Each collection contains a set of documents.

2. **Documents**: A document is a basic unit of data in MongoDB. It is a JSON-like object that can have a flexible schema. Documents in a collection can have different fields and structures.

3. **Fields**: Fields are key-value pairs within a document. Each field has a name and a corresponding value. Fields can store various data types, including strings, numbers, arrays, and nested documents.

4. **Queries**: MongoDB provides a powerful query language for retrieving data from collections. Queries can be used to filter documents based on specific criteria and retrieve the desired results.

5. **Indexes**: Indexes in MongoDB improve the performance of queries by allowing faster data retrieval. They are created on specific fields or combinations of fields and enable efficient searching and sorting.

6. **Aggregation**: MongoDB supports aggregation pipelines, which allow for complex data transformations and aggregations. Aggregation pipelines consist of multiple stages that process and transform the data.

7. **_id**: Each document in a collection has a unique _id field that acts as a primary key. If a document does not have an _id field, MongoDB automatically adds one.

8. **Embedded Data Model**: In this data model, related data is stored together in a single document. This model is useful when the related data is not frequently accessed.
These are just a few of the key concepts related to MongoDB. For more detailed information, refer to the MongoDB documentation.

9. **Normalized Data Model**:  In this model, we store the data in multiple collections and reference one document in another document using the ObjectId of the document.
