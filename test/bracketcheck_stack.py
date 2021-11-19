# BRACKET PARSER
# Mem-parse bracket, keknya bukan masuk ke implementasi parse tree idk
# Yang jelas ini implementasi stack hhe

from token import Token

s = input("Masukkan kumpulan bracket: ")
x = Token.validateBrackets(s)

if x < 0:
	print("Brackets valid.")
else:
	print("Brackets tidak valid!")
	print(s)
	while(x > 0): # print panah di tempat token invalid
		print(" ", end="")
		x -= 1
	print("^")