class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ans = []
        for i in words:
            n = 0
            for j in i:
                # print(bin(n), bin(ord(j)-ord('a')))
                n |= 1 << ord(j)-ord('a')
            ans.append(n)
        fin = 0
        length = list(map(lambda x: len(x), words))
        for x in range(len(ans)):
            for y in range(x+1,len(ans)):
                if ans[x] & ans[y] == 0:
                    fin = max(length[x]*length[y], fin)
        return fin
                
            
