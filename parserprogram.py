# lewat argumen

from src.pycomp.CFG2CNF import run_converter
from src.pycomp.cyk_parser import run_parser
from src.pycomp.lexer import run_lexer

import os
import sys
import argparse

filename = sys.argv[1]
print(filename)

run_converter("src/database/CFG.txt", "src/database/CNF.txt")
cnf_file = 'src/database/CNF.txt'

file = open(filename, encoding="utf8")
text = file.read()
file.close()

print(f"Checking {filename}...")
text_by_line, tokenized_line = run_lexer(filename, text)
run_parser(filename, cnf_file, text)
