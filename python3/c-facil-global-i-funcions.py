#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import sys

name = sys.argv[1:]

if not name: name = 'test.c'
else: name = name[0]

tf = open (name, 'r')
ft = tf.read()
tf.close()

tipus       = '(?P<tipus>int|char|void)'
punter      = '(\s+|\s*(?P<punter>\*+)\s*)'
nom         = '(?P<nom>\w+)'
descriptor  = '((?P<global>[,;=])|(?P<funció>\())'

global_funcio = tipus + punter + nom + '\s*' + descriptor

m = re.search (global_funcio, ft)
print (m)
print (m.groupdict())

def global_funcio (regex, text):
    pass
