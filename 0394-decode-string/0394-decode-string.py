class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        for i in s:
            if i == "[":
                st.append(i)
            elif i == "]":
                chars = []
                while st[-1] != "[":
                    chars.append(st.pop())
                st.pop()
                itter =""
                while st and st[-1].isdigit():
                    itter += st.pop()
                itter = int(itter[::-1])
                chars = chars[::-1]
                for i in range(itter):
                    for j in chars:
                        st.append(j)
            else:
                st.append(i)
            # print(st)
        ans = "".join(st)
        if ans.isnumeric():
            return ""
        return ans