# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head :
            return 
            
        a = head
        b = root = head.next
        while a.next and b.next:
            a.next = b.next
            a = a.next
            b.next = a.next
            b = b.next

        a.next = root
    
        return head