#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Variable:
    def __init__ (self, init = None):
        self.valor          = None
        self.tipus          = None
        self.vegades_punter = None

class Paraula (Variable):
    def __init__ (self, init = None):
        Variable.__init__ (self, init)
        self.localització_relativa  = None
        self.localitzat             = None

class Descriptor_Funció:
    def __init__ (self):
        # Arguments
        self.variables_arguments = dict ()
        self.continuació_arguments = None

        # Variables locals
        self.variables_locals = dict ()

        # Codi
        self.codi = None
