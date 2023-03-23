class Solution:
    def splitString(self, s: str) -> bool:
        sLen = len(s)
        ans = False
        arr = []
        def backtrack(ind):
            if ind >= sLen:
                if len(arr) > 1:
                    return True
                return False
            for i in range(ind, sLen):
                val = s[ind: i+1]
                if not arr or arr[-1] - int(val) == 1:
                    arr.append(int(val))
                    flag = backtrack(i+1)
                    if flag:
                        return True
                    arr.pop()
            return False
                            
        return backtrack(0)
            
        