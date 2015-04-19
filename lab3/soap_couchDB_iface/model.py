__author__ = 'mandriy'


from spyne.model.complex import ComplexModel, Array
from spyne.model.primitive import String
from spyne.model.primitive import UnsignedInt


class Programmer(ComplexModel):
    __namespace__ = 'programmers'

    name = String
    surname = String
    age = UnsignedInt
    languages = Array(String)
    experience = UnsignedInt
    skill = String(values=['junior', 'middle', 'senior'])
