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
from walkers.SteamCrawler import SteamCrawler, WalkerException


class SteamCrawlerTest(unittest.TestCase):

    def setUp(self):
        self.sc = SteamCrawler(configs.__steam_api_key__)
        self.sc_no_api = SteamCrawler()

    def testPermissionsOnNoKey(self):
        try:
            self.sc_no_api.accessSteam(
                'ISteamUser', 'GetPlayerSummaries', 2,
                {'steamids': configs.__steam_test_profile__}
            )
        except PermissionError:
            self.assertEqual(1, 1, 'A permission error was thrown! Hurray!')
        except:
            self.fail('Something else was thrown that shouldn\'t have been')
        else:
            self.fail('The thing didn\'t fail... Which, by the way, it should have')

    def testGetMethods(self):
        self.assertEqual(50, len(self.sc.getAvailableMethods()), "Not enough interfaces were returned")

    def testGetMainLeaderboard(self):
        self.assertEqual(
            247080, int(self.sc.getMainLeaderboard(247080)['response']['appID']),
            "The wrong store application's leaderboard was recovered"
        )

    def testGetTopTenLeaderboard(self):
        json = self.sc.getMainLeaderboard(242680)
        second = self.sc.getIndivLeaderboard(
            242680,
            json['response']['leaderboard'][int(json['response']['leaderboardCount'])-1]['lbid'],
            {'start': 1, 'end': 10}
        )
        self.assertEqual(10, len(second['response']['entries']['entry']), 'Inequality in test results')

    def testGetProfile(self):
        res = self.sc.accessSteam('ISteamUser', 'GetPlayerSummaries', 2, {'steamids': configs.__steam_test_profile__})
        self.assertEqual(
            configs.__steam_test_profile__, res['response']['players'][0]['steamid'],
            "Slight issue in the fact that we don't have the right person"
        )

    def testFailInterfaceGetProfile(self):
        try:
            self.sc.accessSteam('gibberish', 'moregibberish', 0, {})
        except PermissionError:
            self.assertEqual(1, 1, "The exception was triggered correctly")
        except:
            self.fail("The wrong exception was thrown")
        else:
            self.fail("This failing test did not actually fail")

    def testFailParamsGetProfile(self):
        try:
            self.sc.accessSteam('ISteamUser', 'GetPlayerSummaries', 2, {})
        except WalkerException:
            self.assertEqual(1, 1, "We failed correctly")
        except:
            self.fail("The wrong exception was thrown")
        else:
            self.fail("Hrm... This test should fail")


if __name__ == '__main__':
    unittest.main()
