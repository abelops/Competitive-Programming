class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = [[] for i in range(numRows)]
        # gap = numRows - 2
        
        inc = 1
        index = 0                        
        for char in s:
            if index < 0 or index >= numRows:
                inc = (-1 * inc)
                index += (inc * 2)
                
            rows[index].append(char)
            index += inc
            
        return ''.join([''.join(row) for row in rows])
            