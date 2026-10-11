# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s, f = head, head.next
        while f and f.next:
            s = s.next
            f = f.next.next
        
        second = s.next
        s.next = None
        prev = s.next
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2





