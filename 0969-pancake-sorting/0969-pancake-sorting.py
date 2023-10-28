class Solution:
    res = []
    def pancakeSort(self, arr: List[int]) -> List[int]:
        self.res = []
        self.recurhelp(arr, len(arr))
        return self.res
    
    def recurhelp(self, arr, n):
        if n == 1:
            return
        tempmax = 0
        index = 0
        for i in range(n):
            if arr[i] > tempmax:
                tempmax = arr[i]
                index = i
        self.res.append(index + 1)
        self.reverse(arr, 0, index)
        self.res.append(n)
        self.reverse(arr, 0, n - 1)
        
        self.recurhelp(arr, n - 1)
        
        
    
    def reverse(self, arr, i, j):
        while i < j:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
            j -= 1