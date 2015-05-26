__author__ = 'Cynical'

import unittest

from uk.co.m4numbers.walkers import configs
from uk.co.m4numbers.walkers.reddit.RedditCrawler import RedditCrawler


class RedditCrawlerTest(unittest.TestCase):

    def setUp(self):
        self.rc = RedditCrawler(configs.__username__, configs.__password__)

    def test_user(self):
        user = self.rc.request_profile()
        self.assertEqual(user['name'], configs.__username__, "The names were not equal - incorrect login")

    def test_subreddits(self):
        sbrds = self.rc.request_my_subreddits()
        self.assertEqual(24, len(sbrds['data']['children']), "The number of subreddits is incorrect")

    def test_single_subreddit(self):
        sbrd = self.rc.request_subreddit_info("hatfilms")
        self.assertEqual('2uvqu', sbrd['data']['id'], "The ids don't match")


if __name__ == '__main__':
    unittest.main()
