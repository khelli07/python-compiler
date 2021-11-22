# Program JuaraBola
# ...

# KAMUS
# a, b, r, d, k: integer

# ALGORITMA

r = 0
d = 0
k = 0

print("Pertandingan Tim Ric vs Tim Dip")
a = int(input("Banyak bola yang dimasukkan Tim Ric: "))
b = int(input("Banyak bola yang dimasukkan Tim Dip: "))
if a > b: # tim Ric lebih banyak
	r += 1
elif a == b: # dua-duanya menang
	r += 1
	d += 1
else: # a < b, tim Dip lebih banyak
	d += 1

print("Pertandingan Tim Ric vs Tim Kil")
a = int(input("Banyak bola yang dimasukkan Tim Ric: "))
b = int(input("Banyak bola yang dimasukkan Tim Kil: "))
if a > b:  # tim Ric lebih banyak
	r += 1
elif a == b:  # dua-duanya menang
	r += 1
	k += 1
else:  # a < b, tim Kil lebih banyak
	k += 1

print("Pertandingan Tim Dip vs Tim Kil")
a = int(input("Banyak bola yang dimasukkan Tim Dip: "))
b = int(input("Banyak bola yang dimasukkan Tim Kil: "))
if a > b:  # tim Dip lebih banyak
	d += 1
elif a == b:  # dua-duanya menang
	d += 1
	k += 1
else:  # a < b, tim Kil lebih banyak
	k += 1

if (r > k) & (r > d):
	print("Tim Ric yang memenangkan lomba.")
elif (k > r) & (k > d):
	print("Tim Kil  yang memenangkan lomba.")
elif (d > r) & (d > k):
	print("Tim Dip  yang memenangkan lomba.")
else:
	print("Tidak ada yang memenangkan lomba.")