class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        nums = []
        ans = 0
        for i in instructions:
            if not nums:
                nums.append(i)
            else:
                loc = bisect.bisect_right(nums, i)
                loc1 = bisect.bisect_left(nums, i)
                ans+=min(loc1, len(nums)-loc)
                nums.insert(loc, i)
                # nums = nums[:loc] + [i] + nums[loc:]
        return ans % (10**9 +7)