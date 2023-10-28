class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ""
        for i in s:
            ch = ord(i)
            if i != " ":
                if ch >= 97 and ch <= 122:
                    newS+=i
                elif ch >= 65 and ch <= 90:
                    newS+=i.lower()
                elif ch >= 48 and ch <= 57:
                    newS+=i
        if len(newS) % 2 == 0:
            r = len(newS) - 1
            l = 0
            while l < r:
                if newS[l] != newS[r]:
                    return False
                l+=1
                r-=1
            return True
        r = len(newS) - 1
        l = 0
        while l <= r:
            if newS[l] != newS[r]:
                return False
            l+=1
            r-=1
        return True