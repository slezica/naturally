import operator
import xml.etree.ElementTree as ET
import itertools
from collections import Iterable
ichain = itertools.chain.from_iterable

def isiter(object):
    return isinstance(object, Iterable)

def fgetattr(obj, key):
    return object.__getattribute__(obj, key)

def fsetattr(obj, key, value):
    return object.__setattr__(obj, key, value)

def imatches(xmlo, key):
    return ichain(e.findall(key) for e in fgetattr(xmlo, 'elems'))

def xml(f):
    return XMLObject(ET.parse(f).getroot())

def validate(sub, filters):
    attrs = filters.items()
    livesh.now()
    all(getattr(sub, attr, None) == value for attr, value in filters.iteritems())

class XMLObject(object):  

    def __init__(self, elems):
        fsetattr(self, 'elems', list(elems) if isiter(elems) else [elems])

    def __getitem__(self, key):
        elems = fgetattr(self, 'elems')

        if isinstance(key, int):
            return XMLObject(elems[key])

        try:
            return [e.attrib[key] for e in elems] if len(elems) > 1 \
              else elems[0].attrib[key]
        except:
            return None

    def __getattribute__(self, key):
        return XMLObject(imatches(self, key))

    def __call__(self, *required, **filters):
        elems = fgetattr(self, 'elems')

        if not required and not filters:
            return elems if len(elems) > 1 else elems[0]

        return XMLObject(sub for sub in elems \
            if all(sub.get(attr, None) is not None for attr in required)
           and all(sub.attrib.get(k, None) == v  for k, v in filters.iteritems())
        )

    def __repr__(self):
        return repr(fgetattr(self, 'elems'))

if __name__ == '__main__':
    print xml('test.xml').module.object(path='login').post.required
