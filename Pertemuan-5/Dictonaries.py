# Membuat struktur data dictionary
userlogin = {"name" : "Budi", "age" : 30, "Role" : "Admin"}

#mengakses data
print(f"Nama Akun : {userlogin['name']}")
print(f"Umur Akun : {userlogin['age']}")
print(f"Role Akun : {userlogin['Role']}")

# Akses data seluruh
print(userlogin.items())
print(userlogin.keys())
print(userlogin.values())

# Menambahkan data 
userlogin["Email"] = "example@gmail.com"
print(userlogin)

# Menghapus data big-o o(1) 
userlogin.pop("Email")
print(userlogin)

# Mengubah data ke dalam dictionary big-o o(1)
userlogin["Role"] = "User"
print(userlogin)

# Nested dictionary
dbUser = {"user1": {"name": "andi", "age": 30, "role": "admin"},
"user2": {"name": "budi", "age": 25, "role": "user"},
"user3": {"name": "candra", "age": 28, "role": "guest"}}

print(dbUser)
# Akses value base key
print(dbUser["user1"])

# Melakukan pencarian data di dictionary
fineWord = input("Masukakan kata yang ingin dicari: ")
if fineWord in dbUser:
    print("data ditemukan")
    print(dbUser[fineWord])
else:
    print("Kata tidak ditemukan")    