# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        while(head!=None):
            arr.append(head.val)
            head=head.next
        li = ListNode(0)
        head = li
        if(len(arr)%2==0):
            n=int(len(arr)/2)
            res = arr[n:len(arr)]
            for i in range(len(res)):
                no = ListNode(res[i])
                li.next = no
                li=li.next
            return head.next
        else:
            res = arr[int(len(arr)/2):len(arr)]
            for i in range(len(res)):
                no = ListNode(res[i])
                li.next = no
                li = li.next
            return head.next