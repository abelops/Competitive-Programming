class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tempLen = len(temperatures)
        ans = [0] * tempLen
        st = []
        for i in range(tempLen):
            while st and temperatures[st[-1]] < temperatures[i]:
                ind = st.pop()
                ans[ind] = i - ind
            st.append(i)
        return ans