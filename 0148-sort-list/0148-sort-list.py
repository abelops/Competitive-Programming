# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def getMid(node):
            slow = node
            fast = node.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        def merge(node1, node2):
            ans = dum = ListNode()
            while node1 and node2:
                if node1.val > node2.val:
                    ans.next = node2
                    node2 = node2.next
                else:
                    ans.next = node1
                    node1 = node1.next
                ans = ans.next
            if node1:
                ans.next = node1
            if node2:
                ans.next = node2
                
            return dum.next
        
        
        if not head or not head.next:
            return head
        
        leftSide = head
        rightSide = getMid(head)
        temp = rightSide.next
        rightSide.next = None
        rightSide = temp
        
        leftSide = self.sortList(leftSide)
        rightSide = self.sortList(rightSide)
        return merge(leftSide, rightSide)
        
        
        return head
        
            