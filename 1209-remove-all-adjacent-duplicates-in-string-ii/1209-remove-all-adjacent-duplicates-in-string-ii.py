class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st = []
        cur = ""
        count = 0
        for char in s:
            if not st:
                st.append((char, 1))
            else:
                if st[-1][0] == char:
                    if st[-1][1] == k-1:
                        for i in range(k-1):
                            st.pop()
                    else:
                        st.append((char, st[-1][1]+1))
                else:
                    st.append((char, 1))
        return "".join([x[0] for x in st])