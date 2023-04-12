class ThroneInheritance:

    def __init__(self, kingName: str):
        self.start = kingName
        self.curOrder = defaultdict(list)
        self.curOrder[kingName] = []
        self.dead = set()
        self.visited = defaultdict(bool)
        self.visited[kingName] = False

    def birth(self, parentName: str, childName: str) -> None:
        self.curOrder[parentName].append(childName)
        self.curOrder[childName] = []

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        st = [self.start]
        ans = []
        # print(self.curOrder)
        while st:
            poped = st.pop()
            if poped not in self.dead:
                ans.append(poped)
                self.visited[poped] = True
            for king in self.curOrder[poped][::-1]:
                # if self.visited[king]:
                st.append(king)
        return ans


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()