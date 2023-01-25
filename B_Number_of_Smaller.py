inp = input().split(" ")
nLen = int(inp[0])
mLen = int(inp[1])

n = list(map(int, input().split(" ")))
m = list(map(int, input().split(" ")))

t = 0
b = 0
while b < mLen:
    while t < nLen and n[t] < m[b]:
        t+=1
    b+=1
    print(t, end=" ")