__author__ = 'mandriy'

import unittest
import mock
import soap_couchDB_iface.client as soap_client
import time
import threading


class SoapConnectionTest(unittest.TestCase):

    @mock.patch('couchdb.Server')
    def test_create(self, _):
        programmer_to_create = dict(name='TestName1', surname='TestSurname1', languages=['Python', 'Lisp'], age=20,
                                    experience=2, skill='middle', english_level='intermediate')

        def create_test(client):
            p_factory = soap_client.ProgrammerFactory(client.factory)
            programmer_dict = programmer_to_create.copy()
            programmer_dict['languages'] = p_factory.create_languages(programmer_dict['languages'])
            programmer = p_factory.create_programmer(**programmer_dict)
            return client.service.create_programmer(programmer)

        self._connection_test(
            test_method_name='utils.programmers_couch_access.create_programmer',
            expected_res='some_id',
            method_call=create_test,
            method_kw_params=programmer_to_create
        )

    def test_read_all(self):

        self._connection_test(
            test_method_name='utils.programmers_couch_access.get_all_programmers',
            expected_res=[dict(name='TestName1', surname='TestSurname1', languages=['Python', 'Lisp'], age=20,
                               experience=2, skill='middle', english_level='intermediate')],
            method_call=lambda client: map(soap_client.programmer_as_dict, client.service.all_programmers()[0])
        )

    def test_update(self):

        programmer_update = dict(experience=5, english_level='advanced')

        def _update_test(client):
            p_factory = soap_client.ProgrammerFactory(client.factory)
            programmer = p_factory.create_programmer(**programmer_update)
            return client.service.update_programmer('id_to_update', programmer)

        self._connection_test(
            test_method_name='utils.programmers_couch_access.update_programmer',
            expected_res=True,
            method_call=_update_test,
            method_pos_params=('id_to_update', ),
            method_kw_params=programmer_update
        )

    def test_read(self):
        programmer_in_db = {'name': 'Andriy', 'surname': 'Melnyk', 'age': 20, 'languages': ['Lisp', 'Python'],
                            'experience': 2, 'skill': 'senior', 'english_level': 'middle'}

        self._connection_test(
            test_method_name='utils.programmers_couch_access.read_programmer',
            expected_res=programmer_in_db,
            method_call=lambda client: soap_client.programmer_as_dict(client.service.read_programmer('id_to_read')),
            method_pos_params=('id_to_read', )
        )

    def test_delete(self):
        self._connection_test(
            test_method_name='utils.programmers_couch_access.delete_programmer',
            expected_res=True,
            method_call=lambda client: client.service.delete_programmer('id_to_delete'),
            method_pos_params=('id_to_delete', )
        )

    def _connection_test(self, test_method_name, expected_res, method_call, method_pos_params=(), method_kw_params={}):
        from soap_couchDB_iface.service import ProgrammersAccessSoapServer

        with mock.patch(test_method_name, return_value=expected_res) as method_mock:
            stop = threading.Event()
            method_result = {}

            def _stop_server():
                stop.wait()
                ProgrammersAccessSoapServer.stop()

            def _test_client():
                time.sleep(1)
                try:
                    client = soap_client.get_localhost_client()
                    method_result['result'] = method_call(client)
                finally:
                    stop.set()

            client_tester = threading.Thread(target=_test_client)
            server_stopper = threading.Thread(target=_stop_server)
            server_stopper.start()
            client_tester.start()
            ProgrammersAccessSoapServer.start()
            self.assertEqual(expected_res, method_result['result'])
            method_mock.assert_called_once_with(*method_pos_params, **method_kw_params)
