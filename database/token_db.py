# =================== >>
# CONSTANTS
# =================== >>
TAB = '\t'
SPACE = ' '
QUOTES = ["'", '"']
BRACKETS = ['LP', 'RP', 'LSB', 'RSB', 'LCB', 'RCB']
BINARY_OPR = ['PLUS', 'MINUS', 'STAR', 'BINARY_OPR', 'BITWISE_OPR']
DIGITS = '0123456789'
ALPHA = 'abcdefghijklmnopqrstuvwxyz'

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
    (r'\'[^\n\']*\'',           'STRING'),
    (r'\"[^\n\"]*\"',           'STRING'),
    # RESERVED KEYWORDS ========================== >>
    (r'False|True',             'BOOLEAN'),
    (r'None',                   'NONE'),
    (r'as\s',                   'AS'),
    (r'break',                  'BREAK'),
    (r'class\s',                'CLASS'),
    (r'continue',               'CONTINUE'),
    (r'def\s',                  'DEF'),
    (r'if',                     'IF'),
    (r'elif',                   'ELIF'),
    (r'else',                   'ELSE'),
    (r'for\s',                  'FOR'),
    (r'from\s',                 'FROM'),
    (r'import\s',               'IMPORT'),
    (r'pass',                   'PASS'),
    (r'range',                  'RANGE'),
    (r'raise\s',                'RAISE'),
    (r'return',                 'RETURN'),
    (r'while',                  'WHILE'),
    (r'with\s',                 'WITH'),
    (r'not\s',                  'NOT'),
    (r'in\s',                   'IN'),
    (r'and\s|or\s',             'LOGICAL_OPR'),
    (r'not in|is\s|is not',     'COMPARISON'),
    # OTHERS ==================================== >>
    (r'\d+(\.\d*)?',            'NUMBER'),
    (r'[A-Za-z_][\w_]*',        'IDENTIFIER'),
    (r'->',                     'ARROW'),
    # OPERATORS ================================== >>
    (r'\-=|\+=|\*\*=|\*=|%=',   'AUG_ASSIGN'),
    (r'\/\/=|\/=|~=|<<=|>>=',   'AUG_ASSIGN'),
    (r'&=|\|=|\^=',             'AUG_ASSIGN'),
    (r'\-',                     'MINUS'),
    (r'\+',                     'PLUS'),
    (r'\*\*\d+(\.\d*)?',        'POWER'),
    (r'\*\*|%|\/\/|\/',         'BINARY_OPR'),
    (r'\*',                     'STAR'),
    (r'~',                      'BITWISE_NOT'),
    (r'>>|<<|~|&|\||\^',        'BITWISE_OPR'),
    (r'==|!=|>=|<=|>|<',        'COMPARISON'),
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
    (r'\\',                     'BACKSLASH'),

    # CATCH EVERYTHING ELSE HERE
    (r'[^\s\t]*',               'UNCATEGORIZED'),
]