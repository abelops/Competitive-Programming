class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        degree = defaultdict(int)
        mp = defaultdict(list)
            
        for i in prerequisites:
            mp[i[1]].append(i[0])
            # if i[0] in mp and i[1] in mp[i[0]]:
            #     return []
            degree[i[0]] += 1
            if i[1] not in degree:
                degree[i[1]] = 0
        for i in range(numCourses):
            if i not in mp:
                mp[i] = []
            if i not in degree:
                degree[i] = 0
        q = deque()
        ans = []
        for i in degree:
            if not degree[i]:
                q.append(i)
        while q:
            # print(q)
            poped = q.popleft()
            ans.append(poped)
            if mp[poped]:
                for child in mp[poped]:
                    degree[child]-=1
                    if not degree[child]:
                        q.append(child)
        if len(ans) == numCourses:
            return True
        return False