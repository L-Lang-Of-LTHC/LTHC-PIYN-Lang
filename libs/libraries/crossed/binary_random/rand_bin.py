# -*- coding: utf-8 -*-

# ./libs/libraries/crossed/binary_random/rand_bin.py  =>  contains random crossed binary librairy


ishere = 'yes'
############
# IMPORTS
############
from random import randint as rnd
import libs.libraries.binary.binary_sm as bsm

###########
# METHOD
###########

def getrandbin(size):
    temp = ''
    for i in range(size):
        temp += str(rnd(0,1))
    return temp

def readline(line, mode):
    if mode == 0:
        if ':r' in line:
            ls = line.split(':r')
            isexist = False
            for vb in bsm.varb8list:
                if ls[0] == vb.getName():
                    isexist = True
                    rb = getrandbin(8)
                    vb.setValue(rb)
                    break
            if not isexist:
                print('\nLibrary Error: Binary: \n >> ' + ls[0] + ' << don\'t exist\n')
    if mode == 1:
        if ':r' in line:
            ls = line.split(':r')
            isexist = False
            for vb in bsm.varb16list:
                if ls[0] == vb.getName():
                    isexist = True
                    rb = getrandbin(16)
                    vb.setValue(rb)
                    break
            if not isexist:
                print('\nLibrary Error: Binary: \n >> ' + ls[0] + ' << don\'t exist\n')
    if mode == 2:
        if ':r' in line:
            ls = line.split(':r')
            isexist = False
            for vb in bsm.varb32list:
                if ls[0] == vb.getName():
                    isexist = True
                    rb = getrandbin(32)
                    vb.setValue(rb)
                    break
            if not isexist:
                print('\nLibrary Error: Binary: \n >> ' + ls[0] + ' << don\'t exist\n')
