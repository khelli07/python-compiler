# =================== >>
# PARSER
# =================== >>
import itertools, sys
from pycomp.lexer import run_lexer
from pycomp.error import get_error
from pycomp.cfg2cnf import grammar_to_list
from pycomp.utils import get_tag_string

def subs_grammar(union, production, grammar_list):
    '''
    I.S. union is defined, but maybe empty
    F.S. if rule is in list of grammar, and the rule is not in union, 
    we add the rule to it.
    
    For instance, we have production (B, A) and there is a rule such that
    S -> BA and C -> BA in the form of ['S', 'B', 'A'] and ['C', 'B', 'A'].
    Furthermore, let us assume our union is empty, then 
    from union = [] -> union = ['S', 'C'] because they produce BA. 
    '''
    for grammar in grammar_list:
        if (grammar[0] not in union) and (production == tuple(grammar[1:])):
            union.append(grammar[0])

class Parser:
    def __init__(self, filename, cnf_file, text):
        self.filename = filename
        self.cnf_file = cnf_file
        self.text = text

    def parse_cyk(self, tokenized_line, cnf_grammar):
        line = ["'" + token.tag + "'" for token in tokenized_line]
        length = len(line)
        cyk_table = [[[] for _ in range(length)] for _ in range(length)]

        for i in range(length):
            for j in range(length - i):
                if (i == 0):
                    for grammar in cnf_grammar:
                        if (len(grammar) == 2) and (grammar[1] == line[j]):
                            cyk_table[i][j].append(grammar[0])
                else:
                    lprod = []
                    x = 0; y = j + 1
                    while (x != i):
                        cartesian_prod = list(itertools.product(cyk_table[x][j], 
                                                                cyk_table[i - x - 1][y]))
                        lprod.extend(cartesian_prod)
                        x += 1; y += 1
                    
                    union = []
                    for production in lprod:
                        subs_grammar(union, production, cnf_grammar)
                    cyk_table[i][j] = [var for var in set(union)]


        # for i in range(length - 1, -1, -1):
        #     for j in range(length):
        #         print(f"{cyk_table[i][j]}", end="  ")
        #     print()

        return (cyk_table[length - 1][0] != [])

    def parse_text(self):
        text_by_line, tokenized_lines = run_lexer(self.filename, self.text)
        cnf_grammar = grammar_to_list(self.cnf_file)

        if_count = 0
        ctr = 0
        for line in tokenized_lines:
            # print(f"Checking line {ctr + 1}...")

            is_accepted = self.parse_cyk(line, cnf_grammar)
            line_stringified = [get_tag_string(token.tag, line) for token in line]
            # Handle if block
            if is_accepted:
                if 'IF' in line_stringified:
                    if_count += 1
                elif ('ELSE' in line_stringified) and (if_count != 0):
                    if_count -= 1
                elif ('ELIF' in line_stringified) and (if_count == 0):
                    error = get_error('ELIF', line, f"Expected an if statement", text_by_line)
                    error.print_error()
                    sys.exit(1)
                elif ('ELSE' in line_stringified) and (if_count == 0):
                    error = get_error('ELSE', line, f"Expected an if statement", text_by_line)
                    error.print_error()
                    sys.exit(1)
            else:
                initial_token = line[0]
                print(initial_token.pos_start)
                print(text_by_line[initial_token.pos_start.line - 1])
                print("\nSyntax Error Found!")
                print(line)
                sys.exit(1)

            ctr += 1


def run_parser(filename, cnf_file, text):
    parser = Parser(filename, cnf_file, text)
    parser.parse_text()
    print("Yay, your program is accepted!")