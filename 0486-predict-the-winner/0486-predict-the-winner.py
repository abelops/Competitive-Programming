class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:     
        lens = len(nums)
        hasMemo = [[False] * (lens + 1) for _ in range(lens+1)]
        memo = [[None] * (lens + 1) for _ in range(lens+1)]
        def pred(arr, l, r):
            if l > r:
                return 0
            if hasMemo[l][r]:
                return memo[l][r]
            hasMemo[l][r] = True
            memo[l][r] = max((arr[l] - pred(arr,l+1,r)), (arr[r] - pred(arr,l,r-1))) 
            return memo[l][r]
        return pred(nums, 0, len(nums)-1) >= 0