class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = set(nums)
        return (len(hashmap) != len(nums))