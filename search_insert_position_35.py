import bisect
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        length = len(nums)
        if target <= nums[0]:
            return 0
        elif target > nums[-1]:
            return length
        for i in range(1, length):
            if nums[i-1] < target and nums[i] >= target:
                return i


# 1 liner, not sure what this is lol

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect.bisect_left(nums, target)

# binary search

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if target == nums[middle]:
                return middle
            elif target > nums[middle]:
                left = middle + 1
            else:
                right = middle - 1

        return left  # we return left because the target value is equal to left +1 in case its not present, and right can end up as lesser than left

# added to utils too!
