# Enter your code here. Read input from STDIN. Print output to STDOUT
def getHappy():
    st = 0
    i1 = input().split(" ") 
    elem = input().split(" ")
    A = set(input().split(" ")) 
    B = set(input().split(" ")) 
    for i in elem:
        if i in A:
            st+=1
        elif i in B:
            st-=1
    print(st)
getHappy()