__author__ = 'Matthew Ball'

import unittest
from tests import configs
from walkers.FacebookCrawler import FacebookCrawler


class FacebookCrawlerTest(unittest.TestCase):
    def setUp(self):
        self.fc = FacebookCrawler(
            configs.__facebook_acc_token__, configs.__facebook_acc_secret__
        )

    def test_get_feed(self):
        print(self.fc.get_my_posts())

if __name__ == '__main__':
    unittest.main()
