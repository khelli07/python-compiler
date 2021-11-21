# Program isPosNeg
# Menentukan apakah sebuah bilangan adalah bilangan positif, negatif, atau nol. 
# Khusus untuk bilangan positif, tuliskan juga apakah ganjil atau genap.

# KAMUS
# x: integer

# ALGORITMA

x = int(input("Masukkan X: "))
if x > 0: # cek nilai x
	if x % 2 == 0:
		print("X adalah bilangan positif genap")
	else:
		print("X adalah bilangan positif ganjil")
elif x == 0:
	print("X adalah bilangan nol")
else: # x < 0
	print("X adalah bilangan negatif")