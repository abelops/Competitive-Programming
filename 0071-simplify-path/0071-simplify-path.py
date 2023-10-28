class Solution:
    def simplifyPath(self, path: str) -> str:
        st = ["/"]
        path = path.split("/")
        for i in path:
            if i == "..":
                if len(st) > 1:
                    st.pop()
                    st.pop()
            elif i != "" and i != ".":
                st.append(i)
                st.append("/")
        if len(st) > 1:
            st.pop()
        return "".join(st)
        