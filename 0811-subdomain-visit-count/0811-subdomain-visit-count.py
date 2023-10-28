class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        ans = defaultdict(int)
        for i in cpdomains:
            i = i.split(" ")
            rep = int(i[0])
            domain = i[1].split(".")
            tb = domain[-1]
            ans[tb] += rep
            for j in range(len(domain)-2,-1,-1):
                tb = domain[j]+"."+tb
                ans[tb] += rep
        fin = []
        for key in ans:
            fin.append(str(ans[key])+" "+key)
        return fin
        