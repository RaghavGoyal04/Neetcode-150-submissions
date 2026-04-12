class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n
        st = [] # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while st and t > st[-1][0]:
                stackT, stackInd = st.pop()
                res[stackInd] = i - stackInd
            st.append((t, i))
            
        return res
        
        

#      [30,38,30,36,35,40,28]
#       0.  1. 2. 3. 4. 5. 6
# res  [ 0, 0, 0, 0, 0, 0, 0] st = []
# n=>0 [ 0, 0, 0, 0, 0, 0, 0] st = [(38, 0)
# n=>1 [ 1, 0, 0, 0, 0, 0, 0] st = [(38, 1)
# n=>2 [ 1, 0, 0, 0, 0, 0, 0] st = [(38, 1), (30, 2)
# n=>3 [ 1, 0, 1, 0, 0, 0, 0] st = [(38, 1), (36, 3)
# n=>4 [ 1, 0, 1, 0, 0, 0, 0] st = [(38, 1), (36, 3), (35,4)
# n=>5 [ 1, 4, 1, 2, 1, 0, 0] st = [(40, 5)
# n=>6 [ 1, 4, 1, 2, 1, 0, 0] st = [(40, 5), (20, 6)
