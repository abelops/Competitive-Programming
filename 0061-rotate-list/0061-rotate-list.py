# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        tot = 0
        temp = head
        if not head or not head.next or k == 0:
            return head
        while temp:
            temp = temp.next
            tot += 1
        if k >= tot:
            k= k % tot
        if k == 0:
            return head
        ans = head
        count = 0
        fin = ListNode(-1)
        while ans:
            if count == tot - k -1:
                temps = ans.next
                ans.next = None
                fin.next = temps                
                break
            ans = ans.next
            count += 1

        dummy = temps
        while dummy and dummy.next:
            dummy = dummy.next
        dummy.next = head
        return temps
                