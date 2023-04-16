class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        stat = [False] * (right+1)
        if right == 1:
            stat[0] = True
        if right > 1:
            stat[0] = True
            stat[1] = True
            
        ans = []
        fin = [-1,-1]
        for i in range(2, right+1):
            if not stat[i]:
                if ans:
                    if fin[0] == -1 or fin[1] - fin[0] > i - ans[-1]:
                        if ans[-1] >= left:
                            fin = [ans[-1], i]
                    
                ans.append(i)
                for j in range(i * i, right+1, i):
                    stat[j] = True
        # print(ans)
        return fin
        