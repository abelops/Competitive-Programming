#User function Template for python3

class Solution:
    #Heapify function to maintain heap property.
    def swap(self, arr, l, r):
        arr[l], arr[r] = arr[r], arr[l]
    
    def heapify(self,arr, n, i):
        # code here
        max_ = i
        l = 2*max_ + 1
        r = 2*max_ + 2
        
        if l < n and arr[l] > arr[max_]:
            max_ = l
        
        if r < n and arr[r] > arr[max_]:
            max_ = r
        
        if max_ != i:
            arr[i], arr[max_] = arr[max_], arr[i]
            self.heapify(arr, n, max_)
            
                
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        # code here
        for i in range((len(arr)-2)//2, -1, -1):
            self.heapify(arr, n, i)
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here
        self.buildHeap(arr, n)
        # print(arr)
        for i in range(n-1, -1, -1):
            self.swap(arr, 0, i)
            self.heapify(arr, i, 0)

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends