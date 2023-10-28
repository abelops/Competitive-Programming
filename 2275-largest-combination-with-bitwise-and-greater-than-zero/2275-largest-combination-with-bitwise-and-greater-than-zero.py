class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        curMax = [0,0]
        maxLen = max(candidates).bit_length()
        ans = [0] * maxLen
        for i in range(maxLen, -1, -1):
            temp = 0
            ch = 1 << i
            for j in candidates:
                if j & ch:
                    temp+=1
            ans[i-1]= temp 
        return max(ans)