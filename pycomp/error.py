# =================== >>
# ERROR
# =================== >>
from database.token_db import SPACE
from pycomp.utils import get_token, count_length

class Error:
    def __init__(self, name, pos_start, pos_end, message, txtline):
        self.name = name
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.message = message
        self.txtline = txtline

    def print_error(self):
        print(f"In file {self.pos_start.filename}, line {self.pos_start.line}.")
        print(self.txtline)
        print(SPACE * (self.pos_start.col) + '^')
        print(f"{self.name} Error: {self.message}")
        # print(SPACE * (self.pos_start.col) + '^' * (self.pos_end.col - self.pos_start.col))

class IllegalCharError(Error):
    def __init__(self, pos_start, pos_end, message, txtline):
        super().__init__("Illegal Character", pos_start, pos_end, message, txtline)

class InvalidSyntaxError(Error):
    def __init__(self, pos_start, pos_end, message, txtline):
        super().__init__("Syntax", pos_start, pos_end, message, txtline)

def get_error(name, line, message, text_by_line):
    token = get_token(name, line)
    pos_start = token.pos_start.copy()
    pos_end = token.pos_end.copy()
    pos_end.col += count_length(name)

    error = InvalidSyntaxError(pos_start, pos_end, message,
                            text_by_line[token.pos_start.line - 1])
    
    return error