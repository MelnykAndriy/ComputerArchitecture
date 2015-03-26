
import bottle
import utils

utils.set_server_root(__file__)

import server

application = bottle.default_app()