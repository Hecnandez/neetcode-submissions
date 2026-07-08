class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(l, i, total):
            if total == target:
                res.append(l.copy())
                return
            
            if i >= len(nums) or total > target:
                return

            l.append(nums[i])
            dfs(l, i, total + nums[i])

            l.pop()
            dfs(l, i + 1, total)

        dfs([], 0, 0)
        return res