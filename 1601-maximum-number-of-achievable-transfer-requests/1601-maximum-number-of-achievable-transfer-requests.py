class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        ans = []
        c = 0
        def helper(arr):
            leave = defaultdict(int)
            join = defaultdict(int)
            for i in arr:
                if i[0] == i[1]:
                    continue
                leave[i[0]]+=1
                join[i[1]]+=1
            # if join == leave:
            #     print(arr)
            return join == leave
        
        def comb(start, cur):
            nonlocal c
            if cur:
                if helper(cur[:]):
                    c = max(c, len(cur))
                ans.append(cur[:])
            
            for i in range(start, len(requests)):
                # print(i)
                cur.append(requests[i])
                comb(i+1, cur)
                cur.pop()
        comb(0, [])
        # for i in ans:
        #     if len(i) == 8:
        #         print(i, sum(i[0]), sum(i[1]))
        # print(len(ans))
        return c