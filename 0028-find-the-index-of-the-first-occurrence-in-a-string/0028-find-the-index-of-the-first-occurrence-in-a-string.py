class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        search = 0
        l = len(needle)
        for i in range(l):
            search+=(ord(needle[i])-ord('a')+1)*(26**(l-i-1)) 
        # search %= 10 ** 9 + 7
        cur = 0 
        for i in range(l):
            cur += (ord(haystack[i])-ord('a')+1)*(26**(l-i-1))

        if cur  == search:
            return 0
        
        
        for i in range(l, len(haystack)):
            # if cur == search:
            #     return i
            
            cur -= (26 ** (len(needle) - 1) * (ord(haystack[i - len(needle)]) - ord('a') + 1)) 
            
            # cur-= (ord(haystack[i-l-1]) - ord('a')+1) * (26**(l-1))% (10 ** 9 + 7)
            cur*= 26
            cur+= ord(haystack[i]) - ord('a') +1
            # print(cur, search)
            if cur == search:
                return i-l+1

        return -1
            