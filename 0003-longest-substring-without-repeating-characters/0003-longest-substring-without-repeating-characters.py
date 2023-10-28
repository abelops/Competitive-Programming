class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c = 0
        l,r=0,1
        f = list(s)
        if(len(s)==1):
            return 1
        while r<len(f):
            if(len(list(set(f[l:r+1]))) == len(f[l:r+1])):
                c = max(c, r-l+1)
                r+=1
            else:
                while(len(list(set(f[l:r+1]))) != len(f[l:r+1])):
                    l+=1
        return c