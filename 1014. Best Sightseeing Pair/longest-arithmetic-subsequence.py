class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        l = len(nums)
        mp = defaultdict(int)
        
        for i in range(l):
            for j in range(i+1, l):
                diff = nums[j] - nums[i]
                if mp[(i,diff)]:
                    mp[(j,diff)] = mp[(i,diff)] + 1
                else:
                    mp[(j,diff)] = 2
        return max(mp.values())