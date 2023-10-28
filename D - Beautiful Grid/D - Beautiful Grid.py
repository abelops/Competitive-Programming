from math import ceil
test = int(input())
 
for i in range(test):
    r = int(input())
    mat = []
    for f in range(r):
        inp = list(map(lambda x: int(x), [x for x in input()]))
        mat.append(inp)
    
    cost = 0
 
    for row in range(ceil(r / 2)):
        for col in range(r // 2):
            # print(row,col)
            count = sum([
                        mat[row][col],
                        mat[col][-1 - row],
                        mat[-1 - row][-1 - col],
                        mat[-1 - col][row],
                    ])
            cost += min(count, 4 - count)
    print(cost)