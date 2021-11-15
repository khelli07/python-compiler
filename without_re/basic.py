# =================== >>
# CONSTANTS
# =================== >>

DIGITS = "0123456789"
SPACE = ' '
TAB = "\t"
BLANK = [SPACE, TAB]

# =================== >>
# TOKENS
# =================== >>

TT_INT = "TT_INT"
TT_FLOAT = "FLOAT"
TT_PLUS = "PLUS"
TT_MINUS = "MINUS"
TT_MUL = "MUL"
TT_DIV = "DIV"
TT_LPAREN = "LPAREN"
TT_RPAREN = "RPAREN"
TT_EOF = "EOF"

class Token:
    def __init__(self, type_, value=None, pos_start=None, current_pos=None):
        self.type = type_
        self.value = value

        if pos_start: 
            self.pos_start = pos_start.copy()
            self.current_pos = pos_start.copy()
            self.current_pos.advance()
        if current_pos: 
            self.current_pos = current_pos

    def __repr__(self):
        if self.value:
            return f"{self.type}: {self.value}"
        else:
            return f"{self.type}"

# =================== >>
# ERRORS
# =================== >>

class Error:
    def __init__(self, pos_start, current_pos, name, message):
        self.pos_start = pos_start
        self.current_pos = current_pos
        self.name = name
        self.message = message

    def print_error(self):
        print((self.current_pos.col + 2) * SPACE + "^")
        print(f"{self.name} Error: {self.message}")
        print(f"File {self.pos_start.filename}, line {self.pos_start.line + 1}.")

class IllegalCharError(Error):
    def __init__(self, pos_start, current_pos, message):
        super().__init__(pos_start, current_pos, "Illegal Character", message)

class InvalidSyntaxError(Error):
    def __init__(self, pos_start, current_pos, message):
        super().__init__(pos_start, current_pos, "Invalid Syntax", message)


# =================== >>
# POSITION
# =================== >>

class Position:
    def __init__(self, index, line, col, filename, filetext):
        self.index = index 
        self.line = line 
        self.col = col
        self.filename = filename 
        self.filetext = filetext

    def advance(self, current_char=None):
        self.index += 1
        self.col += 1

        if current_char == "\n":
            self.line += 1
            self.col = 0

        return self

    def copy(self):
        return Position(self.index, self.line, self.col, self.filename, self.filetext)


# =================== >>
# LEXER
# =================== >>

class Lexer:
    def __init__(self, filename, text):
        self.filename = filename
        self.text = text
        self.pos = Position(-1, 0, -1, filename, text)
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos.advance(self.current_char)
        self.current_char = self.text[self.pos.index] \
                            if self.pos.index < len(self.text) \
                            else None

    def make_tokens(self):
        tokens = []

        while self.current_char != None:
            if self.current_char in BLANK:
                self.advance()
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())
            elif self.current_char == "+":
                tokens.append(Token(TT_PLUS, pos_start=self.pos))
                self.advance()
            elif self.current_char == "-":
                tokens.append(Token(TT_MINUS, pos_start=self.pos))
                self.advance()
            elif self.current_char == "*":
                tokens.append(Token(TT_MUL, pos_start=self.pos))
                self.advance()
            elif self.current_char == "/":
                tokens.append(Token(TT_DIV, pos_start=self.pos))
                self.advance()
            elif self.current_char == "(":
                tokens.append(Token(TT_LPAREN, pos_start=self.pos))
                self.advance()
            elif self.current_char == ")":
                tokens.append(Token(TT_RPAREN, pos_start=self.pos))
                self.advance()
            else:
                pos_start = self.pos.copy()
                char = self.current_char
                self.advance()
                return [], IllegalCharError(pos_start, self.pos, f"'{char}' not allowed.")
        
        tokens.append(Token(TT_EOF, pos_start=self.pos))
        return tokens, None

    def make_number(self):
        num_str = ""
        dot_ctr = 0
        pos_start = self.pos.copy()

        while self.current_char != None and self.current_char in DIGITS + '.':
            if self.current_char == ".":
                if dot_ctr == 1:
                    warn = Error("Only 1 dot is allowed in a number!")
                    warn.print_error()
                    break 
                else:
                    dot_ctr += 1
                    num_str = "."
            else:
                num_str += self.current_char
            self.advance()

        if dot_ctr == 0:
            return Token(TT_INT, int(num_str), pos_start, self.pos)
        else:
            return Token(TT_FLOAT, float(num_str), pos_start, self.pos)  

# =================== >>
# NODES
# =================== >>

class NumberNode:
    def __init__(self, token):
        self.token = token 

    def __repr__(self):
        return f"{self.token}"

class BinaryOpNode:
    def __init__(self, lnode, op_tok, rnode):
        self.lnode = lnode 
        self.op_tok = op_tok 
        self.rnode = rnode 

    def __repr__(self):
        return f"({self.lnode}, {self.op_tok}, {self.rnode})"

class UnaryOpNode:
    def __init__(self, op_tok, node):
        self.op_tok = op_tok 
        self.node = node

    def __repr__(self):
        return f"({self.op_tok}, {self.node})"

# =================== >>
# PARSER
# =================== >>

class ParseResult:
    def __init__(self):
        self.error = None 
        self.node = None 

    def register(self, res):
        if isinstance(res, ParseResult): 
            if res.error: self.error = res.error
            return res.node

        return res

    def success(self, node):
        self.node = node 
        return self 

    def failure(self, error):
        self.error = error 
        return self 

# =================== >>
# PARSER
# =================== >>

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens 
        self.tkn_idx = -1
        self.advance()

    def advance(self):
        self.tkn_idx += 1
        if self.tkn_idx < len(self.tokens):
            self.current_tkn = self.tokens[self.tkn_idx]
        return self.current_tkn

    # ================================ >> 

    def parse(self):
        res = self.expr()
        if not res.error and self.current_tkn.type != TT_EOF:
            return res.failure(InvalidSyntaxError(self.current_tkn.pos_start, self.current_tkn.current_pos, "Expected '+', '-', '*', or '/'"))
        return res

    def factor(self):
        res = ParseResult()
        token = self.current_tkn

        if token.type in (TT_PLUS, TT_MINUS):
            res.register(self.advance())
            factor = res.register(self.factor())
            if res.error: return res
            return res.success(UnaryOpNode(token, factor))

        elif token.type in (TT_INT, TT_FLOAT):
            res.register(self.advance())
            return res.success(NumberNode(token))
    
        elif token.type == TT_LPAREN:
            res.register(self.advance())
            expr = res.register(self.expr())
            if res.error: return res
            if self.current_tkn.type == TT_RPAREN:
                res.register(self.advance())
                return res.success(expr)
            else:
                return res.failure(InvalidSyntaxError(token.pos_start, token.current_pos, "Expected ')'."))

        return res.failure(InvalidSyntaxError(token.pos_start, token.current_pos, "Expected int or float."))

    def term(self):
        return self.binary_op(self.factor, (TT_MUL, TT_DIV))

    def expr(self):
        return self.binary_op(self.term, (TT_PLUS, TT_MINUS))

    def binary_op(self, func, ops):
        res = ParseResult()
        left = res.register(func())
        if res.error: return res

        while self.current_tkn.type in ops:
            op_tok = self.current_tkn
            res.register(self.advance())
            right = res.register(func())
            if res.error: return res
            left = BinaryOpNode(left, op_tok, right)

        return res.success(left)

# =================== >>
# RUN
# =================== >>

def run(filename, text):
    # Generate tokens
    lexer = Lexer(filename, text)
    tokens, error = lexer.make_tokens()
    if error: return None, error

    # Generate tree (AST)
    parser = Parser(tokens)
    ast = parser.parse()

    return ast.node, ast.error

