# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def revList(self, head):
        prev, cur = None, head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev
    def getDecimalValue(self, head: ListNode) -> int:
        rev = self.revList(head)
        ans = 0
        c = 0 
        while rev:
            ans+=rev.val * (2 ** c)
            rev = rev.next
            c+=1
        return ans
        