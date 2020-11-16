# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        p, q = head, head
        while q:
            if q.val < x:
                q.val, p.val = p.val, q.val
                p = p.next
            q = q.next
        return head
