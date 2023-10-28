# Enter your code here. Read input from STDIN. Print output to STDOUT
def uniq(n, words):
    ans = {}
    for i in words:
        if i not in ans:
            ans[i]= 1
        else:
            ans[i]+=1
    print(len(ans))
    for j in ans.values():
        print(j,end=" ")
a = []
n = int(input())
for i in range(n):
    a.append(input())
uniq(len(a), a)
