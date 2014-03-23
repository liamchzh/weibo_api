# coding: utf-8

import tornado.web
import snspy

APP_KEY = '757112173'
APP_SECRET = '0d096ef25b49ecb931e806d0cc7a558b'
callback = 'https://api.weibo.com/oauth2/default.html'
expires = 1393739173.5


class Base(tornado.web.RequestHandler):
    # c = APIClient(SinaWeiboMixin, APP_KEY, APP_SECRET, callback, expires)
    # url = c.get_authorize_url()
    # r = c.request_access_token('2e010af7bdb63642151a24227e40207d')
    # access_token = r.access_token

    access_token = '2.00bjSVJC0f9lOpf3f7c8c2260KATlY'
    client = snspy.APIClient(snspy.SinaWeiboMixin,
                   app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=callback,
                   access_token=access_token, expires=expires)

class PublictimelineHandler(Base):
    def get(self):
        return self.client.statuses.public_timeline.get()
