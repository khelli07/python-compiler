import os
from pycomp.cfg2cnf import run_converter
from pycomp.cyk_parser import run_parser
from pycomp.lexer import run_lexer

if __name__ == '__main__':
    folder_name = "testcase/"
    run_converter("database/CFG.txt", "database/CNF.txt")
    cnf_file = 'database/CNF.txt'

    listdir = os.listdir("testcase")
    for filename in listdir:
        filename = folder_name + filename
        file = open(filename, encoding="utf8")
        text = file.read()
        file.close()
        
        print(f"Checking {filename}...")
        text_by_line, tokenized_line = run_lexer(filename, text)
        run_parser(filename, cnf_file, text)