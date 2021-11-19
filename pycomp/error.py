# =================== >>
# ERROR
# =================== >>
from database.token_db import SPACE

class Error:
    def __init__(self, name, pos_start, pos_end, message, txtline):
        self.name = name
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.message = message
        self.txtline = txtline

    def print_error(self):
        print(f"{self.name} Error: {self.message}")
        print(f"File {self.pos_start.filename}, line {self.pos_start.line + 1}.")
        print(self.txtline)
        print(SPACE * (self.pos_start.col) + '^' * (self.pos_end.col - self.pos_start.col))

class IllegalCharError(Error):
    def __init__(self, pos_start, pos_end, message, txtline):
        super().__init__("Illegal Character", pos_start, pos_end, message, txtline)

class InvalidSyntaxError(Error):
    def __init__(self, pos_start, pos_end, message, txtline):
        super().__init__("Invalid Syntax", pos_start, pos_end, message, txtline)
