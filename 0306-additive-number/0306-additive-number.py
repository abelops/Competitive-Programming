class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        ans = []
        numLen = len(num)
        def backtrack(ind):
            if ind >= numLen:
                return len(ans) > 2
                
            for i in range(ind+1, numLen+1):
                # print("i=", i)
                # print(ans,num[ind: i], "ind=", ind)
                val = int(num[ind: i])
                if (num[ind] != "0" or val == 0) and (len(ans) < 2 or ans[-1] + ans[-2] == val):
                    ans.append(val)
                    # print("Call")
                    flag = backtrack(i)
                    # print("i was", i)
                    if flag:
                        return True
                    ans.pop()
            return False
        return backtrack(0)