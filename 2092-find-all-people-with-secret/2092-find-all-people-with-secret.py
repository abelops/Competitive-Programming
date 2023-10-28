class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        rep = {}
        for i in range(n):
            rep[i] = i
            
        def representative(x):
            if x not in rep:
                return x
            if x == rep[x]:
                return x
            rep[x] = representative(rep[x]) 
            return rep[x]
            
        def union(x, y):
            xrep = representative(x)
            yrep = representative(y)
        
            if xrep == yrep:
                return
            if xrep == 0:
                rep[yrep] = xrep
            elif yrep == 0:
                rep[xrep] = yrep
            else:
                rep[yrep] = xrep
            
        
        # meetings.sort(key=lambda x: x[2])
        groups = defaultdict(list)
        
        nodes = set()
        for i, j, t in meetings:
            groups[t].append([i,j])
            nodes.add(i)
            nodes.add(j)
        
        # union(firstPerson, 0)
        rep[firstPerson] = 0
        # meetings.sort(key=lambda x: x[2])
        
        ans = set([0])
        for i in sorted(groups):
            # print(i)
            for gr in groups[i]:
                union(gr[0], gr[1])
            for gr in groups[i]:
                rep1 = representative(gr[0])
                rep2 = representative(gr[1])
                if rep1 != 0:
                    rep[gr[0]] = gr[0]
                if rep2 != 0:
                    rep[gr[1]] = gr[1]
        for i in rep:
            val = representative(i)
            if val == 0:
                ans.add(i)

        return list(ans)

            