class Solution:
    def rob(self, nums: List[int]) -> int:
        tot = len(nums)
        def recur(n, amount, flag, memo):
            if flag and n == tot-1:
                return amount
            if n >= tot:
                return amount
            if (n, amount) in memo:
                return memo[(n, amount)]
            left = recur(n+2, amount + nums[n], flag, memo)
            right = recur(n+1, amount, flag, memo)
            maxi = max(left, right)
            memo[(n, amount)] = maxi
            return maxi
        if len(nums) == 1:
            return nums[0]
        return max(recur(0, 0, True, {}), recur(1,0, False, {}))
                