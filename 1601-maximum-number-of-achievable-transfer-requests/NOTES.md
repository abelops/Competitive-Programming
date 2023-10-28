class Solution:
def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
ans = 0
reqLen = len(requests)
def backtrack(depth, prev, start):
# print(depth)
nonlocal ans
# print(depth, prev[0], prev[1])
if not prev[0] and not prev[1]:
ans = max(ans, depth)
if start >= reqLen:
return
for i in range(start, reqLen):
print(requests[i], prev[0], prev[1])
if requests[i][0] not in prev[1]:
prev[0][requests[i][0]] +=1
else:
# print("Else")
prev[1][requests[i][0]] -=1
# print(prev[1])
if prev[1][requests[i][0]] == 0:
prev[1].pop(requests[i][0])
if requests[i][1] not in prev[0]:
prev[1][requests[i][1]] += 1
else:
prev[0][requests[i][1]] -=1
if prev[0][requests[i][1]] == 0:
prev[0].pop(requests[i][1])
backtrack(depth+1, prev, i+1)
# print("REC end")
prev[0].clear()
prev[1].clear()
# depth =
return
backtrack(0, [defaultdict(int), defaultdict(int)], 0)
return ans