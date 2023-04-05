class Solution:
    def minSteps(self, n: int) -> int:
        def factorize(n):
            ans= []
            i = 2
            while i < n: 
                while n % i == 0:
                    ans.append(int(i))
                    n /= i
                i+=1
            if n != 1:
                ans.append(int(n))
            return ans
        return sum(factorize(n))
        
                