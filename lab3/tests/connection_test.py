__author__ = 'mandriy'

import unittest
import mock
import soap_couchDB_iface.service
import soap_couchDB_iface.client as soap_client
import multiprocessing


class SoapConnectionTest(unittest.TestCase):  # Alive database is required

    def setUp(self):
        self._service = multiprocessing.Process(target=soap_couchDB_iface.service.start_soap_service)
        self._service.start()

    def tearDown(self):
        self._service.terminate()

    def test_create(self):
        pass

    def test_read_all(self):
        client = soap_client.get_localhost_client()
        self.assertIsNotNone(client.service.read_programmer('test_id'))

    def test_update(self):
        pass

    def test_read(self):
        pass

    def test_delete(self):
        pass



