import random

# Defining the grammar
VN = ['S', 'A', 'B', 'C']  # Non-terminal symbols
VT = ['a', 'b']  # Terminal symbols
S = 'S'  # Start symbol
P = {  # Production rules
    'S': ['aA', 'aB'],
    'A': ['bS'],
    'B': ['aC'],
    'C': ['a', 'bS']
}
F = 'X'  # Symbol indicating successful completion of the word

# Generate a string from the grammar
def generate_string(start_symbol):

    while any(nt in start_symbol for nt in VN):  # Check for the presence of non-terminal symbols
        for nt in VN:
            if nt in start_symbol:
                start_symbol = start_symbol.replace(nt, random.choice(P[nt]), 1)
    return start_symbol

# Convert grammar to a finite automaton
def grammar_to_finite_automaton():

    transition_function = {}
    for nt in P:
        for production in P[nt]:
            pair = (nt, production[0])
            if len(production) == 2:
                transition_function[pair] = production[1]
            else:
                transition_function[pair] = F
    return transition_function

# Check if a word belongs to the language
def check_word_in_language(word, transitions):

    current_state = S
    for char in word:
        if char not in VT:
            print(f"{word} does not exist")
            return False
        pair = (current_state, char)
        if pair in transitions:
            current_state = transitions[pair]
        else:
            print(f"{word} does not exist")
            return False

    if current_state == F or current_state not in VN:
        print(f"{word} belongs to the grammar")
        return True
    else:
        print(f"{word} does not exist")
        return False

def classify_grammar(VN, VT, P, S):
    is_type_3 = True
    is_type_2 = True

    for lhs, productions in P.items():
        for production in productions:
            # Check for Type 3 (Regular) Grammar
            if not(production == "" or
                   (len(production) == 1 and production in VT) or
                   (len(production) == 2 and production[0] in VT and production[1] in VN)):
                is_type_3 = False

            # Check for Type 2 (Context-Free) Grammar
            if len(lhs) != 1 or not(lhs in VN):
                is_type_2 = False

    if is_type_3:
        return "Type 3 (Regular)"
    elif is_type_2:
        return "Type 2 (Context-Free)"
    else:
        # This example does not cover Type 1 (Context-Sensitive) and Type 0 (Recursively Enumerable) checks
        # as it requires more complex analysis, especially for Type 1.
        return "Type 1 (Context-Sensitive) or Type 0 (Recursively Enumerable)"

# Example usage
VN = ['S', 'A', 'B', 'C']
VT = ['a', 'b']
P = {
    'S': ['aA', 'aB'],
    'A': ['bS'],
    'B': ['aC'],
    'C': ['a', 'bS']
}
S = 'S'

print(classify_grammar(VN, VT, P, S))


# Main function to demonstrate how the code works
def main():
    print('Generated words:')
    for _ in range(5):
        word = generate_string(S)
        print(word)

    print('\nConverting grammar to a finite automaton:')
    transitions = grammar_to_finite_automaton()
    for transition, result in transitions.items():
        print(f"{transition} -> {result}")

    print('\nChecking if words belong to the language:')
    words_to_test = ['aab', 'ab', 'aa', 'ba', 'aabaa', 'aaa', 'aba']
    for word in words_to_test:
        check_word_in_language(word, transitions)

if __name__ == "__main__":
    main()
