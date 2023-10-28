class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        ans = defaultdict(list)
        curMax = []
        for i in range(len(senders)):
            ans[senders[i]].extend(messages[i].split(" "))
            if not curMax:
                curMax = [len(ans[senders[i]]),senders[i]]
            else:
                l = len(ans[senders[i]])
                if curMax[0] == l:
                    curMax = [l, senders[i]] if senders[i] > curMax[1] else curMax
                else:
                    curMax = max(curMax, [l, senders[i]])
        # print(ans)
        return curMax[1]
        