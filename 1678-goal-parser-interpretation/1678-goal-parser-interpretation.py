class Solution:
    def interpret(self, command: str) -> str:
        leng = len(command)
        ans = ""
        i = 0
        while i<leng:
            if command[i] != "(":
                ans+="G"
                i+=1
            else:
                if command[i+1]=="a":
                    ans+="al"
                    i+=4
                else:
                    ans+="o"
                    i+=2
        return ans
                    
                    
                