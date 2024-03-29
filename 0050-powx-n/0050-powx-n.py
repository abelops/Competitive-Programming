class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n >= 0:
            if n == 0:
                return 1
            if n % 2 != 0:
                # print(x * x * x, (n-1)//2)
                return x * self.myPow( x * x, (n-1)//2)
            else:
                # print(x * x, (n-1)//2)
                return self.myPow( x * x, n//2)
        else:
            n = abs(n)
            return 1/(x * self.myPow(x, n-1))
           