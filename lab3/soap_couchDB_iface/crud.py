__author__ = 'kukoban'

import couchdb
from service import soapfunc

_couch = couchdb.Server()
if 'programmers' in _couch:
    _programmers_db = _couch['programmers']
else:
    _programmers_db = _couch.create('programmers')


@soapfunc({'programmer_id': str}, {'name': str, 'surname': str, 'language': str, 'programmer_id': str,
                                   'additional_fields': dict})
def create_programmer(name, surname, language, programmer_id=None, **additional_fields):
    doc = {'name': name, 'surname': surname, 'language': language}
    doc.update(additional_fields)
    if programmer_id:
        doc['_id'] = programmer_id
    created_id, _ = _programmers_db.save(doc)
    return created_id


@soapfunc({'update_successful': bool}, {'programmer_id': str, 'field_updates': dict})
def update_programmer(programmer_id, **field_updates):
    if programmer_id in _programmers_db:
        programmer = _programmers_db[programmer_id]
        for field, value in field_updates.items():
            programmer[field] = value
        _programmers_db[programmer.id] = programmer
        return True
    return False


@soapfunc({'programmer': dict}, {'programmer_id': str})
def read_programmer(programmer_id):
    if programmer_id in _programmers_db:
        return _programmers_db[programmer_id]


@soapfunc({'deleted': bool}, {'programmer_id': str})
def delete_programmer(programmer_id):
    if programmer_id in _programmers_db:
        _programmers_db.delete(_programmers_db[programmer_id])
        return True
    return False
