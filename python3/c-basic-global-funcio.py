#!/usr/bin/env python3

import re
import sys

name = sys.argv[1:]

if not name: name = 'basic.c'
else: name = name[0]

tf = open (name, 'r')
ft = tf.read()
tf.close()

tipus       = '(?P<tipus>int|char|void)'
punter      = '(\s+|\s*(?P<punter>\*+)\s*)'
nom         = '(?P<nom>\w+)'
variables   = '(?P<variables>[^();])*;'
arguments   = '\((?P<arguments>[^()]*)\)'
codi        = '{(?P<codi>[^{}]*)}'

general     = tipus + punter + nom
funcio      = arguments + '\s*' + codi

tot         = general + '\s*(' + variables + '|' + funcio + ')'
m = re.search (tipus + punter + nom, ft)
m = re.match (tot, ft)

if m:
    print ("\ttipus: " + m.group('tipus'))
    if m.group('punter'): print ("\tpunter: " + str(len(m.group('punter'))))
    else: print ("\tpunter: 0")
    print ("\tnom: " + m.group('nom'))
    print (m.group())
else:
    print ("\tNo s'ha trobat res")
