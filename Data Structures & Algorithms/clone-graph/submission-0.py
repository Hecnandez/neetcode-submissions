"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node or node == []: return node

        nodes = {}
        def bfs(node):
            if node in nodes: return

            nodes[node] = Node(node.val)
            nodes[node].neighbors = []
            for n in node.neighbors:
                bfs(n)

        bfs(node)

        for original in nodes.keys():
            copy = nodes[original]
            for n in original.neighbors:
                copy.neighbors.append(nodes[n])

        return nodes[node]