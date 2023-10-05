from typing import List


class Solution():
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for i in range(len(nums)):
            if nums[i]-1 not in nums_set:
                length = 0
                while nums[i] + length in nums_set:
                    length += 1
                longest = max(length, longest)
        return longest


if __name__ == "__main__":
    test = Solution()
    print(test.longestConsecutive([100, 4, 200, 1, 3, 2]))
    test = Solution()
    print(test.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
