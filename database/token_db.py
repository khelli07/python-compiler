# =================== >>
# CONSTANTS
# =================== >>
TAB = '\t'
SPACE = ' '

# =================== >>
# TOKEN PATTERNS
# =================== >>
token_rule = [
    # WHITESPACE AND COMMENTS ==================== >>
    (r'[\s\t]',                  None),
    (r'\\n',                     None),
    (r'#[^\n]*',                'LN_COMMENT'),
    (r'\'{3}',                  'SQ_COMMENT'),
    (r'\"{3}',                  'DQ_COMMENT'),
    # RESERVED KEYWORDS ========================== >>
    (r'False|True',             'BOOLEAN'),
    (r'None',                   'NONE'),
    (r'as\s',                   'AS'),
    (r'break',                  'BREAK'),
    (r'class\s',                'CLASS'),
    (r'continue',               'CONTINUE'),
    (r'def\s',                  'DEF'),
    (r'if\s',                   'IF'),
    (r'elif\s',                 'ELIF'),
    (r'else',                   'ELSE'),
    (r'for\s',                  'FOR'),
    (r'from\s',                 'FROM'),
    (r'import\s',               'IMPORT'),
    (r'pass',                   'PASS'),
    (r'raise\s',                'RAISE'),
    (r'return\s',               'RETURN'),
    (r'while\s',                'WHILE'),
    (r'with\s',                 'WITH'),
    # OTHERS ==================================== >>
    (r'\d+\.\d*',               'FLOAT'),
    (r'\d+',                    'INT'),
    (r'[A-Za-z_][\w_]*',        'IDENTIFIER'),
    (r'->',                     'ARROW'),
    # OPERATORS ================================== >>
    (r'\+\+|\-\-',              'UNARY_OPR'),
    (r'not\s',                  'NOT_OPR'),
    (r'\+|\-|\*|\*\*|%|\/\/|\/','BINARY_OPR'),
    (r'>>|<<|~|&|\||\^',        'BITWISE_OPR'),
    (r'and|or',                 'LOGICAL_OPR'),
    (r'==|!=|>=|<=|>|<',        'COMPARISON'),
    (r'not in|is|is not',       'COMPARISON'),
    (r'in\s',                   'IN'),
    # PUNCTUATIONS  ============================== >>
    (r'\=',                     'ASSIGN'),
    (r'\(',                     'LP'),
    (r'\)',                     'RP'),
    (r'\[',                     'LSB'),
    (r'\]',                     'RSB'),
    (r'\{',                     'LCB'),
    (r'\}',                     'RCB'),
    (r'\.',                     'DOT'),
    (r',',                      'COMMA'),
    (r';',                      'SEMICOLON'),
    (r':',                      'COLON'),
    (r'\'',                     'SQUOTE'),
    (r'\"',                     'DQUOTE'),
    (r'\?',                     'QMARK'),

    # CATCH EVERYTHING ELSE HERE
    (r'[^\s\t]*',               'UNCATEGORIZED'),
]