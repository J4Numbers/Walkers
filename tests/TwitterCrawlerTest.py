from __future__ import print_function
from __future__ import unicode_literals

__author__ = 'Cynical'

import unittest

from tests import configs
from walkers import TwitterCrawler


class TwitterCrawlerTest(unittest.TestCase):

    def setUp(self):
        self.api = TwitterCrawler(
            configs.__twitter_con_key__, configs.__twitter_con_secret__,
            configs.__twitter_acc_token__, configs.__twitter_acc_secret__
        )

    def test_get_timeline(self):
        tweets = self.api.get_my_timeline()
        self.assertEqual(20, len(tweets), "Not enough tweets were returned")

    def test_get_my_tweets(self):
        tweets = self.api.get_my_tweets()
        self.assertEqual(20, len(tweets), "Not enough tweets were returned")

    def test_get_my_last_tweet(self):
        tweet = self.api.get_my_last_tweet()
        self.assertEqual('M4Numbers', tweet[0].user.screen_name, 'Tweet returned was incorrect')

    def test_get_me(self):
        me = self.api.get_me()
        self.assertEqual('144468804', me.id_str, "The wrong person was returned")


if __name__ == '__main__':
    unittest.main()
