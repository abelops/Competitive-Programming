inp = int(input())

for i in range(inp):
    n = int(input())
    nums = list(map(int, input().split(" ")))

    ans = []
    l= 0
    r = n-1
    while l < r:
        ans.append(str(nums[l]))
        ans.append(str(nums[r]))
        l+=1
        r-=1
    if n%2 != 0:
        ans.append(str(nums[l]))
    print(" ".join(ans))