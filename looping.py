# LOOP STATEMENTS
# FOR LOOP DIGUNAKAN UNTUK MENJALANKAN OPERASI BERULANG-ULANG SELAMA SATU KONDISI TERPENUHI

# START 5 STOP 30 STEP 5
for i in range (5, 30, 5):
 print (i)

# START 0 STOP 5 STEP 1
for i in range (5):
 print("lOOPING!" + str(1))

#  BREAK CONTINUE 
# MENGHENTIKAN SEBUAH LOOP WALAUPUN MASIH BERJALAN
# ANGKA KELIPATAN 3 STOP 22
for i in range (3, 35, 3):
 if i == 21:
  break 
 print(i)

for i in range (10, 20, 3):
 if i == 13:
  continue
 
 print(i)

for i in range (1,11):
#   skip semua angka genap
  if i % 2 == 0:
    continue
  
  print(i)

for i in range (1,11):
# jika ia tidak habis dibagi 2
  if i % 2 != 0:
    continue
  
  print(i)

WHILE STATEMENTS
AKAB MENGEKSEKUSI PROGRAM SELAMA BERNILAI TRUE

nilai = 50

while(nilai < 70):
    print("Nilai sekarang: " + str(nilai))
    nilai += 5

UANG = 100

while(UANG > 0):
    print ("Masih punya uang : " + str(UANG))
    UANG -= 10

print("Saldo Tidak cukup!")

# Variabel
# while(variabel > Angka)
    # print(.....)
    # variabel -= Angka

 
