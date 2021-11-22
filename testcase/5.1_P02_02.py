n = int(input("Masukkan nilai N: "))
maxvol = 0
for i in range(n):
	p = int(input("Masukkan panjang balok " + str(i+1) + ": "))
	l = int(input("Masukkan lebar balok " + str(i+1) + ": "))
	t = int(input("Masukkan tinggi balok " + str(i+1) + ": "))
	if (p * l * t) > maxvol:
		maxvol = p * l * t

print("Volume terbesar balok adalah", maxvol, "meter kubik.")
