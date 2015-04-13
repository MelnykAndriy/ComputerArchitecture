__author__ = 'kukoban'

from pysimplesoap.server import SoapDispatcher, SOAPHandler
from BaseHTTPServer import HTTPServer


_dispatcher = SoapDispatcher(
    'example',
    location="http://localhost:8008/",
    action='http://localhost:8008/',  # SOAPAction
    namespace="math",
    prefix="ns0",
    trace=False,
    ns=True
)


def soapfunc(ret_result, args):
    def decorator(func):
        _dispatcher.register_function(
            func.func_name,
            func,
            returns=ret_result,
            args=args
        )
        return func
    return decorator


def run_service():
    httpd = HTTPServer(("", 8008), SOAPHandler)
    httpd.dispatcher = _dispatcher
    httpd.serve_forever()

