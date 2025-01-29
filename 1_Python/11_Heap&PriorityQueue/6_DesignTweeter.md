要点：

帖子的数据结构：
1、每个帖子用一个tuple存储：(timestamp, userid, tweetid)，其中userid是key所以也可以不存储
2、每个人的帖子库用一个heap存储；heap可以存储tuple并按照第一个元素进行排序
3、所有人的帖子存储在一个dictionary中 {user_id: heap}

关注列表：
1、用一个dictionary存储：{user_id: set()}
2、加关注的时候注意要判断id是不是自己的id

其他要点：
1、用timestamp时间戳进行记时
2、这道题的最难点和优化点其实就是 getNewsFeed

最优解 Ot(n) for getNewsFeed
```python
class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)  # userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set)  # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        if len(self.tweetMap[userId]) > 10:
            self.tweetMap[userId].pop(0)
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        self.followMap[userId].add(userId)
        if len(self.followMap[userId]) >= 10:
            maxHeap = []
            for followeeId in self.followMap[userId]:
                if followeeId in self.tweetMap:
                    index = len(self.tweetMap[followeeId]) - 1
                    count, tweetId = self.tweetMap[followeeId][index]
                    heapq.heappush(maxHeap, [-count, tweetId, followeeId, index - 1])
                    if len(maxHeap) > 10:
                        heapq.heappop(maxHeap)
            while maxHeap:
                count, tweetId, followeeId, index = heapq.heappop(maxHeap)
                heapq.heappush(minHeap, [-count, tweetId, followeeId, index])
        else:
            for followeeId in self.followMap[userId]:
                if followeeId in self.tweetMap:
                    index = len(self.tweetMap[followeeId]) - 1
                    count, tweetId = self.tweetMap[followeeId][index]
                    heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
```