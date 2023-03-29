class Solution:
    def countBits(self, n: int) -> List[int]:
        def shiftNum():
            ans = []
            for i in range(n+1):
                c = 0
                while i:
                    if i & 1 == 1:
                        c+=1
                    i = i >> 1
                ans.append(c)
            return ans
        def shiftOne():
            ans = []
            for i in range(n+1):
                c = 0
                one = 1
                while one <= 17:
                    # print(one)
                    if i & one == 1:
                        c+=1
                    one = one << 1
                ans.append(c)
            return ans
        return shiftNum()
            
            