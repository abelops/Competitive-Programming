# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stat = False
        if not head or not head.next:
            return None
        slow = head
        fast = head.next
        while fast and fast.next:
            if slow == fast:
                stat = True
                break
            slow = slow.next
            fast = fast.next.next
        if stat:
            slow = head
            fast = fast.next
            while True:
                if slow == fast:
                    return fast
                slow = slow.next
                fast = fast.next
        return None