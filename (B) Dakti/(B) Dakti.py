num = int(input())
 
words = []
for i in range(num):
    wor = input().split(" ")
    ans = {}
    for f in wor:
        st = []
        n = ""
        w = ""
        for j in f:
            if j.isdigit():
                n+=j
            else:
                w+=j
        ans[int(n)] = w
    printed = ""
    for c,p in enumerate(sorted(ans.keys())):
        printed+=ans[p]
        if c < len(ans.keys())-1:
            printed+=" "
    print(printed)
 
 