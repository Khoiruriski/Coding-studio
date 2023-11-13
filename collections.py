#TUPLE (Tidak bisa diubah)
# Kalo list menggunakan '[]' kalo tuple menggunakan '()'
tupleExample = (2,3,'Pyton',True,50)
# print(tupleExample)
# # tupleExample[0] = 4
print(tupleExample[-2])

# DICTIONARY (Menyimpan data dalam bentuk key : value)
# Format var = {identity}
customer = {
    "id" : 100,
    "nama" : "adam",
    "umur" : 23
}
# Add Key
customer["pekerjaan"] = "Programmer"
# metdhod
customer.pop("umur")
# Dictionary ga punya indeks punyanya key
print(customer)
print(customer["nama"])
# print(customer["umur"])

# SET (Kumpulan elemen unik yang tidak memiliki urutan)
# Union (Gabungan)
numbers1 = {1,3,5,8,7,10}
numbers2 = {1,2,3,4,6,8,11}
# Union (Gabungan)
numbersUnion = numbers1.union(numbers2)
# Difference (Perbedaan)
difference1 = numbers1.difference(numbers2)
# Intersection (Irisan)
intersection1 = numbers1.intersection(numbers2)
# Syimetric Difference (Kebalikan irisan)
SymDifference = numbers1.symmetric_difference(numbers2)

# {1, 2, 3, 4, 5, 6, 7, 8, 10, 11}
print(numbersUnion)
# {10, 5, 7}
print(difference1)
# {8, 1, 3}
print(intersection1)
# {2, 4, 5, 6, 7, 10, 11}
print(SymDifference)

print('Hello world')