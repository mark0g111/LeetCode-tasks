# Given two integer arrays pushed and popped each with distinct values,
# return true if this could have been the result of a sequence of push
# and pop operations on an initially empty stack, or false otherwise.

from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        res = [pushed[0]]
        i = 1
        j = 0
        while j < len(popped):
            if len(res) != 0 and res[-1] == popped[j]:
                res.pop()
                j += 1
            else:
                if i < len(pushed):
                    res.append(pushed[i])
                    i += 1
                else:
                    break
        return res == []
