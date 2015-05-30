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
