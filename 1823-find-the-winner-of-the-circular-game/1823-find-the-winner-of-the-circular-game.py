class Solution:
    def cust(self,ar: list,k: int) -> int:
        if(len(ar)==1):
            f= ar[0]
            return int(f)
        if(len(ar)>=k):
            ar.pop(k-1)
            newAr = ar[k-1:len(ar)] + ar[0:k-1]
        else:
            i1=-1
            for i in range(k):
                if(i1==len(ar)-1):
                    i1=0
                elif(i1<len(ar)):
                    i1+=1
            ar.pop(i1)
            newAr = ar[i1:len(ar)] + ar[0:i1]
        return self.cust(newAr,k)
    def findTheWinner(self, n: int, k: int) -> int:
        ar = [x for x in range(1,n+1)]
        return self.cust(ar,k)