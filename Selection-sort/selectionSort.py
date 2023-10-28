#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        min_val = i
        for j in range(i + 1,len(arr)):
            if arr[min_val] > arr[j]:
                min_val = j
        return [arr[min_val], arr[i], min_val]
        
    def selectionSort(self, arr,n):
        #code here
        for index in range(len(arr)-1):
            ans = self.select(arr, index)
            arr[index],arr[ans[2]] = ans[0], ans[1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends