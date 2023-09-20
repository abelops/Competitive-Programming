class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if b == "":
            return 0
        if a == b or b in a:
            return 1
        lenb = len(b)
        lena = len(a)
        c = 0
        newA = a
        while len(newA) < max(lena, lenb)*2:
            newA +=a
            c+=1
            if b in newA:
                return c+1
        return -1
            