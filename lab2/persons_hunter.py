__author__ = 'mandriy'
# -*- coding: utf-8 -*-

import os
import utils
import server

if os.getenv('LAB2_TASKS'):
    server.init_server(utils.get_files(os.getenv('LAB2_TASKS')))
    # server.init_server([u'asfasf\n Шевченко Т. Г.', u'Шевченко А. Н.\n asfafa', u'Путин В. В.'])
    server.run_server()

