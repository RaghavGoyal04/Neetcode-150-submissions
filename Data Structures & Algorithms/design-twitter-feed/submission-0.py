class Twitter:
    def __init__(self):
        self.links = defaultdict(set)  # (user_id -> [followeeId])
        self.global_tweets = []  # (tweetId, userId) maxheap with latest tweet first
        self.feed_len = 10
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        # self.user_tweets[userId].add(tweetId)
        self.time += 1
        heapq.heappush_max(self.global_tweets, (self.time, tweetId, userId))
        # heapq.heappush_max(self.global_tweets, (tweetId, userId))
        # print(f"{len(self.global_tweets)=}")

    def getNewsFeed(self, userId: int) -> List[int]:
        total_followers = {userId}
        total_followers.update(self.links[userId])
        # print(f"{userId=} -> {total_followers=}")

        temp_global_tweets = []
        res = []
        curr_len = 0
        while len(self.global_tweets) and curr_len < self.feed_len:
            time, t_id, u_id = heapq.heappop_max(self.global_tweets)
            # t_id, u_id = heapq.heappop_max(self.global_tweets)
            # print(f"while poping: {t_id=}, {u_id=}")
            if u_id in total_followers:
                res.append(t_id)
                curr_len += 1
            temp_global_tweets.append((time, t_id, u_id))
            # temp_global_tweets.append((t_id, u_id))

        for i in temp_global_tweets:
            heapq.heappush_max(self.global_tweets, i)
        temp_global_tweets = []
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.links[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.links and followeeId in self.links[followerId]:
            self.links[followerId].remove(followeeId)
