# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        st = []
        c = -1
        dum = ListNode(-1,head)
        while dum:
            c+=1
            dum = dum.next
        ans = [0] * c
        
        i = 0
        while head:
            if not st:
                st.append((i, head.val))
                head = head.next
                i+=1
                continue
            while st and st[-1][1] < head.val:
                ans[st[-1][0]] = head.val
                st.pop()
            st.append((i, head.val))
            i+=1
            head = head.next
            
            
        return ans