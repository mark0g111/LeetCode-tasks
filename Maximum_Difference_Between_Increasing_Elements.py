# Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j]
# (i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].
#
# Return the maximum difference. If no such i and j exists, return -1.
from typing import List


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        max_dif = -1
        min_num = nums[0]
        for i in range(len(nums)):
            max_dif = max(max_dif, nums[i] - min_num)
            min_num = min(min_num, nums[i])
        if max_dif == 0:
            max_dif = -1
        return max_dif
