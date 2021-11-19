from stack import Stack

#########
# TOKEN #
#########

# Token terdiri dari:
# type, jenis token apakah simbol
# value, nilai token, jika num

class Token:
	### constructor ###
	def __init__(self, type, value=None):
		self.type = type
		self.value = value

	### representasi sebagai string ###
	def __repr__(self):
		if self.value: return f'{self.type}:{self.value}'
		return f'{self.type}'


	#### PRIMITIF ####

	# Mengembalikan token yang sesuai dengan jenis simbol.
	def to_token(x):
		if x == '(':
			return "L_PARENT"
		elif x == ')':
			return "R_PARENT"
		elif x == '[':
			return "L_BOXBRACKETS"
		elif x == ']':
			return "R_BOXBRACKETS"
		elif x == '{':
			return "L_BRACES"
		elif x == '}':
			return "R_BRACES"
		elif x == '<':
			return "L_ANGLEBRACKETS"
		elif x == '>':
			return "R_ANGLEBRACKETS"
		else:
			return "INVALID_TOKEN"
	
	# Mengembalikan list of token dari string s
	def tokenize(s):
		# if s == "":
		# 	return None
		# else:
		# 	return Token.tokenize(s[0]).append(Token.tokenize(s[1:]))
		tokenList = []
		for i in s:
			tokenList.append(Token.to_token(i))
		return tokenList

	# Mengembalikan True jika token bracket x dan y berpasangan
	# dengan syarat x kurung buka dan y kurung tutup
	# Contoh: isTokenMatching("L_BRACES", "R_BRACES") = True
	def isBracketMatching(x, y):
		return (x[1:] == y[1:]) and (x[0] == 'L') and (y[0] == 'R')
	
	# Validasi bracket dalam tokenList
	# mengembalikan indeks di mana brackets tidak valid. 
	def isBracketsValid(tokenList):
		bracketStack = []
		i = 0 # increment indeks tokenList
		isValid = True
		while isValid and (i < len(tokenList)):
			if tokenList[i] != "INVALID_TOKEN":
				if tokenList[i][0] == 'L':
					Stack.push(bracketStack, tokenList[i])
					i += 1
				else: # tokenlist awalan 'R'
					if Token.isBracketMatching(Stack.top(bracketStack), tokenList[i]):
						Stack.pop(bracketStack)
						i += 1
					else:
						isValid = False
			else:
				isValid = False
		if isValid and Stack.isEmpty(bracketStack):
			return -1
		else:
			return i

	def validateBrackets(s):
		return Token.isBracketsValid(Token.tokenize(s))