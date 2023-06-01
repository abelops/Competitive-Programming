class Solution:
    def rob(self, nums: List[int]) -> int:
        numCop = nums.copy()
        for i in range(1, len(nums)):
            if i > 2:
                numCop[i] = numCop[i] + max(numCop[1:i-1])
        # print(numCop)
        ans1 = max(numCop)
        numCop = nums.copy()
        for i in range(len(nums)-1):
            if i > 1:
                numCop[i] = numCop[i] + max(numCop[:i-1])
        ans2 = max(numCop)
        return max(ans1, ans2)
                