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