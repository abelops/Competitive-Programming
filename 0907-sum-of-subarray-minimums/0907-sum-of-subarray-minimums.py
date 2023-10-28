class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        st = []
        leng = len(arr)
        b1 = [0] *  leng
        b2 = [0] * leng
        
        for i in range(len(arr)):
            while st and arr[st[-1]] >= arr[i]:
                poped = st.pop()
                b1[poped] = i - poped
            st.append(i)
            
        while st:
            poped = st.pop()
            b1[poped] = leng - poped
        st = []
        for i in range(leng-1, -1, -1):
            while st and arr[st[-1]] > arr[i]:
                poped = st.pop()
                b2[poped] = poped - i
            st.append(i)
        while st:
            poped = st.pop()
            b2[poped] = poped + 1
        ans = 0 
        for i in range(len(arr)):
            ans+= arr[i] * b1[i] * b2[i]
            
        return ans % (10**9 + 7)