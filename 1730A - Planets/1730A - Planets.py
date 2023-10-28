from collections import Counter, defaultdict
testCase = int(input())

for i in range(testCase):
    inp = input().split(" ")
    cost2 = int(inp[1])
    cost = 0
    planets = list(map(lambda a:int(a), input().split(" ")))
    mp = Counter(planets)
    for j in mp:
        if mp[j] == 1:
            cost+= 1
        elif mp[j] > 1 and cost2 > mp[j]:
            cost+= mp[j]
        else:
            cost+=cost2
    print(cost)
