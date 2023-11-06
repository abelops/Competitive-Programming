class Solution:
    def countOfAtoms(self, formula: str) -> str:
        st = []
        for i in formula:
            if st:
                if not st[-1].isdigit():
                    if i.islower() and st[-1] !=")" and st[-1] != "(":
                        poped = st.pop()
                        poped+=i
                        st.append(poped)
                    elif not i.isdigit() and st[-1] != "(":
                        st.append("1")
                        st.append(i)
                    else:
                        st.append(i)
                else:
                    if st[-1].isdigit() and i.isdigit():
                        poped = st.pop()
                        poped+=i
                        st.append(poped)
                    else:
                        st.append(i)
            else:
                st.append(i)
        if not st[-1].isdigit():
            st.append("1")
        # print(st)
        st1 = []
        closed = False
        for i in st:
            # print(st1)
            if not st1:
                st1.append(i)
            else:
                if i == ")":
                    closed = True
                elif closed:
                    tmp = []
                    while st1[-1] != "(":
                        poped = st1.pop()
                        if poped.isdigit():
                            tmp.append(str(int(poped)*int(i)))
                        else:
                            tmp.append(poped)
                    st1.pop()
                    closed = False
                    # print(tmp)
                    for j in tmp[::-1]:
                        st1.append(j)
                else:
                    st1.append(i)
        ans = defaultdict(int)
        for i in range(len(st1)):
            if st1[i].isdigit():
                ans[st1[i-1]]+=int(st1[i])
        return "".join([ char + (str(ans[char]) if ans[char] > 1 else "")  for char in sorted(ans.keys()) ])
        
                            
                    
                    
                