class Solution:
	def detectCycle(self, V, adj):
		parents = {u: u for u in range(V)}
		rank = [0]*V
		
		def find_p(u):
		    if parents[u] != u:
		        parents[u] = find_p(parents[u])
		    return parents[u]
	
	    def union_p(u, v):
	        root_u = find_p(u)
            root_v = find_p(v)
            
	        if root_u == root_v:
                return False # Cycle detected!
            
            if rank[root_u] > rank[root_v]:
                parents[root_v] = root_u
            elif rank[root_u] < rank[root_v]:
                parents[root_u] = root_v
            else:
                parents[root_v] = root_u
                rank[root_u] += 1
		    
		    return True
		    
		for u in range(V):
		    for v in adj[u]:
		        if u < v :
    		        if not union_p(u, v):
                        return True
		        
        return False

if __name__ == '__main__':
  directed_graph_with_cycle = {
        0: [1],
        1: [2],
        2: [0, 3],
        3: []
    }
  directed_graph_without_cycle = {
      0: [1],
      1: [2],
      2: [3],
      3: []
  }

  print(Solution.detectCycle(4, directed_graph_with_cycle))
  print(Solution.detectCycle(4, directed_graph_without_cycle))
  
		        
		
