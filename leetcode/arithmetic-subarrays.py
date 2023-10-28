class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for i in range(len(l)):
            sub = nums[l[i]:r[i]+1]
            sub.sort()
            stat = True
            ga = sub[1]-sub[0]
            for j in range(len(sub)-1):
                if(sub[j+1]-sub[j]!=ga):
                    stat=False
            ans.append(stat)
        return ans
                
            