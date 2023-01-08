class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evenNums = []
        evenSum = 0
        ans = []
        
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                evenNums.append(i)
                evenSum+=nums[i]
        # print(evenNums, evenSum)
        
        for j in range(len(queries)):
            newNum = queries[j][0] + nums[queries[j][1]]
            if newNum % 2 == 0 and newNum != 0:
                if queries[j][1] not in evenNums:
                    evenNums.append(queries[j][1])
                    evenSum+= newNum
                else:
                    evenSum -= nums[queries[j][1]]
                    evenSum += newNum
            else:
                if queries[j][1] in evenNums:
                    evenNums.remove(queries[j][1])
                    evenSum-= nums[queries[j][1]]
            # print(nums[queries[j][1]], newNum)
            nums[queries[j][1]] = newNum
            ans.append(evenSum)
            # print(nums,evenNums, evenSum)
        return ans