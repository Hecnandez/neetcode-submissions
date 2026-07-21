class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memory = [1] * len(nums)

        for i in range(len(nums) - 1, - 1, - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    memory[i] = max(memory[i], 1 + memory[j])
        
        return max(memory)