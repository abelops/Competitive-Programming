class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def check(p1, p2):
            dist = sqrt( (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 )
            if dist <= p1[2]:
                return True
            return False
        
        ans = 0
        mp = defaultdict(int)
        for i in range(len(bombs)):
            if tuple(bombs[i]) not in mp:     
                visited = [False] * len(bombs)
                temp = 0
                st = [bombs[i]]
                while st:
                    poped = st.pop() 
                    temp1 = 0
                    temp+=1
                    for j in range(len(bombs)):
                        if i != j:
                            if check(poped, bombs[j]) and not visited[j]:
                                visited[j] = True
                                st.append(bombs[j])
                                temp1+=1
                    mp[tuple(poped)] = temp1
                ans = max(ans, temp)
        return ans
            