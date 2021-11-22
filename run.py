from pycomp.cfg2cnf import run_converter
from pycomp.cyk_parser import run_parser
from pycomp.lexer import run_lexer

if __name__ == '__main__':
    folder_name = "testcase/"
    run_converter("database/CFG.txt", "database/CNF.txt")
    cnf_file = 'database/CNF.txt'

    for i in range(1,10):
        filename = f"TC{i}.txt"
        file = open(folder_name + filename, encoding="utf8")
        text = file.read()
        file.close()
        
        print(f"Checking {filename}...")
        text_by_line, tokenized_line = run_lexer(filename, text)
        run_parser(filename, cnf_file, text)