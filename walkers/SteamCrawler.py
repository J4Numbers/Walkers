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
__base__ = "https://steamcommunity.com/stats/{0}/leaderboards/{1}/?xml=1"
__profile__ = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={0}&steamids={1}"

import requests


class SteamCrawler:

    game = 0

    def __init__(self, apiKey):
        self.headers = {"User-Agent": "other:walkers:v0.0.1 (by /u/M477h3w1012)"}
        self.apiKey = apiKey

    def assignGame(self, id):
        self.game = id

    def getMainLeaderboard(self):
        res = requests.get(__base__.format(self.game, ""), headers=self.headers)
        return res.content

    def getIndivLeaderboard(self, ind):
        res = requests.get(__base__.format(self.game, ind), headers=self.headers)
        return res.content

    def getDataOnProfileId(self, profileId):
        res = requests.get(__profile__.format(self.apiKey, profileId), headers=self.headers)
        return res.json()