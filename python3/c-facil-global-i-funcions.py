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

def _comptador_obert_tancat (text, diccionari, on_comptar):
    valor = 1
    index = 0
    regex = '[^' + on_comptar + ']*'

    while valor:
        trobar = re.match (regex, text[index:])
        if not trobar:
            print ('Error, no tanca:', on_comptar, '\n', text)
            return False

        byte = text[index + trobar.end()]
        index += trobar.end() +1
        if byte == on_comptar[0]: valor+=1
        elif byte == on_comptar[1]:valor-=1
    diccionari[on_comptar] = text[:index -1]
    return index

def _global_funció (regex, text, index, variables, funcions):
    trobar = re.match (regex, text[index:])
    # Finalitza?
    if not trobar: return (False, index)

    print (trobar)
    print (trobar.groupdict())
    diccionari = trobar.groupdict ()
    index += trobar.end ()

    if trobar.group ('funció'):
        index += _comptador_obert_tancat (text[index:], diccionari, '()')

        trobar = re.match ('\s*{', text[index:])
        if not trobar:
            print ('ERROR, no hi ha codi després dels arguments!')
            return (False, 0)
        index += trobar.end ()

        index += _comptador_obert_tancat (text[index:], diccionari, '{}')
        funcions[diccionari['nom']] = None
        return (True, index)

    elif trobar.group ('global'):
        pass
    return (False, 0)

def global_funció (regex, text):
    variables_globals = dict ()
    descriptor_funció = dict ()
    bolea = True
    index = 0
    #while bolea and (index < len(text)):
    while bolea:
        (bolea, index) = _global_funció (regex, text, index, variables_globals, descriptor_funció)
    return descriptor_funció

t = global_funció (str_global_funció, ft)
