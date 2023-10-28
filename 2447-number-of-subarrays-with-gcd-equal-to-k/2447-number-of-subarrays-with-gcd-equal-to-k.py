class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)
        numsLen = len(nums)
        for i in range(numsLen):
            cur = 0
            for j in range(i, numsLen):
                cur = gcd(cur, nums[j])
                mp[cur]+=1
        return mp[k]