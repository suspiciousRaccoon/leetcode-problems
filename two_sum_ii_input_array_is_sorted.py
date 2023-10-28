from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        2 pointer approach, depending on the result of target_sum we either move the right_index to the left, or the left_index to the right
        We are guaranteed this approach works due to numbers being in non-decreasing order, and there being always a solution.
        """
        left_index, right_index = 1, len(numbers) - 1

        while left_index < right_index:
            target_sum = numbers[left_index] + numbers[right_index]
            if target_sum > target:
                right_index -= 1
            elif target_sum < target:
                left_index += 1
            else:
                return [left_index + 1, right_index + 1]
        return []

    def SlowtwoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(0, len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1]
