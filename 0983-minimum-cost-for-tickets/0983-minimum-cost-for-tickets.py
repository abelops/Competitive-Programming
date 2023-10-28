class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = days[-1]
        arr = [0] * (n+1)
        d = [1, 7, 30]
        days = set(days)
        for i in range(1, n+1):
            arr[i] = float('inf')
            for dur, cost in zip(d, costs):
                if i not in days:
                    arr[i] = arr[i-1]
                else:
                    arr[i] = min(arr[i], cost+arr[max(0,i-dur)])  
            
        # print(arr)
        return arr[-1]
                
                