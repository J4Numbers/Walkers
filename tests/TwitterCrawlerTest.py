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
        print(tweets)
        for tweet in tweets:
            print(tweet)


if __name__ == '__main__':
    unittest.main()
