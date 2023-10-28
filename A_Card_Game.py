inp = int(input())

nums = list(map(int, input().split(" ")))

wube = 0
henok = 0

cur = "w"
l = 0
r = inp - 1
while l <= r:
    if cur == "w":
        if nums[l] > nums[r]:
            wube+=nums[l]
            cur="h"
            l+=1
        else:
            wube+=nums[r]
            cur="h"
            r-=1
    else:
        if nums[l] > nums[r]:
            henok+=nums[l]
            cur="w"
            l+=1
        else:
            henok+=nums[r]
            cur="w"
            r-=1

print(wube, henok)  