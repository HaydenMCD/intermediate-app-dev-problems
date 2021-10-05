# Hayden McDowall
# Otago Polytechnic 2021


class PostfixCalculator:
    def __init__(self):
        self.stack = []
        self.token_map = {
            "+": lambda: self.push(self.pop() + self.pop()),
            "-": lambda: self.push(self.pop() - self.pop()),
            "*": lambda: self.push(self.pop() * self.pop()),
            "/": lambda: self.push(self.pop() / self.pop()),
            "print": lambda: self.print()
        }

    def push(self, sth):
        self.stack.append(int(sth))

    def pop(self):
        return self.stack.pop()

    def print(self):
        print(self.pop())

    def run(self, code):
        # Splits the user input up based on whitespace. eg: 1 1 + will become "1", "1", "+"
        tokens = code.split(" ")
        c = 0
        while c < len(tokens):
            current = tokens[c]
            if current.isnumeric():  # If current contains only numbers then it will push to the stack
                self.push(current)
                c += 1
            elif current in self.token_map:  # Checks if current is in the token_map
                self.token_map[current]()
                c += 1
            else:
                # Error if an invalid character is entered by user
                raise SyntaxError(f"{current}: Invalid syntax.")


calc = PostfixCalculator()
userInput = input('Please enter your equation: ')
calc.run(f"{userInput} print")
