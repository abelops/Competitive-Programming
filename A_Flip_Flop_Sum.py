
inp = int(input())
for i in range(inp):
    l = int(input())
    nums = list(map(int, input().split(" ")))
    tot = sum(nums)
    st = []
    stat = False
    for i in nums:
        if not st:
            st.append(i)
        else:
            if st[-1] == -1 and i == -1:
                print(tot+4)
                stat = True
                break
        st.append(i)
    if not stat:
        if -1 in nums:
            print(tot)
        else:
            print(tot-4)
