class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prf = [nums[0]]
        rev = deque([nums[-1]])
        for i,ir in zip(range(1,len(nums)), range(len(nums)-2, -1,-1)):
            prf.append(prf[i-1]+nums[i])
            rev.appendleft(rev[0]+nums[ir])
        for i,(n1,n2) in enumerate(zip(prf, rev)):
            if(n1==n2):
                return i
        return -1