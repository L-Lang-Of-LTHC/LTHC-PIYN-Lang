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
varsalist = [vl.StrVarAll('DefaultStrVarAll_CreatedByLanguageSystem_00000000')]

############
# METHODS
############

def varn(line):
    already = False
    if '=' in line and not already:
        ls = line.split('=')
        isexist = False
        for vn in varnlist:
            if ls[0] == vn.getName():
                isexist = True
                vn.setValue(float(ls[1]))
        if not isexist:
            varnlist.append(vl.NumVar(ls[0],float(ls[1])))
        already = True
    elif '>' in line and not already:
        ls = line.split('>')
        isexist = False
        for vn in varnlist:
            if ls[0] == vn.getName():
                isexist = True
                print(vn.getValue())
        if not isexist:
            print('\nVARN Error: \n >> ' + ls[0] + ' << don\'t exist\n')
        already = True
    elif '<' in line and not already:
        ls = line.split('<')
        isexist = False
        for vn in varnlist:
            if ls[0] == vn.getName():
                isexist = True
                temp = input(' VARN > ')
                try:
                    vn.setValue(float(temp))
                except:
                    print('\nInput error: you have to give a float\n')
        if not isexist:
            print('\nVARN Error: \n >> ' + ls[0] + ' << don\'t exist\n')
        already = True
    elif '++' in line and not already:
        ls = line.split('++')
        isexist = False
        for vn in varnlist:
            if ls[0] == vn.getName():
                isexist = True
                vn.incValue()
        if not isexist:
            print('\nVARN Error: \n >> ' + ls[0] + ' << don\'t exist\n')
        already = True
    elif '--' in line and not already:
        ls = line.split('--')
        isexist = False
        for vn in varnlist:
            if ls[0] == vn.getName():
                isexist = True
                vn.decValue()
        if not isexist:
            print('\nVARN Error: \n >> ' + ls[0] + ' << don\'t exist\n')
        already = True
    elif '+' in line and not already:
        ls = line.split('+')
        isexist1 = False
        isexist2 = False
        for vn1 in varnlist:
            if ls[0] == vn1.getName():
                isexist1 = True
                for vn2 in varnlist:
                    if ls[1] == vn2.getName():
                        isexist2 = True
                        vn1.setValue(vn1.getValue()+vn2.getValue())
        if not isexist1:
            print('\nVARN Error: \n >> ' + ls[0] + ' << don\'t exist\n')
        else:
            if not isexist2:
                print('\nVARN Error: \n >> ' + ls[1] + ' << don\'t exist\n')
        already = True
    elif '-' in line and not already:
        ls = line.split('-')
        isexist1 = False
        isexist2 = False
        for vn1 in varnlist:
            if ls[0] == vn1.getName():
                isexist1 = True
                for vn2 in varnlist:
                    if ls[1] == vn2.getName():
                        isexist2 = True
                        vn1.setValue(vn1.getValue()-vn2.getValue())
        if not isexist1:
            print('\nVARN Error: \n >> ' + ls[0] + ' << don\'t exist\n')
        else:
            if not isexist2:
                print('\nVARN Error: \n >> ' + ls[1] + ' << don\'t exist\n')
        already = True
    elif '*' in line and not already:
        ls = line.split('*')
        isexist1 = False
        isexist2 = False
        for vn1 in varnlist:
            if ls[0] == vn1.getName():
                isexist1 = True
                for vn2 in varnlist:
                    if ls[1] == vn2.getName():
                        isexist2 = True
                        vn1.setValue(vn1.getValue()*vn2.getValue())
        if not isexist1:
            print('\nVARN Error: \n >> ' + ls[0] + ' << don\'t exist\n')
        else:
            if not isexist2:
                print('\nVARN Error: \n >> ' + ls[1] + ' << don\'t exist\n')
        already = True
    elif '/' in line and not already:
        ls = line.split('/')
        isexist1 = False
        isexist2 = False
        for vn1 in varnlist:
            if ls[0] == vn1.getName():
                isexist1 = True
                for vn2 in varnlist:
                    if ls[1] == vn2.getName():
                        isexist2 = True
                        vn1.setValue(vn1.getValue()/vn2.getValue())
        if not isexist1:
            print('\nVARN Error: \n >> ' + ls[0] + ' << don\'t exist\n')
        else:
            if not isexist2:
                print('\nVARN Error: \n >> ' + ls[1] + ' << don\'t exist\n')
        already = True
    elif '%' in line and not already:
        ls = line.split('%')
        isexist1 = False
        isexist2 = False
        for vn1 in varnlist:
            if ls[0] == vn1.getName():
                isexist1 = True
                for vn2 in varnlist:
                    if ls[1] == vn2.getName():
                        isexist2 = True
                        vn1.setValue(vn1.getValue()%vn2.getValue())
        if not isexist1:
            print('\nVARN Error: \n >> ' + ls[0] + ' << don\'t exist\n')
        else:
            if not isexist2:
                print('\nVARN Error: \n >> ' + ls[1] + ' << don\'t exist\n')
        already = True

def vars(line):
    already = False
    if '=' in line and not already:
        ls = line.split('=')
        isexist = False
        for vs in varslist:
            if ls[0] == vs.getName():
                isexist = True
                vs.setValue(ls[1])
        if not isexist:
            varslist.append(vl.StrVar(ls[0],ls[1]))
        already = True
    elif '>' in line and not already:
        ls = line.split('>')
        isexist = False
        for vs in varslist:
            if ls[0] == vs.getName():
                isexist = True
                print(vs.getValue())
        if not isexist:
            print('\nVARS Error: \n >> ' + ls[0] + ' << don\'t exist\n')
        already = True
    elif '<' in line and not already:
        ls = line.split('<')
        isexist = False
        for vs in varslist:
            if ls[0] == vs.getName():
                isexist = True
                temp = input(' VARS > ')
                vs.setValue(temp)
    elif '++' in line and not already:
        ls = line.split('++')
        isexist = False
        for vs in varslist:
            if ls[0] == vs.getName():
                isexist = True
                vs.incValue()
        if not isexist:
            print('\nVARS Error: \n >> ' + ls[0] + ' << don\'t exist\n')
        already = True
    elif '--' in line and not already:
        ls = line.split('--')
        isexist = False
        for vs in varslist:
            if ls[0] == vs.getName():
                isexist = True
                vs.decValue()
        if not isexist:
            print('\nVARS Error: \n >> ' + ls[0] + ' << don\'t exist\n')
        already = True
    elif '+' in line and not already:
        ls = line.split('+')
        isexist1 = False
        isexist2 = False
        for vs1 in varslist:
            if ls[0] == vs1.getName():
                isexist1 = True
                for vs2 in varslist:
                    if ls[1] == vs2.getName():
                        isexist2 = True
                        vs1.setValue(vs1.getValue()+vs2.getValue())
        if not isexist1:
            print('\nVARS Error: \n >> ' + ls[0] + ' << don\'t exist\n')
        else:
            if not isexist2:
                print('\nVARS Error: \n >> ' + ls[1] + ' << don\'t exist\n')
        already = True

def varsa(line):
    already = False
    if '=' in line and not already:
        ls = line.split('=')
        isexist = False
        for vs in varsalist:
            if ls[0] == vs.getName():
                isexist = True
                vs.setValue(ls[1])
        if not isexist:
            varsalist.append(vl.StrVarAll(ls[0],ls[1]))
        already = True
    elif '>' in line and not already:
        ls = line.split('>')
        isexist = False
        for vs in varsalist:
            if ls[0] == vs.getName():
                isexist = True
                print(vs.getValue())
        if not isexist:
            print('\nVARSA Error: \n >> ' + ls[0] + ' << don\'t exist\n')
        already = True
    elif '<' in line and not already:
        ls = line.split('<')
        isexist = False
        for vs in varsalist:
            if ls[0] == vs.getName():
                isexist = True
                temp = input(' VARSA > ')
                vs.setValue(temp)
    elif '+' in line and not already:
        ls = line.split('+')
        isexist1 = False
        isexist2 = False
        for vs1 in varsalist:
            if ls[0] == vs1.getName():
                isexist1 = True
                for vs2 in varsalist:
                    if ls[1] == vs2.getName():
                        isexist2 = True
                        vs1.setValue(vs1.getValue()+vs2.getValue())
        if not isexist1:
            print('\nVARSA Error: \n >> ' + ls[0] + ' << don\'t exist\n')
        else:
            if not isexist2:
                print('\nVARSA Error: \n >> ' + ls[1] + ' << don\'t exist\n')
        already = True
