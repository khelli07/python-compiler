# NIM/Nama : ...
# Tanggal : ...
# Deskripsi : ...

# Program CounttoN
# Menerima bilangan N dan menuliskan 1 sampai N

# KAMUS
# i, n: integer

# ALGORITMA
n = int(input("Masukkan N: "))
for i in range(1, n+1):
    print(i, end="")
    if i != n:
        print(" ", end="")
