class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pref = [0] * 1002
        
        for pep, st, end in trips:
            pref[st+1] += pep
            pref[end+1] -= pep
            
        for i in range(1,1002):
            pref[i] += pref[i-1]
            if pref[i] > capacity:
                return False
        
        return True