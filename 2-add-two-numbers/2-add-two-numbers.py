# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = ""
        while(l1!=None):
            n1+=str(l1.val)
            l1 = l1.next
        n2 = ""
        while(l2!=None):
            n2+=str(l2.val)
            l2 = l2.next
        n1 = n1[-1::-1]
        n2 = n2[-1::-1]
        sums = int(n1) + int(n2)
        sums = list(str(sums))
        sums.reverse()
        
        dummy = ListNode(0)        
        head = dummy        
        for i in sums:
            newNode = ListNode(i)
            head.next = newNode
            head = head.next             
        return dummy.next
            