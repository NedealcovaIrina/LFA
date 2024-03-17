import re

# Define patterns for different types of tokens. Each token is represented by a pair:
# the name of the token and the regular expression that describes it.
TOKEN_PATTERNS = [
    ('NUMBER', r'\d+'),  # Integers
    ('IDENTIFIER', r'[a-zA-Z_]\w*'),  # Identifiers (variables, functions)
    ('OPERATOR', r'[+\-*/]'),  # Mathematical operators
    ('WHITESPACE', r'\s+'),  # Whitespace characters (will not be included in the results)
]

# Compile the regular expressions into one, using groups. Each group
# is named according to the token type, allowing us to determine
# the type of the token found.
token_regex = '|'.join('(?P<%s>%s)' % pair for pair in TOKEN_PATTERNS)


def lex(characters):
    # The lexical analyzer function. It takes an input string and returns
    # a list of tokens as pairs (token_type, value).

    tokens = []  # List to store the results

    # Find matches for all tokens in the string. The finditer function returns an iterator
    # over all found matches, allowing us to process them one by one.
    for match in re.finditer(token_regex, characters):
        kind = match.lastgroup  # The type of the current token (e.g., 'NUMBER')
        value = match.group()  # The string that matches the token

        # Skip tokens corresponding to spaces, as they do not carry
        # useful information for further analysis.
        if kind != 'WHITESPACE':
            tokens.append((kind, value))  # Add the token to the list

    return tokens  # Return the list of tokens


# Example of use
input_string = "x = 10 + 5 / y"
tokens = lex(input_string)  # Call the lexer to analyze the string
print(tokens)  # Print the list of tokens
