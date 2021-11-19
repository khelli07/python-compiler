# =================== >>
# LEXER
# =================== >>
import sys, re
from database.token_db import token_rule
from pycomp.error import Error
from pycomp.utils import count_length

class Token:
    def __init__(self, tag, value=None, pos_start=None, pos_end=None):
        self.tag = tag
        self.value = value

        if pos_start: 
            self.pos_start = pos_start.copy()
            self.pos_end = pos_start.copy()
        if pos_end: 
            self.pos_end = pos_end

    def __repr__(self):
        return f"[{self.tag}: {self.value}]"

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

    def tokenize(self, rules=token_rule):
        tokens = []

        text_by_lines = self.text.split("\n")
        col_incr = 0
        isComment = False
        while self.pos.index < len(self.text):
            match = None
            for rule in rules:
                pattern, tag = rule
                regex = re.compile(pattern)
                match = regex.match(self.text, self.pos.index)
                if match:
                    string = match.group(0)
                    col_incr = count_length(string)
                    if tag:
                        pos_start = self.pos.copy()
                        pos_end = self.pos.copy()
                        pos_end.col += count_length(string)
                        token = Token(tag, string, pos_start, pos_end)
                        tokens.append(token)
                        if tag in ('SQ_COMMENT', 'DQ_COMMENT'):
                            isComment = not(isComment)
                    break

            if tag == 'UNCATEGORIZED' and not(isComment): 
                error = Error("Illegal Character", pos_start, pos_end,
                            f"Character not allowed", text_by_lines[self.pos.line - 1])
                error.print_error()
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
