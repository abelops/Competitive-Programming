# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head):
        l = ListNode(0,head)
        
        while l.next:
            if l.next.val % 2 != 0:
                l = l.next
                continue
            print(l.val)
            dum = l.next
            while dum.val % 2 == 0:
                dum = dum.next
            print("item:", dum)
            temp = l.next
            dum.next = temp
            l.next = dum
            print("head:", head)
            
            l = l.next
            
        return head


class createList():
    def create(li):
        head = ListNode(li[0])
        l = head
        for i in li[1:]:
            l.next = ListNode(i)
            l = l.next
        return head
inp = [1,2,3,4,5]
head = createList.create(inp)

s = Solution()
s.oddEvenList(head)
                