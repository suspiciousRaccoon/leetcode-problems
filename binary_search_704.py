from typing import List
from utils import binary_search


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return binary_search(nums, target)
