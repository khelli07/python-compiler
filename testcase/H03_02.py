# NIM/Nama : ...
# Tanggal : ...
# Deskripsi : ...

# Program IsAnagram
# Mengecek apakah array A dan B merupakan anagram,
# Dengan asumsi tiap elemen pada array A dan B 
# merupakan bilangan positif dengan nilai maksimal 10 (1 <= ai <= 10)

# KAMUS
# na, nb, i : integer
# arr_a : array[1..na] of integer
# arr_b : array[1..nb] of integer
# freq_a, freq_b : array[1..10] of integer
# same : boolean

# ALGORITMA

# inisialisasi tabel frekuensi
freq_a = [0 for i in range(10)]
freq_b = [0 for i in range(10)]

# input array A
na = int(input("Masukkan banyaknya elemen A: "))
arr_a = [0 for i in range(na)]
for i in range(na):
	arr_a[i] = int(input("Masukkan banyaknya elemen A ke-" + str(i+1) + ": "))
	freq_a[arr_a[i]-1] += 1

# input array B
nb = int(input("Masukkan banyaknya elemen B: "))
arr_b=[0 for i in range(nb)]
for i in range(nb):
	arr_b[i]=int(input("Masukkan banyaknya elemen B ke-" + str(i+1) + ": "))
	freq_b[arr_b[i]-1] += 1

# cek kesamaan tabel frekuensi
# arr_b anagram dari arr_a jika freq_a == freq_b
i = 0
isAnagram = True
while isAnagram and (i < 10): # cek masing-masing elemen
	if freq_a[i] != freq_b[i]:
		isAnagram = False
	else:
		i += 1

if isAnagram:
	print("B adalah anagram dari A")
else:
	print("B bukan anagram dari A")