class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        salary.pop()
        salary.pop(0)
        sums = 0
        for i in salary:
            sums+=i
        ans = round(sums/len(salary), 5)
        return ans