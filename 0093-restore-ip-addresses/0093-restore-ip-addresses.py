class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        totLen = len(s)
        def backtrack(ind, state):
            # print(state)
            if ind == totLen:
                if len(state) == 4:
                    temp = ""
                    for i in range(len(state)):
                        temp+=state[i]
                        if i < 3:
                            temp+="."
                    ans.append(temp)
                return
            
            for i in range(ind, totLen):
                val = s[ind:i+1]
                # print(val[0] != "0" and len(val) > 1)
                if val[0] == "0" and len(val) > 1:
                    break
                if int(val) <= 255:
                    state.append(val)
                    backtrack(i+1, state)
                    state.pop()
                
            return
            
        backtrack(0,[])
        # print(ans)
        return ans