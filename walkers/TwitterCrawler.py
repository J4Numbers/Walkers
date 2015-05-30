__author__ = 'Cynical'

import tweepy


class TwitterCrawler:

    api = 0

    def __init__(self, con_key, con_secret, acc_key, acc_secret):
        auth = tweepy.OAuthHandler(con_key, con_secret)
        auth.set_access_token(acc_key, acc_secret)
        self.api = tweepy.API(auth)

    def get_my_timeline(self):
        return self.api.home_timeline()
