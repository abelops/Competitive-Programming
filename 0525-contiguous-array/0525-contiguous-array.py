class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mp = {0:-1}
        s = 0
        ans = 0
        for i,n in enumerate(nums):
            if(n==0):
                s-=1
            else:
                s+=1
            if(s not in mp):
                mp[s]=i
            else:
                ans = max(ans, i-mp[s])
        return ans