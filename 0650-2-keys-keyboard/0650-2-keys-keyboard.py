class Solution:
    def minSteps(self, n: int) -> int:
        ans= 0
        i = 2
        while i < n: 
            while n % i == 0:
                ans+=int(i)
                n /= i
            i+=1
        if n != 1:
            ans+=int(n)
        return ans
        
                