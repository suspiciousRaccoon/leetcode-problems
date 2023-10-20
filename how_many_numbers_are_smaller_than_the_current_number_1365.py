from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        d = {}
        for index, value in enumerate(sorted(nums)):
            if value not in d:
                d[value] = index
        return [d[value] for value in nums]


class BadSolution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            counter = 0
            for j in range(len(nums)):
                if nums[j] != nums[i] and nums[i] > nums[j]:
                    counter += 1
            answer.append(counter)
        return answer
