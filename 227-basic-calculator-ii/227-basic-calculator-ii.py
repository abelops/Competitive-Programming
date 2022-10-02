class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = "+"
        s= s.replace(" ","")
        i=0
        while(i<len(s)):
            if(s[i].isdigit()):
                cur=""
                while(i<len(s) and s[i].isdigit()):
                    cur+=s[i]
                    i+=1
                i-=1
                if(sign=="-"):
                    stack.append(str(-int(cur)))
                elif(sign=="+"):
                    stack.append(cur)
                elif(sign=="*"):
                    n1 = stack.pop()
                    stack.append(str(int(n1)*int(cur)))
                elif(sign=="/"):
                    n1 = stack.pop()
                    stack.append(str(int(int(n1)/int(cur))))
            else:
                sign=s[i]
            i+=1
        ans = 0
        for j in stack:
            ans+=int(j)
        return ans