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

"""
    These three locations all hold some significance when considering the Steam
    web api. The base is very much the key factor in many of the queries that
    will be performed on Steam's api, allowing for interfaces, methods, and versions
    to be plugged and changed mercilessly.

    The auth location is a link that will always be accessible to us and anyone else
    trying to use this library, and it will return a list of all of our available
    methods whenever it is prodded by us. Finally, the leaderboards location is a
    tad on the legacy side, as Valve have not built in leaderboard functionality into
    their steamworks api quite yet.
"""
__base__ = 'https://api.steampowered.com/{0}/{1}/v{2:04d}/'
__auth__ = __base__.format('ISteamWebAPIUtil', 'GetSupportedAPIList', 1)
__leaderboard__ = 'https://steamcommunity.com/stats/{0}/leaderboards/{1}/'


import requests
import xmltodict

from walkers.WalkerExceptions import WalkerException


class SteamCrawler:
    def __init__(self, apiKey=''):
        self.headers = {"User-Agent": "other:walkers:v0.0.1 (by /u/M477h3w1012)"}
        self.apiKey = apiKey
        self.__buildInterfaces()

    def __buildInterfaces(self):
        params = {}
        if self.apiKey != '':
            params['key'] = self.apiKey
        self.interfaces = {}
        t_map = requests.get(__auth__, headers=self.headers, params=params).json()['apilist']['interfaces']
        for interface in t_map:
            mtemp, temp, t, m = ({},) * 4
            for method in interface['methods']:
                t[method['version']] = method
                temp.update(t)
                m[method['name']] = temp
                mtemp.update(m)
            self.interfaces[interface['name']] = mtemp

    def updateApiKey(self, apiKey):
        self.apiKey = apiKey
        self.__buildInterfaces()

    def checkAccess(self, interface, method, version):
        return \
            interface in self.interfaces and \
            method in self.interfaces[interface] and \
            version in self.interfaces[interface][method]

    def requiresKey(self, interface, method, version):
        for param in self.interfaces[interface][method][version]['parameters']:
            if param['name'] == 'key':
                return True
        return False

    def checkParameterSet(self, interface, method, version, parameters):
        for param in self.interfaces[interface][method][version]['parameters']:
            if not param['optional']:
                if not param['name'] in parameters:
                    raise WalkerException(
                        'Non-Optional Parameter Missing! {0} ({1}): {2}'.format(
                            param['name'], param['type'], param['description']
                        )
                    )
        return True

    def accessSteam(self, interface, method, version, parameters):
        try:
            if self.checkAccess(interface, method, version):
                if self.requiresKey(interface, method, version):
                    parameters['key'] = self.apiKey
                if self.checkParameterSet(interface, method, version, parameters):
                    ret = requests.get(
                        __base__.format(
                            interface, method, version,
                        ), headers=self.headers, params=parameters
                    )
                    if 'format' in parameters:
                        if parameters['format'] == 'json':
                            return ret.json()
                        else:
                            return ret.content
                    return ret.json()
                else:
                    raise Exception("Parameter set was incorrect for some reason")
            else:
                raise PermissionError("The interface and method combo you were trying to access"
                                      " either didn't exist, or wasn't accessible to you"
                                      )
        except:
            raise

    def getAvailableMethods(self):
        return self.interfaces

    def getMainLeaderboard(self, gameId):
        res = requests.get(__leaderboard__.format(gameId, ""), headers=self.headers, params={'xml': 1})
        return xmltodict.parse(res.content)

    def getIndivLeaderboard(self, gameId, ind, params):
        params['xml'] = 1
        res = requests.get(__leaderboard__.format(gameId, ind), headers=self.headers, params=params)
        return xmltodict.parse(res.content)
