class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)
        runningSum = 0
        ans = 0
        mp[0] = 1
        for i in nums:
            runningSum += i
            ans += mp[runningSum % k]
            mp[runningSum % k] += 1
        return ans
