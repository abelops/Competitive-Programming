class Solution:
    def numTeams(self, rating: List[int]) -> int:
        l = len(rating)
        arr = [0] * l
        arr1 = [0] * l
        ans = 0
        for i in range(l):
            for j in range(i,-1,-1):
                if rating[i] > rating[j]:
                    arr[i]+=1
                if rating[i] < rating[j]:
                    arr1[i]+=1
                
        for i in range(l):
            for j in range(i,-1,-1):
                if rating[i] > rating[j]:
                    ans+=arr[j]
                if rating[i] < rating[j]:
                    ans+=arr1[j]  
        return ans