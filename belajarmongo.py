import pymongo
import os

myclient = pymongo.MongoClient ("mongodb://localhost:27017/")
mydb = myclient["mahasiswa"]

mycol = mydb["profilMahasiswa"]

def insert_data(mycol):
    while(True):
        name = input("Masukkan Name:")
        nim = input("Masukkan Nim:")
        mydict = { "name": name, "nim": nim}
        x = mycol.insert_one(mydict)
        print(x.inserted_id)
        jawab = input('tambahkan data atau tidak?')
        if jawab == 'tidak':
            break
    
    os.system("cls")

def show_data(mycol):
    for x in mycol.find():
        print(x)

def update_data(mycol):
    myquery = {input("masukkan nama field: ") : input("masukkan nama value: ")}
    print("update data")
    newvalues = {"$set": {input("masukkan nama field: ") : input("masukkan nama value: ")}}

    mycol.update_one(myquery, newvalues)

def delete_data(mycol):
    myquery = {input("masukkan nama field: ") : input("masukkan nama value: ")}
    mycol.delete_one(myquery)

def search_data(mycol):
    for x in mycol.find({input("masukkan nama field: ") : input("masukkan nama value: ")}):
        print(x)


def show_menu(mycol):
    print("=== APLIKASI DATABASE MONGODB PYTHON ===")
    print("1. Insert Data")
    print("2. Tampilkan Data")
    print("3. Update Data")
    print("4. Hapus Data")
    print("5. Cari Data")
    print("0. Keluar")
    print("------------------")
    menu = input("Pilih menu> ")

    os.system("cls")

    if menu == "1":
        insert_data(mycol)
    elif menu == "2":
        show_data(mycol)
    elif menu == "3":
        update_data(mycol)
    elif menu == "4":
        delete_data(mycol)
    elif menu == "5":
        search_data(mycol)
    elif menu == "0":
        exit()
    else:
        print("Menu salah!")
 
 
if __name__ == "__main__":
    while (True):
        show_menu(mycol)