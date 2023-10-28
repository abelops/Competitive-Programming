class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        mp = defaultdict(int)
        for i in range(len(nums)):
            mp[i] = nums[i]
        nums = sorted(nums)
        ans = []
        mpItems = mp.items()
        for i in range(len(mpItems)):
            ans.append(nums.index(mp[i]))
        return ans
        