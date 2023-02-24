class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans = {}
        maxFruit = 0
        l = 0
        fruitLen = len(fruits)
        for r in range(fruitLen):
            ans[fruits[r]] = 1 + ans.get(fruits[r],0)
            while len(ans) > 2:
                ans[fruits[l]] -= 1
                if ans[fruits[l]] <= 0:
                    ans.pop(fruits[l])
                l+=1
            maxFruit = max(maxFruit, r-l+1)
            # print(l,r,ans)
        return maxFruit
                
            