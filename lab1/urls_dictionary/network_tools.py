__author__ = 'mandriy'

import urllib2
from gevent import monkey, joinall, spawn
from time import time


def get_url_text(url):
    connection = None
    try:
        connection = urllib2.urlopen(url.encode('cp1251'))
        return unicode(connection.read(), 'utf8')
    except:
        raise Exception("Can't process url %s properly." % url,)
    finally:
        if connection:
            connection.close()


def protected_map(func, sequence, protector):
    return map(lambda elem: protector(func, elem),
               sequence)


def std_map_urls_sources(url_text_processor,
                         urls,
                         error_handler=lambda f, *acts: f(*acts)):
    print "std map"
    start = time()
    res = protected_map(lambda protected_url:
                        url_text_processor(get_url_text(protected_url)),
                        urls,
                        error_handler)
    finish = time()
    print "elapsed time %f" % (finish - start)
    return res


def gevent_map_urls_sources(url_text_processor,
                            urls,
                            error_handler=lambda f, *acts: f(*acts)):
    print "gevent map"
    start = time()
    words_getters = [spawn(lambda spwn_url:
                           error_handler(lambda protected_url:
                                         url_text_processor(
                                             get_url_text(protected_url)),
                                         spwn_url),
                           url) for url in urls]
    joinall(words_getters)
    res = [words_getter.value for words_getter in words_getters]
    finish = time()
    print "elapsed time %f" % (finish - start)
    return res


__net_lib__ = 'std'

map_urls_sources = std_map_urls_sources


def set_net_lib(libname):
    global map_urls_sources
    if libname == 'std':
        map_urls_sources = std_map_urls_sources
    elif libname == 'gevent':
        monkey.patch_all()
        map_urls_sources = gevent_map_urls_sources
    else:
        raise Exception('Unresolved library.')
