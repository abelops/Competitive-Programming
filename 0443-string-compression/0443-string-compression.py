class Solution:
    def compress(self, chars: List[str]) -> int:
        st = [chars[0]]
        coun = 1
        for i in range(1,len(chars)):
            if chars[i] != st[-1]:
                if coun>1:
                    for j in range(len(str(coun))):
                        st.append(str(coun)[j])
                coun=1
                st.append(chars[i])
            else:  
                coun+=1
        if coun>1:
            for j in range(len(str(coun))):
                st.append(str(coun)[j])
        chars[:]=st
        return len(chars)