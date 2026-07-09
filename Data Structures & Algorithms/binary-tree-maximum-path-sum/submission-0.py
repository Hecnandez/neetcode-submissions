# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(current):
            if not current:
                return 0

            leftMax = max(dfs(current.left), 0)
            rightMax = max(dfs(current.right), 0)
            res[0] = max(res[0], current.val + leftMax + rightMax)
            return max(leftMax, rightMax) + current.val

        dfs(root)
        return res[0]
