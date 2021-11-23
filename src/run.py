import os
import re
from algorithm.CFG2CNF import CFG2CNF
from algorithm.CYK_Parser import cyk_parser as parser

filename = input("Input file name: ")
file = open("../test/" + filename, 'r')
text = file.read()

