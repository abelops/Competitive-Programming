class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        l = len(s)
        cur = 0
        prev = 1
        for i in range(l-k, l):
            cur += (ord(s[i]) - 96) * prev
            prev*=power
        ans = 0
        if cur % modulo == hashValue:
            ans = l - k
        
        newPow = power ** (k-1)
        for i in range(l-k-1,-1,-1):
            cur -= (ord(s[i+k]) - 96) * newPow
            cur*=power
            cur+=(ord(s[i]) - 96)
            if cur % modulo == hashValue:
                ans = i
        return s[ans:ans+k]
        
        
            