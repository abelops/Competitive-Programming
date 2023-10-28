class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def getFact(n):
            ans = set()
            i = 2
            while n>1:
                while n % i == 0:
                    ans.add(i)
                    n//=i
                i+=1
            return ans
        fin = set()
        for i in nums:
            fin.update(getFact(i))
        return len(fin)