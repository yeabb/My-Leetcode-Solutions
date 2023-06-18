import heapq
class Twitter:

    def __init__(self):
        self.users={}  #users={userId:[set(following),set(followers)]}
        self.time=-1
        self.posts={}     # posts= {userId:[heap of 10 recent posts]}
        
        #user={userId}
        #users={1:[{}, {}, [(-1,1)] ]}
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time-=1
        if userId not in self.users:
            self.users[userId]=[set()]
            self.posts[userId]=[]

        self.posts[userId].append((self.time, tweetId))

        

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId in self.users:
            heap=[]
            for i in range(1, 11):
                tempHeap=[]

                if len(self.posts[userId])>=i:
                    heapq.heappush(tempHeap, self.posts[userId][-1*i])
              
                for following in self.users[userId][0]:
                    if len(self.posts[following])>=i:
                        heapq.heappush(tempHeap, self.posts[following][-1*i])
                if tempHeap:
                    while tempHeap:
                        heapq.heappush(heap, heapq.heappop(tempHeap))
                else:
                    break

            tweets=[]
            track=0
            while heap and track<10:
                tweet=heapq.heappop(heap)[1]
                tweets.append(tweet)
                track+=1
            
            return tweets



    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId]=[set()]
            self.posts[followerId]=[]
        if followeeId not in self.users:
            self.users[followeeId]=[set()]
            self.posts[followeeId]=[]
        self.users[followerId][0].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        
        
        if followerId in self.users and followeeId in self.users[followerId][0]: 
            self.users[followerId][0].remove(followeeId)
       
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)