inp = int(input())

for i in range(inp):
    l = int(input())
    nums = list(map(int,input().split(" ")))
    st = []
    for i in nums:
        if not st:
            st.append(i)
        else:
            if st[-1] < 0:
                if i > st[-1] and i < 0:
                    st.pop()
                    st.append(i)
                elif i > 0:
                    st.append(i)
            else:
                if i > st[-1] and i > 0:
                    st.pop()
                    st.append(i)
                elif i < 0:
                    st.append(i)
    # print(st)
    print(sum(st))