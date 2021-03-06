# -*- coding: utf8 -*-
# Redesigned by @guneysus

import __builtin__
from forbiddenfruit import curse

lcase_table = tuple(u'abcçdefgğhıijklmnoöprsştuüvyz')
ucase_table = tuple(u'ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ')

def upper(data):
    translate_table = {
            ord(u'i') : u'İ',
            ord(u'ı') : u'I'}
    data = data.translate(translate_table)
    result = ''
    for char in data:
        try:
            char_index = lcase_table.index(char)
            ucase_char = ucase_table[char_index]
        except:
            ucase_char = char
        result += ucase_char
    return result

def lower(data):
    translate_table = {
            ord(u'İ') : u'i',
            ord(u'I') : u'ı'}
    data = data.translate(translate_table)
    result = ''
    for char in data:
        try:
            char_index = ucase_table.index(char)
            lcase_char = lcase_table[char_index]
        except:
            lcase_char = char
        result += lcase_char
    return result

def capitalize(data):
    return data[0].upper() + data[1:].lower()

def title(data):
    return " ".join(map(lambda x: x.capitalize(), data.split()))

curse(__builtin__.unicode, 'upper', upper)
curse(__builtin__.unicode, 'lower', lower)
curse(__builtin__.unicode, 'capitalize', capitalize)
curse(__builtin__.unicode, 'title', title)

class unicode_tr(unicode):
    """For Backward compatibility"""
    def __init__(self, arg):
        super(unicode_tr, self).__init__(*args, **kwargs)

if __name__ == '__main__':
    print u'istanbul'.upper()
    print u'İSTANBUL'.lower()
