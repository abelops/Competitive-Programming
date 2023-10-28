# Enter your code here. Read input from STDIN. Print output to STDOUT
def both():
    lengths = input().split(" ")
    aLen = lengths[0]
    bLen = lengths[1]
    inpA = {}
    for i in range(int(aLen)):
        val = input()
        if val not in inpA:
            inpA[val] = [i+1]
        else:
            inpA[val].append(i+1)
    stat = False
    ans = ""
    for i in range(int(bLen)):
        val = input()
        if val in inpA:
            stat = True
            for i in inpA[val]:
                print(i, end=" ")
            print("")
        else:
            print(-1)
    # print(aLen, bLen, inpA) 
both()