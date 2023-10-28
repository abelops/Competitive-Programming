class Solution:
    def isValid(self, s: str) -> bool:
        mp = {')':'(', '}':'{', ']':'['}
        st = []
        for c in s:
            if len(st)==0 or not c in mp.keys():
                st.append(c)
            elif mp.get(c)==st[-1]:
                st.pop()
            else:
                st.append(c)
        return len(st)==0