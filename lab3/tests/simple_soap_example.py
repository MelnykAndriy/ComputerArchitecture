__author__ = 'kukoban'

import unittest
from multiprocessing.process import Process
from pysimplesoap.client import SoapClient
from pysimplesoap.server import SoapDispatcher, SOAPHandler
from BaseHTTPServer import HTTPServer


class SoapExample(unittest.TestCase):

    def setUp(self):

        def soap_test_server():

            def add(a, b):
                """Add two values"""
                return a+b

            dispatcher = SoapDispatcher(
                'example',
                location="http://localhost:8008/",
                action='http://localhost:8008/',  # SOAPAction
                namespace="http://example.com/sample.wsdl",
                prefix="ns0",
                trace=False,
                ns=True)

            # register the user function
            dispatcher.register_function(
                'add',
                add,
                returns={'AddResult': int},
                args={'a': int, 'b': int}
            )

            httpd = HTTPServer(("", 8008), SOAPHandler)
            httpd.dispatcher = dispatcher
            httpd.serve_forever()

        self._process = Process(target=soap_test_server)
        self._process.start()

    def tearDown(self):
        self._process.terminate()

    def test_soap(self):
        # create a simple consumer
        client = SoapClient(
            location="http://localhost:8008/",
            action='http://localhost:8008/',  # SOAPAction
            namespace="http://example.com/sample.wsdl",
            soap_ns='soap',
            trace=False,
            ns=False
        )

        # call the remote method
        response = client.add(a=2, b=2)

        # extract and convert the returned value
        result = response.AddResult

        self.assertEqual(int(result), 4, 'Basic soap example')