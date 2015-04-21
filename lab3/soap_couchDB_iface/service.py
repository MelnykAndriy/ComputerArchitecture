__author__ = 'mandriy'

from spyne import ServiceBase, rpc, String, Boolean, Iterable, Application
from spyne.protocol.soap import Soap11
from soap_couchDB_iface.model import Programmer
from wsgiref.simple_server import make_server
from spyne.server.wsgi import WsgiApplication
import utils.programmers_couch_access as programmers_db
import logging


class ProgrammersAccessService(ServiceBase):

    @rpc(Programmer, _returns=String)
    def create_programmer(self, programmer):
            if programmer:
                programmer_dict = programmer.as_dict()
                return programmers_db.create_programmer(**programmer_dict)

    @rpc(String, Programmer, _returns=String)
    def create_programmer_with_id(self, programmer_id, programmer):
        if programmer:
            programmer_with_id = {"_id": programmer_id}
            programmer_with_id.update(programmer.as_dict())
            return programmers_db.create_programmer(**programmer_with_id)

    @rpc(String, Programmer, _returns=Boolean)
    def update_programmer(self, update_id, updates):
        if updates:
            updates = {field: new_val for field, new_val in updates.as_dict().items() if new_val}
            return programmers_db.update_programmer(update_id, **updates)

    @rpc(String, _returns=Boolean)
    def delete_programmer(self, programmer_id):
        return programmers_db.delete_programmer(programmer_id)

    @rpc(String, _returns=Programmer)
    def read_programmer(self, programmer_id):
        return programmers_db.read_programmer(programmer_id)

    @rpc(_returns=Iterable(Programmer))
    def all_programmers(self):
        programmers = programmers_db.get_all_programmers()
        return (Programmer(**programmer) for programmer in programmers)


class ProgrammersAccessSoapServer(object):
    _server = None

    @classmethod
    def start(cls, port=4242):
        application = Application(
            [ProgrammersAccessService],
            'programmers',
            in_protocol=Soap11(validator='lxml'),
            out_protocol=Soap11()
        )

        wsgi_application = WsgiApplication(application)

        logging.basicConfig(level=logging.DEBUG)
        logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)

        cls._server = make_server('localhost', port, wsgi_application)
        cls._server.serve_forever()

    @classmethod
    def stop(cls):
        if cls._server:
            cls._server.shutdown()
            cls._server.server_close()