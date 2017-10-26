import regex
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
m = regex.search (tipus + punter + nom, ft)

if m:
    print ("\ttipus: " + m.group('tipus'))
    if m.group('punter'): print ("\tpunter: " + str(len(m.group('punter'))))
    else: print ("\tpunter: 0")
    print ("\tnom: " + m.group('nom'))
else:
    print ("\tNo s'ha trobat res")
