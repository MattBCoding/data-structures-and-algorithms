# Stack based code linter
from stack import Stack


# implement linter class
class Linter:
    def __init__(self):
        # create a stack
        self.stack = Stack()

    # helper function to check if a char is an opening brace
    def is_opening_brace(self, char):
        return char in ["(", "{", "["]

    # helper function to check if a char is a closing brace
    def is_closing_brace(self, char):
        return char in [")", "}", "]"]

    # helper function to check if a char is a match for another char
    def is_not_a_match(self, opening, closing):
        return (
            opening == "("
            and closing != ")"
            or opening == "{"
            and closing != "}"
            or opening == "["
            and closing != "]"
        )

    # lint method
    def lint(self, code):
        # we start a loop which reads each character in out code
        for char in code:
            # if the char is an opening brace
            if self.is_opening_brace(char):
                # push the char onto the stack
                self.stack.push(char)
            # if the char is a closing brace
            elif self.is_closing_brace(char):
                # pop from stack
                popped_opening_brace = self.stack.pop()
                # if the stack was empty, so what we popped was None
                # it means that an opening brace was missing
                if popped_opening_brace == None:
                    return f"{char} doesn't have opening brace"

                # if the popped opening brace doesn't match the closing brace
                if self.is_not_a_match(popped_opening_brace, char):
                    return f"{char} has a mismatched opening brace"

        # if we get to the end of line, and the stack isn't empty
        if not self.stack.is_empty():
            # it means there was an opening brace missing
            return f"{self.stack.read()} doesn't have a closing brace"

        # if we get to the end of the line and the stack is empty
        # it means there were no errors
        return True


# test the linter
code_to_test = "(let x = {y: [1, 2, 3]})"
linter = Linter()
result = linter.lint(code_to_test)
print(result)
assert result == True
incorrect_code_to_test = "(let x = {y: [1, 2, 3})"
incorrect_result = linter.lint(incorrect_code_to_test)
print(incorrect_result)
assert incorrect_result == "} has a mismatched opening brace"
