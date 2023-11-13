# Lambda Function
# Membuat sebuah function menjadi lebih singkat

def tambah5(nomer):
    total = nomer + 5
    return total

nomer = 10
tambahNomer5 = tambah5(nomer)
print(tambahNomer5)

tambah5 = lambda x: x+2
print(tambah5(5))