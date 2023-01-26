class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mp = defaultdict(int)
        for i in range(len(s)):
            mp[s[i]] = i
        
        ans = []
        maxWind = 0
        start = 0
        for i, ch in enumerate(s):
            maxWind = max(mp[ch], maxWind)
            if i == maxWind:
                ans.append(i - start + 1)
                start = i + 1
        return ans
            
        