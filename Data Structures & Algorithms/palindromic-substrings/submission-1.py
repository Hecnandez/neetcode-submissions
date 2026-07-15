class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        def expandMiddle(start, end):
            current = 1
            while start - 1 >= 0 and end + 1 <= len(s) - 1 and s[start - 1] == s[end + 1]:
                start -= 1
                end += 1
                current += 1
            
            return current

        for i in range(0, len(s)):
            start = i
            end = i
            while end < len(s) - 1 and s[end + 1] == s[start]:
                end += 1
                res += 1
            res += expandMiddle(start, end)

        return res