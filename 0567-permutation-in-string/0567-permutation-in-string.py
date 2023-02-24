class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Dict = {}
        s2Dict = {}
        s1Len = len(s1)
        s2Len = len(s2)
        
        if s1Len > s2Len:
            return False
        for i in s1:
            s1Dict[i] = 1 + s1Dict.get(i,0)
        
        for i in range(s1Len-1):
            s2Dict[s2[i]] = 1 + s2Dict.get(s2[i],0)
        
        l = 0
        for i in range(s1Len-1,s2Len):
            s2Dict[s2[i]] = 1 + s2Dict.get(s2[i],0)
            
            if s2Dict == s1Dict:
                return True
            s2Dict[s2[l]] -= 1
            if s2Dict[s2[l]] <= 0:
                s2Dict.pop(s2[l])
            l+=1
        return False