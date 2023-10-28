class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        rep = defaultdict(set)
        size = defaultdict(int)
        accs = defaultdict(set)
        names = []
        for i in range(len(accounts)):
            rep[i] = i
            accs[i] = set(accounts[i][1::])
            size[i]=1
            names.append(accounts[i][0])
            
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
                
        for i in range(len(accounts)):
            for j in range(i+1, len(accounts)):
                if len(accs[i] & accs[j]) > 0:
                    # print(i,j)
                    union(i, j)
        ans = []
        # print(rep)
        for key, val in rep.items():
            if key != val:
                newval = find(val)
                accs[newval] = accs[key].union(accs[newval])
                # if accs[val]:
                #     del accs[val]
        for key, val in rep.items():
            if key == val:
                temp = [names[key]]
                temp+=sorted(accs[key])
                ans.append(temp)
                
        # print(accs, rep, names)
        return ans
                