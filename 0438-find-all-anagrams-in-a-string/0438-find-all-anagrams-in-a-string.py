class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l = 0
        k = len(p)
        mp = defaultdict(int)
        window = defaultdict(int)
        ans = []
        for i in range(k):
            mp[p[i]]+=1
        for i in range(len(s)):
            window[s[i]] += 1
            if i-l == k-1:
                if window == mp:
                    ans.append(l)
                window[s[l]]-=1
                if window[s[l]] == 0:
                    window.pop(s[l])
                l+=1
        return ans
                
                
        