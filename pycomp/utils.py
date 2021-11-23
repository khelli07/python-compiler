# =================== >>
# UTILS
# =================== >>
from database.token_db import TAB

def count_length(string, tab_length=4):
    length = len(string)
    if TAB in string:
        ctr = string.count(TAB)
        length -= ctr
        length += ctr * tab_length

    return length

def is_bracket_match(tag1, tag2):
    if (tag1 == 'LP'):
        return tag2 == 'RP'
    elif (tag1 == 'LSB'):
        return tag2 == 'RSB'
    elif (tag1 == 'LCB'):
        return tag2 == 'RCB'
    else:
        return False

def get_token(tag_name, token_line):
    for token in token_line:
        if token.tag == tag_name:
            return token

def get_tag_string(tag_name, token_line):
    token = get_token(tag_name, token_line)
    return token.tag

def stringify_line(line):
    tag_list = [get_tag_string(token.tag, line) for token in line]
    return tag_list