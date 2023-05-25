class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0
        for i in bills:
            if i == 5:
                fives+=1
            if i == 10:
                if fives > 0:
                    fives-=1
                    tens+=1
                else:
                    return False
            if i == 20:
                if tens > 0 and fives > 0:
                    tens-=1
                    fives-=1
                elif tens == 0 and fives > 2:
                    fives-=3
                else:
                    return False
        return True