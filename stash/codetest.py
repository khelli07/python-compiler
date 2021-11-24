import itertools, sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'python-compiler')))
from pycomp.cfg2cnf import grammar_to_list
from pycomp.cyk_parser import subs_grammar

'''
This code is a tester for Cocke-Younger-Kasami Algorithm
The token sample is taken from Wikipedia.
'''
# CNF
grammar_list = grammar_to_list("./stash/CNF_Wiki.txt")

# Take sample token
sample_token = "SHE EATS A FISH WITH A FORK"
token_list = ["'" + token + "'" for token in sample_token.split(" ")]
print(token_list)
length = len(token_list)

cyk_table = [[[] for _ in range(length)] for _ in range(length)]

for i in range(length):
    for j in range(length - i):
        if (i == 0):
            for grammar in grammar_list:
                if (len(grammar) == 2) and (grammar[1] == token_list[j]):
                    cyk_table[i][j].append(grammar[0])
        else:
            lprod = []
            x = 0; y = j + 1
            while (x != i):
                cartesian_prod = list(itertools.product(cyk_table[x][j], cyk_table[i - x - 1][y]))
                lprod.extend(cartesian_prod)
                x += 1
                y += 1
            
            union = []
            for production in lprod:
                subs_grammar(union, production, grammar_list)
            cyk_table[i][j] = [var for var in set(union)]

for i in range(length - 1, -1, -1):
    for j in range(length):
        print(f"{cyk_table[i][j]}", end="  ")
    print()

'''
        text_by_line = self.text.split("\n")
        quote_stack = []

        state = 'q0'
        while self.pos.index < len(self.text):
            current_char = self.text[self.pos.index]
            if (current_char == "\n"):
                state = 'q0'
                self.pos.line += 1
                self.pos.col = -1
            elif (current_char in ['\t', ' ']):
                state = 'q0'
            elif (current_char in QUOTES):
                if (len(quote_stack) == 0):
                    quote_stack.append(current_char)
                else:
                    top_stack = quote_stack[-1]
                    if (top_stack == current_char):
                        quote_stack.pop()
                    else:
                        quote_stack.append(current_char)

            elif len(quote_stack) == 0: # Means not in string
                if current_char in DIGITS:
                    state = 'q1'
                elif current_char in ALPHA or current_char in ALPHA.upper():
                    if state == 'q1':
                        state = 'q2'
                        error = InvalidSyntaxError(self.pos, self.pos,
                                        f"Invalid variable name", text_by_line[self.pos.line - 1])
                        error.print_error()
                        sys.exit(1)
                else:
                    state = 'q0'

            self.pos.index += 1
            self.pos.col += 1

        # RESET
        self.pos = Position(0, 1, 0, self.filename, self.text)
    '''