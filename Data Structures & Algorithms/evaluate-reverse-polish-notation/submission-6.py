class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # st = []
        # for t in tokens:
        #     if t in "+-*/"::
        #         a = st.pop()
        #         b = st.pop()
        #         if t == '+':
        #             st.append(a+b)
        #         elif t == '-':
        #             st.append(b-a)
        #         elif t == '*':
        #             st.append(a*b)
        #         else:
        #             # print(a, b, b//a)
        #             st.append(int(float(b)/a))
        #     else:
        #         st.append(int(t))
        #     # print(st)
        # return st[0]

        #recursive using dfs
        def dfs():
            t = tokens.pop()
            if t not in '+-*/':
                return int(t)
            a = dfs()
            b = dfs()

            if t == '+':
                return b+a
            elif t == '-':
                return b-a
            elif t == '*':
                return b*a
            else:
                return int(float(b)/a)
        return dfs()


        