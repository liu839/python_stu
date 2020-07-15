def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    newNode=ListNode(0)
    ansNode=newNode
    flag=-1
    while l1 or l2 or flag:
        if flag!=-1:
            newNode.next=ListNode(0)
            newNode=newNode.next
        else:
            flag=0
        if l1 and l2:
            sum=l1.val+l2.val
            l1=l1.next
            l2=l2.next
        elif l1:
            sum=l1.val
            l1=l1.next
        elif l2:
            sum=l2.val
            l2=l2.next
        else:
            sum=0
        newNode.val=(sum+1)%10 if flag==1 else sum%10
        flag=1 if sum+flag>9 else 0 
    return ansNode