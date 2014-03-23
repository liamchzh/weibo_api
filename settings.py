# coding: utf-8

import os
import controllers 

settings = {"template_path" : os.path.join(os.path.dirname(__file__), "templates")}

urls = [(r'/public_timeline', controllers.PublictimelineHandler),
        ]

