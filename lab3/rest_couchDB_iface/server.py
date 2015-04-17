__author__ = 'mandriy'

from bottle import run, route, delete, put, post, request
import json
import utils.programmers_couch_access as programmers


@route('/programmer')
def get_programmers():
    return {'programmers': programmers.get_all_programmers()}


@route('/programmer/<programmer_id>/')
def get_programmer_by_id(programmer_id):
    return {'programmer': programmers.read_programmer(programmer_id)}


@put('/programmer')
def create_programmer():
    programmer = json.load(request.body())
    try:
        programmers.create_programmer(**programmer)
    except TypeError:
        return {'created': True}
    return {'created': False}


@post('/programmer/<programmer_id>/')
def update_programmer(programmer_id):
    programmer_update = json.load(request.body())
    return {'updated': programmers.update_programmer(programmer_id, **programmer_update)}


@delete('/programmer/<programmer_id>/')
def delete_programmer_by_id(programmer_id):
    return {'deleted': programmers.delete_programmer(programmer_id)}


def run_rest_server():
    run(server='paste')