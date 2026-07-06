# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1: return head
        
        def reverseSection(section):
            for i in range(k - 1, 0, -1):
                section[i].next = section[i-1]
        
        sections = []
        currSection = []
        tmp = head
        while tmp:
            currSection.append(tmp)
            if len(currSection) == k:
                sections.append(currSection)
                currSection = []
            tmp = tmp.next
        
        for section in sections:
            reverseSection(section)

        # Connect sections
        for i in range(len(sections) - 1):
            sections[i][0].next = sections[i+1][-1]

        # leftover nodes
        sections[-1][0].next = currSection[0] if currSection else None

        return sections[0][-1]