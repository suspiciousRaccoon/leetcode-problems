from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return [int(digit) for digit in str(int("".join(map(lambda x: str(x), digits))) + 1)]


class SolutionForLoop:
    def plusOne(self, digits: List[int]) -> List[int]:
        array = []
        new_digits = str(int("".join(map(lambda x: str(x), digits))) + 1)
        for digit in new_digits:
            array.append(int(digit))
        return array


class NormalSolution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        elif len(digits) == 1 and digits[0] == 9:
            return [1, 0]
        else:
            digits[-1] = 0
            print(digits[0:-1])
            digits[0:-1] = self.plusOne(digits[0:-1])
            print(digits[0:-1])
            return digits
