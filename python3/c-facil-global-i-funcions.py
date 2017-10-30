#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from objectes import *

import re
import sys

name = sys.argv[1:]

if not name: name = 'test.c'
else: name = name[0]

tf = open (name, 'r')
ft = tf.read()
tf.close()

#variables_globals = dict ()
#descriptor_funció = dict ()

tipus       = '(?P<tipus>int|char|void)'
punter      = '(\s+|\s*(?P<punter>\*+)\s*)'
nom         = '(?P<nom>\w+)'
descriptor  = '((?P<global>[,;=])|(?P<funció>\())'

str_global_funció = '\s*' + tipus + punter + nom + '\s*' + descriptor


def _global_funció (regex, text, index, variables, funcions):
    text = text[index:]
    r = re.match (regex, text)
    print (r)
    print (r.groupdict())

    # Finalitza?
    if not r:
        return (False, 0)

    if r.group ('funció'):
        pass
    elif r.group ('global'):
        pass
    return (False, 0)

def global_funció (regex, text):
    variables_globals = dict ()
    descriptor_funció = dict ()
    bolea = True
    index = 0
    while bolea:
        (bolea, index) = _global_funció (regex, text, index, variables_globals, descriptor_funció)
    pass

global_funció (str_global_funció, ft)
