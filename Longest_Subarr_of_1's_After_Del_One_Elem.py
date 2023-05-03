# Given a binary array nums, you should delete one element from it.
#
# Return the size of the longest non-empty subarray containing only 1's in the resulting array.
# Return 0 if there is no such subarray.
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if 0 not in nums or nums.count(0) == 1:
            return len(nums) - 1
        else:
            nulls = []

            for i in range(len(nums)):
                if nums[i] == 0:
                    nulls.append(i)

            res = [nulls[1] - 1]

            for j in range(2, len(nulls)):
                res.append(nulls[j] - nulls[j - 2] - 2)

            res.append(len(nums) - nulls[-2] - 2)

            return max(res)
