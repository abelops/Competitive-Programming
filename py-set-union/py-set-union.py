# Enter your code here. Read input from STDIN. Print output to STDOUT
def union():
    engNum = input()
    engId = list(map(lambda a: int(a), input().split(" ")))
    freNum = input()
    freId = list(map(lambda a: int(a), input().split(" ")))
    engId+=freId
    print(len(set(engId)))
union()