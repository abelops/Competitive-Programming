class Solution:
    def minimumDeletions(self, s: str) -> int:
        pref = []
        prefRev = []
        sLen = len(s)
        c = sLen - 1
        for i in s:
            if i == "a":
                pref.append(1)
            else:
                pref.append(0)
            if s[c] == "a":
                prefRev.append(1)
            else:
                prefRev.append(0)
            c -= 1
        for i in range(1, len(pref)):
            pref[i] += pref[i-1]
            prefRev[i] += prefRev[i-1]
            
        prefRev = prefRev[::-1]
        # print(pref, prefRev)
        allA = len(pref) - pref[-1]
        allB = pref[-1]
        ans = min(allA, allB)
        for i in range(len(pref)):
            if i+1 < len(pref):
                ans = min((i-pref[i]+1) + prefRev[i+1], ans)
            else:
                ans = min(i-pref[i]+1, ans)
        return ans
        