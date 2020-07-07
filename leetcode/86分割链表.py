class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        l1=ListNode(None)
        l2=ListNode(None)
        p1=l1
        p2=l2
        while head:
            if head.val<x:
                p1.next=head
                p1=p1.next
            elif head.val>=x:
                p2.next=head
                p2=p2.next
            head=head.next
        p1.next=l2.next
        p2.next=None
        return l1.next