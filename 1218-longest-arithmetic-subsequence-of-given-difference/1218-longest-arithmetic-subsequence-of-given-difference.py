class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        leng = len(arr)
        mp = defaultdict(int)
        maxi = -float("inf")
        for i in arr:
            n = i - difference
            mp[i] = mp[n] + 1
            maxi = max(maxi, mp[i])
        return maxi