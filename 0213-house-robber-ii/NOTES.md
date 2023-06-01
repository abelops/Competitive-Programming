arr = [(0,nums[0]),(-1, 0)]
tot = len(nums)
for i in range(1, tot):
print(arr)
if arr[0][0] + 2 < tot-1:
arr[0] = (arr[0][0]+2, arr[0][1]+ nums[arr[0][0]+2])
if arr[1][0] + 2 < tot:
arr[1] = (arr[1][0]+2, arr[1][1]+ nums[arr[1][0]+2])
# print(arr)
return max(arr[0][1], arr[1][1], max(nums))