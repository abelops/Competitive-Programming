class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def recur(n, amount):
            # print(n, amount)
            if n >= len(nums):
                return amount
            if (n, amount) in memo:
                return memo[(n, amount)]
            left = recur(n+2, amount + nums[n])
            right = recur(n+1, amount)
            maxi = max(left, right)
            memo[(n, amount)] = maxi
            return maxi
        return recur(0, 0)
            
                
            