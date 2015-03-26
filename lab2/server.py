__author__ = 'mandriy'
# -*- coding: utf-8 -*-

from bottle import post, route, run, template, static_file, request
from tasks_managment.task_manager import TextTaskStack, EmptyTaskStack
import json
import utils
from xml.etree import ElementTree
from xml.dom import minidom


tasks_manager = TextTaskStack()


@route('/')
def index():
    return template('index')


@route('/info')
def get_processing_info():
    return template('info')


@route('/participate')
def get_task():
    return template('task')


@route('/get-task')
def task_getting():
    try:
        task_id, text = tasks_manager.get_task()
        task_json = '{ "task_id" : %d, "text" : "%s" }' % (task_id, utils.normalize_text_for_json(text))
    except EmptyTaskStack:
        if tasks_manager.work_is_done():
            task_json = '{ "task_id": 0, "text": "" }'
        else:
            task_json = '{ "task_id": -1, "text": ""}'
    return task_json

@post('/save-result')
def save_result():
    result_json = json.loads(request.body.read())
    print "submit task with id %d" % (result_json["task_id"],)
    tasks_manager.submit_task(result_json["task_id"], result_json["result"])


@route('/task-rollback/<task_id:int>')
def task_rollback(task_id):
    print "in rollback %d" % (task_id,)
    tasks_manager.rollback_task(task_id)


@route(r'/js/<filename:re:[a-zA-Z0-9]+\.js>')
def js_getting(filename):
    return static_file(filename, root='js/')


@route('/system-snapshot')
def get_system_snapshot():
    snapshot = tasks_manager.system_snapshot()
    return '{ "active" : %(active)d,' \
           '  "available" : %(available)d,' \
           '  "done" : %(done)d  }' % snapshot


@route('/report')
def report_page():
    return template('report')


@route('/report-download')
def produce_result():
    root = ElementTree.Element("persons")
    for results in tasks_manager.done_part():
        if results:
                for person_name in results:
                    person = ElementTree.SubElement(root, "person")
                    person.text = person_name
    return minidom.parseString(ElementTree.tostring(root, 'utf-8')).toprettyxml(indent="    ").encode("utf8")


@route('/accept-receiving/<task_id:int>')
def accept_recv(task_id):
    tasks_manager.accept_task(task_id)


def run_server():
    run()