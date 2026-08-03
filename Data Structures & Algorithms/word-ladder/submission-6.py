class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0
        
        adj = defaultdict(set)
        visited = set()
        word_len = len(beginWord)
        wordList.append(beginWord)
        n = len(wordList)

        for word in wordList:
            for j in range(word_len):
                pattern = word[:j] + '*' + word[j+1:]
                adj[pattern].add(word)

        # print(adj)

        q = deque([(beginWord, 1)])
        visited.add(beginWord)

        while q:
            u, steps = q.popleft()
            if u == endWord:
                return steps
            
            for j in range(word_len):
                pattern = u[:j] + '*' + u[j+1:]
                for v in adj[pattern]:
                    if v not in visited:
                        visited.add(v)
                        q.append((v, steps+1))
        
        return 0


                