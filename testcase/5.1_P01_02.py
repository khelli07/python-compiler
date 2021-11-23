# Program ...
# ...

# KAMUS
# a, b, c, d: integer
# r1, r2: real

# ALGORITMA

a = int(input("Masukkan nilai A: "))
b = int(input("Masukkan nilai B: "))
c = int(input("Masukkan nilai C: "))

d = (b ** 2) - (4 * a * c)

if d < 0:
	print("Tidak memiliki solusi riil.")
elif d == 0:
	r1 = ((b * -1) + (d ** (1/2))) / (2 * a)
	if int(r1) == r1:
		r1 = int(r1)
	print("Solusi dari persamaannya hanya satu, yaitu " + str(r1) + ".")
else: # d > 0
	r1 = ((b * -1) + (d ** (1/2))) / (2 * a)
	if int(r1) == r1:
		r1 = int(r1)
	r2 = ((b * -1) - (d ** (1/2))) / (2 * a)
	if int(r2) == r2:
		r2 = int(r2)
	print("Solusi dari persamaannya ada dua yaitu " + str(r1) + " dan " + str(r2) + ".")
