class Solution:
    def checkValidString(self, s: str) -> bool:
        """
            ()
            (*)
            (*))
            *(
        """
        op = []
        st = []
        for i,n in enumerate(s):
            if n == "(":
                op.append(i)
            elif n == "*":
                st.append(i)
            elif n == ")":
                if len(op) == len(st)==0:
                    return False
                if len(op)>0:
                    op.pop()
                else:
                    if len(st)>0:
                        st.pop()
        while op and st:
            if op.pop()>st.pop():
                return False
        if len(op)==0:
            return True
                    