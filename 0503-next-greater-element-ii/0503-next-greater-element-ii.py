class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        st = []
        lens = len(nums[:])
        nums.extend(nums)
        ans = [-1] * (len(nums))
        for i in range(len(nums)):
            while st and nums[st[-1]] < nums[i]:
                temp = st.pop()
                ans[temp] = nums[i]
            st.append(i)
        return ans[:lens]
        