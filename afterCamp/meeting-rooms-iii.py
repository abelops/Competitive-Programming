class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        ans = defaultdict(int)
        meetings.sort()
        current = []
        room = [x for x in range(n)]
        heapify(room)
        for i in range(len(meetings)):
            while current and current[0][0] <= meetings[i][0]:
                t,r = heappop(current)
                heappush(room, r)
            if room:
                r = heappop(room)
                heappush(current, (meetings[i][1], r))
            else:
                endT,r = heappop(current)
                diff = meetings[i][1] - meetings[i][0]
                heappush(current, (endT+diff, r))
            ans[r]+=1
            # print(current)
                
        
        maxi = max(ans.values())
        sol = min([x for x in ans if ans[x] == maxi])
        return sol
                        
                    
        