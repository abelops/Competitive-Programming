class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        rep = {}
        nonEqual = []
        size = {}
        for elem in equations:
            if elem[1] == "!":
                nonEqual.append(elem)
            rep[elem[0]] = elem[0]
            rep[elem[3]] = elem[3]
            size[elem[0]] = 1
            size[elem[3]] = 1
        
        def find(x):
            if x == rep[x]:
                return x
            rep[x] = find(rep[x])
            return rep[x]
        
        def union(x, y):
            repx = find(x)
            repy = find(y)
            
            if repx == repy:
                return
            if size[repx] > size[repy]:
                rep[repy] = repx
                size[repx] += size[repy]
            else:
                rep[repx] = repy
                size[repy] += size[repx]
            return
        
        for elem in equations:
            if elem[1] == "=":
                union(elem[0], elem[3])
        for elem in equations:
            if elem[1] == "!":
                flag = find(elem[0]) == find(elem[3])
                if flag:
                    return False
        return True
        
            
            