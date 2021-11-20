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

def get_token(tag_name, token_line):
    for token in token_line:
        if token.tag == tag_name:
            return token

def get_tag_string(tag_name, token_line):
    token = get_token(tag_name, token_line)
    return token.tag