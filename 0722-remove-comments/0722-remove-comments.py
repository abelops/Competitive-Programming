class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        st = []
        multiComment = False
        
        for i in range(len(source)):
            for j in range(len(source[i])):
                if len(st) > 0:
                    if st[-1] == "/" and source[i][j] == "/":
                        st.pop()
                        st.append("/n")
                        break
                    elif st[-1] == "/" and source[i][j] == "*":
                        multiComment = True
                        st.pop()
                        continue
                if not multiComment:
                    st.append(source[i][j])
                    if j == len(source[i])-1:
                        st.append("/n")
                elif multiComment:
                    if len(st) > 0:
                        if st[-1] == "*" and source[i][j] == "/":
                            multiComment = False
                            while len(st) > 0:
                                if st[-1] == "*":
                                    st.pop()
                                else:
                                    break
                            if j == len(source[i])-1 and i > 0 and i < len(source)-1:
                                st.append("/n")
                        elif st[-1] == "*" and source[i][j] != "/":
                            st.pop()
                    if source[i][j] == "*":
                        st.append("*")
                        
        ans = []
        tmp = []
        for i in st:
            if i != "/n":
                tmp.append(i)
            else:
                if len(tmp) > 0:
                    ans.append("".join(tmp))
                tmp = []
        return ans
                
                