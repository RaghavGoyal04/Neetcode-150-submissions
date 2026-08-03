class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {src: [] for src, dst in tickets}
        tickets.sort()
        for src, dst in tickets:
            adj[src].append(dst)

        res = ["JFK"]
        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True

            if src not in adj:
                return False

            temp = adj[src]
            for i, v in enumerate(temp):
                adj[src].pop(i) # this is required as otherwise we will go into a cycle
                res.append(v)
                if dfs(v): return True # found the shortest path
                adj[src].insert(i, v)
                res.pop()
            return False

        dfs("JFK")
        return res