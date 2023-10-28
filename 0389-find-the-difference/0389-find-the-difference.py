class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        mp = {}
        for i in range(len(s)):
            if s[i] not in mp:
                mp[s[i]]=[i]
            else:
                mp[s[i]].append(i)
                
        for i in range(len(t)):
            if t[i] not in mp.keys():
                return t[i]
            elif len(mp[t[i]]) == 0:
                return t[i]
            else:
                mp[t[i]].pop()
        return ""