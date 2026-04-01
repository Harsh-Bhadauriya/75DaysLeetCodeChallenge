class Solution:
    def evalRPN(self, tokens):
        st = []
        
        for t in tokens:
            if t in "+-*/":
                b = st.pop()
                a = st.pop()
                
                if t == "+":
                    st.append(a + b)
                elif t == "-":
                    st.append(a - b)
                elif t == "*":
                    st.append(a * b)
                else:
                    st.append(int(a / b))  # truncate toward 0
            else:
                st.append(int(t))
        
        return st[0]
print(Solution().evalRPN(["2","1","+","3","*"]))