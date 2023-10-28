# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def dis(self):
        dum = self.head 
        while dum and dum.next:
            print(dum.val)
            dum = dum.next
            
    def reverseList(self, head, start, end):
        prev, cur = None, head
        lastVal = None
        count = 0
        while count < end - start+1:
            tem = cur.next
            cur.next = prev
            prev = cur
            cur = tem
            count+=1
        # self.dis()
        return [prev, tem]
        
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        c = 1
        dummy = ListNode(0)
        dummy.next = head
        temp = dummy
        self.head = head
        if left == right:
            return head
        while temp.next != None:
            if c == left:
                ans = self.reverseList(temp.next, left, right)
                temp.next = ans[0]
            temp = temp.next
            c+=1
        if dummy.next != None and right - left + 1 > 0:
            temp.next = ans[1]
        # self.dis()
        return dummy.next