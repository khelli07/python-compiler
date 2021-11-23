# =================== >>
# CFG to CNF Converter
# =================== >>
import copy

# SUPPORT FUNC
def is_terminal(string):
    return "'" in string

def is_unit_prod(rule):
    return len(rule) == 2 and not(is_terminal(rule[1]))

def subs_unit_prod(rule, grammar_dict):
    ''' 
    Rule has a length of two, let's say ['A', 'B']
    which is the same as A -> B. We want to eliminate this unit production.
    For instance, if B -> CD | EF then we make ['A', 'C', 'D'] and ['A', 'E', 'F'].

    Remember, the input should already be in the form of dict,
    i.e. B -> CD | EF is B -> CD; B -> EF (in the file)
    or ['B', 'C', 'D'] and ['B', 'E', 'F'] (in the list of grammar)
    The function will return only new rules that corresponds to the input rule.
    '''
    nrlist = []
    repeat = False
    for grammar in grammar_dict[rule[1]]:
        new_rule = [rule[0]]
        new_rule[1:] = grammar[1:]
        if (is_unit_prod(new_rule)):
            repeat = True
        nrlist.append(new_rule)

    return nrlist, repeat

# MAIN FUNC
def grammar_to_list(filename):
    ''' 
    Read grammar from file, the file example can be accessed in database/CFG.txt
    Production rule in form of S -> A B will be converted to ['S', 'A', 'B']
    The S produciton is not unique. There maybe another rule with S, e.g. ['S', 'C', 'D']. 
    It depends on the grammar input file.
    '''
    with open(filename) as cfg:
        lines = cfg.readlines()
    
    readline = [ln.replace("\n", "").split(" -> ") for ln in lines]
    grammar_list = []
    for line in readline:
        if (len(line) >= 2):
            grammar_name = line[0]
            grammar_bodies = line[1].split(" | ")
            for grammar in grammar_bodies:
                new_grammar = [grammar_name]
                new_grammar.extend(grammar.strip().split())
                grammar_list.append(new_grammar)

    return grammar_list

def grammar_to_dict(filename):
    '''
    Similar to function above, but in dictionary form.
    For instance, the output of S -> A B | C will looks like:
    grammar_dict = {'S' : [['S', 'A', 'B],
                        ['S', 'C]], ...}
    '''
    with open(filename) as cfg:
        lines = cfg.readlines()
    
    lines = [ln.replace("\n", "").split(" -> ") for ln in lines]

    grammar_dict = {}
    for line in lines:
        grammar_list = []
        if (len(line) >= 2):
            grammar_name = line[0].strip()
            grammar_bodies = line[1].split(" | ")
            for grammar in grammar_bodies:
                new_grammar = [grammar_name]
                new_grammar.extend(grammar.strip().split())
                grammar_list.append(new_grammar)

        if grammar_name in grammar_dict.keys():
            grammar_dict[grammar_name].extend(grammar_list)
        else:
            grammar_dict[grammar_name] = grammar_list

    return grammar_dict

def handle_unit_production(grammar_dict):
    '''
    Remove all unit production in the form of A -> B with substitution.
    I.S. There maybe unit production in grammar dictionary
    F.S. No more unit production, all unit productions
    have been substituted.
    '''
    repeat = True
    while repeat:
        repeat = False
        for _, rules in grammar_dict.items():
            i = 0
            while i < len(rules):
                if is_unit_prod(rules[i]):
                    new_rule, repeat = subs_unit_prod(rules[i], grammar_dict)
                    rules.pop(i)
                    rules.extend(new_rule)
                else:
                    i += 1

def CFG2CNF(grammar_dict):
    '''
    Return CFG in the form of Chomsky Normal Form
    in which the only productions allowed are:
    1. A -> BC, where A, B, and C are variables (nonterminal).
    2. B -> b, where b is a terminal.
    Note that this function does not handle epsilon productions.
    '''
    cnf_rules = copy.deepcopy(grammar_dict)
    
    # Handle unit production
    handle_unit_production(cnf_rules)

    # Handle more than two variables and/or terminals
    # e.g. Convert S -> X Y Z to S -> X A; A -> Y Z
    ctr = 0
    extended_rule = []
    extended_dict = {}
    for key, rules in cnf_rules.items():
        for i in range(len(rules)):
            if (len(rules[i]) > 3): # NOT IN CHOMSKY NORMAL FORM
                new_product = rules[i][2:]
                rules[i] = rules[i][:2]

                # If the rule is already generated, no need to regenerate
                new_rule = None
                for rule in extended_rule:
                    if new_product == rule[1:]:
                        new_rule = rule[0]
                        break
                
                # Add new production to list if not found
                if not(new_rule):
                    new_rule = new_product[0] + str(ctr)
                    ctr += 1
                    new_product.insert(0, new_rule)
                    extended_rule.append(new_product)
                else:
                    new_product.insert(0, new_rule)

                # Add rule to the end
                rules[i].append(new_rule)
    
    ctr = 0
    tmp = []
    for i in range(len(extended_rule)):
        if (len(extended_rule[i]) > 3):
            new_product = extended_rule[i][2:]
            extended_rule[i] = extended_rule[i][:2]

            new_rule = None
            for rule in tmp:
                if new_product == rule[1:]:
                    new_rule = rule[0]
                    break
                
            if not(new_rule):
                new_rule = new_product[0] + "_EXT" + str(ctr)
                ctr += 1
                new_product.insert(0, new_rule)
                extended_rule.append(new_product)
            else:
                new_product.insert(0, new_rule)

            extended_rule[i].append(new_rule)
        
    for rule in extended_rule:
        extended_dict[rule[0]] = [rule]

    cnf_rules.update(extended_dict)

    # Take unique productions only and sort them
    for key, rules in cnf_rules.items():
        rules = set(tuple(l) for l in rules)
        rules = sorted(rules, key=lambda x: (x[-1]))
        rules = [list(rule) for rule in rules]
        cnf_rules[key] = rules

    return cnf_rules

def run_converter(filein, fileout):
    grammar_dict = grammar_to_dict(filein)
    cnf_rules = CFG2CNF(grammar_dict)

    f = open(fileout, "w")

    for _, rules in cnf_rules.items():
        for rule in rules:
            f.write(f"{rule[0]} ->")
            for i in range(1, len(rule)):
                f.write(f" {rule[i]}")
            f.write("\n")

    f.close()