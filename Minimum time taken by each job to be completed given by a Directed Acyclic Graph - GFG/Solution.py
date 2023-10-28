from typing import List
from collections import defaultdict, deque

class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        # code here
        ans = [0] * n
        mp = defaultdict(list)
        deg = defaultdict(int)
        for start, end in edges:
            mp[start-1].append(end-1)
            deg[end-1]+=1
        q = deque()
        for i in range(n):
            if not deg[i]:
                q.append(i)
                ans[i] = 1
        while q:
            poped = q.popleft()
            for neighbor in mp[poped]:
                deg[neighbor]-=1
                if not deg[neighbor]:
                    q.append(neighbor)
                ans[neighbor] = max(ans[neighbor], ans[poped]+1)
        return " ".join(map(str, ans))
        

#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        
        
        edges=IntMatrix().Input(a[1], a[1])
        
        obj = Solution()
        res = obj.minimumTime(a[0],a[1], edges)
        
        print(res)
        

# } Driver Code Ends
