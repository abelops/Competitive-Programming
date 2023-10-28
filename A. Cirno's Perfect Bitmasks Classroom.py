def numI(): return int(input())
def numII(): return list(input())
def numIII(): return list(map(int, input().split(' ')))
def strInp(): return input()
def strInpI(): return list(input())

def solve():
    testCase = numI()
    for i in range(testCase):
        num = numI()       
        if num == 1:
            print(3)
        else:
            ans = num & -num 
            if ans == num:
                ans+=1
            print(ans)
solve()