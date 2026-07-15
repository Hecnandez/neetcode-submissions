class Solution:
    def rob(self, nums: List[int]) -> int:
        op1, op2 = 0, 0
        for n in nums:
            temp = max(n + op1, op2)
            op1 = op2
            op2 = temp

        return op2