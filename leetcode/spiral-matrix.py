class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        tot = len(matrix) * len(matrix[0])
        l = 0
        r = len(matrix[0])-1
        t = 0
        b = len(matrix)-1
        d = "h"
        i1, i2 = 0,0
        for i in range(tot):
            ans.append(matrix[i1][i2])
            if(d=="h"):
                if(i2==r):
                    d="v"
                    t+=1
                    i1+=1
                else:
                    i2+=1
            elif(d=="v"):
                if(i1==b):
                    d="-h"
                    r-=1
                    i2-=1
                else:
                    i1+=1
            elif(d=="-h"):
                if(i2==l):
                    d="-v"
                    b-=1
                    i1-=1
                else:
                    i2-=1
            elif(d=="-v"):
                if(i1==t):
                    d="h"
                    l+=1
                    i2+=1
                else:
                    i1-=1
        return ans