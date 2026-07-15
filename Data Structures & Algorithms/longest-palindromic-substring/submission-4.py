class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        
        def expandMiddle(start, end):
            current = s[start:end + 1]
            while start - 1 >= 0 and end + 1 <= len(s) - 1 and s[start - 1] == s[end + 1]:
                start -= 1
                end += 1
                current = s[start:end + 1]
            
            return current

        for i in range(0, len(s)):
            start = i
            end = i
            while end < len(s) - 1 and s[end + 1] == s[start]:
                end += 1
            expansion = expandMiddle(start, end)
            if len(expansion) > len(res):
                res = expansion

        return res