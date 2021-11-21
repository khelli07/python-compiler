# =================== >>
# LEXER
# =================== >>
import sys, re
from database.token_db import token_rule
from pycomp.error import IllegalCharError, InvalidSyntaxError
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

    def __repr__(self):
        return f"In file {self.filename}, line: {self.line}, column: {self.col}"

    def copy(self):
        return Position(self.index, self.line, self.col, self.filename, self.filetext)

class Lexer:
    def __init__(self, filename, text):
        self.filename = filename
        self.text = text + "\n"
        self.pos = Position(0, 1, 0, filename, text)

    def tokenize(self, rules=token_rule):
        token_list = []
        tokenized_lines = []

        text_by_line = self.text.split("\n")
        col_incr = 0
        single_quote_comment = False; sq_token = ""
        double_quote_comment = False; dq_token = ""
        line = []
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
                        
                        if tag == "SQ_COMMENT":
                            single_quote_comment = not(single_quote_comment)
                            sq_token = token
                        elif tag == "DQ_COMMENT":
                            double_quote_comment = not(double_quote_comment)
                            dq_token = token
                        elif not(single_quote_comment or double_quote_comment):
                            token_list.append(token)
                            line.append(token)

                    break

            if tag == 'UNCATEGORIZED' and not(single_quote_comment or double_quote_comment): 
                error = IllegalCharError(pos_start, pos_end, f"Character not allowed",
                                        text_by_line[self.pos.line - 1])
                error.print_error()
                print(line)
                sys.exit(1)
            else:
                self.pos.col += col_incr
                self.pos.index = match.end(0)
                if (self.text[self.pos.index - 1] == '\n'):
                    if len(line) != 0:
                        tokenized_lines.append(line)
                        line = []
                    self.pos.col = 0
                    self.pos.line += 1

        # Kalau long comment belum selesai
        if single_quote_comment:
            error = InvalidSyntaxError(sq_token.pos_start, sq_token.pos_end, 
                                    f"EOF while scanning triple-quoted string literal",
                                    text_by_line[sq_token.pos_start.line - 1])
            error.print_error()
            sys.exit(1)
            
        # Kalau long comment belum selesai
        if double_quote_comment:
            error = InvalidSyntaxError(dq_token.pos_start, dq_token.pos_end, 
                                    f"EOF while scanning triple-quoted string literal",
                                    text_by_line[dq_token.pos_start.line - 1])
            error.print_error()
            sys.exit(1)

        
        return text_by_line, tokenized_lines

def run_lexer(filename, text):
    lx = Lexer(filename, text)
    return lx.tokenize()
