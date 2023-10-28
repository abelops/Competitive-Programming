import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        min_heap = [(nums1[0] + nums2[0], 0, 0)]
        pairs = []

        while min_heap and len(pairs) < k:
            current_sum, index1, index2 = heapq.heappop(min_heap)
            pairs.append([nums1[index1], nums2[index2]])
            
            if index2 == 0 and index1 + 1 < len(nums1):
                next_sum = nums1[index1+1] + nums2[index2]
                next_index1 = index1 + 1
                next_index2 = index2
                heapq.heappush(min_heap, (next_sum, next_index1, next_index2))
            if index2 + 1 < len(nums2):
                next_sum = nums1[index1] + nums2[index2+1]
                next_index1 = index1
                next_index2 = index2 + 1
                heapq.heappush(min_heap, (next_sum, next_index1, next_index2))

        return pairs