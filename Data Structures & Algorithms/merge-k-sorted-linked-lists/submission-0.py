# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        front = None
        rear = None
        while True:
            targetIndex = -1
            smallestHead = 1001
            for i, head in enumerate(lists):
                if not head: continue
                if head.val <= smallestHead:
                    targetIndex = i
                    smallestHead = head.val
            if targetIndex == -1: break
            if not front:
                front = rear = lists[targetIndex]
            else:
                rear.next = lists[targetIndex]
                rear = lists[targetIndex]    
            lists[targetIndex] = lists[targetIndex].next
        return front