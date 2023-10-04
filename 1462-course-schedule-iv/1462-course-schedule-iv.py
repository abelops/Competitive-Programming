class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        mat = [[0 if i == j else float("inf") for i in range(numCourses+1)] for j in range(numCourses+1)]
        for start, end in prerequisites:
            mat[start][end] = 1

        for k, dk in enumerate(mat):
            for i, di in enumerate(mat):
                for j in range(numCourses + 1):
                    if di[k] + dk[j] < di[j]:
                        di[j] = di[k] + dk[j]
        ans = []
        for start, end in queries:
            d = mat[start][end]
            if d == float("inf"):
                ans.append(False)
            else:
                ans.append(True)
        return ans
        
        