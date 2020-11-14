# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p, q = head, head.next
        master = q
        flag = 1
        temp = 0
        while True:
            p.next = q.next
            q.next = p
            if temp:
                temp.next=q
            if p.next:
                if not p.next.next:
                    break
                temp = p
                p = p.next
                q = p.next
            else:
                break
        return master