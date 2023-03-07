class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        # def searchForLen(arr, w):
        #     l = 0
        #     r = len(arr)-1
        #     wLen = w
        #     ans = -1
        #     while l <= r:
        #         mid = l + (r-l)//2
        #         if len(arr[mid]) >= wLen:
        #             r = mid - 1
        #             ans = mid
        #         elif len(arr[mid]) < wLen:
        #             l = mid + 1
        #     # print(ans)
        #     return ans
                    
        words = sorted([sorted(x) for x in words])
        queries =  [sorted(x) for x in queries]
        wordsLen = len(words)
        words = [x.count(x[0]) for x in words]
        # print(words, queries)
        ans = []
        for i in queries:
            countOfChar = i.count(i[0])
            # firstWord = searchForLen(words, countOfChar)
            # if firstWord == -1:
            #     ans.append(0)
            #     continue
            c = 0
            for j in range(wordsLen):
                c1 = i.count(i[0])
                c2 = words[j]
                # print(c1, i[0], c2, words[j][0], words[j])
                if c1 < c2:
                    c+=1
            ans.append(c)
        return ans