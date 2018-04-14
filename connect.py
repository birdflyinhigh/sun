from pymongo import MongoClient


conn = MongoClient(host='127.0.0.1', port=27017)


print(conn.address)
print(conn.database_names())

