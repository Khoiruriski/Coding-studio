# STRING 
# DAPAT DIDEKLARASIKAN MENGGUNAKAN TANDA PETIK SATU ('')
# CONTOH : 'PYTON' & "PYTON"

NIM ="22051204135"
Nama = 'Adam'
print(Nama + " Memiliki NIM " + NIM)

# ESCAPE CHARACTER (\"  A  \")
# BERFUNGSI UNTUK MENYISIPKAN KARAKTER ILEGAL DALAM SEBUAH STRING

print("\"SELAMAT DATANG DI BELAJAR PYTON ADAM !\"")
print("\"SELAMAT DATANG DI \"BELAJAR PYTON\" ADAM !\"")

#  STRING METHODS 
text = "Belajar Pyton"

print(text.capitalize())
print(text.title())
print(text.upper())
print(text.lower())
print(text.split(' '))
print(text.index('a'))
print(len(text))

# SLICING STRINGS
# BERGUNA UNTUK MENGEMBALIKAN KARAKTER Yang BERADA DALAM RENTANGINDEKS YANG DIBERIKAN

print(text[:])
print(text[0])
print(text[:5])
print(text[-1])

# STRING CONCATENATION
# MENGGABUNGKAN DUA BUAH STRING KITA MENGGUNAKAN SYNTAX +
x = "SELAMAT DATANG"
y = " ADAM !"
print(x + y)
print(x + " " + y)
print(x + " " + y + " " + str(100))

# STRING FORMAT
# UNTUK MENGGABUNGKAN STRING DAN ANGKA MENGGUNAKAN format()

mangga = 5
apel = 7
pisang = 4
text = "adam memberi {} mangga, {} apel, dan {} pisang."
print(text.format(mangga,apel, pisang))

# In VS Not IN
# KITA DAPAT MEMERIKSA SEBUAH SUBSTRING ADA DALAM STRING APA TIDAK
text1 = "Coding Studio"
print("Studio" in text1)
print("Code" in text1)

penutupan = "Tugas selesai ! Selamat Beristirahat Tuan :)"
print(penutupan)