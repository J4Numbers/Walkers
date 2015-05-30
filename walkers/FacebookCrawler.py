__author__ = 'Matthew Ball'

import facebook


class FacebookCrawler:
    def __init__(self, key, secret):
        f = facebook.get_app_access_token(key, secret)
        self.token = f
        self.graph = facebook.GraphAPI(f)

    def get_my_posts(self):
        return self.graph.request("/v2.3/me/feed")

