class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        ans = set()
        for i in nums:
            if i > 9:
                ans.add(i)
                ans.add(int(str(i)[::-1]))
            else:
                ans.add(i)
        return len(ans)
        