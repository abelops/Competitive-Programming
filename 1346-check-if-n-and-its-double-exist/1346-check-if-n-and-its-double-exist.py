class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        mp = {}
        for i, num in enumerate(arr):
            if i not in arr:
                mp[num] = i
        for i, num in enumerate(arr):
            if num*2 in mp:
                if mp[num*2] != i:
                    return True
        return False
#         for i in range(len(arr)):
#             for j in range(len(arr)):
#                 if arr[i] * 2 == arr[j] and i != j:
#                     return True
#         return False
            
            
        