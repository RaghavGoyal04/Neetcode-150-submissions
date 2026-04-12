class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        operators = {"+", "-", "*", "/"}
        for t in tokens:
            if t in operators:
                a = st.pop()
                b = st.pop()
                if t == '+':
                    st.append(a+b)
                elif t == '-':
                    st.append(b-a)
                elif t == '*':
                    st.append(a*b)
                else:
                    # print(a, b, b//a)
                    st.append(int(b/a))
            else:
                st.append(int(t))
            # print(st)
        return st[0]


        