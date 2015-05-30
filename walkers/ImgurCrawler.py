__author__ = 'Matthew Ball'

import imgurpython


class ImgurCrawler:

    __client = 0

    def __init__(self, client, secret, pin):
        conn = imgurpython.ImgurClient(client, secret)
        auth_url = conn.get_auth_url('pin')

        creds = conn.authorize(pin, 'pin')
        conn.set_user_auth(creds['access_token'], creds['refresh_token'])

        self.__client = conn

    def request_profile(self, name):
        ret = self.__client.get_account(name)
        return ret
