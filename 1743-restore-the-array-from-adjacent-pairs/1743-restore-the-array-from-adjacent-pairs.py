class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        mp = defaultdict(list)
        for i,j in adjacentPairs:
            mp[i].append(j)
            mp[j].append(i)
        visited = set()
        ans = []
        for i in mp:
            if len(mp[i]) == 1:
                visited.add(i)
                # ans.append(i)
                st = [i]
                while st:
                    poped = st.pop()
                    ans.append(poped)
                    for j in mp[poped]:
                        if j not in visited:
                            st.append(j)
                            visited.add(j)
                break
        return ans