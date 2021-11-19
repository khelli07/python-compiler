# VARIABLE NAME CHECKER
# Cek apakah variabel diterima oleh Python menggunakan Finite Automata
# referensi: https://www.geeksforgeeks.org/designing-deterministic-finite-automata-set-1/

import re # kalo boleh

#########
# VarFA #
#########

class VarFA:
	def check(name):
		return VarFA.q0(name)

	def q0(name): # inital state
		# cek apakah huruf pertama adalah alfabet atau _
		if re.match("[a-zA-Z_]", name[0]):
			return VarFA.q1(name[1:])
		else:
			return VarFA.q3(name)

	def q1(name): 
		# huruf kedua, ketiga, dan seterusya berupa alphanumeric
		if name == "":
			return VarFA.q2(name)
		elif re.match("[a-zA-Z0-9_]", name[0]):
			return VarFA.q1(name[1:])
		else:
			return VarFA.q3(name)

	def q2(name): # final state
		return True

	def q3(name): # dead state
		return False

################
# Main Program #
################

s = input("Nama variabel: ")
if VarFA.check(s):
	print("A valid variable name")
else:
	print("Not a valid variable name")