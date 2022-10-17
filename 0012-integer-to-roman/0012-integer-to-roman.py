class Solution:
    def intToRoman(self, num: int) -> str:
        r = {1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
        l = pow(10,len(str(num))-1)
        ans = ""
        for i,n in enumerate(str(num)):
            if(int(n)*l in r):
                ans+=r[int(n)*l]
            elif(int(n)==9):
                ans+=r[1*l]
                ans+=r[1*l*10]
            elif(int(n)==4):
                ans+=r[1*l]
                ans+=r[5*l]
            else:
                if(int(n)<5):
                    for i in range(int(n)):
                        ans+=r[1*l]
                elif(int(n)>5):
                    ans+=r[5*l]
                    for i in range(int(n)-5):
                        ans+=r[1*l]
            l/=10
        return ans