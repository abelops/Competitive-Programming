# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = []
        num2 = []
        cur = l1
        while cur:
            num1.append(str(cur.val))
            cur = cur.next
        cur = l2
        while cur:
            num2.append(str(cur.val))
            cur = cur.next
        sums = str(int("".join(num1)) + int("".join(num2)))
        ans = ListNode()
        dummy = ans
        for i in sums:
            temp = ListNode(i)
            dummy.next = temp
            dummy = dummy.next
        return ans.next