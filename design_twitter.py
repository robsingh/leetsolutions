'''
Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, 
and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:

Twitter() Initializes your twitter object.

void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the user userId. 
Each call to this function will be made with a unique tweetId.

List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the user's news feed. 
Each item in the news feed must be posted by users who the user followed or by the user themself. 
Tweets must be ordered from most recent to least recent.

void follow(int followerId, int followeeId) 
The user with ID followerId started following the user with ID followeeId.

void unfollow(int followerId, int followeeId) 
The user with ID followerId started unfollowing the user with ID followeeId.
'''
from typing import List

class Twitter:
    def __init__(self):
        self.tweets = {} # stores tweet for each user
        self.following = {} # stores who follows whom
        self.time = 0 # timestamp to track the tweets

    def postTweet(self, userId:int, tweetId:int) -> None:
        self.time += 1
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((self.time, tweetId))
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].pop(0)


    def getNewsFeed(self, userId:int) -> List[int]:
        # gets feed from user and the users they follow
        feed = self.tweets.get(userId, [])[:]
        if userId in self.following:
            for followee in self.following[userId]:
                feed.extend(self.tweets.get(followee, []))
        # sort tweets by time and return the 10 most recent
        feed.sort(reverse = True, key=lambda x:x[0])
        return [tweet[1] for tweet in feed[:10]] 


    def follow(self, followerId:int, followeeId:int) -> None:
        # record that followerId is following followeeID
        if followeeId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)
    
    def unfollow(self, followerId:int, followeeId:int) -> None:
        # remove followeeId from followerId's following list
        if followerId in self.following:
            self.following[followerId].discard(followerId)



obj = Twitter()
obj.postTweet(1, 101)
obj.postTweet(1, 102)
obj.follow(1,2)
obj.postTweet(2, 201)
obj.unfollow(1,2)
obj.postTweet(2, 202)
print(obj.getNewsFeed(1))

