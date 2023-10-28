inp = int(input())
cont = list(map(lambda a: int(a), input().split(" ")))
maxi = 0
mini = 0
ans = 0 
for c,i in enumerate(cont):
    if c == 0:
        maxi = i
        mini = i
    else:
        if i > maxi and i <= 10000:
            ans+=1
            maxi = i
        elif i < mini and i >= 0:
            ans+=1
            mini = i
    # print(maxi, mini)
print(ans)