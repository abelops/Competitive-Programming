class Solution:
    def balancedString(self, s: str) -> int:
        mp = defaultdict(int)
        target = Counter(s)
        for i in s:
            mp[i] = 0
            if target[i] == len(s)/4:
                target.pop(i)
        targetSum = 0
        for i in target:
            target[i] -= int(len(s)/4)
            if target[i] > 0:
                targetSum += target[i]
        targetBac = target.copy()
        for i in targetBac:
            if target[i] < 0:
                target.pop(i)
        if targetSum == 0:
            targetSum = len(s)/4
            
        found = 0
        cur = defaultdict(int)
        ans = []  
        l = 0
        ans = []
        for r,char in enumerate(s):
            if char in target:
                cur[char] += 1
                if cur[char] <= target[char]:
                    found+=1
            while found == targetSum:
                ans.append([r-l+1,l,r])
                if s[l] in cur:
                    cur[s[l]] -= 1
                    if cur[s[l]] < target[s[l]]:
                        found -= 1
                l+=1
        if ans:
            ans = min(ans)
            return len(s[ans[1]:ans[2]+1])
        return 0
                