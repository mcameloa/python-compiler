import ply.lex as lex

# Global varibles
lex_result = []

tokens = [
    'IDENTIFIER',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'ASSING',
    'LPAREN',
    'RPAREN',
    'SINGLE_QUOTE',
    'QUOTE',
    'STRING',
    'POINT',
    'COMMA',
    'LBRACKE',
    'RBRACKE',
    'END_LINE',
    'COMMENT',
    'SPACE'
]

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ASSING = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_SINGLE_QUOTE = r'\''
t_QUOTE = r'\"'
t_POINT = r'\.'
t_COMMA = r'\,'
t_LBRACKE = r'\{'
t_RBRACKE = r'\}'
t_END_LINE = r';'


# Ignored characters
t_ignore = " [\t]|"

reserved = {
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'while': 'WHILE',
    'import': 'IMPORT',
    'require': 'REQUIRE',
    'var': 'VAR',
    'let': 'LET',
    'const': 'CONST',
    'function': 'FUNCTION',
    'break': 'BREAK',
    'for': 'FOR'
}

tokens = tokens + list(reserved.values())

def t_COMMENT(t):
    r'//.*'
    pass

def t_SPACE(t):
    r'\n'
    pass

def t_LET(t):
    r'let'
    t.type = reserved.get(t.value, 'LET')
    return t

def t_ELSE(t):
    r'else'
    t.type = reserved.get(t.value, 'ELSE')
    return t

def t_WHILE(t):
    r'while'
    t.type = reserved.get(t.value, 'WHILE')
    return t

def t_IMPORT(t):
    r'import'
    t.type = reserved.get(t.value, 'IMPORT')
    return t

def t_REQUIRE(t):
    r'require'
    t.type = reserved.get(t.value, 'REQUIRE')
    return t

def t_VAR(t):
    r'var'
    t.type = reserved.get(t.value, 'VAR')
    return t

def t_CONST(t):
    r'const'
    t.type = reserved.get(t.value, 'CONST')
    return t

def t_FUNCTION(t):
    r'function'
    t.type = reserved.get(t.value, 'FUNCTION')
    return t

def t_BREAK(t):
    r'break'
    t.type = reserved.get(t.value, 'BREAK')
    return t

def t_FOR(t):
    r'for'
    t.type = reserved.get(t.value, 'FOR')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'(\'([^\'])*\')|(\"([^\"])*\")'
    return t

def t_error(token):
    global lex_result

    line = str(token.lineno)
    value = str(token.value)
    pos = str(token.lexpos)

    state = f"ERROR: Invalid token {value} at {line}:{pos}"
    lex_result.append(state)
    token.lexer.skip(1)


analyzer = lex.lex()


def main(data):
    global lex_result

    analyzer = lex.lex()
    analyzer.input(data)

    lex_result.clear()
    while True:
        token = analyzer.token()
        if not token:
            break

        line = str(token.lineno)
        token_type = str(token.type)
        value = str(token.value)
        pos = str(token.lexpos)

        state = f"Line {line} | Type {token_type} | Value {value} | Position {pos}"

        lex_result.append(state)

    print_results()


def print_results():
    for result in lex_result:
        print(result)


if __name__ == '__main__':
    while True:
        user_input = input("Enter a expression: ")
        main(user_input)
        print_results()
