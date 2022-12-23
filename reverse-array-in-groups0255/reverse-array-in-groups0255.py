#User function template for Python

class Solution:	
    #Function to reverse every sub-array group of size k.
	def reverseInGroups(self, arr, N, K):
		# code here
		c=0
		for i in range(0,N,K):
		    arr[i:i+K] = arr[i:i+K][::-1]
