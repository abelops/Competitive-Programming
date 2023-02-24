inp = int(input())
 
 
for i in range(inp):
    st = False
    ps = True
    for j in range(8):
        inputList = input()
        while len(inputList) == 0:
            inputList = input()
        ans = [int(ind) for ind, x in enumerate(inputList) if x=="#"]
        if st and ps:
            print(j+1, ans[0]+1)
            st = False
            ps = False
        if len(ans) > 1:
            if ans[1] - ans[0] == 2:
                st = True