class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ded = 0
        ans = [[] for x in range(len(strs[0]))]
        
        for i in range(len(strs[0])):
            for j in range(len(strs)):
                if len(ans[i]) > 0:
                    if max(ans[i]) > ord(strs[j][i]):
                        ded+=1
                        break
                ans[i].append(ord(strs[j][i]))
        return ded
            
                