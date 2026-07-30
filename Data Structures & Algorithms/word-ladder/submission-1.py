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

        q = deque([(beginWord, 1)])
        visited.add(u)

        while q:
            u, steps = q.popleft()
            if u == endWord:
                return steps
            for v in adj[u]:
                if v not in visited:
                    visited.add(v)
                    q.append((v, steps+1))
        
        return 0


                