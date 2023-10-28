class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set([n])
        def getSum(digits):
            digits = list(map(int, list(str(digits))))
            ans = [x*x for x in digits]
            return sum(ans)
        
        while True:
            n = getSum(n)
            if n == 1:
                return True
            if n in visited:
                return False
            visited.add(n)
        
        
            
        return True