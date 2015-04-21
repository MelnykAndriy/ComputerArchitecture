__author__ = 'mandriy'


import unittest
import soap_couchDB_iface.service
import soap_couchDB_iface.client as soap_client
import multiprocessing
import time


class SoapIntegrationTest(unittest.TestCase):  # Alive database is required

    def setUp(self):
        self._service_process = multiprocessing.Process(
            target=lambda: soap_couchDB_iface.service.ProgrammersAccessSoapServer.start()
        )
        self._service_process.start()
        self._programmer_dict_1 = dict(name='TestName1', surname='TestSurname1', languages=['Python', 'Lisp'], age=20,
                                       experience=2, skill='middle', english_level='intermediate')
        self._programmer_dict_2 = dict(name='TestName2', surname='TestSurname2', languages=['Java', 'C#'],
                                       age=20, experience=0, skill='junior', english_level='beginner')
        time.sleep(1)

    def tearDown(self):
        self._service_process.terminate()

    def test_1create(self):
        client = soap_client.get_localhost_client()
        p_factory = soap_client.ProgrammerFactory(client.factory)
        self._programmer_dict_1['languages'] = p_factory.create_languages(self._programmer_dict_1['languages'])
        self._programmer_dict_2['languages'] = p_factory.create_languages(self._programmer_dict_2['languages'])
        programmer1 = p_factory.create_programmer(**self._programmer_dict_1)
        programmer2 = p_factory.create_programmer(**self._programmer_dict_2)
        self.assertEqual('test_id_1', client.service.create_programmer_with_id('test_id_1', programmer1))
        self.assertEqual('test_id_2', client.service.create_programmer_with_id('test_id_2', programmer2))

    def test_2read(self):
        client = soap_client.get_localhost_client()
        self.assertEqual(self._programmer_dict_1,
                         soap_client.programmer_as_dict(client.service.read_programmer('test_id_1')))
        self.assertEqual(self._programmer_dict_2,
                         soap_client.programmer_as_dict(client.service.read_programmer('test_id_2')))

    def test_3update(self):
        client = soap_client.get_localhost_client()
        p_factory = soap_client.ProgrammerFactory(client.factory)
        programmer1_update = p_factory.create_programmer(
            skill='senior', age=21, english_level='advanced',
            languages=p_factory.create_languages(['Python' 'Lisp' 'Scala' 'Haskell'])
        )
        programmer2_update = p_factory.create_programmer(
            age=30, skill='middle', english_level='pre-intermediate'
        )
        self.assertTrue(client.service.update_programmer('test_id_1', programmer1_update))
        self.assertTrue(client.service.update_programmer('test_id_2', programmer2_update))

    def test_4read_all(self):
        client = soap_client.get_localhost_client()
        all_programmers = client.service.all_programmers()[0]
        self._programmer_dict_1['skill'] = 'senior'
        self._programmer_dict_1['english_level'] = 'advanced'
        self._programmer_dict_1['age'] = 21
        self._programmer_dict_1['languages'] = ['Python' 'Lisp' 'Scala' 'Haskell']
        self._programmer_dict_2['age'] = 30
        self._programmer_dict_2['skill'] = 'middle'
        self._programmer_dict_2['english_level'] = 'pre-intermediate'
        all_programmers_dict = [soap_client.programmer_as_dict(programmer) for programmer in all_programmers]
        self.assertIn(self._programmer_dict_1, all_programmers_dict)
        self.assertIn(self._programmer_dict_2, all_programmers_dict)

    def test_5delete(self):
        client = soap_client.get_localhost_client()
        delete_programmer1_res = client.service.delete_programmer('test_id_1')
        read_programmer1_res = client.service.read_programmer('test_id_1')
        self.assertTrue(delete_programmer1_res and read_programmer1_res is None)
        delete_programmer2_res = client.service.delete_programmer('test_id_2')
        read_programmer2_res = client.service.read_programmer('test_id_2')
        self.assertTrue(delete_programmer2_res and read_programmer2_res is None)
