__author__ = 'kukoban'

from pysimplesoap.server import SoapDispatcher, SOAPHandler
from pysimplesoap.client import SoapClient
from BaseHTTPServer import HTTPServer
import utils.programmers_couch_access as programmers
from utils.model import Programmer


def get_client():
    return SoapClient(
        location="http://localhost:8008/",
        action='http://localhost:8008/',  # SOAPAction
        namespace="programmers",
        trace=False,
        ns=False
    )

_dispatcher = SoapDispatcher(
    'couch_db',
    location="http://localhost:8008/",
    action='http://localhost:8008/',  # SOAPAction
    namespace="programmers",
    prefix="ns0",
    trace=False,
    ns=True
)


def soapfunc(returns, args):

    def decorator(func):
        _dispatcher.register_function(
            func.func_name,
            func,
            returns=returns,
            args=args
        )
        return func
    return decorator


@soapfunc(returns={'programmer_id': str}, args=Programmer.soap_wildcard())
def create_programmer(**programmer):
    print programmer
    return programmers.create_programmer(**programmer)


@soapfunc(returns={'deleted': bool}, args={'programmer_id': str})
def delete_programmer(programmer_id):
    return programmers.delete_programmer(programmer_id)


@soapfunc(returns={'programmer': Programmer.soap_wildcard()}, args={'programmer_id': str})
def read_programmer(programmer_id):
    return {'programmer': programmers.read_programmer(programmer_id)}


@soapfunc(returns={'updated': bool}, args={'programmer_id': str, 'updates': list})
def update_programmer(programmer_id, updates):
    print 'in update_programmer_wrapper'
    print programmer_id
    print updates
    return programmers.update_programmer(programmer_id, **updates)


def start_soap_service():
    httpd = HTTPServer(("", 8008), SOAPHandler)
    httpd.dispatcher = _dispatcher
    httpd.serve_forever()

