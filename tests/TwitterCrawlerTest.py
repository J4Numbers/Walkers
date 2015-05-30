"""
    Copyright 2015 Matthew D. Ball (M4Numbers)

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

from __future__ import print_function
from __future__ import unicode_literals

__author__ = 'Matthew Ball'

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
