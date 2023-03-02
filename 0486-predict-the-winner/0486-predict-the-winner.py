class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:        
        def pred(arr, l, r):
            if l > r:
                return 0
            return max((arr[l] - pred(arr,l+1,r)), (arr[r] - pred(arr,l,r-1))) 
        return pred(nums, 0, len(nums)-1) >= 0