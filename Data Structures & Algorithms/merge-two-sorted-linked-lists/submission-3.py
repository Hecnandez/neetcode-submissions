# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        res = None
        i, j = list1, list2
        while i or j:
            val = 0
            if i and (not j or i.val <= j.val):
                val = i.val
                i = i.next
            else:
                val = j.val
                j = j.next

            if res == None:
                res = ListNode(val)
                head = res
            else:
                newNode = ListNode(val)
                res.next = newNode
                res = newNode
        return head