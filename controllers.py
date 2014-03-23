# coding: utf-8

import tornado.web
import settings
import snspy


class Base(tornado.web.RequestHandler):
    # c = APIClient(SinaWeiboMixin, APP_KEY, APP_SECRET, callback, expires)
    # url = c.get_authorize_url()
    # r = c.request_access_token('2e010af7bdb63642151a24227e40207d')
    # access_token = r.access_token

    access_token = '2.00bjSVJC0f9lOpf3f7c8c2260KATlY'
    client = snspy.APIClient(snspy.SinaWeiboMixin,
                   app_key=settings.APP_KEY, app_secret=settings.APP_SECRET, redirect_uri=settings.callback,
                   access_token=access_token, expires=settings.expires)

class PublictimelineHandler(Base):
    def get(self):
        return self.client.statuses.public_timeline.get()
