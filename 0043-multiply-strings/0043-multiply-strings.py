class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = 0
        n2 = 0
        for i,n in enumerate(num1):
            n1 += (10**(len(num1) -i-1)) * (ord(n)-48)
            
        for i,n in enumerate(num2):
            n2 += (10**(len(num2) -i-1)) * (ord(n)-48)
            
        return str(n1 * n2)
        