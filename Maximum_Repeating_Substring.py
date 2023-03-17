class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        count = 0
        while True:
            if word * (count + 1) not in sequence:
                return count
            count += 1
