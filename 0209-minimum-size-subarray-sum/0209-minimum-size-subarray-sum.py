class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r=0,0
        ans=[]
        su=0
        ind = True
        while l<len(nums):
            if ind:
                su+=nums[r]
            if(su>=target):
                while su>=target:
                    ans.append(r-l+1)
                    su-=nums[l]
                    l+=1
            if r+1<len(nums):
                r+=1
            else:
                ind=False
                if l<len(nums):
                    su-=nums[l]
                    l+=1
        if len(ans)==0:
            return 0
        return min(ans)
        