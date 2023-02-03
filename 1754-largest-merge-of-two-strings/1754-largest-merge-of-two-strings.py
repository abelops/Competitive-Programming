class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        t = 0
        b = 0
        
        w1Len = len(word1)
        w2Len = len(word2)
        maxLen = len(max(word1, word2, key=len))
        ans = ""
        
        while True:
            if t >= w1Len and b >= w2Len:
                break
            if t < w1Len and b < w2Len:
                if word1[t] == word2[b]:
                    if word1[t:] > word2[b:]:
                        ans+=word1[t]
                        t+=1
                    else:
                        ans+=word1[t]
                        b+=1
                elif word1[t] > word2[b]:
                    ans+=word1[t]
                    t+=1
                else:
                    ans+=word2[b]
                    b+=1
            elif t < w1Len:
                ans+=word1[t]
                t+=1
            elif b < w2Len:
                ans+=word2[b]
                b+=1
            
        return ans
                
        