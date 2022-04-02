class User:
    def __init__(self, user_id, username):
        print("new user is being created...")
        self.id = user_id
        self.username = username
        self.following = 0
        self.follower = 0



    def follow(self, user):
        user.follower += 1
        self.following += 1

user_1 = User("Ebube", "232")
user_2 = User("Grace", "221")
user_3 = User("Grace", "221")

user_2.follow(user_1)
user_3.follow(user_1)
print(user_1.follower)
print(user_1.following)