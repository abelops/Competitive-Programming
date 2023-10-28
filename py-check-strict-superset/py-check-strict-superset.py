# Enter your code here. Read input from STDIN. Print output to STDOUT
def strictSet():
    a = set(map(lambda f: int(f), input().split(" ")))
    otherLeng = int(input())
    for i in range(otherLeng):
        n = list(map(lambda f: int(f), input().split(" ")))
        for j in n:
            if j not in a:
                print(False)
                return
        else:
            continue
        break
    print(True)
strictSet()