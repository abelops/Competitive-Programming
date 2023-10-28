class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        ans = [0] * 1002
        for pas, start, end in trips:
            ans[start + 1] += pas
            ans[end + 1] -= pas
            
        for i in range(1,1000):
            s = ans[i-1] + ans[i]
            if s > capacity:
                return False
            ans[i] = s
        return True
    
