from typing import List


class Post:

    def __init__(self, post_id: int, tweet_id: int):
        self.post_id = post_id
        self.tweet_id = tweet_id


class User:

    def __init__(self):
        self.follows = []
        self.posts = []

    def add_post(self, post: Post):
        self.posts.append(post)

    def follow(self, user_id: int):
        self.follows.append(user_id)

    def unfollow(self, user_id: int):
        self.follows.remove(user_id)


class Twitter:

    def __init__(self):
        self.users = {}
        self.last_post_id = 0

    def post_tweet(self, user_id: int, tweet_id: int):
        if not (user_id in self.users.keys()):
            self.users[user_id] = User()

        user = self.users[user_id]
        user.add_post(Post(self.last_post_id, tweet_id))
        self.last_post_id += 1

    def get_news_feed(self, user_id: int) -> List[int]:
        posts: List[Post] = []
        user = self.users[user_id]
        for i in user.follows:
            follow_user = self.users[i]
            follow_posts = follow_user.posts
            posts.extend(follow_posts)

        sorted_posts = []
        for i in range(0, self.last_post_id):
            for post in posts:
                if post.post_id == i:
                    sorted_posts.append(post.tweet_id)
                    break

        return (sorted_posts[::-1])[:10]

    def follow(self, follower_id: int, followee_id: int):
        if not(follower_id in self.users.keys()):
            self.users[follower_id] = User()

        user = self.users[follower_id]
        user.follow(followee_id)

    def unfollow(self, follower_id: int, followee_id: int):
        if not (follower_id in self.users.keys()):
            self.users[follower_id] = User()

        user = self.users[follower_id]
        user.unfollow(followee_id)


code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)