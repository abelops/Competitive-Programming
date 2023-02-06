class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        count = 0
        
        top = 0
        bot = 0
        
        players = sorted(players)
        trainers = sorted(trainers)
        
        while top < len(players) and bot < len(trainers):
            if players[top] > trainers[bot]:
                bot+=1
            else:
                count+=1
                bot+=1
                top+=1
        return count