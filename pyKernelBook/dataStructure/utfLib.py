# File: xml-parsers-expat-example-2.py
# -*- coding: utf-8 -*-
'''
# -*- coding: iso-8859-1 -*-
'''
from xml.parsers import expat
import sys
import os
import re
import codecs
import string

def smart_str(s, encoding='utf-8', errors='strict'):
    if not isinstance(s, basestring):
        try:
            return str(s)
        except UnicodeEncodeError:
            return unicode(s).encode(encoding, errors)
    elif isinstance(s, unicode):
        return s.encode(encoding, errors)
    elif s and encoding != 'utf-8':
        return s.decode('utf-8', errors).encode(encoding, errors)
    else:
        return s

if __name__ == '__main__':
    main(sys.argv)




