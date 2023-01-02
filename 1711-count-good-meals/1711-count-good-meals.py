from collections import Counter
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        mod = 10**9 + 7
        ans = 0
        powers = set()
        cur = 1
        powers.add(1)
        while cur < 2**21:
            cur *= 2
            powers.add(cur)
        mp = Counter(deliciousness)
        for j in mp.items():
            for pwr in powers:
                p = pwr - j[0]
                if p in mp:
                    if p == j[0]:
                        ans += int((j[1]-1) * j[1] / 2)
                    else:
                        ans += mp[p] * j[1]
            mp[j[0]]=0
        return ans % mod
        
        
        