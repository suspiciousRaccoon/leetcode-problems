import bisect
from typing import List
from utils import binary_search


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return binary_search(nums, target)

    def search_bisec(self, nums: List[int], target: int) -> int:
        index = bisect.bisect_left(nums, target)
        return index if index < len(nums) and nums[index] == target else -1
