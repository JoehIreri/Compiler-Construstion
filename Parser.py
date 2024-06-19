# Node.py
from abc import ABC, abstractmethod

class Node(ABC):
    @abstractmethod
    def evaluate(self):
        pass

# NumberNode.py
class NumberNode(Node):
    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return self.value

# BinaryOperationNode.py
class BinaryOperationNode(Node):
    def __init__(self, left, right, operator):
        self.left = left
        self.right = right
        self.operator = operator

    def evaluate(self):
        if self.operator == '+':
            return self.left.evaluate() + self.right.evaluate()
        elif self.operator == '-':
            return self.left.evaluate() - self.right.evaluate()
        elif self.operator == '*':
            return self.left.evaluate() * self.right.evaluate()
        elif self.operator == '/':
            return self.left.evaluate() / self.right.evaluate()
        else:
            raise ValueError(f"Unknown operator: {self.operator}")
        # Parser.py
class Parser:
    def __init__(self, input):
        self.input = input
        self.pos = -1
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos += 1
        self.current_char = self.input[self.pos] if self.pos < len(self.input) else None

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()
            def parse_number(self):
                num_str = ''
        while self.current_char is not None and (self.current_char.isdigit() or self.current_char == '.'):
            num_str += self.current_char
            self.advance()
        return float(num_str)

    def factor(self):
        self.skip_whitespace()
        if self.current_char == '(':
            self.advance()
            node = self.expr()
            if self.current_char == ')':
                self.advance()
            else:
                raise ValueError("Expected ')'")
            return node
        elif self.current_char.isdigit() or self.current_char == '.':
            return NumberNode(self.parse_number())
        else:
            raise ValueError(f"Unexpected character: {self.current_char}")

    def term(self):
        node = self.factor()
        while self.current_char in ('*', '/'):
            op = self.current_char
            self.advance()
            node = BinaryOperationNode(node, self.factor(), op)
        return node

    def expr(self):
        node = self.term()
        while self.current_char in ('+', '-'):
            op = self.current_char
            self.advance()
            node = BinaryOperationNode(node, self.term(), op)
        return node

    def parse(self):
        node = self.expr()
        if self.current_char is not None:
            raise ValueError(f"Unexpected character: {self.current_char}")
        return node
    # main.py
def main():
    expression = "(3 + 5) * 2 / (7 - 2)"
    parser = Parser(expression)
    ast = parser.parse()
    print("Result:", ast.evaluate())  # Result: 3.26

if __name__ == "__main__":
    main()