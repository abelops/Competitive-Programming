from collections import deque
class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split(" ")
        maxWord = max(s, key=len)
        ans = [deque() for x in range(len(maxWord))]
        for ind, word in reversed(list(enumerate(s))):
            for i in range(len(maxWord)):
                if i < len(word):
                    ans[i].appendleft(word[i])
                else:
                    if len(ans[i]) > 0:
                        ans[i].appendleft(" ")

                
        fin = []
        for i in ans:
            fin.append("".join(i))
            
        return fin
                