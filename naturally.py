import operator
import xml.etree.ElementTree as ET

from itertools import chain

def islist(object):
    return isinstance(object, list)

def isiter(object):
    return isinstance(object, Iterable)

def fgetattr(obj, key):
    return object.__getattribute__(obj, key)

def fsetattr(obj, key, value):
    return object.__setattr__(obj, key, value)

class XMLObject(object):  

    def __init__(self, elems):
        fsetattr(self, 'elems', list(elems) if isiter(elems) else [elems])

    def __getitem__(self, key):
        elems = fgetattr(self, 'elems')

        try:
            return [e.attrib[key] for e in elems] if len(elems)  > 1 \
              else elems[0].attrib[key]
        except KeyError:
            return None

    def __getattribute__(self, key):
        elems = fgetattr(self, 'elems')
        return XMLObject(chain.from_iterable(e.findall(key) for e in elems))
