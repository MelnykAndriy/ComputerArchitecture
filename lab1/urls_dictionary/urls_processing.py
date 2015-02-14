__author__ = 'Andriy'


def process_urls(urls_to_process):
    result_dict = dict()
    for url in urls_to_process:
        process_url(url)

    return result_dict


def process_url(url):
    pass