inp = int(input())

for i in range(inp):
    inputs = input()
    chrs = []
    for i in inputs:
        chrs.append(i)
    st = []
    for i in chrs:
        if not st:
            st.append(i)
        else:
            if st[-1] == i:
                st.pop()
                st.append("*")
            else:
                st.append(i)
    st= list(set(st))
    st = sorted(st,key=ord)
    ans = "".join([x for x in st if x !="*"])
    print(ans)