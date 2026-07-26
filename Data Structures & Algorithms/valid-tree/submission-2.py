class DUS:
    #disjoint union set 
    def __init__(self, n):
        self.parents = {i: i for i in range(n)}
    
    def find_parent(self, p):
        if p != self.parents[p]:
            self.parents[p] = self.find_parent(self.parents[p])
        return self.parents[p]

    def has_cycle_by_union(self, p1, p2):
        p1_parent, p2_parent = self.find_parent(p1), self.find_parent(p2)
        #already a cycle is present thus marking it as false
        if p1_parent == p2_parent:
            return True
        
        if p1_parent < p2_parent:
            self.parents[p2_parent] = p1_parent
        elif p1_parent > p2_parent:
            self.parents[p1_parent] = p2_parent

        return False

class Solution:    
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        dus = DUS(n)
        for u, v in edges:
            if dus.has_cycle_by_union(u, v):
                return False

        # print(f'{dus.parents=}')
         
        return True if len(set(dus.find_parent(i) for i in range(n))) == 1 else False
            
