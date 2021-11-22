n = int(input("Masukkan nilai N (dalam derajat) = "))

for jam in range(12):
	for menit in range(60):
		# hitung tambahan pergerakan jam
		e = menit // 12
		# hitung total selisih derajat
		if (jam * 30 + e * 6 < menit * 6):
			derajat = menit * 6 - (jam * 30 + e * 6)
		else:
			derajat = jam * 30 + e * 6 - menit * 6
		# reflektif
		if derajat > 180:
			derajat = 360 - derajat
		# output
		if derajat == n:
			if jam < 10:
				print("0", end="")
			print(str(jam) + ":", end="")
			if menit < 10:
				print("0", end="")
			print(str(menit))
