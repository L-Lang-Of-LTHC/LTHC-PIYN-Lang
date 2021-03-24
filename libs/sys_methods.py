# -*- coding: utf-8 -*-

# ./libs/sys_methods.py  =>  contains default methods of this programming language system

############
# IMPORTS
############
import libs.var_lib as vl
import utils.linker as lk

############
# Usefull
############
varnlist = [vl.NumVar('DefaultNumVar_CreatedByLanguageSystem_00000000')]
varslist = [vl.StrVar('DefaultStrVar_CreatedByLanguageSystem_00000000')]
varsalist = [vl.StrVarAll('DefaultStrVarAll_CreatedByLanguageSystem_00000000')]
varflist = [vl.FuncVar('DefaultFuncVar_CreatedByLanguageSystem_00000000')]

def scan():
    out = '\n'
    if len(varnlist) > 1:
        out += '  VARN > \n'
        for i in range(1, len(varnlist)):
            out += '    ' + varnlist[i].getName() + ' :> ' + str(varnlist[i].getValue()) + ' \n'
    if len(varslist) > 1:
        out += '\n  VARS > \n'
        for i in range(1, len(varslist)):
            out += '    ' + varslist[i].getName() + ' :> ' + str(varslist[i].getValue()) + ' \n'
    if len(varsalist) > 1:
        out += '\n  VARSA > \n'
        for i in range(1, len(varsalist)):
            out += '    ' + varsalist[i].getName() + ' :> ' + str(varsalist[i].getValue()) + ' \n'
    if len(varflist) > 1:
        out += '\n  VARF > \n'
        for i in range(1, len(varflist)):
            out += '    ' + varflist[i].getName() + ' :> ' + str(varflist[i].getFile()) + ' \n'
    return out

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
    elif '#sa' in line and not already:
        ls = line.split('#sa')
        isexist1 = False
        isexist2 = False
        for vn in varnlist:
            if ls[0] == vn.getName():
                isexist1 = True
                for vs in varsalist:
                    if ls[0] == vs.getName():
                        isexist2 = True
                        try:
                            vn.setValue(float(vs.getValue()))
                        except:
                            print('\nCasting error\n')
        if not isexist1:
            print('\nVARN Error: \n >> ' + ls[0] + ' << don\'t exist\n')
        else:
            if not isexist2:
                print('\nVARSA Error: \n >> ' + ls[0] + ' << don\'t exist\n')
        already = True
    elif '#s' in line and not already:
        ls = line.split('#s')
        isexist1 = False
        isexist2 = False
        for vn in varnlist:
            if ls[0] == vn.getName():
                isexist1 = True
                for vs in varslist:
                    if ls[0] == vs.getName():
                        isexist2 = True
                        try:
                            vn.setValue(float(vs.getValue()))
                        except:
                            print('\nCasting error\n')
        if not isexist1:
            print('\nVARN Error: \n >> ' + ls[0] + ' << don\'t exist\n')
        else:
            if not isexist2:
                print('\nVARS Error: \n >> ' + ls[0] + ' << don\'t exist\n')
        already = True
    elif '#' in line and not already:
        ls = line.split('#')
        isexist1 = False
        isexist2 = False
        for vn in varnlist:
            if ls[0] == vn.getName():
                isexist1 = True
                for vs in varslist:
                    if ls[0] == vs.getName():
                        isexist2 = True
                        try:
                            vn.setValue(float(vs.getValue()))
                        except:
                            print('\nCasting error\n')
        if not isexist1:
            print('\nVARN Error: \n >> ' + ls[0] + ' << don\'t exist\n')
        else:
            if not isexist2:
                print('\nVARS Error: \n >> ' + ls[0] + ' << don\'t exist\n')
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
    elif '#n' in line and not already:
        ls = line.split('#n')
        isexist1 = False
        isexist2 = False
        for vs in varslist:
            if ls[0] == vs.getName():
                isexist1 = True
                for vn in varnlist:
                    if ls[0] == vn.getName():
                        isexist2 = True
                        vs.setValue(str(vn.getValue()))
        if not isexist1:
            print('\nVARS Error: \n >> ' + ls[0] + ' << don\'t exist\n')
        else:
            if not isexist2:
                print('\nVARN Error: \n >> ' + ls[0] + ' << don\'t exist\n')
        already = True
    elif '#' in line and not already:
        ls = line.split('#')
        isexist1 = False
        isexist2 = False
        for vs in varslist:
            if ls[0] == vs.getName():
                isexist1 = True
                for vs2 in varsalist:
                    if ls[0] == vs2.getName():
                        isexist2 = True
                        vs.setValue(vs2.getValue())
        if not isexist1:
            print('\nVARS Error: \n >> ' + ls[0] + ' << don\'t exist\n')
        else:
            if not isexist2:
                print('\nVARSA Error: \n >> ' + ls[0] + ' << don\'t exist\n')
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
    elif '#n' in line and not already:
        ls = line.split('#n')
        isexist1 = False
        isexist2 = False
        for vs in varsalist:
            if ls[0] == vs.getName():
                isexist1 = True
                for vn in varnlist:
                    if ls[0] == vn.getName():
                        isexist2 = True
                        vs.setValue(str(vn.getValue()))
        if not isexist1:
            print('\nVARSA Error: \n >> ' + ls[0] + ' << don\'t exist\n')
        else:
            if not isexist2:
                print('\nVARN Error: \n >> ' + ls[0] + ' << don\'t exist\n')
        already = True
    elif '#' in line and not already:
        ls = line.split('#')
        isexist1 = False
        isexist2 = False
        for vs in varsalist:
            if ls[0] == vs.getName():
                isexist1 = True
                for vs2 in varslist:
                    if ls[0] == vs2.getName():
                        isexist2 = True
                        vs.setValue(vs2.getValue())
        if not isexist1:
            print('\nVARSA Error: \n >> ' + ls[0] + ' << don\'t exist\n')
        else:
            if not isexist2:
                print('\nVARS Error: \n >> ' + ls[0] + ' << don\'t exist\n')
        already = True

def ssum(line):
    if '=' in line:
        isexist1 = False
        isexist2 = False
        ls = line.split('=')
        for vn in varnlist:
            if ls[0] == vn.getName():
                isexist1 = True
                for vs in varslist:
                    if ls[1] == vs.getName():
                        isexist2 = True
                        vn.setValue(vs.ssum())
        if not isexist1:
            print('\nVARN Error: \n >> ' + ls[0] + ' << don\'t exist\n')
        else:
            if not isexist2:
                print('\nVARS Error: \n >> ' + ls[1] + ' << don\'t exist\n')
    else:
        print('\nSSUM Syntax Error: expected \'=\' between variables\' name')

def hssum(line):
    if '=' in line:
        isexist1 = False
        isexist2 = False
        ls = line.split('=')
        for vn in varnlist:
            if ls[0] == vn.getName():
                isexist1 = True
                for vs in varslist:
                    if ls[1] == vs.getName():
                        isexist2 = True
                        vn.setValue(vs.hssum())
        if not isexist1:
            print('\nVARN Error: \n >> ' + ls[0] + ' << don\'t exist\n')
        else:
            if not isexist2:
                print('\nVARS Error: \n >> ' + ls[1] + ' << don\'t exist\n')
    else:
        print('\nHSSUM Syntax Error: expected \'=\' between variables\' name')

def smudi(line):
    if '=' in line:
        isexist1 = False
        isexist2 = False
        ls = line.split('=')
        for vn in varnlist:
            if ls[0] == vn.getName():
                isexist1 = True
                for vs in varslist:
                    if ls[1] == vs.getName():
                        isexist2 = True
                        vn.setValue(vs.smudi())
        if not isexist1:
            print('\nVARN Error: \n >> ' + ls[0] + ' << don\'t exist\n')
        else:
            if not isexist2:
                print('\nVARS Error: \n >> ' + ls[1] + ' << don\'t exist\n')
    else:
        print('\nSMUDI Syntax Error: expected \'=\' between variables\' name')

def hsmudi(line):
    if '=' in line:
        isexist1 = False
        isexist2 = False
        ls = line.split('=')
        for vn in varnlist:
            if ls[0] == vn.getName():
                isexist1 = True
                for vs in varslist:
                    if ls[1] == vs.getName():
                        isexist2 = True
                        vn.setValue(vs.hsmudi())
        if not isexist1:
            print('\nVARN Error: \n >> ' + ls[0] + ' << don\'t exist\n')
        else:
            if not isexist2:
                print('\nVARS Error: \n >> ' + ls[1] + ' << don\'t exist\n')
    else:
        print('\nHSMUDI Syntax Error: expected \'=\' between variables\' name')

def compare_cmp(line):
    if ':' in line:
        ltemp = line.split(':')
        if len(ltemp) > 1:
            if '=>' in ltemp[1]:
                ltemp2 = ltemp[1].split('=>')
                ls = [ltemp[0],ltemp2[0],ltemp2[1]]
                isexist1 = False
                isexist2 = False
                isexist3 = False
                for vn1 in varnlist:
                    if ls[0] == vn1.getName():
                        isexist1 = True
                        for vn2 in varnlist:
                            if ls[1] == vn2.getName():
                                isexist2 = True
                                for vn3 in varnlist:
                                    if ls[2] == vn3.getName():
                                        isexist3 = True
                                        v1 = vn1.getValue()
                                        v2 = vn2.getValue()
                                        if v1 > v2:
                                            vn3.setValue(1)
                                        if v1 == v2:
                                            vn3.setValue(0)
                                        if v1 < v2:
                                            vn3.setValue(-1)
                if not isexist1:
                    print('\nVARN Error: \n >> ' + ls[0] + ' << don\'t exist\n')
                else:
                    if not isexist2:
                        print('\nVARN Error: \n >> ' + ls[1] + ' << don\'t exist\n')
                    else:
                        if not isexist3:
                            print('\nVARN Error: \n >> ' + ls[2] + ' << don\'t exist\n')
            else:
                print('\nCMP Syntax Error: expected \'=>\' between second variable\'s name and third variable\'s name')
        else:
            print('\nCMP Syntax Error: missing args')
    else:
        print('\nCMP Syntax Error: expected \':\' between first variable\'s name and second variable\'s name')

def compare_cmps(line):
    if ':' in line:
        ltemp = line.split(':')
        if len(ltemp) > 1:
            if '=>' in ltemp[1]:
                ltemp2 = ltemp[1].split('=>')
                ls = [ltemp[0],ltemp2[0],ltemp2[1]]
                isexist1 = False
                isexist2 = False
                isexist3 = False
                for vs1 in varslist:
                    if ls[0] == vs1.getName():
                        isexist1 = True
                        for vs2 in varslist:
                            if ls[1] == vs2.getName():
                                isexist2 = True
                                for vn in varnlist:
                                    if ls[2] == vn.getName():
                                        isexist3 = True
                                        v1 = vs1.ssum()
                                        v2 = vs2.ssum()
                                        vl1 = len(vs1.getValue())
                                        vl2 = len(vs2.getValue())
                                        if vl1 > vl2:
                                            vn.setValue(1)
                                        if vl1 < vl2:
                                            vn.setValue(-1)
                                        if vl1 == vl2:
                                            if v1 > v2:
                                                vn.setValue(1)
                                            if v1 == v2:
                                                vn.setValue(0)
                                            if v1 < v2:
                                                vn.setValue(-1)
                if not isexist1:
                    print('\nVARS Error: \n >> ' + ls[0] + ' << don\'t exist\n')
                else:
                    if not isexist2:
                        print('\nVARS Error: \n >> ' + ls[1] + ' << don\'t exist\n')
                    else:
                        if not isexist3:
                            print('\nVARN Error: \n >> ' + ls[2] + ' << don\'t exist\n')
            else:
                print('\nCMPS Syntax Error: expected \'=>\' between second variable\'s name and third variable\'s name')
        else:
            print('\nCMPS Syntax Error: missing args')
    else:
        print('\nCMPS Syntax Error: expected \':\' between first variable\'s name and second variable\'s name')

def compare_cmpr(line):
    if ':' in line:
        ltemp = line.split(':')
        if len(ltemp) > 1:
            if '=>' in ltemp[1]:
                ltemp2 = ltemp[1].split('=>')
                ls = [ltemp[0],ltemp2[0],ltemp2[1]]
                isexist1 = False
                isexist2 = False
                isexist3 = False
                for vs1 in varslist:
                    if ls[0] == vs1.getName():
                        isexist1 = True
                        for vs2 in varslist:
                            if ls[1] == vs2.getName():
                                isexist2 = True
                                for vn in varnlist:
                                    if ls[2] == vn.getName():
                                        isexist3 = True
                                        v1 = vs1.getValue()
                                        v2 = vs2.getValue()
                                        if v1 == v2:
                                            vn.setValue(0)
                                        else:
                                            vn.setValue(-2)
                if not isexist1:
                    print('\nVARS Error: \n >> ' + ls[0] + ' << don\'t exist\n')
                else:
                    if not isexist2:
                        print('\nVARS Error: \n >> ' + ls[1] + ' << don\'t exist\n')
                    else:
                        if not isexist3:
                            print('\nVARN Error: \n >> ' + ls[2] + ' << don\'t exist\n')
            else:
                print('\nCMPR Syntax Error: expected \'=>\' between second variable\'s name and third variable\'s name')
        else:
            print('\nCMPR Syntax Error: missing args')
    else:
        print('\nCMPR Syntax Error: expected \':\' between first variable\'s name and second variable\'s name')

def compare_cmpra(line):
    if ':' in line:
        ltemp = line.split(':')
        if len(ltemp) > 1:
            if '=>' in ltemp[1]:
                ltemp2 = ltemp[1].split('=>')
                ls = [ltemp[0],ltemp2[0],ltemp2[1]]
                isexist1 = False
                isexist2 = False
                isexist3 = False
                for vs1 in varsalist:
                    if ls[0] == vs1.getName():
                        isexist1 = True
                        for vs2 in varsalist:
                            if ls[1] == vs2.getName():
                                isexist2 = True
                                for vn in varnlist:
                                    if ls[2] == vn.getName():
                                        isexist3 = True
                                        v1 = vs1.getValue()
                                        v2 = vs2.getValue()
                                        if v1 == v2:
                                            vn.setValue(0)
                                        else:
                                            vn.setValue(-2)
                if not isexist1:
                    print('\nVARSA Error: \n >> ' + ls[0] + ' << don\'t exist\n')
                else:
                    if not isexist2:
                        print('\nVARSA Error: \n >> ' + ls[1] + ' << don\'t exist\n')
                    else:
                        if not isexist3:
                            print('\nVARN Error: \n >> ' + ls[2] + ' << don\'t exist\n')
            else:
                print('\nCMPRA Syntax Error: expected \'=>\' between second variable\'s name and third variable\'s name')
        else:
            print('\nCMPRA Syntax Error: missing args')
    else:
        print('\nCMPRA Syntax Error: expected \':\' between first variable\'s name and second variable\'s name')

def varf(line):
    if '=' in line:
        ls = line.split('=')
        isexist = False
        for vf in varflist:
            if ls[0] == vf.getName():
                isexist = True
        if not isexist:
            varflist.append(vl.FuncVar(ls[0],ls[1]))

def fcall(line):
    if len(line) > 0:
        isexist = False
        for vf in varflist:
            if line == vf.getName():
                isexist = True
                lk.link(vf.getFile(), 0)
        if not isexist:
            print('\nVARF Error: \n >> ' + line + ' << don\'t exist\n')
    else:
        print('\nFCALL Error: specify a file')

def lt(line):
    if ':' in line:
        ls = line.split(':')
        isexist1 = False
        isexist2 = False
        for vn in varnlist:
            if ls[0] == vn.getName():
                isexist1 = True
                if vn.getValue() == -1:
                    for vf in varflist:
                        if ls[1] == vf.getName():
                            isexist2 = True
                            lk.link(vf.getFile(), 0)
                else:
                    isexist2 = True
        if not isexist1:
            print('\nVARN Error: \n >> ' + ls[0] + ' << don\'t exist\n')
        else:
            if not isexist2:
                print('\nVARF Error: \n >> ' + ls[1] + ' << don\'t exist\n')
    else:
        print('\nLT Error: missing \':\'')

def gt(line):
    if ':' in line:
        ls = line.split(':')
        isexist1 = False
        isexist2 = False
        for vn in varnlist:
            if ls[0] == vn.getName():
                isexist1 = True
                if vn.getValue() == 1:
                    for vf in varflist:
                        if ls[1] == vf.getName():
                            isexist2 = True
                            lk.link(vf.getFile(), 0)
                else:
                    isexist2 = True
        if not isexist1:
            print('\nVARN Error: \n >> ' + ls[0] + ' << don\'t exist\n')
        else:
            if not isexist2:
                print('\nVARF Error: \n >> ' + ls[1] + ' << don\'t exist\n')
    else:
        print('\nGT Error: missing \':\'')

def ne(line):
    if ':' in line:
        ls = line.split(':')
        isexist1 = False
        isexist2 = False
        for vn in varnlist:
            if ls[0] == vn.getName():
                isexist1 = True
                vl = vn.getValue()
                if vl == -1 or vl == -2 or vl == 1:
                    for vf in varflist:
                        if ls[1] == vf.getName():
                            isexist2 = True
                            lk.link(vf.getFile(), 0)
                else:
                    isexist2 = True
        if not isexist1:
            print('\nVARN Error: \n >> ' + ls[0] + ' << don\'t exist\n')
        else:
            if not isexist2:
                print('\nVARF Error: \n >> ' + ls[1] + ' << don\'t exist\n')
    else:
        print('\nNE Error: missing \':\'')

def eq(line):
    if ':' in line:
        ls = line.split(':')
        isexist1 = False
        isexist2 = False
        for vn in varnlist:
            if ls[0] == vn.getName():
                isexist1 = True
                if vn.getValue() == 0:
                    for vf in varflist:
                        if ls[1] == vf.getName():
                            isexist2 = True
                            lk.link(vf.getFile(), 0)
                else:
                    isexist2 = True
        if not isexist1:
            print('\nVARN Error: \n >> ' + ls[0] + ' << don\'t exist\n')
        else:
            if not isexist2:
                print('\nVARF Error: \n >> ' + ls[1] + ' << don\'t exist\n')
    else:
        print('\nEQ Error: missing \':\'')
