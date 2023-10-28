noTest = int(input())

for i in range(noTest):
    inp = int(input())
    num = sorted(list(map(int, input().split(" "))))

    l, r = 0, 1
    while r < inp:
        if num[r] - num[l] == 1 or num[r] == num[l]:
            l+=1
            r+=1
        else:
            break
    if r == inp:
        print("YES")
    else:
        print("NO")