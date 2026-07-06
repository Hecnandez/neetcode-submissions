class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = []
        for i in range(len(nums)):
            diffs.append(target - nums[i])

        for j in range(len(nums) - 1, 0, -1):
            if nums[j] in diffs:
                return [diffs.index(nums[j]), j]