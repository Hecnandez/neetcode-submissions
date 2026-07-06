# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res = []
        level = 0

        def addChildren(level, node):
            if not node: return
            if level < len(res):
                res[level].append(node.val)
            else:
                res.append([node.val])
            if node.left: addChildren(level + 1, node.left)
            if node.right: addChildren(level + 1, node.right)

        addChildren(level, root)
        return res