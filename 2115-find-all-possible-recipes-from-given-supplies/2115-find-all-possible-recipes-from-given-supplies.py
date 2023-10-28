class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies = set(supplies)
        degree = defaultdict(int)
        mp = defaultdict(list)
            
        ans = []
        for i in range(len(recipes)):
            for ings in ingredients[i]:
                if ings not in supplies:
                    mp[ings].append(recipes[i])
                    degree[recipes[i]] += 1
        q = deque()
        for i in recipes:
            if not degree[i]:
                q.append(i)
        while q:
            poped = q.popleft()
            ans.append(poped)
            for child in mp[poped]:
                degree[child] -= 1
                if not degree[child]:
                    q.append(child)
        return ans