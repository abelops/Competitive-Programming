inp = int(input())

for i in range(inp):
    lens = input().split(" ")
    r = int(lens[0])
    c = int(lens[1])
    mat = []
    for cols in range(r):
        cs = input()
        ans = []
        for h in cs:
            ans.append(h)
        mat.append(ans)

    fin = []
    for cols in zip(*mat):
        colRev = list(cols)[::-1]
        p = 0
        while p < len(colRev):
            if colRev[p] == "*":
                for j in range(p-1, -1, -1):
                    if colRev[j] == "o" or colRev[j] == "*":
                        if j+1 < len(colRev):
                            colRev[p]="."
                            colRev[j+1] = "*"
                            break
                    if j == 0:
                        colRev[p]="."
                        colRev[0] = "*"

            p+=1
        fin.append(colRev[::-1])

    for z in zip(*fin):
        print("".join(list(z)))
