import itertools
from pycomp.cfg2cnf import retrieve_grammar
from pycomp.cyk_parser import subs_grammar

# CYK
grammar_list = retrieve_grammar("./testcase/CNF_T.txt")

# Take token
sample_token = "'SHE' 'EATS' 'A' 'FISH' 'WITH' 'A' 'FORK'"
token_list = sample_token.split(" ")
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