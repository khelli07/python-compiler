# NIM/Nama : ...
# Tanggal : ...
# Deskripsi : ...

# Program BalikUrutan
# Menerima N buah bilangan dan menuliskan kembali
# bilangan tersebut dengan urutan terbalik.

# KAMUS
# n,i : integer
# arr : array[1..n] of integer

# ALGORITMA

n = int(input("Masukkan N: "))
arr = [0 for i in range(n)]

# input elemen array
for i in range(n):
	arr[i] = int(input())

# balik
for i in range(n-1, -1, -1):
	print(arr[i])