# #                            BOOLEAN

# x = 5
# y = 10
# z = 15
# print((x < y)) 

#  NOT 
# print(not(x > y))
# print((x < y))

# # AND
# print(x < y and y > z)
# print(x < y or y > z)
# # x < y = 5 < 10 = True (statement 1)
# y > z = 10 > 15 = False (statement 2)
# Statement 1 AND Statement 2 = True and False = Fa
# Statement 1 OR Statement 2 = True and False = True

#IF ELSE ELIF

# a = 10
# b = 15
# # c = input("MASUKKAN ANGKA PERTAMA : ")
# # d = input("MASUKKAN ANGKA KEDUA : ")

# # print ("ANGKA PERTAMA ADALAH " + str(c) + " ANGKA KEDUA ADALAH " + str(d))
# if (c == d and c < d): #true
#     print("Angka pertama sama dengan kedua")
# else:
#     print("Angka pertama tidak sama dengan kedua")
# if c < d: #True
#     print("Angka pertama Kurang dari kedua")
# else:
#     print("Angka pertama  tidak Kurang dari kedua") 
# if c > d: #True
#     print("Angka pertama Lebih dari kedua")
# else:
#     print("Angka pertama tidak Lebih dari kedua")

# STATEMENTS 3

a = input(" A = ") 
b = input(" B = ") 

print("Input Angka A = " + str(a) + " input angka B = " + str(b))
if a > b:
    print("A Lebih Besar Dari B")
elif a == b:
    print( "A sama dengan B")
else:
    print ("B lebih besar dari A")

