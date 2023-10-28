from collections import Counter
inp = input().split(" ")
r = int(inp[0])
c = int(inp[1])

mat = []
for i in range(r):
    col = list(map(lambda x: x, input()))
    mat.append(col)
ans = ""
for i in mat:
    for j, ver in zip(i, zip(*mat)):
        newList = Counter(i + list(ver))
        if newList[j] == 2:
            ans+=j
print(ans)
         
        
