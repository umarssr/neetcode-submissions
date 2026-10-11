# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        myset = set()
        while head.next != None:
            if head in myset:
                return True
            myset.add(head)
            head = head.next
        return False
        