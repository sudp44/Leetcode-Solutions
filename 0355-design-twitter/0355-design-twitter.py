import heapq
from typing import List

class Twitter:
    # Global timestamp shared across all instances (like static in Java)
    _timestamp = 0

    class Tweet:
        def __init__(self, tweet_id: int, time: int):
            self.id = tweet_id
            self.time = time
            self.next = None   # points to the next older tweet (or None)

    class User:
        def __init__(self, user_id: int):
            self.id = user_id
            self.followed = set()
            self.follow(user_id)               # follow self
            self.tweet_head = None             # most recent tweet

        def follow(self, user_id: int):
            self.followed.add(user_id)

        def unfollow(self, user_id: int):
            # Cannot unfollow self; remove only if present
            if user_id != self.id and user_id in self.followed:
                self.followed.remove(user_id)

        def post_tweet(self, tweet_id: int, timestamp: int):
            new_tweet = Twitter.Tweet(tweet_id, timestamp)
            new_tweet.next = self.tweet_head   # link older tweets
            self.tweet_head = new_tweet

    def __init__(self):
        self.user_map = {}   # userId -> User object

    def _get_user(self, user_id: int) -> 'Twitter.User':
        """Return the User object for user_id, creating it if necessary."""
        if user_id not in self.user_map:
            self.user_map[user_id] = self.User(user_id)
        return self.user_map[user_id]

    def postTweet(self, userId: int, tweetId: int) -> None:
        user = self._get_user(userId)
        timestamp = Twitter._timestamp
        Twitter._timestamp += 1
        user.post_tweet(tweetId, timestamp)

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.user_map:
            return []

        # Collect tweet heads of all followed users (including self)
        followed_users = self.user_map[userId].followed
        max_heap = []   # will store tuples (-time, tweet) to simulate max-heap

        for uid in followed_users:
            if uid in self.user_map:   # user may not exist if only followed but never posted
                tweet = self.user_map[uid].tweet_head
                if tweet:
                    heapq.heappush(max_heap, (-tweet.time, id(tweet), tweet))
                    # id(tweet) is used to break ties when times are equal,
                    # because Tweet objects can't be compared directly.

        news_feed = []
        count = 0
        while max_heap and count < 10:
            _, _, tweet = heapq.heappop(max_heap)
            news_feed.append(tweet.id)
            count += 1
            if tweet.next:
                heapq.heappush(max_heap, (-tweet.next.time, id(tweet.next), tweet.next))

        return news_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        follower = self._get_user(followerId)
        # Ensure the followee exists in the system
        self._get_user(followeeId)
        follower.follow(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.user_map and followerId != followeeId:
            self.user_map[followerId].unfollow(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna