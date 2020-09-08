import ply.lex as lex

# Global varibles
lex_result = []

tokens = [
    'NAME',
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'ASSING',
    'LPAREN',
    'RPAREN',
]

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ASSING = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'


# Ignored characters
t_ignore = " \t"

reserved = {
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'while': 'WHILE',
    'import': 'IMPORT',
    'require': 'REQUIRE',
    'var': 'VAR',
    'let': 'LET',
    'const': 'const'
}

tokens = tokens + list(reserved.values())


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
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
