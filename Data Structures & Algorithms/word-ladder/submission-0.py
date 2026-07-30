class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0
        
        word_len = len(beginWord)
        n = len(wordList)

        def is_possible(a, b):
            l = 0
            mismatches = 0 
            for l in range(word_len):
                if a[l] != b[l]:
                    mismatches += 1

                if mismatches > 1:
                    return False
            
            return True

        adj = defaultdict(set)
        visited = set()

        wordList.append(beginWord)
        for u in wordList:
            for v in wordList:
                if u == v:
                    continue
                
                # print(f'checking {u} and {v}')
                if is_possible(u, v):
                    adj[u].add(v)

        # print(adj)

        self.steps = float('inf')

        def dfs(u, cur_steps):
            if cur_steps >= self.steps:   # prune: can't possibly improve
                return

            visited.add(u)
            cur_steps += 1
            if u == endWord:
                self.steps = min(self.steps, cur_steps)
                visited.remove(u) # otherwise we permanently mark it as visited as this will cause issue for other branches
                return 
            
            for v in adj[u]:
                if v not in visited:
                    dfs(v, cur_steps)
            
            cur_steps -= 1
            visited.remove(u)
            
        dfs(beginWord, 0)
        return 0 if self.steps == float('inf') else self.steps


                