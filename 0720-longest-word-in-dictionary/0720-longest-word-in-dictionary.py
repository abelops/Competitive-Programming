class Solution:
    def longestWord(self, words: List[str]) -> str:
        # return ""
        mp = defaultdict(int)
        ans = []
        l = len(words)
        for i in range(l):
            mp[words[i]] = i
        for i in range(l):
            stat = False
            if len(words[i]) == 1:
                ans.append(words[i])
                continue
            for j in range(len(words[i])-1):
                if words[i][:j+1] not in mp:
                    break
                if j == len(words[i])-2:
                    stat = True    
            if stat:
                ans.append(words[i])
        if not ans:
            return ""
        maxLen = len(max(ans, key=len))
        newAns = list(filter(lambda item: len(item) == maxLen, ans))
        return sorted(newAns)[0]