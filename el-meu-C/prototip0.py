#!/usr/bin/env python3

import re
import sys

name = sys.argv[1:]

if not name: name = '00.c'
else: name = name[0]

tf = open (name, 'r')
ft = tf.read()
tf.close()

gran_lectura = '{(?P<variables_globals>[^{}]*)}' + '\s*' + '{(?P<funcions>(.|\n)*)}'

m = re.match (gran_lectura, ft, re.M)


def declaracions_de_variables (text):
    tipus = '(?P<tipus>int|char|void)'
    punter= '(?P<punter>\**)'
    no_nom= '\-+/%\.,;:[\]<=>(){ }~`!@#$^&*|\\"\''
    nom = '(?P<nom>[^0-9' + no_nom + '][^' + no_nom + ']*)'
    valor = '(=\s*(?P<valor>[^' + no_nom + ']*))?'
    tot = tipus + '\s*' + punter + '\s*' + nom + '\s*' + valor
    print (tot)
    for m in re.finditer (tot, text):
        print ('tipus: ', m.group('tipus'), flush=True, end='\t')
        print ('punter: ', m.group('punter'), end='\t')
        print ('nom: ', m.group('nom'), end='\t')
        print ('valor: ', m.group('valor'))

def declaracions_de_funcions (text):
    tipus = '(?P<tipus>int|char|void)'
    punter= '(?P<punter>\**)'
    no_nom= '\-+/%\.,;:[\]<=>(){}~`!@#$^&*|\\"\'' + '\r\n\t\f\v '
    nom = '(?P<nom>[^0-9' + no_nom + '][^' + no_nom + ']*)'
    arguments = '{(?P<arguments>[^{}]*)}'
    variables_locals = '{(?P<variables_locals>[^{}]*)}'
    codi = '{(?P<codi>[^{}]*)}'
    tot = '\s*'.join ([tipus, punter, nom, arguments, variables_locals])
    for m in re.finditer (tot, text):
        print ('nom: ', m.group('nom'), end='\t')
        print ('si')
    return m

# Primer necessito noms funcions
# Segon necessito els operadors amb els noms i com són associatius
#
def string_a_token (trobat):
    declaracions_de_variables (trobat.group('variables_globals'))
    return declaracions_de_funcions (trobat.group('funcions'))

if not m:
    print ("No s'ha trobat res")
else:
    l = string_a_token (m)
    print (l)
