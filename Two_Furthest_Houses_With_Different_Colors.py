# There are n houses evenly lined up on the street, and each house is beautifully painted.
# You are given a 0-indexed integer array colors of length n, where colors[i] represents the color of the ith house.
# Return the maximum distance between two houses with different colors.

from typing import List


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        l = len(colors)
        i = 0
        j = l - 1
        while colors[j] == colors[0]:
            j -= 1
        while colors[i] == colors[l-1]:
            i += 1
        return max(j, l-1-i)
