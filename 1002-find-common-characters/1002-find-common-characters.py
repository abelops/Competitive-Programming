class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        wordList = [ 0 for x in range(26)]
        ans=[]
            
        for i in range(len(words)):
            for j in range(26):
                tmp = words[i].count(chr(97+j))
                if i == 0:
                    wordList[j]+=tmp
                elif wordList[j] > 0:
                    wordList[j] = min(tmp,wordList[j])
            
                
        for i in range(len(wordList)):
            if wordList[i] > 0:
                for j in range(wordList[i]):
                    ans.append(chr(i+97))
        return(ans)