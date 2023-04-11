# You are given a string s, which contains stars *.
#
# In one operation, you can:
#
# Choose a star in s.
# Remove the closest non-star character to its left, as well as remove the star itself.
# Return the string after all stars have been removed.

class Solution:
    def removeStars(self, s: str) -> str:
        if s.count('*') == len(s) / 2:
            return ''
        else:
            res = []
            for i in s:
                if i != '*':
                    res.append(i)
                else:
                    res.pop()
        return ''.join(res)
