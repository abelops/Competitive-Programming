class Solution:
    def romanToInt(self, s: str) -> int:
        r = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ans = r[s[len(s)-1]]
        for i in range(len(s)-2,-1,-1):
            if(r[s[i+1]]>r[s[i]]):
                ans-=r[s[i]]
            else:
                ans+=r[s[i]]
        return ans