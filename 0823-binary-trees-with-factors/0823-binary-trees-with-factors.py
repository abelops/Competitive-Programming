class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        l = len(arr)
        store = set(arr)
        ans = l
        arr.sort()
        dp = [1] * l
        for i in range(l):
            for j in range(i):
                if not arr[i] % arr[j] and arr[i] // arr[j] in store:
                    pos = arr.index(arr[i] // arr[j])
                    dp[i]+= dp[j] * dp[pos]
            
        return sum(dp) % (10 ** 9 + 7)
                    
            