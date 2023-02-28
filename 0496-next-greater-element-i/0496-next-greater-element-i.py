class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st = []
        mp = defaultdict(int)
        for i in nums2:
            if not st:
                st.append(i)
            else:
                while st and st[-1] < i:
                    temp = st.pop()
                    mp[temp] = i
                st.append(i)
        for i in st:
            mp[i] = -1
        ans = []
        for i in nums1:
            ans.append(mp[i])
        return ans
                