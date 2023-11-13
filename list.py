# #LIST
# # LIST ADALAH SEBUAH KOLEKSI YANG TERURUT DAN DAPAT DIGANTI
# # LIST BISA MENAMPUNG ELEMEN DUPLIKAT

# listexample = ['Adam',13,23.5,True,45]
# print(listexample[0])
# print(listexample[1:4])
# print(listexample[-1])
# print(listexample)

# # List Operations (CRUD)

# # Create data (append,insert)
# listitem = [54,'Pyton',3,85,50]
# listitem.insert(1,'Data Dcience')
# listitem.append("Javascript")
# print(listitem)

# # Read data
# listangka = [40,55,20,75,85]
# if 40 in listangka:
#    print('Terdapat angka 40 dalam list')
#    length = len(listangka)
#    print(length)

# # Update data
# listangka = [40,55,20,75,85]
# for item in listangka:
#     if item % 2 == 0:
#      print(item)

# # Delete Data (remove,pop,del,clear)
# listitem = [54,'Pyton',3,85,50]
# print(listitem)
# listitem.remove('Pyton') #Spesifik Nulis
# listitem.pop() #Mengambil dan menghapus elemen terakhir
# del listitem[2] #Spesifik
# listitem.clear() #Keseluruhan
# print(listitem)

# COPY 
# listangka = [40,55,20,75,85]
# listangka2 = listangka.copy()
# listangka2[0] = 100
# print(listangka)
# print(listangka2)

#CONCAT (+ dan extend)t

listangka = [40,55,20,75,85]
listangka2 = [70,100]
listangka.extend(listangka2) #Masukkan List 2 ke List 1
print(listangka)

# INDEX
listangka = [40,55,20,75,85]
print(listangka.index(75))

# SORT
listangka = [40,55,20,75,85]
listangka.sort() #Mensorstir Elemen
print(listangka)

# REVERSE

listangka = [40,55,20,75,85]
listangka.reverse() #Membalik elemen depan ke belakang
print(listangka)