# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        
        def build(l,r):
            if l == r:
                return None
            mid = (l+r)//2
            left = build(l, mid)
            node = TreeNode(arr[mid])
            right = build(mid+1, r)
            node.left = left
            node.right = right
            return node
        return build(0, len(arr))
        