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

__author__ = 'Matthew Ball'

import unittest

from tests import configs
from walkers.RedditCrawler import RedditCrawler


class RedditCrawlerTest(unittest.TestCase):

    def setUp(self):
        self.rc = RedditCrawler(
            configs.__reddit_username__, configs.__reddit_password__,
            configs.__reddit_client__, configs.__reddit_secret__
        )

    def test_user(self):
        user = self.rc.request_profile()
        self.assertEqual(
            user['name'], configs.__reddit_username__,
            "The names were not equal - incorrect login"
        )

    def test_subreddits(self):
        sbrds = self.rc.request_my_subreddits()
        self.assertEqual(24, len(sbrds['data']['children']), "The number of subreddits is incorrect")

    def test_single_subreddit(self):
        sbrd = self.rc.request_subreddit_info("hatfilms")
        self.assertEqual('2uvqu', sbrd['data']['id'], "The ids don't match")


if __name__ == '__main__':
    unittest.main()
