# VARIABLE NAME CHECKER
# Cek apakah variabel diterima oleh Python menggunakan Finite Automata
# referensi: https://www.geeksforgeeks.org/designing-deterministic-finite-automata-set-1/

#########
# VarFA #
#########

# diterima oleh FA jika VarFA.check(s) = True

from database.token_db import DIGITS, ALPHA

class VarFA:
	def check(name):
		return VarFA.q0(name)

	def q0(name):  # inital state
		# cek apakah huruf pertama adalah alfabet atau _
		if name[0] in ALPHA or name[0] in ALPHA.upper() or name[0] == '_':
			return VarFA.q1(name[1:])
		else:
			return VarFA.q3()

	def q1(name): # cek huruf kedua, ketiga, dan seterusya berupa alphanumeric
		if name == "":
			return VarFA.q2()
		elif name[0] in ALPHA or name[0] in ALPHA.upper() or name[0] in DIGITS or name[0] == '_':
			return VarFA.q1(name[1:])
		else:
			return VarFA.q3()

	def q2(): # final state, kalo diterima
		return True

	def q3(): # dead state(?)
		return False