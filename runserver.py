# coding: utf-8

import tornado.ioloop
import settings

application = tornado.web.Application(settings.urls, **settings.settings)

if __name__ == "__main__":
    application.listen(7777)
    tornado.ioloop.IOLoop.instance().start()
