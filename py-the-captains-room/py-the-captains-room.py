# Enter your code here. Read input from STDIN. Print output to STDOUT
def getCap():
    num = int(input())
    li = input().split(" ")
    ans = {}
    for i in li:
        ans[i] = 1 + ans.get(i,0)
    for i in ans.keys():
        if ans[i]==1:
            print(i)
getCap()
 