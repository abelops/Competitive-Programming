class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0 for x in range(len(boxes))]
        boxes = [x for x in boxes]
        
        for i in range(len(boxes)):
                for j in range(len(boxes)):
                    if boxes[j] == '1':
                        if i != j:
                            ans[i]+=abs(j-i)
        return ans
                    