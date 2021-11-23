import os
import re
from algorithm.CFG2CNF import CFG2CNF
from algorithm.CYK_Parser import cyk_parser

#############
#   TOKEN   #
#############

class Token(object):
	def __init__(self, type, val):
		self.type = type
		self.val = val

	def __str__(self):
		if self.val:
			return f'<{self.type}:{self.val}>'
		else:
			return f'<{self.type}>'

#######################
#   LEXER/TOKENIZER   #
#######################

class LexerError(Exception):
	def __init__(self, pos):
		self.pos = pos

class Lexer(object):
    def __init__(self, rules, skip_whitespace=True):
        idx = 1