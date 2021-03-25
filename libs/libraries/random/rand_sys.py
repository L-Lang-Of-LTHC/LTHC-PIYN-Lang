# -*- coding: utf-8 -*-

# ./libs/libraries/random/rand_sys.py  =>  contains random library instructions analyzer


ishere = 'yes'
############
# IMPORTS
############
import libs.libraries.random.rand_lib as lrl
import libs.sys_methods as sm

###########
# METHOD
###########

def readline(line,mode):
    if mode == 0:
        if ':' in line:
            ltemp = line.split(':')
            if ',' in ltemp[1]:
                ltemp2 = ltemp[1].split(',')
                ls = [ltemp[0],ltemp2[0],ltemp2[1]]
                for vn in sm.varnlist:
                    if ls[0] == vn.getName():
                        vn.setValue(lrl.rnd_num(int(ls[1]), int(ls[2])))
                        break
            else:
                print('\Library Error: Random: missing \',\' minima and maxima')
        else:
            print('\Library Error: Random: missing \':\' between VARN type variable and minima')
    if mode == 1:
        if ':' in line:
            ls = line.split(':')
            for vs in sm.varslist:
                if ls[0] == vs.getName():
                    vs.setValue(lrl.rnd_str(int(ls[1])))
                    break
        else:
            print('\Library Error: Random: missing \':\' between VARS type variable and wanted number of char')
    if mode == 2:
        if ':' in line:
            ls = line.split(':')
            for vsa in sm.varsalist:
                if ls[0] == vsa.getName():
                    vsa.setValue(lrl.rnd_str(int(ls[1])))
                    break
        else:
            print('\Library Error: Random: missing \':\' between VARSA type variable and wanted number of char')
