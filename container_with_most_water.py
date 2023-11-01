from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        max_area = 0
        while left < right:
            max_area = max(max_area, (right-left) *
                           min(heights[left], heights[right]))
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_area

    def BruteForcemaxArea(self, heights: List[int]) -> int:
        max_area = 0
        for left in range(len(heights)):
            for right in range(left + 1, len(heights)):
                max_area = max(max_area, (right-left) *
                               min(heights[left], heights[right]))
        return max_area
