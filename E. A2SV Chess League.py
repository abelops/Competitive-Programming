
def numI(): return int(input())
def numII(): return list(input())
def numIII(): return list(map(int, input().split(' ')))
def strInp(): return input()
def strInpI(): return list(input())

def merge(nums,k):
    if len(nums) <= 1:
        return nums
    a1 = merge(nums[:len(nums)//2],k)
    a2 = merge(nums[len(nums)//2:],k)
    new_arr = []
    l1, l2 = 0,0 
    while l1 < len(a1) or l2 < len(a2):
        num1, idx1 = a1[l1] if l1 < len(a1) else (float('inf'), idx1)
        num2, idx2 = a2[l2] if l2 < len(a2) else (float('inf'), idx2)
        if num1 <= num2:
            if a2[0][0] - k <= num1: new_arr.append(tuple([num1, idx1]))
            l1 += 1
        else:
            if a1[0][0] - k <= num2: new_arr.append(tuple([num2, idx2]))
            l2 += 1
    return new_arr



def solve():
    n, k = numIII()
    ind = [x for x in range(1, (2**n)+1)]
    arr = numIII()
    players = [(arr[i], i+1) for i in range(2**n)]
    
    win = merge(players, k)
    print(*([i[1]  for i in sorted(win, key = lambda x: x[1])]))
solve()
