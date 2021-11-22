# NIM/Nama : ...
# Tanggal : ...
# Deskripsi : ...

# Program IsPalindrome
# Menerima sebuah string dan menuliskan apakah
# string tersebut palindrom

# KAMUS
# n, i: integer
# s: string
# isPalindrome: boolean

# ALGORITMA

n = int(input("Masukkan panjang string: "))
s = input("Masukkan string: ")

i = 0
isPalindrome = True
while isPalindrome and (i < (n // 2)):
	if s[i] != s[n-i-1]:
		isPalindrome = False
	else:
		i += 1

if isPalindrome:
    print(s + " adalah palindrom")
else:
    print(s + " bukan palindrom")
