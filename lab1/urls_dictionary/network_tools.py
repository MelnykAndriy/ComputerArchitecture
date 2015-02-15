__author__ = 'mandriy'

from urllib import urlopen
from xml.etree.ElementTree import parse


def std_url_to_tree(url):
    with urlopen(url) as url_connection:
        return parse(url_connection).getroot()


def gevent_url_to_tree(url):
    pass


__net_lib__ = 'std'

# __libs_func__ = {'std': {'url_to_tree':  std_url_to_tree},
#                  'gevent': {'url_to_tree': gevent_url_to_tree}}
#
# def get_net_func(func_name):
#     return __libs_func__[__net_lib__][func_name]

# def set_net_lib(libname):
#     if libname in __libs_func__.keys():
#         global __net_lib__
#         __net_lib__ = libname


url_to_tree = std_url_to_tree


def set_net_lib(libname):
    global url_to_tree
    if libname == 'std':
        url_to_tree = std_url_to_tree
    elif libname == 'gevent':
        url_to_tree = gevent_url_to_tree
    else:
        raise Exception('Unresolved library.')
