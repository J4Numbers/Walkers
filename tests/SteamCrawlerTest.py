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
import xml.etree.ElementTree as ET

from tests import configs
from walkers.SteamCrawler import SteamCrawler


class SteamCrawlerTest(unittest.TestCase):

    def setUp(self):
        self.sc = SteamCrawler(configs.__steam_api_key__)

    def testGetMain(self):
        self.sc.assignGame(247080)
        et = ET.fromstring(self.sc.getMainLeaderboard())
        print(et)

    def testGetProfile(self):
        res = self.sc.getDataOnProfileId(configs.__steam_test_profile__)
        self.assertEqual(
            configs.__steam_test_profile__, res['response']['players'][0]['steamid'],
            "Slight issue in the fact that we don't have the right person"
        )


if __name__ == '__main__':
    unittest.main()
