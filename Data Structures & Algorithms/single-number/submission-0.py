class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {n: 0 for n in nums}

        for n in nums:
            count[n] += 1

        for n in nums:
            if count[n] == 1: return n