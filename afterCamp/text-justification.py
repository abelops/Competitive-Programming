class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        arr = []
        cur = 0
        words.reverse()
        while words:
            popedWord = words.pop()
            arr.append(popedWord)
            cur+=len(popedWord)
            if cur + len(arr)-1 > maxWidth:
                poped = arr.pop()
                words.append(poped)
                cur -= len(poped)
                l = len(arr)
                space = maxWidth - cur
                if l == 1:
                    sp = " " * (maxWidth-len(arr[0]))
                    ans.append(arr[0]+sp)
                elif space % (l-1) == 0:
                    s = " " * (space // (l-1))
                    ans.append(s.join(arr))
                else:
                    s = " " * (space // (l-1))
                    mod = space % (l-1)
                    temp = []
                    i = 0
                    # print(s.join(arr), "_________",mod)
                    arr.reverse()
                    # print(arr)
                    while arr:
                        curPoped = arr.pop()
                        # print(mod,curPoped+s+" " * mod)
                        if len(arr) != 0:
                            temp.append(curPoped+s+(" " if mod > 0 else ""))
                        else:
                            temp.append(curPoped)
                        i+=1
                        mod-=1
                    ans.append("".join(temp))
                arr = []
                cur = 0
        if arr:
            l = len(arr)
            space = maxWidth - cur
            if l == 1:
                sp = " " * (maxWidth-len(arr[0]))
                ans.append(arr[0]+sp)
            else:
                sp = " ".join(arr)
                ans.append(sp+ " " *(maxWidth-len(sp)))
            
        return ans