# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head: return None
        prev, curr = head, head
        size = 0
        i = 0
        temp = head
        while temp:
            size += 1
            temp = temp.next
            
        target = size - n
        while curr and i < target:
            prev = curr
            curr = curr.next
            i += 1

        if target == 0:
            return head.next
        elif target < size:
            prev.next = curr.next
        else:
            prev.next = None
        return head