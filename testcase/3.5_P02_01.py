n = int(input("Masukkan bilangan N: "))

i = n
jmlbil = 0
while(i > 0):
	jmlbil += i % 10
	i = i // 10

print(jmlbil)