class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st = []
        for i in s:
            if i == "(":
                st.append(i)
            elif i == ")":
                if st[-1] == "(":
                    st.pop()
                    if st:
                        if st[-1] != "(" and st[-1] != ")":
                            temp = st.pop() + 1
                            st.append(temp)
                        else:
                            st.append(1)
                    else:
                        st.append(1)
                else:
                    temp = st.pop()
                    st.pop()
                    if st:
                        if st[-1] != "(" and st[-1] != ")":
                            temp1 = st.pop()
                            st.append(temp1 + temp*2)
                        else:
                            st.append(temp * 2)
                    else:
                        st.append(temp * 2)
            # print(st)
        return st[-1]