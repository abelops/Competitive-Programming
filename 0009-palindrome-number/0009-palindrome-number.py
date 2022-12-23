class Solution:
    def isPalindrome(self, x: int) -> bool:
        x= str(x)
        y = x[::-1]
        if int(x)<0:
            return False
        if x==y:
            return True
        else:
            return False