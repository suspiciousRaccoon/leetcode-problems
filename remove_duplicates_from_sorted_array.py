"""
This problem is not very well written.
This is a comment that describes what must be done, written by nvythedead

"They don't really want you to remove the duplicates. They want you to sort the uniques at the front, then return the length of the sorted part. Then, behind the scenes, they slice the array at the length you give them and the result of that is what they check."
"Just FYI, this sh_t drove me crazy..."


"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            else:
                nums[counter] = nums[i]
                counter += 1
        return counter

# I'm not writting testcases lol
