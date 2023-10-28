class Solution:
    def longestPalindrome(self, s: str) -> str:
        pal = ""
        for i in range(len(s)):
            l,r = i,i
            while l>=0 and r<len(s) and s[l]==s[r]:
                if len(pal) < r-l+1:
                    pal=s[l:r+1]
                    print(s[l:r+1])
                l-=1
                r+=1
            l,r = i,i+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if len(pal) < r-l+1:
                    pal=s[l:r+1]
                    print(s[l:r+1])
                l-=1
                r+=1
        return pal