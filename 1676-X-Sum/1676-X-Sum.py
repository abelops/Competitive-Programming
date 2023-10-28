inp = int(input())

for i in range(inp):
    mat = []
    pd = {}
    nd = {}
    rowCol = input().split(" ")
    r = int(rowCol[0])
    c = int(rowCol[1])

    
    for i in range(r):
        val = list(map(lambda a: int(a), input().split(" ")))
        mat.append(val)
    ans = []


    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if i+j not in pd:
                pd[i+j] = mat[i][j]
            else:
                pd[i+j] += mat[i][j]
            if j-i not in nd:
                nd[j-i] = mat[i][j]
            else:
                nd[j-i] += mat[i][j]

    fin = []
    print(pd, nd)
    # for i,j in zip(pd.keys(), nd.keys()):
    #     fin.append(pd[i]+nd[j])
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            fin.append(pd[i+j] + nd[j-i] - mat[i][j])

    print(max(fin))