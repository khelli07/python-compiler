# Program 01
# ...

# KAMUS
# a, b, c, n: integer

# ALGORITMA

n = int(input("Masukkan angka 3 digit: "))

a = n // 100
b = (n // 10) - (a * 10)
c = n % 10

if (a < b) & (b < c):
	print("Klasifikasi angka tersebut adalah angka dengan digit membesar.")
elif (a > b) & (a > c):
	print("Klasifikasi angka tersebut adalah angka dengan digit mengecil.")
else: # tidak beraturan
	print("Klasifikasi angka tersebut adalah angka dengan digit tidak beraturan.")