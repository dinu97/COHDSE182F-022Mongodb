import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017/")
db=client["logindb"];
collection=db["tbllogin"]
print(client.list_database_names());
value={"UserID":"u002","UserName" : "vinu", "Password" : "vinu123"}
cmd=collection.insert_one(value)
print(cmd);
for r in collection.find():
	print(r);
input("\n Press enter to exit")