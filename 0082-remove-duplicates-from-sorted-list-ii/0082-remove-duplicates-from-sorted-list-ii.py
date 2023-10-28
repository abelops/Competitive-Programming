# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head==None):
            return head
        stack = []
        rep = []
        temp = head
        cur = head.val
        while head:
            if(head.val in stack):
                stack.pop()
            elif(head.val not in rep):
                stack.append(head.val)
            rep.append(head.val)
            head=head.next
        li = ListNode(0)
        bac = li
        for i in stack:
            li.next=ListNode(i)
            li=li.next
        return bac.next
                
            