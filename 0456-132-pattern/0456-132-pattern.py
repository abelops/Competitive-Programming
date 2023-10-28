class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        mins = []
        for i in range(len(nums)):
            if i == 0:
                mins.append(i)
            else:
                if nums[i] < nums[mins[-1]]:
                    mins.append(i)
                else:
                    mins.append(mins[-1])
        st = []
        for i in range(len(nums)):
            while st and nums[st[-1]] <= nums[i]:
                st.pop()
            if st:
                if nums[mins[st[-1]]] < nums[i]:
                    return True
            st.append(i)
        return False
                