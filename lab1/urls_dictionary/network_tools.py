__author__ = 'mandriy'

from urllib2 import urlopen


def get_url_text(url):
    connection = None
    try:
        connection = urlopen(url)
        return connection.read()
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
    return protected_map(lambda protected_url:
                         url_text_processor(get_url_text(protected_url)),
                         urls,
                         error_handler)


def gevent_map_urls_sources(url_text_processor, urls):
    pass


__net_lib__ = 'std'

map_urls_sources = std_map_urls_sources

def set_net_lib(libname):
    global url_to_tree
    if libname == 'std':
        url_to_tree = std_map_urls_sources
    elif libname == 'gevent':
        url_to_tree = gevent_map_urls_sources
    else:
        raise Exception('Unresolved library.')


