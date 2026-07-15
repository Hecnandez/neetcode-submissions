class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        last = nums.pop()
        opA1, opA2 = 0, 0
        for n in nums:
            temp = max(n + opA1, opA2)
            opA1 = opA2
            opA2 = temp

        nums.append(last)
        nums.reverse()
        nums.pop()
        opB1, opB2 = 0, 0
        for n in nums:
            temp = max(n + opB1, opB2)
            opB1 = opB2
            opB2 = temp

        return max(opA2, opB2)