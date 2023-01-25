inp = int(input())
nums = sorted(list(map(lambda a: int(a), input().split(" "))))

ans = 0
c = 1
for i in nums:
    ans+=abs(i-c)
    # print(i,c)
    c+=1
print(ans)