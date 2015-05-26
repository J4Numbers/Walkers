__author__ = 'Cynical'

import imgurpython

from uk.co.m4numbers.walkers import configs


class ImgurCrawler:

    __client = 0

    def __init__(self, pin):
        conn = imgurpython.ImgurClient(configs.__imgur_client__, configs.__imgur_secret__)
        auth_url = conn.get_auth_url('pin')

        creds = conn.authorize(pin, 'pin')
        conn.set_user_auth(creds['access_token'], creds['refresh_token'])

        self.__client = conn

    def request_profile(self, name):
        ret = self.__client.get_account(name)
        return ret
