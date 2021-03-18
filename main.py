from instabot import Bot
bot = Bot()
bot.login(username="", password="")

######  upload a picture #######
bot.upload_photo("abc.jpg", caption="Caption Here")

######  follow someone #######
bot.follow("elonrmuskk")

######  send a message #######
bot.send_message("Hello from Instagram", ['user1','user2'])

######  get follower info #######
my_followers = bot.get_user_followers("xyz")

for follower in my_followers:
    print(follower)

#### Unfollow All the Followers ####
bot.unfollow_everyone()
