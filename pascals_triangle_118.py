from typing import List


class Solution:
    def generate(self, num_rows: int) -> List[List[int]]:
        output = [[1]]
        for _ in range(1, num_rows):
            output.append(
                [a + b for a, b in zip([0] + output[-1], output[-1] + [0])])
        return output
