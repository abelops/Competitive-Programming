# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = head
        r = head
        
        while l:
            while r and r.val == l.val:
                r = r.next
            l.next = r
            l = l.next
            
        return head 
        