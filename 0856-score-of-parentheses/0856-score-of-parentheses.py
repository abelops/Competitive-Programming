class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st = [0]
        for i in s:
            if i == ")":
                temp = st.pop()
                if temp == 0:
                    st[-1] += 1
                else:
                    st[-1] += 2 * temp
            else:
                st.append(0)
        return st[0]
                
    
            