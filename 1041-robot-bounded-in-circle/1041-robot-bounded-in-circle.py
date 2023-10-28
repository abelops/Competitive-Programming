class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        d = "T"
        pos = [0,0]
        goStat = False
        for i in instructions:
            # print(pos, d)
            if i == "G":
                goStat = True
                if d == "T":
                    pos[1]+=1
                elif d == "B":
                    pos[1]-=1
                elif d == "L":
                    pos[0]-=1
                elif d == "R":
                    pos[0]+=1
                
            elif i == "L":
                if d == "T":
                    d = "L"
                elif d == "B":
                    d = "R"
                elif d == "L":
                    d = "B"
                elif d == "R":
                    d = "T"
            elif i == "R":
                if d == "T":
                    d = "R"
                elif d == "B":
                    d = "L"
                elif d == "L":
                    d = "T"
                elif d == "R":
                    d = "B"
        # print(d, pos)
        if (goStat and d != "T") or pos == [0,0]:
            return True
        return False
    
    
    