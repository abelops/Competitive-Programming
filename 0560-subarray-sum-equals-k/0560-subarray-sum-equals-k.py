class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = {0:1}
        su = 0
        cou = 0
        for i in nums:
            su+=i
            if(su-k in mp):
                cou+=mp[su-k]
            if(su not in mp):
                mp[su]=1
            else:
                mp[su]+=1
        return cou