#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import sys

name = sys.argv[1:]

# Per buscar el primer element.
string_regex = '(?P<línia>//)|(?P<conjunt>/\*)'

if not name: name = 'test.c'
else: name = name[0]

tf = open (name, 'r')
ft = tf.read()
tf.close()

def eliminar_substring (inici, final, text):
    return text[:inici] + text[final:]

def _eliminar_comentari (començar_regex, text):
    buscar = re.search (començar_regex, text)

    if not buscar:
        return (False, 0, text)

    if buscar.group('línia'):
        inici = buscar.start()
        final = text[inici:].find('\n') # No sumo perquè no volem \n.
        return (True, inici, eliminar_substring (inici, inici + final, text))

    elif buscar.group('conjunt'):
        inici = buscar.start()
        final = text[inici:].find('*/') +2 # Sumo perquè volem */.
        return (True, inici, eliminar_substring (inici, inici + final, text))

    else:
        print ("No sé com he arribat aquí")
        return (False, 0, text)

def eliminar_comentaris (regex, text):
    bolea = True
    index = 0
    while bolea:
        (bolea, index, text) = _eliminar_comentari(regex, text)
    return text

m = eliminar_comentaris (string_regex, ft)
print (m)
