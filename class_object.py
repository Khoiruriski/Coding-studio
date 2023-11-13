# CLASS 
# Sebuah Class merupakan blueprint untk membuat object

class Manusia :
    nama = "Adam"

obj = Manusia() #Object
print(type(obj))
print(obj.nama)

class Angka:
    jumlah = 5

a = Angka()
print(a.jumlah)

# __init__()
# Mendeklarasikan property yang berbeda yang dimiliki oleh sebuah class

class Person:
    # Membuat Function dalam sebuah kelas
    def __init__(self, name, age, nilai):
        self.name = name
        self.age = age
        self. nilai = nilai
    
    def salam(self):
        print("Halo, " + self.name + "!")

p1 = Person("Adam", 20,95)
p2 = Person("Hawa", 19,93)

p1.salam()
p2.salam()

# print(p1.name)
# print(p1.__dict__) #Semua properti di print Terdiri dari key : Value
# print(p2.__dict__)

class Hewan: #Parent Class
    def __init__ (self,nama,Jenis) :
        self.nama = nama
        self.Jenis = Jenis
    def salam(self) :
        print("hello world")

class kucing (Hewan) : #Child Class
    def __init__ (self,nama,Jenis,warna,umur):
        #Super mengacu pada class animal
        super().__init__(nama,Jenis)
        self.warna = warna
        self.umur = umur

class anjing :
    def __init__ (self,nama,Jenis,warna,tinggi):
        super().__init__(nama,Jenis)
        self.warna = warna
        self.tinggi = tinggi

garfield = kucing()