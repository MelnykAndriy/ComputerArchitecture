__author__ = 'mandriy'


from bottle import route, run, template, static_file


@route('/info')
def get_processing_info():
    return template('info')


@route('/get-task')
def get_task():
    return template('task')


@route(r'/js/<filename:re:[a-zA-Z0-9]+\.js>')
def js_getting(filename):
    return static_file(filename, root='js/')


def run_server():
    run()