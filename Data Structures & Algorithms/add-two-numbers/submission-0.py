# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = l1, l2
        r = 0
        head = None
        cur = None
        while n1 or n2 or r:
            a = n1.val if n1 else 0
            b = n2.val if n2 else 0
            s = a + b + r
            newValue = 0
            if s >= 10:
                r = 1
                newValue = s - 10
            else:
                r = 0
                newValue = s
            newNode = ListNode(newValue)
            if not head:
                head = newNode
                cur = newNode
            else:
                cur.next = newNode
                cur = newNode
            if n1: n1 = n1.next
            if n2: n2 = n2.next
        return head
