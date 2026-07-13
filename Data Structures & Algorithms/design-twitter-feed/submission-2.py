class Twitter:
    def __init__(self):
        self.links = defaultdict(set)  # (user_id -> [followeeId])
        self.user_tweets = defaultdict(list) # (userId, tweetId)
        self.feed_len = 10
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.user_tweets[userId].append((self.time, tweetId))
    
    def _merge_k_sorted_arrays_desc(self, arrays):
        result = []
        max_heap = []
        # 1. Initialize the heap with 1st value of arr as that's most recent 
        for arr_idx, arr in enumerate(arrays):
            if arr:
                j = len(arr) - 1
                # Push (val, array index, element index)
                heapq.heappush_max(max_heap, (arr[j], arr_idx, j))
        
        result = []
        while max_heap and len(result) < self.feed_len:
            val, arr_idx, elem_j = heapq.heappop_max(max_heap)
            result.append(val)
            if elem_j - 1 >= 0:
                next_j =  elem_j - 1
                heapq.heappush_max(max_heap, (arrays[arr_idx][next_j], arr_idx, next_j))
        return result
        

    def getNewsFeed(self, userId: int) -> List[int]:
        self.links[userId].add(userId)
        all_tweets = []
        for user in self.links[userId]:
            all_tweets.append(self.user_tweets[user])
        #merge k sorted arrays in desc order
        res = self._merge_k_sorted_arrays_desc(all_tweets)
        return list(map(lambda x: x[1], res))

    def follow(self, followerId: int, followeeId: int) -> None:
        self.links[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.links and followeeId in self.links[followerId]:
            self.links[followerId].remove(followeeId)
