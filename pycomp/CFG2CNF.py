# =================== >>
# CFG to CNF Converter
# =================== >>
import copy

# SUPPORT FUNC
def isTerminal(string):
    return "'" in string

def retrieve_grammar(filename):
    ''' 
    Read grammar from file, the file example can be accessed in database/CFG.txt
    Production rule in form of S -> A B will be converted to ['S', 'A', 'B']
    The S produciton is not unique. There maybe another rule with S, e.g. ['S', 'C', 'D']. 
    It depends on the grammar input file.
    '''

    with open(filename) as cfg:
        lines = cfg.readlines()
    
    # LOG stands for "List of Grammar"
    log = [ln.replace("->", "").split() for ln in lines]
    log = [grammar for grammar in log if len(grammar) != 0]
    return log

def subs_unit_prod(rule, log):
    ''' 
    Rule has a length of two, let's say ['A', 'B']
    which is the same as A -> B. We want to eliminate this unit production.
    For instance, if B -> CD | EF then we make ['A', 'C', 'D'] and ['A', 'E', 'F'].

    Remember, the input should already be in the form of list,
    i.e. B -> CD | EF is B -> CD; B -> EF (in the file)
    or ['B', 'C', 'D'] and ['B', 'E', 'F'] (in the list of grammar)
    The function will return only new rules that corresponds to the input rule.
    '''
    nrlist = []
    for grammar in log:
        new_rule = [rule[0]]
        if grammar[0] == rule[1] and grammar != rule:
            new_rule[1:] = grammar[1:]
            nrlist.append(new_rule)
    
    return nrlist


def handle_unit_production(list_of_grammar):
    '''
    Remove all unit production in the form of A -> B with substitution.
    The function will return new list of grammar which all unit productions
    have been substituted.
    '''
    rules = copy.deepcopy(list_of_grammar)
    rlength = len(list_of_grammar)
    for i in range(rlength):
        if (len(rules[i]) == 2) and not(isTerminal(rules[i][1])):
            new_rule = subs_unit_prod(rules[i], list_of_grammar)
            rules.pop(i)
            rules.extend(new_rule)

    return rules
                    

def CFG2CNF(list_of_grammar):
    '''
    Return CFG in the form of Chomsky Normal Form
    in which the only productions allowed are:
    1. A -> BC, where A, B, and C are variables (nonterminal).
    2. B -> b, where b is a terminal.
    Note that this function does not handle epsilon productions.
    '''
    cnf_rules = copy.deepcopy(list_of_grammar)
    rlength = len(cnf_rules)

    # Handle more than two variables and/or terminals
    # e.g. Convert S -> X Y Z to S -> X A; A -> Y Z
    ctr = 0
    for i in range(rlength):
        if (len(cnf_rules[i]) > 3): # NOT CHOMSKY
            new_product = cnf_rules[i][2:]
            cnf_rules[i] = cnf_rules[i][:2]

            # Add new variable (extended)
            new_rule = new_product[0] + "_EXT" + str(ctr)
            cnf_rules[i].append(new_rule)
            new_product.insert(0, new_rule)
            ctr += 1

            # Insert to one place after this rule
            # so after this rule is processed, we immediately process the next one.
            # The concept is similar to recursivity
            cnf_rules.insert(i + 1, new_product)

    # Handle unit production (by theory it should be pre-process)
    # But, because for loop can not do tracking, I'll do post-process
    cnf_rules = handle_unit_production(cnf_rules)

    # Take unique productions only and sort them
    cnf_rules = set(tuple(l) for l in cnf_rules)
    cnf_rules = sorted(cnf_rules, key=lambda x: x[0])
    cnf_rules = [list(rule) for rule in cnf_rules]
    return cnf_rules

def run_converter(filein, fileout):
    log = retrieve_grammar(filein)
    cnf_rules = CFG2CNF(log)

    f = open(fileout, "w")

    for rule in cnf_rules:
        f.write(f"{rule[0]} ->")
        for i in range(1, len(rule)):
            f.write(f" {rule[i]}")
        f.write("\n")

    f.close()

run_converter("database/CFG.txt", "database/CNF.txt")
