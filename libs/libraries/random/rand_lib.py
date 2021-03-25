# -*- coding: utf-8 -*-

# ./libs/libraries/random/rand_lib.py  =>  contains random library method definitions

############
# IMPORTS
############
from random import randint as rnd
from libs.var_lib import ALLOWED_CHARS as alch

############
# METHODS
############

def rnd_num(minima, maxima):
    return float(rnd(minima, maxima))

def rnd_str(size):
    out = ''
    for i in range(size):
        out += alch[rnd(0, len(alch))]
    return out
