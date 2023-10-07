"""
2, 1, +, 3, *
use operators with last 2 values
2 + 1, then the result is multiplied by 3

4, 13, 5, /, +
In this case we leave 4 in the stack and do 13 / 5 first, then we sum 4 and it's result

'10','6','9','3','+','-11','*','/','*','17','+','5','+'
we sum 9+3, then add it back to the stack, and add -11 to it. we do 9+3 multiplied by -11. then we divide it and so fort

the trick is to focus only on the last 2 numbers of the stack, and do operations and adding the result to the stack inmediatly

Note that:
    The valid operators are '+', '-', '*', and '/'.
    Each operand may be an integer or another expression.
    The division between two integers always truncates toward zero.
    There will not be any division by zero.
    The input represents a valid arithmetic expression in a reverse polish notation.
    The answer and all the intermediate calculations can be represented in a 32-bit integer.
"""


from typing import List


class Solution:
    def __init__(self):
        self.stack = []

    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            '+': lambda x, y: x+y,
            '-': lambda x, y: y-x,
            '*': lambda x, y: x*y,
            # <- division is decimal by default, also rounds towards 0
            '/': lambda x, y: int(y/x),
        }
        for i in range(len(tokens)):
            if tokens[i] not in operators:
                self.stack.append(int(tokens[i]))
            else:
                x, y = self.stack.pop(), self.stack.pop()
                self.stack.append(operators[tokens[i]](x, y))
        return self.stack[-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.evalRPN(['2', '1', '+', '3', '*']))
    print(solution.evalRPN(['4', '13', '5', '/', '+']))
    print(solution.evalRPN(['10', '6', '9', '3', '+',
          '-11', '*', '/', '*', '17', '+', '5', '+']))
    print(solution.evalRPN(['18']))
