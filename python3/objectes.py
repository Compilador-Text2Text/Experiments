#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Variable:
    def __init__ (self):
        self.valor          = None
        self.tipus          = None
        self.vegades_punter = None

class Paraula (Variable):
    def __init__ (self):
        Variable.__init__ (self)
        self.localització_relativa  = None
        self.localitzat             = None
