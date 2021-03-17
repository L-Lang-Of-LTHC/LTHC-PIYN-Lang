# -*- coding: utf-8 -*-

# ./libs/sys_methods.py  =>  contains default methods of this programming language system

############
# IMPORTS
############
import libs.var_lib as vl

############
# Usefull
############
varnlist = [vl.NumVar('DefaultNumVar_CreatedByLanguageSystem_00000000')]
varslist = [vl.StrVar('DefaultStrVar_CreatedByLanguageSystem_00000000')]

############
# METHODS
############

def varn(line):
    if '=' in line:
        ls = line.split('=')
        isexist = False
        for vn in varnlist:
            if ls[0] == vn.getName():
                isexist = True
                vn.setValue(float(ls[1]))
        if not isexist:
            varnlist.append(vl.NumVar(ls[0],float(ls[1])))
    elif ':' in line:
        ls = line.split(':')
        isexist = False
        for vn in varnlist:
            if ls[0] == vn.getName():
                isexist = True
                print(vn.getValue())
        if not isexist:
            print('VARN Error: \n >> ' + ls[0] + ' << don\'t exist')

def vars(line):
    if '=' in line:
        ls = line.split('=')
        isexist = False
        for vs in varslist:
            if ls[0] == vs.getName():
                isexist = True
                vs.setValue(ls[1])
        if not isexist:
            varslist.append(vl.StrVar(ls[0],ls[1]))
    elif ':' in line:
        ls = line.split(':')
        isexist = False
        for vs in varslist:
            if ls[0] == vs.getName():
                isexist = True
                print(vs.getValue())
        if not isexist:
            print('VARS Error: \n >> ' + ls[0] + ' << don\'t exist')
