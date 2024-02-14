import random

class Grammar:
    def __init__(self):
        self.VN = {'S', 'A', 'B', 'C'}  # Non-terminal symbols
        self.VT = {'a', 'b'}  # Terminal symbols
        self.P = {  # Production rules
            'S': ['aA', 'aB'],
            'A': ['bS'],
            'B': ['aC'],
            'C': ['a', 'bS']
        }
        self.S = 'S'  # Start symbol

    def generateString(self):
        # Function to recursively expand and generate strings based on production rules
        def expand(symbol):
            if symbol in self.VN:
                productions = self.P[symbol]
                chosen_production = random.choice(productions)
                return ''.join(expand(sym) for sym in chosen_production)
            else:
                return symbol
        return expand(self.S)

class FiniteAutomaton:
    def __init__(self, states, alphabet, transition_function, start_state, accepting_states):
        self.Q = states  # States
        self.Sigma = alphabet  # Alphabet
        self.delta = transition_function  # Transition function
        self.q0 = start_state  # Start state
        self.F = accepting_states  # Accepting states

    def stringBelongsToLanguage(self, inputString):
        # Function to check if a given string belongs to the language defined by the automaton
        current_state = self.q0
        for char in inputString:
            if (current_state, char) in self.delta:
                current_state = self.delta[(current_state, char)]
            else:
                return False
        return current_state in self.F

def grammar_to_FA(grammar):
    # Define finite automaton states, alphabet, transitions, start and accepting states
    states = {'q0', 'q1', 'q2', 'q3', 'q4', 'qF'}
    alphabet = {'a', 'b'}
    transition_function = {
        ('q0', 'a'): 'q1',
        ('q1', 'b'): 'q2',
        ('q2', 'a'): 'q3',
        ('q3', 'a'): 'q4',
    }
    start_state = 'q0'
    accepting_states = {'q4'}
    return FiniteAutomaton(states, alphabet, transition_function, start_state, accepting_states)

def main():
    grammar = Grammar()
    print("Generated strings from the grammar:")
    for _ in range(5):
        print(grammar.generateString())

    fa = grammar_to_FA(grammar)
    test_string = "abaa"
    if fa.stringBelongsToLanguage(test_string):
        print(f"String {test_string} belongs to the language.")
    else:
        print(f"String {test_string} does not belong to the language.")

if __name__ == "__main__":
    main()
