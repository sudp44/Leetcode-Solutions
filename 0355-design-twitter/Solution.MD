**Design Twitter**

---

**Problem**  
Design a simplified version of Twitter where users can post tweets, follow/unfollow other users, and view the 10 most recent tweets from themselves and the users they follow (sorted from most recent to least recent).

**Core Idea**  
- Each user has a **linked list of their own tweets** (newest first).  
- A **global timestamp** determines tweet ordering.  
- To build a news feed, use a **max‑heap** that merges the tweet heads of all followed users (including self).  
- Keep popping the most recent tweet and push its older sibling back into the heap, repeating up to 10 times.

**Internal Data Structures**  
- `Tweet`: stores `id`, `time`, and a `next` pointer (singly linked list).  
- `User`: stores `id`, a `followed` set (includes self), and a `tweet_head` pointer.  
- `user_map`: dictionary mapping `user_id -> User`.  
- Global `_timestamp` (class variable) incremented on every tweet.

**Algorithm Steps**

**`postTweet(userId, tweetId)`**  
1. Get (or create) the user.  
2. Create a new `Tweet` with current timestamp and insert it at the head of the user's tweet list.  
3. Increment global timestamp.

**`getNewsFeed(userId)`**  
1. If user doesn't exist, return `[]`.  
2. Build a max‑heap with the **tweet head** of every followed user (skip users who haven't tweeted).  
   - Python's `heapq` is a min‑heap → store `(-tweet.time, id(tweet), tweet)` to simulate max‑heap.  
   - `id(tweet)` breaks ties when times are equal (prevents comparing Tweet objects directly).  
3. Pop from the heap up to 10 times:  
   - Append `tweet.id` to the result.  
   - If the popped tweet has a `next` (older tweet), push that next tweet into the heap.  
4. Return the collected tweet IDs.

**`follow(followerId, followeeId)`**  
- Ensure both users exist in `user_map`.  
- Add `followeeId` to the follower's `followed` set.

**`unfollow(followerId, followeeId)`**  
- If follower exists and is not trying to unfollow themselves, remove `followeeId` from their `followed` set.

**Time Complexity**  
- `postTweet`: O(1)  
- `getNewsFeed`: O(F + k log F) where F = number of followed users (≤ 500), k = 10 → effectively O(1)  
- `follow` / `unfollow`: O(1) on average (set operations)

**Space Complexity**  
- O(U + T) where U = number of users, T = total tweets stored (each tweet as a node in linked lists).

**Why the Skeleton Looks Minimal**  
- LeetCode gives only the public methods. The inner classes `Tweet` and `User` are implementation details you design yourself. The signature doesn’t force a specific internal structure.

**Common Pitfalls**  
- Forgetting that a user follows themselves → include self in the followed set from the start.  
- Not handling users who have never tweeted (their `tweet_head` is `None`).  
- Python heap tie‑breaking: tuples with same timestamp would compare the next element (Tweet), which is not comparable → use `id(tweet)` as a unique tie‑breaker.  
- Storing tweets in a list instead of a linked list → merging becomes less efficient.  
- Not incrementing the global timestamp correctly (leads to wrong ordering).

**Memory Hook**  
> *"Each user has a tweet list (LIFO). Global clock ticks on every tweet. News feed = merge k sorted lists (the followed users' tweet heads) using a max‑heap, take top 10."*
