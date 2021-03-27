# -*- coding: utf-8 -*-

# ./libs/libraries/binary/binary_sm.py  =>  contains binary library methods


ishere = 'yes'
############
# IMPORTS
############
import libs.libraries.binary.var_lib as bvl
import libs.sys_methods as sm

############
# Usefull
############
varb8list = [bvl.Bin8('DefaultBin8_CreatedByLanguageSystem_00000000')]
varb16list = [bvl.Bin16('DefaultBin16_CreatedByLanguageSystem_00000000')]
varb32list = [bvl.Bin32('DefaultBin32_CreatedByLanguageSystem_00000000')]

def initthis():
    sm.varnames.extend(['DefaultBin8_CreatedByLanguageSystem_00000000','DefaultBin16_CreatedByLanguageSystem_00000000','DefaultBin32_CreatedByLanguageSystem_00000000'])

###########
# METHOD
###########

def readline(line, mode):
    if mode == 0:
        already = False
        if '=n' in line and not already:
            ls = line.split('=n')
            isexist = False
            for vb in varb8list:
                if ls[0] == vb.getName():
                    isexist = True
                    vb.setValueNum(int(ls[1]))
                    break
            if not isexist:
                    print('\nLibrary Error: Binary: \n >> ' + ls[0] + ' << don\'t exist\n')
            already = True
        elif '>n' in line and not already:
            ls = line.split('>n')
            isexist = False
            for vb in varb8list:
                if ls[0] == vb.getName():
                    isexist = True
                    print(vb.getValueNum())
                    break
            if not isexist:
                print('\nLibrary Error: Binary: \n >> ' + ls[0] + ' << don\'t exist\n')
            already = True
        elif '<n' in line and not already:
            ls = line.split('<n')
            isexist = False
            for vb in varb8list:
                if ls[0] == vb.getName():
                    isexist = True
                    temp = input(' Binary Lib BIN8 > ')
                    try:
                        vb.setValueNum(int(temp))
                    except:
                        print('\nInput error: you have to give an integer\n')
                    break
            if not isexist:
                print('\nLibrary Error: Binary: \n >> ' + ls[0] + ' << don\'t exist\n')
            already = True
        if '=' in line and not already:
            ls = line.split('=')
            isexist = False
            for vb in varb8list:
                if ls[0] == vb.getName():
                    isexist = True
                    vb.setValue(ls[1])
                    break
            if not isexist:
                if ls[0] not in sm.varnames:
                    varb8list.append(bvl.Bin8(ls[0], ls[1]))
                    sm.varnames.append(ls[0])
                else:
                    print('\n Variable Naming Error: two variables cannot have the same name')
            already = True
        elif '>' in line and not already:
            ls = line.split('>')
            isexist = False
            for vb in varb8list:
                if ls[0] == vb.getName():
                    isexist = True
                    print(vb.getValue())
                    break
            if not isexist:
                print('\nLibrary Error: Binary: \n >> ' + ls[0] + ' << don\'t exist\n')
            already = True
        elif '<' in line and not already:
            ls = line.split('<')
            isexist = False
            for vb in varb8list:
                if ls[0] == vb.getName():
                    isexist = True
                    temp = input(' Binary Lib BIN8 > ')
                    vb.setValue(temp)
                    break
            if not isexist:
                print('\nLibrary Error: Binary: \n >> ' + ls[0] + ' << don\'t exist\n')
            already = True
    if mode == 1:
        already = False
        if '=n' in line and not already:
            ls = line.split('=n')
            isexist = False
            for vb in varb16list:
                if ls[0] == vb.getName():
                    isexist = True
                    vb.setValueNum(int(ls[1]))
                    break
            if not isexist:
                    print('\nLibrary Error: Binary: \n >> ' + ls[0] + ' << don\'t exist\n')
            already = True
        elif '>n' in line and not already:
            ls = line.split('>n')
            isexist = False
            for vb in varb16list:
                if ls[0] == vb.getName():
                    isexist = True
                    print(vb.getValueNum())
                    break
            if not isexist:
                print('\nLibrary Error: Binary: \n >> ' + ls[0] + ' << don\'t exist\n')
            already = True
        elif '<n' in line and not already:
            ls = line.split('<n')
            isexist = False
            for vb in varb16list:
                if ls[0] == vb.getName():
                    isexist = True
                    temp = input(' Binary Lib BIN16 > ')
                    try:
                        vb.setValueNum(int(temp))
                    except:
                        print('\nInput error: you have to give an integer\n')
                    break
            if not isexist:
                print('\nLibrary Error: Binary: \n >> ' + ls[0] + ' << don\'t exist\n')
            already = True
        if '=' in line and not already:
            ls = line.split('=')
            isexist = False
            for vb in varb16list:
                if ls[0] == vb.getName():
                    isexist = True
                    vb.setValue(ls[1])
                    break
            if not isexist:
                if ls[0] not in sm.varnames:
                    varb16list.append(bvl.Bin16(ls[0], ls[1]))
                    sm.varnames.append(ls[0])
                else:
                    print('\n Variable Naming Error: two variables cannot have the same name')
            already = True
        elif '>' in line and not already:
            ls = line.split('>')
            isexist = False
            for vb in varb16list:
                if ls[0] == vb.getName():
                    isexist = True
                    print(vb.getValue())
                    break
            if not isexist:
                print('\nLibrary Error: Binary: \n >> ' + ls[0] + ' << don\'t exist\n')
            already = True
        elif '<' in line and not already:
            ls = line.split('<')
            isexist = False
            for vb in varb16list:
                if ls[0] == vb.getName():
                    isexist = True
                    temp = input(' Binary Lib BIN16 > ')
                    vb.setValue(temp)
                    break
            if not isexist:
                print('\nLibrary Error: Binary: \n >> ' + ls[0] + ' << don\'t exist\n')
            already = True
    if mode == 2:
        already = False
        if '=n' in line and not already:
            ls = line.split('=n')
            isexist = False
            for vb in varb32list:
                if ls[0] == vb.getName():
                    isexist = True
                    vb.setValueNum(int(ls[1]))
                    break
            if not isexist:
                    print('\nLibrary Error: Binary: \n >> ' + ls[0] + ' << don\'t exist\n')
            already = True
        elif '>n' in line and not already:
            ls = line.split('>n')
            isexist = False
            for vb in varb32list:
                if ls[0] == vb.getName():
                    isexist = True
                    print(vb.getValueNum())
                    break
            if not isexist:
                print('\nLibrary Error: Binary: \n >> ' + ls[0] + ' << don\'t exist\n')
            already = True
        elif '<n' in line and not already:
            ls = line.split('<n')
            isexist = False
            for vb in varb32list:
                if ls[0] == vb.getName():
                    isexist = True
                    temp = input(' Binary Lib BIN32 > ')
                    try:
                        vb.setValueNum(int(temp))
                    except:
                        print('\nInput error: you have to give an integer\n')
                    break
            if not isexist:
                print('\nLibrary Error: Binary: \n >> ' + ls[0] + ' << don\'t exist\n')
            already = True
        if '=' in line and not already:
            ls = line.split('=')
            isexist = False
            for vb in varb32list:
                if ls[0] == vb.getName():
                    isexist = True
                    vb.setValue(ls[1])
                    break
            if not isexist:
                if ls[0] not in sm.varnames:
                    varb32list.append(bvl.Bin32(ls[0], ls[1]))
                    sm.varnames.append(ls[0])
                else:
                    print('\n Variable Naming Error: two variables cannot have the same name')
            already = True
        elif '>' in line and not already:
            ls = line.split('>')
            isexist = False
            for vb in varb32list:
                if ls[0] == vb.getName():
                    isexist = True
                    print(vb.getValue())
                    break
            if not isexist:
                print('\nLibrary Error: Binary: \n >> ' + ls[0] + ' << don\'t exist\n')
            already = True
        elif '<' in line and not already:
            ls = line.split('<')
            isexist = False
            for vb in varb32list:
                if ls[0] == vb.getName():
                    isexist = True
                    temp = input(' Binary Lib BIN32 > ')
                    vb.setValue(temp)
                    break
            if not isexist:
                print('\nLibrary Error: Binary: \n >> ' + ls[0] + ' << don\'t exist\n')
            already = True
