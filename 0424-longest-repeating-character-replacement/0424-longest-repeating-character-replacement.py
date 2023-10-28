class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        target = set(s)
        targetLen = len(target)
        ans = 0
        sLen = len(s)
        for i in target:
            l = 0
            count = 0
            for j in range(sLen):
                if s[j] != i:
                    count += 1
                if count > k:
                    while l < sLen and s[l] == i:
                        l += 1
                    l += 1
                    count -= 1
                ans = max(j-l+1, ans)
        return ans            
        