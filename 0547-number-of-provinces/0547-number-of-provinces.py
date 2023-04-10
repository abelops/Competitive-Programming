class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        mp = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1:
                    mp[i+1].append(j+1)
        # print(mp)
        
        provinces = []
        visited = []  
        for i in range(len(isConnected)):
            st = [i+1]
            ans = []
            while st:
                poped = st.pop()
                if poped not in visited:
                    ans.append(poped)
                    visited.append(poped)
                for i in mp[poped]:
                    if i != poped and i not in visited:
                        st.append(i)
                # print(visited)
            if ans:
                provinces.append(ans)
        # print(provinces)
        return len(provinces)
            
            