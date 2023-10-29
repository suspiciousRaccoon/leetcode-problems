from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}  # num:index
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[nums[i]] = i
        return


class BadSolution():
    def twoSum(self, nums, target):
        for index_1, number_1 in enumerate(nums):
            for index_2, number_2 in enumerate(nums):
                if index_1 is not index_2 and number_1 + number_2 == target:
                    return [index_1, index_2]
