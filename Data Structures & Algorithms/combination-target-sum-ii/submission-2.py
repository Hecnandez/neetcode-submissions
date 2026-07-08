class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(l, i, total):
            if total == target and l not in res:
                res.append(l.copy())

            if i >= len(candidates) or total > target:
                return

            l.append(candidates[i])
            dfs(l, i + 1, total + candidates[i])

            l.pop()
            while i < len(candidates) - 1 and candidates[i] == candidates[i+1]:
                i += 1
            dfs(l, i + 1, total)
        
        dfs([], 0, 0)
        return res