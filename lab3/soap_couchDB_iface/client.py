__author__ = 'mandriy'


from suds.client import Client


def get_localhost_client(port=4242):
    client = Client('http://localhost:%d?wsdl' % port, cache=None)
    return client


def list_from_string_array(string_array, func=str):
    return [func(el) for el in string_array.string]


_programmer_translate_dict = {
    'name': str,
    'surname': str,
    'skill': str,
    'age': int,
    'experience': int,
    'languages': list_from_string_array,
    'english_level': str
}


def programmer_as_dict(programmer):
    programmer_dict = {}
    for field, val in programmer:
        if field in _programmer_translate_dict:
            programmer_dict[field] = _programmer_translate_dict[field](val)
        else:
            programmer_dict[field] = val
    return programmer_dict


class ProgrammerFactory(object):

    def __init__(self, client_factory):
        self._factory = client_factory

    def create_programmer(self, **kwargs):
        programmer = self._factory.create('Programmer')
        for field in dict(programmer).keys():
            if field in kwargs:
                programmer[field] = kwargs[field]
            else:
                programmer[field] = None
        return programmer

    def create_languages(self, languages):
        languages_string_array = self._factory.create('stringArray')
        for lang in languages:
            languages_string_array.string.append(lang)
        return languages_string_array
