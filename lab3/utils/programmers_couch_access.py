__author__ = 'kukoban'

import couchdb
from threading_utils import make_thread_safe

_couch = couchdb.Server()

if 'programmers' in _couch:
    _programmers_db = _couch['programmers']
else:
    _programmers_db = _couch.create('programmers')


@make_thread_safe('programmers')
def create_programmer(name, surname, languages, **additional_fields):
    doc = {'name': name, 'surname': surname, 'languages': languages}
    doc.update(additional_fields)
    created_id, _ = _programmers_db.save(doc)
    return created_id


@make_thread_safe('programmers')
def update_programmer(programmer_id, **field_updates):
    if programmer_id in _programmers_db:
        programmer = _programmers_db[programmer_id]
        for field, value in field_updates.items():
            programmer[field] = value
        _programmers_db[programmer.id] = programmer
        return True
    return False


@make_thread_safe('programmers')
def read_programmer(programmer_id):
    if programmer_id in _programmers_db:
        return _programmers_db[programmer_id]


@make_thread_safe('programmers')
def delete_programmer(programmer_id):
    print 'in delete_programmer : %s\n\n' % programmer_id,
    if programmer_id in _programmers_db:
        _programmers_db.delete(_programmers_db[programmer_id])
        return True
    return False


@make_thread_safe('programmers')
def get_all_programmers():
    return [dict(_programmers_db[programmer_id]) for programmer_id in _programmers_db]
