class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        fin = ""
        strs.sort()
        word1= strs[0]
        word2= strs[-1]
        for i in range(len(word1)):
            if i > len(word2):
                break
            if word1[i]==word2[i]:
                fin+=word1[i]
            else:
                break
        return fin
    
            
        