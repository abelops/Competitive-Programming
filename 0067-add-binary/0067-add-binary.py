class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ma = max(a,b,key=len)
        ans = ""
        carry = 0
        a = a[::-1]
        b = b[::-1]
        for i in range(len(ma)):
            if i < len(a) and i < len(b):
                ans+=str((int(a[i]) + int(b[i]) + carry) % 2)
                carry = (int(a[i]) + int(b[i]) + carry) // 2
            elif i < len(a):
                ans+=str((int(a[i]) + carry) % 2)
                carry = (int(a[i]) + carry) // 2
            elif i < len(b):
                ans+=str((int(b[i]) + carry) % 2)
                carry = (int(b[i]) + carry) // 2
        if carry == 1:
            ans+=str(carry)
        return ans[::-1]
        
            
        