inp = int(input())
 
for i in range(inp):
    nums = str(input())
    if len(set(nums)) != 3:
        print(0)
        continue
    l = 0
    r = 0
    mini = 10000000
 
    one = 0
    two = 0
    three = 0
 
 
    nLen = len(nums)
    while r <= nLen:
        while(one > 0 and two > 0 and three > 0):
            if nums[l] == "1":
                one -= 1
            elif nums[l] == "2":
                two -= 1
            elif nums[l] == "3":
                three-=1
            l+=1
            mini = min(mini, r-l+1)
        if one > 0 and two > 0 and three > 0:
            mini = min(mini, r-l+1)
        if r < nLen:
            if nums[r] == "1":
                one += 1
            elif nums[r] == "2":
                two += 1
            elif nums[r] == "3":
                three+=1
        r+=1
    if (one > 0 and two > 0 and three > 0) and nLen == 3:
        mini = min(mini, r-l)
    print(mini)