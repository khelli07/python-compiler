# PROGRAM

# KAMUS

# ALGORITMA

n = int(input("Masukkan banyak elemen: "))
arr = [0 for i in range(n)]

for i in range(n):
	arr[i] = int(input("Masukkan elemen ke-" + str(i+1) + ": "))
	
for i in range(n-1, 0, -1):
	if arr[i] < arr[i-1]:
		arr[i] += arr[i-1]
	elif arr[i] > arr[i-1]:
		arr[i] -= arr[i-1]

print("Hasil akhir:")
for i in range(n):
	print(arr[i], end=" ")