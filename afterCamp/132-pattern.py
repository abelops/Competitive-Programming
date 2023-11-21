class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        mins = [nums[0]]
        for i in range(1, len(nums)):
            mins.append(min(nums[i], mins[-1]))
        st = []
        for i in range(len(nums)):
            if not st:
                st.append(i)
            else:
                while st and nums[st[-1]] <= nums[i]:
                    st.pop()
                # if st:
                #     print(st, mins[st[-1]], nums[i])
                if st and mins[st[-1]] < nums[i]:
                    return True
                st.append(i)
        return False
