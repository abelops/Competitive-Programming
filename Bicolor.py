from collections import defaultdict
def numI(): return int(input())
def numII(): return list(input())
def numIII(): return list(map(int, input().split(' ')))
def strInp(): return input()
def strInpI(): return list(input())



def solve():
    inps = numI()
    while inps!=0:
        lines = numI()
        mp = defaultdict(list)
        for i in range(lines):
            fro, to = numIII()
            mp[fro].append(to) 
            mp[to].append(fro)
        colors = defaultdict(bool)
        def dfs(num):
            if num not in colors:
                colors[num]= True
            temp = not colors[num]
            for child in mp[num]:
                if child in colors:
                    if colors[child] != temp:
                        return False
                    continue
                colors[child] = temp
                childCall = dfs(child)
                if not childCall:
                    return False             
            return True
        
        ans = True
        for i in range(1, inps+1):
            if i not in colors:
                ans = ans and dfs(i)
        
        if ans:
            print("BICOLOURABLE.")
        else:
            print("NOT BICOLOURABLE.")
        inps = numI()
solve()