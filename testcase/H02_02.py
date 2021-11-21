# NIM/Nama : ...
# Tanggal : ...
# Deskripsi : ...

# Program Nearest10x
# Menerima bilangan N dan menuliskan 
# bilangan 10^x terkecil yang lebih dari N

# KAMUS
# x, i, n: integer

# ALGORITMA
n = int(input("Masukkan N: "))
x = 1
while x <= n:
	x *= 10
print(x)