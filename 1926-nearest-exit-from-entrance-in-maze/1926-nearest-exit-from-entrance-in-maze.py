class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        d = [(0,1),(0,-1),(1,0),(-1,0)]
        def check(x,y):
            return 0 <= x < len(maze) and 0 <= y < len(maze[0])
        def isEdge(x,y):
            if x == 0 or x== len(maze)-1 or y == 0 or y == len(maze[0])-1:
                return True
        
        q = deque([entrance])
        level = 0
        visited = set()
        visited.add(tuple(entrance))
        while q:
            level += 1
            l = len(q)
            for _ in range(l):
                i, j = q.popleft()
                for x,y in d:
                    dx = i + x
                    dy = j + y
                    if check(dx,dy) and maze[dx][dy] == "." and (dx,dy) not in visited:
                        if isEdge(dx,dy):
                            return level
                        q.append([dx,dy])
                        visited.add((dx,dy))
        return -1