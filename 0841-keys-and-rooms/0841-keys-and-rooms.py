class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = deque([0])
        ans = 1
        visited = set([0])
        while q:
            poped = q.popleft()
            for i in rooms[poped]:
                if i not in visited:
                    q.append(i)
                    ans+=1
                    visited.add(i)
        return True if ans == len(rooms) else False