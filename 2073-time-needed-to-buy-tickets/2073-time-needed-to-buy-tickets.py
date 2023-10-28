class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        c = 0
        i = 0
        while True:
            if tickets[k] == 0:
                return c
            if tickets[i] > 0:
                c+=1
            tickets[i] -= 1
            if i < len(tickets)-1:
                i+=1
            else:
                i = 0
            
            