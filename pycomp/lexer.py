import sys
import re
from database.token_db import token_expr

class Token:
    def __init__(self, tag, value=None, pos_start=None, current_pos=None):
        self.tag = tag
        self.value = value

        if pos_start: 
            self.pos_start = pos_start.copy()
            self.current_pos = pos_start.copy()
        if current_pos: 
            self.current_pos = current_pos

    def __repr__(self):
        if self.value:
            return f"{self.type}: {self.value}"
        else:
            return f"{self.type}"

class Position:
    def __init__(self, index, line, col, filename, filetext):
        self.index = index 
        self.line = line 
        self.col = col
        self.filename = filename 
        self.filetext = filetext

    def copy(self):
        return Position(self.index, self.line, self.col, self.filename, self.filetext)

class Lexer:
    def __init__(self, filename, text):
        self.filename = filename
        self.text = text
        self.pos = Position(0, 1, 0, filename, text)

    def tokenize(self, rules=token_expr):
        col_incr = 0
        tokens = []
        text_by_lines = self.text.split("\n")
        while self.pos.index < len(self.text):
            match = None
            for rule in rules:
                pattern, tag = rule
                regex = re.compile(pattern)
                match = regex.match(self.text, self.pos.index)
                if match:
                    string = match.group(0)
                    col_incr = len(string)
                    if tag:
                        token = (string, tag)
                        tokens.append(token)
                    break 

            if not match: 
                sys.stderr.write(f"Lexical Error: illegal character '{self.text[self.pos.index]}'\n")
                sys.stderr.write(f"pos: {self.pos.index}, col: {self.pos.col}, line: {self.pos.line}\n")
                sys.stderr.write(f"{text_by_lines[self.pos.line - 1]}\n")
                sys.stderr.write(" " * (self.pos.col) + "^")
                sys.exit(1)
            else:
                self.pos.col += col_incr
                self.pos.index = match.end(0)
                if (self.text[self.pos.index - 1] == '\n'):
                    self.pos.col = 0
                    self.pos.line += 1

        return tokens

def run_lexer(filename, text):
    lx = Lexer(filename, text)

    return lx.tokenize()
