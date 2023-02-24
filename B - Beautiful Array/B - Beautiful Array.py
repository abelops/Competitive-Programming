inp = int(input())
n = []
p = []
ans = [[],[],[]]
 
 
ns = input().split(" ")
nums = list(map(lambda x: int(x), ns))
# print(nums)
 
for j in nums:
    if j < 0:
        n.append(j)
    else:
        p.append(j)
 
if len(n) % 2 == 0:
    for i in range(len(n)):
        if i == 0:
            ans[0].append(str(n[i]))
        else:
            if i < len(n)-1:
                ans[1].append(str(n[i]))
            else:
                ans[2].append(str(n[i]))
else:
    for i in range(len(n)):
        if i == 0:
            ans[0].append(str(n[i]))
        else:
            ans[1].append(str(n[i]))
for i in p:
    if i == 0:
        ans[2].append(str(i))
    else:
        ans[1].append(str(i))
 
for fin in ans:
    print(len(fin), " ".join(fin))