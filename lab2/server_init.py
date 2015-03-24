__author__ = 'mandriy'
# -*- coding: utf-8 -*-

import server
import os
from os.path import isdir, exists, join


def get_files(path):
    def travers_files(path, func):
        if isdir(path):
            return reduce(lambda files, file_or_dir:
                          files + travers_files(join(path, file_or_dir), func),
                          os.listdir(path),
                          [])
        else:
            return [func(path)]

    def read_file(file):
        with open(file, "r") as f:
            return f.read()

    if exists(path):
        return travers_files(path, read_file)
    else:
        return []


def init():
    if os.getenv('LAB2_TASKS'):
        server.tasks_manager.load_tasks(get_files(os.getenv('LAB2_TASKS')))
        print server.tasks_manager.system_snapshot()
        # server.tasks_manager.load_tasks([u'asfasf Шевченко Т. Г.', u'Шевченко А. Н. asfafa', u'Путин В. В.'   ])