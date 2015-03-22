__author__ = 'mandriy'
# -*- coding: utf-8 -*-

from bottle import post, route, run, template, static_file, request
from tasks_managment.task_manager import TextTaskSystem

tasks_manager = TextTaskSystem()


@route('/info')
def get_processing_info():
    return template('info')


@route('/participate')
def get_task():
    return template('task')


@route('/get-task')
def task_getting():
    json = '{ "task_id" : %d, "text" : "%s" }' % tasks_manager.get_task()
    return json


@post('/result')
def save_result():
    result_json = request.body.read()
    task_id = 0  # TODO
    result = []  # TODO
    tasks_manager.submit_task(task_id, result)


@route('/task-rollback')
def task_rollback():
    task_id = 0  # TODO
    tasks_manager.rollback_task(task_id)


@route(r'/js/<filename:re:[a-zA-Z0-9]+\.js>')
def js_getting(filename):
    return static_file(filename, root='js/')


iter = 0
snapshots = [
{"active": 0,
"available": 10,
"done": 0},
{"active": 3,
"available": 7,
"done": 0},
{"active": 3,
"available": 6,
"done": 1},
{"active": 3,
"available": 2,
"done": 5},
{"active": 2,
"available": 0,
"done": 8},
{"active": 0,
"available": 0,
"done": 10}]

@route('/system-snapshot')
def get_system_snapshot():
    global iter
    snapshot = snapshots[iter]
    iter += 1
    return '{ "active" : %(active)d,' \
           '  "available" : %(available)d,' \
           '  "done" : %(done)d  }' % snapshot

def run_server():
    run()