from typing import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        operators = {"C": lambda: stack.pop(),
                     "D": lambda: stack.append(stack[-1]*2),
                     "+": lambda: stack.append(stack[-1] + stack[-2])}

        for operation in operations:
            if operation not in operators:
                stack.append(int(operation))
            else:
                operators[operation](stack)
        return sum(stack)


class SlowSolution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        operators = ["C", "D", "+"]
        for operation in operations:
            if operation not in operators:
                stack.append(int(operation))
            elif operation == "C":
                stack.pop()
            elif operation == "D":
                stack.append(stack[-1] * 2)
            elif operation == "+":
                stack.append(stack[-1] + stack[-2])
        return sum(stack)
