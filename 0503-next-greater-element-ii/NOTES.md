class Solution:
def nextGreaterElements(self, nums: List[int]) -> List[int]:
st = []
nums.extend(nums)
mp = defaultdict(int)
dis = []
for i in range(len(nums)):
if st:
while st and nums[st[-1]] < nums[i]:
temp = st.pop()
mp[temp] = nums[i]
st.append(i)
st = []
for i in range(len(nums)):
if i not in mp:
mp[i] = -1
ans = []
for i in range(len(nums)):
ans.append(mp[i])
return ans[:int(len(nums)/2)]