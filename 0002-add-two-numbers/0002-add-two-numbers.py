# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def revNum(self, head):
        num = ""
        cur = head
        while cur:
            num+=str(cur.val)
            cur = cur.next
        return num[::-1]
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = int(self.revNum(l1))
        l2 = int(self.revNum(l2))
        ans = str(l1+l2)[::-1]
        fin = ListNode(-1)
        temp = fin
        for i in ans:
            temp.next = ListNode(i)
            temp = temp.next
        return fin.next