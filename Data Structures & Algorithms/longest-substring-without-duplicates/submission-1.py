class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        best = 0
        hashmap = set()
        while r < len(s):
            if s[r] not in hashmap:
                hashmap.add(s[r])
                best = max(len(hashmap), best)
                r += 1
            else:
                hashmap.remove(s[l])
                l += 1
        return best
    