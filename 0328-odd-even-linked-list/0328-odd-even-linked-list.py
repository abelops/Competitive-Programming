# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = ListNode(0)
        even = ListNode(0)
        i = 1
        if not head:
            return head
        while head:
            if i % 2 == 0:
                e = even
                while e.next:
                    e = e.next
                e.next = ListNode(head.val)
            else:
                o = odd
                while o.next:
                    o = o.next
                o.next = ListNode(head.val)
            head = head.next
            i+=1
        o.next.next = even.next
        return odd.next
            
                