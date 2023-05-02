# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
#
# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        max_num = 0
        for i in range(k):
            if s[i] in vowels:
                max_num += 1
        cur_num = max_num
        for i in range(1, len(s) - k + 1):
            if s[i - 1] in vowels:
                cur_num -= 1
            if s[i + k - 1] in vowels:
                cur_num += 1
            max_num = max(max_num, cur_num)
        return max_num
