class DUS:
    def __init__(self, n):
        self.parents = {i: i for i in range(n)}
    def find(self, p):
        if p != self.parents[p]:
            self.parents[p] = self.find(self.parents[p])
        return self.parents[p]
    def union(self, p1, p2):
        p1_par, p2_par = self.find(p1), self.find(p2)
        if p1_par == p2_par:
            return False
        if p1_par > p2_par:
            self.parents[p1_par] = p2_par
        else:
            self.parents[p2_par] = p1_par
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        dus = DUS(n+1)
        for u, v in edges:
            if not dus.union(u, v):
                return [u, v]
        
        return []



