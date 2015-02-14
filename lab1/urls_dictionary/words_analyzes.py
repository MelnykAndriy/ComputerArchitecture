__author__ = 'Андрій'


def get_base_form(word):
    return word


def make_occurrence_dictionary(words):
    ret_dic = dict()
    for word in map(get_base_form, words):
        if ret_dic.get(word):
            ret_dic[word] += 1
        else:
            ret_dic[word] = 1
    return ret_dic