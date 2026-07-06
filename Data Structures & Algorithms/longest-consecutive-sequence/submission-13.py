class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums = sorted(set(nums))
        print("my nums: ", nums)
        best = 1
        current = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                current += 1
                best = max(current, best)
            else:
                current = 1
        return best