class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [-1]
        for i in range(len(arr)-1, 0, -1):
            if arr[i] > ans[-1]:
                ans.append(arr[i])
            else:
                ans.append(ans[-1])
        return reversed(ans)
        