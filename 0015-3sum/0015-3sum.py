class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        mp={}
        ans = []
        nums.sort()
        for i,n in enumerate(nums):
            if i>0 and n==nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                if l==r:
                    break
                if nums[l]+nums[r]+n == 0:
                    a = [n,nums[l],nums[r]]
                    if a not in ans:
                        ans.append(a)
                if nums[l]+nums[r]+n > 0:
                    r-=1
                else:
                    l+=1
        return ans