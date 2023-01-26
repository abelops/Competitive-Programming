class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans = 0
        people = sorted(people)
        
        l = 0
        r = len(people)-1
        
        while l <= r:
            if people[r] == limit or people[r] + people[l] > limit:
                ans+=1
                r-=1
            else:
                ans+=1
                r-=1
                l+=1
        return ans
                
                