class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prl = [nums[0]]
        rev = nums[::-1]
        prr = [rev[0]]
        for i in range(1,len(nums)):
            prl.append(nums[i]+prl[-1])
            prr.append(rev[i]+prr[-1])
        prr.reverse()
        for i in range(len(nums)):
            if(prl[i]==prr[i]):
                return i
        return -1