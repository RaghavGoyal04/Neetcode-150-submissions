class DUS:
    def __init__(self, n):
        self.parents = {i: i for i in range(n)}

    def find(self, p):
        if p != self.parents[p]:
            self.parents[p] = self.find(self.parents[p])
        return self.parents[p]

    def union(self, p1, p2):
        p1_par, p2_par = self.find(p1), self.find(p2)
        if p1_par < p2_par:
            self.parents[p2_par] = p1_par
        elif p1_par > p2_par:
            self.parents[p1_par] = p2_par

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(set)
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)
        
        dsu = DUS(n)

        for u, v in edges:
            dsu.union(u, v)
        
        return len(set(dsu.find(i) for i in range(n)))
