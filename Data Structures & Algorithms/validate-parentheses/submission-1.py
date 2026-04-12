class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        brackets = {']' : '[', '}' : '{', ')' : '('}
        for i in s:
            if i in brackets:
                if not st or brackets[i] != st[-1]: 
                    return False 
                else:
                    st.pop()
            else:
                st.append(i)
        return False if st else True
            
        