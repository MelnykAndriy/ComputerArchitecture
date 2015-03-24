
import bottle
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(__file__))

import server

application = bottle.default_app()