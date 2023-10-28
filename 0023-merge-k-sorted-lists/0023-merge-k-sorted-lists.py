# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans = ListNode(0)
        head = ans
        ar = []
        an = set([])
        while len(an) <len(lists):
            for i in range(len(lists)):
                if(lists[i]==None):
                    an.add(i)
                else:
                    ar.append(lists[i].val)
                    lists[i]=lists[i].next
        ar.sort()
        print(ar)
        for i in ar:
            ans.next = ListNode(i)
            ans=ans.next
        return head.next