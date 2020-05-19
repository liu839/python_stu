class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None
def partition(self, head: ListNode, x: int) -> ListNode:
    if not head :
        return
    low=0