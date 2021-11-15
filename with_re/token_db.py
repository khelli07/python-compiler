token_expr = [
    # WHITESPACE AND COMMENTS ==================== >>
    (r'[\s\t]+',                 None),
    (r'\\n',                    'NEWLINE'),
    (r'#[^\n]*',                'SHORT_COMMENT'),
    (r'\'\'\'',                 'LONG_COMMENT'),
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
    # (r';',                      'SEMICOLON'),
    (r':',                      'COLON'),
    (r'\'',                     'SQUOTE'),
    (r'\"',                     'DQUOTE'),
    # OPERATORS ================================== >>
    (r'\+|\-|\*|\/|\*\*|%',     'BINOPR'),
    (r'\+\+|\-\-',              'UNOPR'),
    (r'and|or|not',             'LOGOPR'),
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
    (r'[0-9]+',                                 'INT'),
    (r'[A-Za-z_][A-Za-z0-9_]*|\?',              'ID'),
    (r'==|!=|>=|<=|>|<|in|not in|is|is not',    'COMPARISON'),
]