from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        counter = 0
        uniques = 0
        for i in range(len(nums)):
            if nums[i - counter] == val:
                nums.pop(i - counter)
                counter += 1
            else:
                uniques += 1
        return uniques
