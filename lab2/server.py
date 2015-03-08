__author__ = 'mandriy'


from bottle import route, run, template


@route('/info')
def get_processing_info():
    return template('info')


@route('/get-task')
def get_task():
    return template('task')


def run_server():
    run(host='localhost', port=8080)