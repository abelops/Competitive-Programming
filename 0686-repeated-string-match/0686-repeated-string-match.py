class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:            
        lps = [0] * len(b)
        prev, i = 0, 1
        
        while i < len(b):
            if b[prev] == b[i]:
                lps[i] = prev + 1
                prev+=1
                i+=1    
            else:
                if prev == 0:
                    i+=1
                else:
                    prev = lps[prev-1]
        bPtr = 0
        tPtr = 0
        count = 0
        
        while tPtr < len(a):
            if tPtr == 0:
                count+=1
            if a[tPtr] == b[bPtr]:
                tPtr+=1
                tPtr%=len(a)
                bPtr+=1
            else:
                if bPtr == 0:
                    tPtr+=1
                elif count > 2:
                    return -1
                else:
                    bPtr = lps[bPtr-1]
            if bPtr == len(b):
                return count
                
        # print(tPtr)/
        return -1
        
        