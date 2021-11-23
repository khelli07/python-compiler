# Program KalkulatorSederhana
# Menerima 2 buah angka dan sebuah karakter operasi, 
# dan menuliskan hasil perhitungannya.
# Operator yang diterima adalah + (tambah), - (kurang), * (kali), 
# / (bagi,dibulatkan ke bawah), % (sisa bagi).

# KAMUS
# a, b, c: integer
# op: char

# ALGORITMA

# input
a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))
op = input("Masukkan operator: ")

# proses operasi bilangan
if op == '+':
	c = a + b
	print(a, op, "=", c)
elif op == '-':
	c = a - b
	print(a, op, "=", c)
elif op == '*':
	c = a * b
	print(a, op, "=", c)
elif op == '/':
	if b == 0:
		print("Error.")
	else:
		c = a // b
		print(a, op, "=", c)
else: # op = "%"
	c = a % b
	print(a, op, "=", c)
