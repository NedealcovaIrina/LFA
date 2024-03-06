

class ProductionRule:
    def __init__(self, left_side, right_side):
        self.left_side = left_side
        self.right_side = right_side

class ChomskyGrammar:
    def __init__(self):
        self.VN = {'S', 'A', 'B', 'C'}
        self.VT = {'a', 'b'}
        self.P = [
            ProductionRule('S', 'aA'),
            ProductionRule('A', 'bS'),
            ProductionRule('S', 'aB'),
            ProductionRule('B', 'aC'),
            ProductionRule('C', 'a'),
            ProductionRule('C', 'bS'),
        ]

    def classify(self):
        if self.is_type_3():
            return "Type 3 (Regular)"
        elif self.is_type_2():
            return "Type 2 (Context-Free)"
        elif self.is_type_1():
            return "Type 1 (Context-Sensitive)"
        elif self.is_type_0():
            return "Type 0 (Unrestricted)"
        else:
            return "Invalid grammar"

    def is_type_0(self):
        # All grammars are Type 0
        return True

    def is_type_1(self):
        # Check if all production rules are of the form α -> β where |α| <= |β|
        for rule in self.P:
            if len(rule.left_side) > len(rule.right_side):
                return False
        return True

    def is_type_2(self):
        # Check if all production rules are of the form A -> γ where A is a non-terminal and γ is a string of terminals or non-terminals
        for rule in self.P:
            if len(rule.left_side) != 1 or rule.left_side not in self.VN:
                return False
            if not all(c in self.VN.union(self.VT) for c in rule.right_side):
                return False
        return True

    def is_type_3(self):
        # Check if all production rules are of the form A -> aB or A -> a where A and B are non-terminals and a is a terminal
        for rule in self.P:
            if len(rule.right_side) > 2:
                return False
            if len(rule.right_side) == 1 and rule.right_side[0] not in self.VT:
                return False
            if len(rule.right_side) == 2 and not (rule.right_side[0] in self.VT and rule.right_side[1] in self.VN):
                return False
        return True

grammar = ChomskyGrammar()
print(grammar.classify())
