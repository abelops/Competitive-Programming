class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        mp = defaultdict(list)
        deg = defaultdict(int)
        for prereq,course in prerequisites:
            mp[prereq].append(course)
            deg[course]+=1
        q = deque()
        for i in range(numCourses):
            if not deg[i]:
                q.append(i)
        ans = defaultdict(set)
        while q:
            poped = q.popleft()
            for i in mp[poped]:
                deg[i]-=1
                ans[i].add(poped)
                ans[i].update(ans[poped])
                if not deg[i]:
                    q.append(i)
        fin = []   
        for prereq, course in queries:
            if prereq in ans[course]:
                fin.append(True)
            else:
                fin.append(False)
        return fin
        