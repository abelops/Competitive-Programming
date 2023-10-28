# Enter your code here. Read input from STDIN. Print output to STDOUT
def studentDiff():
    engNum = input()
    engId = set(map(lambda a: int(a), input().split(" ")))
    freNum = input()
    freId = set(map(lambda a: int(a), input().split(" ")))
    c = 0
    for i in engId:
        if i not in freId:
            c+=1
    print(c)
studentDiff()