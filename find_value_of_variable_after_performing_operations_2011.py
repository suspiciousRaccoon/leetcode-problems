"""
Felt like doing an easy one today :3
"""

from typing import List


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        operations_table = {
            "++X": lambda x: x+1,
            "X++": lambda x: x+1,
            "--X": lambda x: x-1,
            "X--": lambda x: x-1,
        }

        variable = 0

        for i in range(len(operations)):
            variable = operations_table[operations[i]](variable)
        return variable
