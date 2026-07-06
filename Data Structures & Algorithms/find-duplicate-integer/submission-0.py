class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        aps = set()
        for num in nums:
            if num in aps: return num
            aps.add(num)