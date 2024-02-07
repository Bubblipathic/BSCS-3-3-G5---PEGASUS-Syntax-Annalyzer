from Dictionaries import DIGITS, ALPHABETS, OPERATORS, RESERVEDORKEY_WORDS, NOISE_WORDS, SPECIAL_SYMBOLS

def is_valid(lexeme):
    # Check if the word is not empty
    if not lexeme:
        return False
    
    # Check if the first character is a letter or an underscore
    if not (lexeme[0].isalpha() or lexeme[0] == '_'):
        return False

    # Check the remaining characters
    for char in lexeme[1:]:
        if not (char.isalpha() or char.isdigit() or char == '_'):
            return False
    
    # If all checks pass, it's a valid identifier
    return True

def contains_alphabet(input_str):
    return any(char.isalpha() for char in input_str)

def contains_num(input_str):
    return any(char.isdigit() for char in input_str)


def lexeme(token):
    if token in RESERVEDORKEY_WORDS:
        return RESERVEDORKEY_WORDS[token]
    elif token in NOISE_WORDS:
        return NOISE_WORDS[token]
    elif token in OPERATORS:
        return OPERATORS[token]
    elif token in SPECIAL_SYMBOLS:
        return SPECIAL_SYMBOLS[token]
    elif token and (token[0] == token[-1] and token[0] == '"' and len(token) > 3):
        return 'STR_LIT' 
    elif token and (token[0] == token[-1] and token[0] == "'" and len(token) <= 3):
        return 'CHAR_LIT'
    elif contains_num(token) and '.' in token:
        return 'FLT_LIT'
    elif token.isdigit():
        return 'INT_LIT'
    elif token == '\\n':
        return 'DEL_STMT'
    elif token == '\\t':
        return 'TAB_SPC'
    elif token.startswith(':') and is_valid(token):
        return 'IDENT_DT'
    elif is_valid(token):
        return 'IDENT'
    elif token.startswith("//"):
        return 'SINGLE_COMM'
    elif token and (token[0] == '/' and token[1] == '*' and token[-1] == '/' and token[-2] == '*'):
        return 'MULTI_COMM'
    else:
        return 'INVALID'
    
