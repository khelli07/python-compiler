# NIM/Nama : ...
# Tanggal : ...
# Deskripsi : ...

# Program IsPrime
# Menerima bilangan N dan menentukan
# apakah X adalah bilangan prima

# KAMUS
# i, x: integer
# isPrime: boolean

# ALGORITMA
isPrime = True
x = int(input("Masukkan X: "))
for i in range(2, x):
    if x % i == 0:
        isPrime = False

if isPrime:
    print(x, "adalah bilangan prima")
else:
    print(x, "bukan bilangan prima")
