# FUNCTION
# (Kumpulan code Untuk memanggil kumpulan kode sebelumnya untuk digunakan kembali dalam suatu program)

# SYNTAX
# Function Name : Nama dari Function
# Argument : Nilai yang di erikan ke function
# Function Body :Isi dari sebuah Function
# Return value : Hasil yang dikembalikan oleh function

# CREATE AND CALL (Def)
# Untuk membuat sebuah fungsi

# def halo():
#     print("Hello, Adam!")
#     print("Nice to meet You !")

# halo()

# PASSING ARGUMEN
# Untuk memasukkan argumen pada fungsi

# Parameter nama,umur
def halo(nama, umur):
    print("Hello "+ nama)
    print("Kamu sekarang umur " + str(umur) + " tahun")
    print("Nice to meet You " + nama)
    
# Argumen = "adam",20
halo("Adam",20)
