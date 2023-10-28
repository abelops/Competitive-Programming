"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        mp = defaultdict(list)
        imp = defaultdict(int)
        for i in employees:
            mp[i.id].extend(i.subordinates)
            imp[i.id]=i.importance
        st = [id]
        ans = []
        tot = 0
        while st:
            # print(st)
            poped = st.pop()
            ans.append(poped)
            tot+=imp[poped]
            for i in mp[poped]:
                st.append(i)
        return tot
        