inp = int(input())

nums = list(map(int, input().split(" ")))

odd = False
even = False

for i in nums:
    if i % 2 == 0:
        even = True
    else:
        odd = True

if odd and even:
    nums = sorted(nums)

for i in nums:
    print(i, end=" ")