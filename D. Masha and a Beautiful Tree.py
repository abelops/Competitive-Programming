from math import sqrt
def numI():
    return int(input())
def numII():
    return list(input())
def numIII():
    return list(map(int, input().split(' ')))
def strInp():
    return input()
def strInpI():
    return list(input())

c = 0
def merge(arr):
    global c
    if len(arr) == 1:
        return arr
    mid = len(arr)//2
    left = merge(arr[:mid])
    right = merge(arr[mid:])
    if left[0] > right[0]:
        c+=1
        right.extend(left)
        return right
    left.extend(right)
    return left

def solve():
    global c
    testCase = numI()
    for i in range(testCase):
        c = 0
        size = numI()
        leaf = numIII()
        ans = merge(leaf)
        if ans == sorted(ans):
            print(c)
        else:
            print(-1)
solve()