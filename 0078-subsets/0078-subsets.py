class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        leng = 2**len(nums)
        for i in range(leng):
            temp = []
            ch = i
            cur = len(nums)-1
            while ch > 0:
                if ch & 1:
                    temp.append(nums[cur])
                ch >>=1
                cur-=1
            ans.append(temp)
        return ans
    
    