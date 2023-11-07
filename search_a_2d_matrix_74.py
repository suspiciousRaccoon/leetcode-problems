from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1

        while left <= right:
            mid = (left + right) // 2
            row, col = mid // cols, mid % cols
            guess = matrix[row][col]

            if guess == target:
                return True
            elif guess < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

    def DoubleBinarySearchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        top, bot = 0, len(matrix) - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        if not (top <= bot):
            return False
        row = (top + bot) // 2
        left, right = 0, len(matrix[row]) - 1
        while left <= right:
            middle = (left + right) // 2
            if target > matrix[row][middle]:
                left = middle + 1
            elif target < matrix[row][middle]:
                right = middle - 1
            else:
                return True
        return False

    def BruteForceSearchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            for num in matrix[i]:
                if num == target:
                    return True
        return False
