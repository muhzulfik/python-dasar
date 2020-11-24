import pymongo

myclient = pymongo.MongoClient ("mongodb://localhost:27017/")
mydb = myclient["mahasiswa"]
#dblist = myclient.list_database_names()
#if "mahasiswa" in dblist:
#print ("The database exists.")
mycol = mydb["profilMahasiswa"]
#collist = mydb.list_collection_names()
#if "customers" in collist:
#print ("The collection exists.")
mylist = [
{ "NIM": "17561001", "Nama": "Diaz", "IPK": 3.80},
{ "NIM": "17561002", "Nama": "Destya", "IPK": 4.00},
{ "NIM": "17561003", "Nama": "Rufina", "IPK": 3.85},
{ "NIM": "17561004", "Nama": "Pramudita", "IPK": 3.90},
{ "NIM": "17561005", "Nama": "Andro", "IPK": 2.80},
{ "NIM": "17561006", "Nama": "Oktaviarsyah", "IPK": 3.98},
{ "NIM": "17561007", "Nama": "Oktrianda", "IPK": 3.70}
]
x = mycol.insert_many(mylist)
#print list of the _id values of the inserted documents:
print(x.inserted_ids)