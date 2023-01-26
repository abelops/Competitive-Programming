class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        r = int(sqrt(c))
        l = 0
        while l <= r:
            if l**2 + r**2 == c:
                return True
            if l**2 + r**2 > c:
                r -= 1
            elif l**2 + r**2 < c:
                l +=1
        return False
        
        