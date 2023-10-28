class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        ma = 0
        c=0
        v = ['a','e','i','o','u']
        l,r=0,0
        st=True
        while r<len(s): 
            if(s[r] in v and st):
                c+=1 
            if(r+1-l==k):
                ma = max(ma, c)
                if(s[l] in v):
                    c-=1
                l+=1
                st = False
            else: 
                r+=1
                st=True
        return ma