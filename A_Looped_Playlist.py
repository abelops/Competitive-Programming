n,p=map(int,input().split())
li=list(map(int,input().split()))
Sum,ma=0,0
for i in range(n):
    if Sum+lii>=p:
        ma=i+1
        break
    else: Sum+=lii 
if ma: print (1,ma)
else:  print((p//sum(li))%n + 1 , p//sum(li)+1)