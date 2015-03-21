__author__ = 'mandriy'
# -*- coding: utf-8 -*-

from bottle import post, route, run, template, static_file, request


@route('/info')
def get_processing_info():
    return template('info')


@route('/get-task')
def get_task():
    return template('task')

iter = 0
test = [u'Шевченко Т. Г. Шевченко Тарас ГригоровичШевченко Тарас Григорович', u'bpajfslah Франко И. Я. asfalsf',
        u'Путін В. В.']

@route('/get-text')
def text_getting():
    print "in get-text"
    global iter
    res = test[iter]
    iter += 1
    return res


@post('/result')
def save_result():
    print request.body.read()
    print "in save-result"


@route(r'/js/<filename:re:[a-zA-Z0-9]+\.js>')
def js_getting(filename):
    return static_file(filename, root='js/')


def run_server():
    run()