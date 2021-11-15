import sys
from typing import Text
from lexer import *

if __name__ == '__main__':
    filename = sys.argv[1]
    file = open(filename)
    text = file.read()
    file.close()
    tokens = run_lexer(filename, text)
    for token in tokens:
        print(token)