# =================== >>
# LEXER
# =================== >>
import sys, re
from database.token_db import token_rule, BRACKETS
from pycomp.error import IllegalCharError, InvalidSyntaxError
from pycomp.utils import count_length, is_bracket_match

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
        return f"In file {self.filename}, line: {self.line}"

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
        
        bracket_stack = []
        
        sq_comment = False; sq_token = ""
        dq_comment = False; dq_token = ""
        eof_error = False
        
        line = []
        col_incr = 0
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
                        
                        # Handle comment
                        if tag == 'SQ_COMMENT':
                            sq_comment = not(sq_comment)
                            sq_token = token
                        elif tag == 'DQ_COMMENT':
                            dq_comment = not(dq_comment)
                            dq_token = token
                        elif not(sq_comment or dq_comment):
                            # Handle bracket
                            if tag in BRACKETS:
                                if (len(bracket_stack) == 0):
                                    bracket_stack.append(token)
                                else:
                                    stack_top = bracket_stack[-1]
                                    if is_bracket_match(stack_top.tag, tag):
                                        bracket_stack.pop()
                                    else:
                                        bracket_stack.append(token)

                            token_list.append(token)
                            line.append(token)
                    break

            if tag == 'UNCATEGORIZED' and not(sq_comment or dq_comment):
                if tag == 'UNCATEGORIZED': 
                    error = IllegalCharError(pos_start, pos_end, "Character not allowed",
                                            text_by_line[self.pos.line - 1])
                    error.print_error()
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

        if sq_comment or dq_comment:
            if sq_comment: error_token = sq_token
            elif dq_token: error_token = dq_token
            message = "EOF while scanning triple-quoted string literal"
            eof_error = True
        elif len(bracket_stack) != 0:
            error_token = bracket_stack.pop()
            if error_token.tag in ['LP', 'LSB', 'LCB']:
                message = f"Did you forget to close the bracket? Unmatched '{error_token.value}'"
            elif error_token.tag in ['RP', 'RSB', 'RCB']:
                message = f"Did you forget to open the bracket? Unmatched '{error_token.value}'"
            eof_error = True

        if (eof_error):
            error = InvalidSyntaxError(error_token.pos_start, error_token.pos_end, message,
                        text_by_line[error_token.pos_start.line - 1])
            error.print_error()
            sys.exit(1)           

        return text_by_line, tokenized_lines

def run_lexer(filename, text):
    lx = Lexer(filename, text)
    return lx.tokenize()
