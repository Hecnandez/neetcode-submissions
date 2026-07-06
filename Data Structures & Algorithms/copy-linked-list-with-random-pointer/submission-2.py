"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes = {None: None}
        temp = head
        while temp:
            # We save old nodes as keys rather than the value to ensure uniqueness
            nodes[temp] = Node(temp.val)
            temp = temp.next
        temp = head
        while temp:
            nodes[temp].next = nodes[temp.next]
            nodes[temp].random = nodes[temp.random]
            temp = temp.next

        return nodes[head]