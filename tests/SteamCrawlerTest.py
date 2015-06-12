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
from walkers.SteamCrawler import SteamCrawler
from walkers.WalkerExceptions import WalkerException

"""
    Depending on the level of debug you require, alter the number
    below so that it reflects what you wish to be shown in the tests
    as some of them may fail due to timeout if too many tests are
    ran at the same time.

    0 - This is a full debug run of all tests
    1 - This is a run of a few of the tests: mainly the more intensive ones
    2 - This is a run of most of the tests, consisting of many of the less-
        intensive tests in this file
"""
__debug_key__ = 0

class SteamCrawlerTest(unittest.TestCase):

    def setUp(self):
        self.sc = SteamCrawler(configs.__steam_api_key__)
        self.sc_no_api = SteamCrawler()

    """
        This method tests whether or not we are able to get through to the
        web api when we are accessing a valid interface, but one which we
        do not have the permissions to access; I.E. the Player Summaries
        interface, which requires a valid API Key to be used.
    """
    @unittest.skipIf(__debug_key__ == 1, "Testing Permissions with no API key has been skipped for this run.")
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

    """
        This method tests the number of methods we have available to us as a
        valid api key holder. This may change for those people accessing it,
        but at the current time, with a brand new api key, there are 50 interfaces
        to which I can claim access.
    """
    @unittest.skipIf(__debug_key__ == 1, "Testing the number of methods returned has been skipped for this run.")
    def testGetMethods(self):
        self.assertEqual(50, len(self.sc.getAvailableMethods()), "Not enough interfaces were returned")

    @unittest.skipIf(__debug_key__ == 2, "Testing a fetch of the main leaderboard has been skipped for this run")
    def testGetMainLeaderboard(self):
        self.assertEqual(
            247080, int(self.sc.getMainLeaderboard(247080)['response']['appID']),
            "The wrong store application's leaderboard was recovered"
        )

    @unittest.skipIf(__debug_key__ == 2, "Testing a fetch of the top 10 in the last leaderboard has "
                                         "been skipped for this run")
    def testGetTopTenLeaderboard(self):
        json = self.sc.getMainLeaderboard(242680)
        second = self.sc.getIndivLeaderboard(
            242680,
            json['response']['leaderboard'][int(json['response']['leaderboardCount'])-1]['lbid'],
            {'start': 1, 'end': 10}
        )
        self.assertEqual(10, len(second['response']['entries']['entry']), 'Inequality in test results')

    @unittest.skip("Reasons")
    def testGetProfile(self):
        res = self.sc.accessSteam('ISteamUser', 'GetPlayerSummaries', 2, {'steamids': configs.__steam_test_profile__})
        self.assertEqual(
            configs.__steam_test_profile__, res['response']['players'][0]['steamid'],
            "Slight issue in the fact that we don't have the right person"
        )

    @unittest.skipIf(__debug_key__ == 1, "Testing a failing interface fetch has been skipped for this run.")
    def testFailInterfaceGetProfile(self):
        try:
            self.sc.accessSteam('gibberish', 'moregibberish', 0, {})
        except PermissionError:
            self.assertEqual(1, 1, "The exception was triggered correctly")
        except:
            self.fail("The wrong exception was thrown")
        else:
            self.fail("This failing test did not actually fail")

    @unittest.skipIf(__debug_key__ == 1, "Testing a failing profile fetch has been skipped for this run.")
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
