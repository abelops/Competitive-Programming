class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)
        fin = []
        for i in nums:
            if ans[i-1] == i:
                fin.append(i)
            ans[i-1] = i
        return fin