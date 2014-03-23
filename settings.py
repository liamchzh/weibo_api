# coding: utf-8

import os
import controllers 

settings = {"template_path" : os.path.join(os.path.dirname(__file__), "templates")}

urls = [(r'/public_timeline', controllers.PublictimelineHandler),
        ]


APP_KEY = '757112173'
APP_SECRET = '0d096ef25b49ecb931e806d0cc7a558b'
callback = 'https://api.weibo.com/oauth2/default.html'
expires = 1393739173.5
