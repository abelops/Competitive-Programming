# Enter your code here. Read input from STDIN. Print output to STDOUT
numberOfTestCase = int(input())
for i in range(numberOfTestCase):
    length = int(input())
    nums = list(map(lambda a: int(a), input().split(" ")))
    l = 0
    r = length - 1
    st = [max(nums[l],nums[r])]
    ans = "Yes"
    while l != r:
        if nums[l] <= nums[r]:
            if nums[r] > st[-1]:
                ans = "No"
                break
            r-=1
        else:
            if nums[l] > st[-1]:
                ans = "No"
            l+=1
    print(ans)