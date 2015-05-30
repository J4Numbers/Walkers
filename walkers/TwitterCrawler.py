__author__ = 'Matthew Ball'

import tweepy


class TwitterCrawler:

    api = 0

    def __init__(self, con_key, con_secret, acc_key, acc_secret):
        auth = tweepy.OAuthHandler(con_key, con_secret)
        auth.set_access_token(acc_key, acc_secret)
        self.api = tweepy.API(auth)

    def get_my_timeline(self):
        return self.api.home_timeline()

    def get_my_tweets(self):
        return self.api.user_timeline()

    def get_my_last_tweet(self):
        return self.api.user_timeline({'count':1})

    def get_me(self):
        return self.api.verify_credentials()
