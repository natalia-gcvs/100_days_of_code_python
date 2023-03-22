from internet_speed_tweet_bot import InternetSpeedTweetBot

PROMISED_DOWN = 150
PROMISED_UP = 10

TWITTER_EMAIL = ""
TWITTER_PASSWORD = ""
TWITTER_USERNAME = ""

bot = InternetSpeedTweetBot()

bot.tweet_at_provider(email=TWITTER_EMAIL, username=TWITTER_USERNAME,
                      password=TWITTER_PASSWORD, promised_down=PROMISED_DOWN, promised_up=PROMISED_UP)






