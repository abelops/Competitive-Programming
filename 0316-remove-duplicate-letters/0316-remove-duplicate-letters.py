class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        mp = defaultdict(int)
        for i in range(len(s)):
            mp[s[i]] = i
        st = []
        for i in range(len(s)):
            if s[i] not in st:
                while st and s[i] < st[-1] and i < mp[st[-1]]:
                    st.pop()
                st.append(s[i])
        return "".join(st)
    

                