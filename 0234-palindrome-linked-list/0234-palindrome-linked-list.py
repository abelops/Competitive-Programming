# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getMidIndex(self,head):
        slow = head
        fast = head
        count = 0
        fastCount = 0
        while slow:
            slow = slow.next
            if fast and fast.next:
                fast = fast.next.next
                fastCount += 1
            count+=1
        return [fastCount, count]
    
    def reverseHalf(self,mid, ind):
        prev, cur = None, mid
        c = 0 
        while cur and c <= ind:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            c+=1
        return prev
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        outPut = self.getMidIndex(head)
        mid = outPut[0]
        # print(mid)
        if mid == -1:
            return False
        
        mid -=1
        # print("mid", mid)
        count = 0
        temp = head
        stat = False
        
        # print(temp.val)
        if outPut[1] == 2:
            if head.val != head.next.val:
                return False
        while temp:
            # print("count", count)
            if stat and rev and nex:
                # print(nex.val, rev.val)
                if rev.val != nex.val:
                    return False
                rev = rev.next
                nex = nex.next
                continue
            elif count == mid:
                nex = temp.next
                rev = self.reverseHalf(head, mid)
                if outPut[1] % 2 != 0:
                    nex = nex.next
                    if rev.val != nex.val:
                        return False
                stat = True
                # print(rev.val, nex.val)
            temp = temp.next 
            count+=1
        return True