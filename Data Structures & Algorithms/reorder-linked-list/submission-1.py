# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        q = collections.deque()
        cur = head
        while cur:
            q.append(cur)
            cur = cur.next
        
        half = len(q) // 2
        for i in range(0, half if len(q) % 2 else half - 1, 1):
            last = q.pop()
            last.next = q[i].next
            q[i].next = last
            q[-1].next = None