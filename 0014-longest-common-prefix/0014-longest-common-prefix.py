class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        stat = True
        i = 0
        fin = ""
        strs.sort(key=len, reverse=True)
        ch=False
        while stat and i<len(strs[0]):
            cur = strs[0][i]
            for j in range(1,len(strs)):
                if i<len(strs[j]):
                    if strs[j][i]!=cur:
                        stat = False
                        ch = False
                        break
                    else:
                        ch=True
                else:
                    ch = False
            if ch:
                fin+=cur
            i+=1
        return fin
    
            
        