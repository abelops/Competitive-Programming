class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        ma = max(arr)
        st = [arr[0]]
        d = "inc"
        if len(arr) == 1 or arr.index(ma) == len(arr)-1:
            return False
        for i in range(1,len(arr)):
            if d == "inc":
                if st[-1] >= arr[i]:
                    return False
                else:
                    st.append(arr[i])
            else:
                if st[-1] <=  arr[i]:
                    return False
                else:
                    st.append(arr[i])
            if arr[i] == ma:
                d = "dec"
        return True
        
        