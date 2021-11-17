# =================== >>
# TOKEN PATTERNS
# =================== >>
token_expr = [
    # WHITESPACE AND COMMENTS ==================== >>
    (r'[\s\t]',                  None),
    (r'\\n',                     None),
    (r'#[^\n]*',                'LN_COMMENT'),
    (r'\'{3}',                  'SQ_COMMENT'),
    (r'\"{3}',                  'DQ_COMMENT'),
    # RESERVED KEYWORDS ========================== >>
    (r'False',                  'FALSE'),
    (r'None',                   'NONE'),
    (r'True',                   'TRUE'),
    (r'as',                     'AS'),
    (r'break',                  'BREAK'),
    (r'class',                  'CLASS'),
    (r'continue',               'CONTINUE'),
    (r'def',                    'DEF'),
    (r'if',                     'IF'),
    (r'elif',                   'ELIF'),
    (r'else',                   'ELSE'),
    (r'for',                    'FOR'),
    (r'from',                   'FROM'),
    (r'import',                 'IMPORT'),
    (r'pass',                   'PASS'),
    (r'raise',                  'RAISE'),
    (r'return',                 'RETURN'),
    (r'while',                  'WHILE'),
    (r'with',                   'WITH'),
    # OTHERS ==================================== >>
    (r'\d+\.\d*',               'FLOAT'),
    (r'\d+',                    'INT'),
    (r'[A-Za-z_][\w_]*',        'ID'),
    (r'->',                     'ARROW'),
    # OPERATORS ================================== >>
    (r'\+\+|\-\-',              'UNOPR'),
    (r'\+|\-|\*|\/|\*\*|%',     'BINOPR'),
    (r'and|or|not',             'LOGOPR'),
    (r'==|!=|>=|<=|>|<',        'COMPARISON'),
    (r'in|not in|is|is not',    'COMPARISON'),
    # PUNCTUATIONS  ============================== >>
    (r'\=',                     'ASSIGN'),
    (r'\(',                     'LP'),
    (r'\)',                     'RP'),
    (r'\[',                     'LSB'),
    (r'\]',                     'RSB'),
    (r'\{',                     'LCB'),
    (r'\}',                     'RCB'),
    (r'\.',                     'DOT'),
    (r',',                      'COLON'),
    (r';',                      'SEMICOLON'),
    (r':',                      'COLON'),
    (r'\'',                     'SQUOTE'),
    (r'\"',                     'DQUOTE'),
    (r'\?',                     'QMARK'),

    # CATCH EVERYTHING ELSE HERE
    (r'.*',                     'UNCATEGORIZED'),
]