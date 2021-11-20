import sys
from pycomp.cyk_parser import run_parser
from pycomp.lexer import run_lexer

if __name__ == '__main__':
    filename = sys.argv[1]
    file = open(filename)
    text = file.read()
    file.close()
    
    cnf_file = 'database/CNF.txt'
    token_list, tokenized_line = run_lexer(filename, text)
    run_parser(filename, cnf_file, text)