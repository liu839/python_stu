# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return []
        real = head
        while real and real.val == val:
                head = real.next
                real = head
        try:   
            temp = real.next
            while temp:
                if temp.val == val:
                    real.next = temp.next
                else:
                    real = temp
                temp = real.next
        except:
            pass
        return head