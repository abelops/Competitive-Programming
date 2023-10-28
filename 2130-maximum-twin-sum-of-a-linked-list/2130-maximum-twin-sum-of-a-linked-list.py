# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rev(self, head):
        prev, cur = None, head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev 
    def pairSum(self, head: Optional[ListNode]) -> int:
        ans = 0
        slow = head
        fast = head.next 
        while fast.next:
            fast = fast.next.next
            slow = slow.next
        revHalf = self.rev(slow.next)
        slow.next = revHalf
        slow = slow.next
        while slow:
            ans = max(slow.val + head.val, ans)
            head = head.next
            slow = slow.next
        return ans