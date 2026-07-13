class Twitter:
    def __init__(self):
        self.links = defaultdict(set)  # (user_id -> [followeeId])
        self.user_tweets = defaultdict(list) # (userId, tweetId)
        self.feed_len = 10
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.user_tweets[userId].append((self.time, tweetId))
        
    def getNewsFeed(self, userId: int) -> List[int]:
        self.links[userId].add(userId)
        res = []
        for user in self.links[userId]:
            res.extend(self.user_tweets[user])
        return list(map(lambda x: x[1] , sorted(res, reverse=True, key = lambda x: x[0])[:self.feed_len]))

    def follow(self, followerId: int, followeeId: int) -> None:
        self.links[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.links and followeeId in self.links[followerId]:
            self.links[followerId].remove(followeeId)
