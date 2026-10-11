# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        counter = 0
        curr = head
        while curr:
            counter +=1
            curr = curr.next
        if n == counter:
            return head.next
        target = counter - n -1
        counter2 = 0
        curr2 = head
        while counter2 != target:
            curr2 = curr2.next
            counter2 +=1
        curr2.next = curr2.next.next
        return head

        