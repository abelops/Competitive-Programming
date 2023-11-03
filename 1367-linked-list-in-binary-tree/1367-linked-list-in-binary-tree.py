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
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        check = ""
        while head:
            check+=str(head.val)
            head = head.next
        def dfs(cur, built, ans):
            if check in built or check == built: 
                return True
            if not cur:
                return ans
            ans =  ans or dfs(cur.left, built+str(cur.val), ans)
            ans = ans or dfs(cur.right, built+str(cur.val), ans)
            return ans
        return dfs(root, "", False)
        
        
            