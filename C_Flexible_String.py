from itertools import combinations
 
 
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    a = input()
    b = input()
    chars = list(set(a))
    k = min(K, len(chars))
    ans = 0
    for comb in combinations(chars, k):
        print(comb)
        comb = set(comb)
        temp = 0
        prev = 0
        for i, ch in enumerate(a):
            # print(ch in comb)
            if b[i] == ch or ch in comb:
                prev += 1
                temp += prev
            else:
                prev = 0
        ans = max(ans, temp)
    print(ans)