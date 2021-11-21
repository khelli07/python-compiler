# https://drive.google.com/file/d/12z0RZBZmvDpvErkNFct2ukRo-67MS5Ao/view

n = int(input("Masukkan banyak bilangan: "))
arr = [0 for i in range(n)]

for i in range(n):
	arr[i] = int(input("Masukkan nilai bilangan ke-" + str(i+1) + ": "))

bilpop = 0
for i in range(n-2):
	for j in range(i+1, n-1):
		for k in range(j+1, n):
			if (i == j + k) or (j == i + k) or (k == i + j):
				bilpop += 1

print("Terdapat", bilpop, "bilangan Populer.")