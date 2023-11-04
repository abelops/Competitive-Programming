class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for i in asteroids:
            if not st:
                st.append(i)
            else:
                stat = True
                while st and (st[-1] > 0 and i < 0):
                    if abs(st[-1]) < abs(i):
                        st.pop()
                    elif abs(st[-1]) == abs(i):
                        st.pop()
                        stat = False
                        break
                    else:
                        stat = False
                        break
                if stat:
                    st.append(i)
        return st
                    
                    
                
                    
                    
                    
                
                    