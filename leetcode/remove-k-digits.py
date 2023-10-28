class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        num = list(num)
        ans = []
        for i in range(len(num)):
            if(k>0 and len(ans)>0):
                while(num[i]<ans[-1] and k>0):
                    a = ans.pop()
                    k-=1
                    if(len(ans)==0):
                        break
            ans.append(num[i])
        for j in range(k):
            ans.pop()
        if(len(ans)==0):
            ans="0"
        else:
            ans = str(int("".join(ans)))
        return ans