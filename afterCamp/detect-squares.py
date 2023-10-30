class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)]+=1

    def count(self, point: List[int]) -> int:
        ans = 0
        px, py = point
        for x, y in list(self.points):
            if abs(px - x) == abs(py - y) and (x != px and y != py):
                ans+=self.points[(x,y)] * self.points[(px, y)] * self.points[(x, py)]
        return ans

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)