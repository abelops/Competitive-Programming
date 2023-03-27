class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        totLen = len(s)
        def backtrack(ind, state):
            # print(state)
            if ind == totLen:
                stat = True
                if len(state) == 4:
                    temp = ""
                    for i in range(len(state)):
                        temp+=state[i]
                        if state[i][0] == "0" and len(state[i]) > 1:
                            stat = False
                            break
                        if i < 3:
                            temp+="."
                    if stat:
                        ans.append(temp)
                return
            
            for i in range(ind, totLen):
                val = s[ind:i+1]
                # print(val[0] != "0" and len(val) > 1)
                if int(val) <= 255:
                    state.append(val)
                    backtrack(i+1, state)
                    state.pop()
                
            return
            
        backtrack(0,[])
        # print(ans)
        return ans