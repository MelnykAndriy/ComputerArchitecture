__author__ = 'mandriy'


class SoapCompatible(object):

    @classmethod
    def soap_wildcard(cls):
        pass


class Model(SoapCompatible):
    _model_pattern = None

    @classmethod
    def soap_wildcard(cls):
        wildcard = {'_id': str}
        for arg, type_specifier in cls.get_model_pattern().items():
            wildcard[arg] = type_specifier.soap_wildcard()
        return wildcard

    @classmethod
    def get_model_pattern(cls):
        if cls._model_pattern is None:
            cls._model_pattern = cls.init_model_pattern()
        return cls._model_pattern

    @classmethod
    def init_model_pattern(cls):
        pattern = {'_id': Str}
        for name, type_specifier in cls.__dict__.items():
            if not name.startswith('__'):
                pattern[name] = type_specifier
        return pattern

    def __new__(cls, **fields):
        rep = {}
        for name, type_specifier in cls.get_model_pattern().items():
            if name in fields and fields[name] is not None:
                if not issubclass(type_specifier, Model):
                    rep[name] = type_specifier(fields[name])
                else:
                    rep[name] = type_specifier(**fields[name])
            else:
                rep[name] = None
        return rep


class TypedList(object):

    @staticmethod
    def of(list_type):

        class TypedListOf(SoapCompatible):
            _list_type = list_type

            def __new__(cls, seq):
                return [cls._list_type(item) for item in seq]

            @classmethod
            def soap_wildcard(cls):
                return [cls._list_type.soap_wildcard()]

        return TypedListOf


class Int(SoapCompatible):

    @classmethod
    def soap_wildcard(cls):
        return int

    def __new__(cls, *args):
        return int(*args)


class Str(SoapCompatible):

    @classmethod
    def soap_wildcard(cls):
        return str

    def __new__(cls, *args):
        return str(*args)


class Programmer(Model):

    name = Str
    surname = Str
    age = Int
    languages = TypedList.of(Str)
    experience = Int
    skill_level = Int


