class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        b = [ [position[x],speed[x]] for x in range(len(position))]
        b.sort(reverse=True)
        fleet = []
        for i in b:
            if(len(fleet)==0):
                fleet.append(i)
            else:
                if((target-i[0])/i[1]>(target-fleet[-1][0])/fleet[-1][1]):
                    fleet.append(i)
        return(len(fleet))