# -*- coding: utf-8 -*-

# ./libs/readline.py  =>  contains default method for analyze line

############
# IMPORTS
############
import libs.keyword_lib as kl
import libs.sys_methods as sm

##############
# CONSTANTS
##############
V = 'VARN'
S = 'VARS'
SA = 'VARSA'
VF = 'VARF'

SS = 'SSUM'
HSS = 'HSSUM'

SM = 'SMUDI'
HSM = 'HSMUDI'

C = 'CMP'
CS = 'CMPS'
CR = 'CMPR'
CRA = 'CMPRA'

F = 'FCALL'

LT = 'LT'
GT = 'GT'
NE = 'NE'
EQ = 'EQ'

############
# METHODS
############

def readline(line,inshell):
    if inshell:
        already = False
        if kl.hasKeyWord(line, V) and not already:
            line = line[len(V):len(line)]
            sm.varn(line)
            already = True
        elif kl.hasKeyWord(line, SA) and not already:
            line = line[len(SA):len(line)]
            sm.varsa(line)
            already = True
        elif kl.hasKeyWord(line, S) and not already:
            line = line[len(S):len(line)]
            sm.vars(line)
            already = True
        elif kl.hasKeyWord(line, HSM) and not already:
            line = line[len(HSM):len(line)]
            sm.hsmudi(line)
            already = True
        elif kl.hasKeyWord(line, SM) and not already:
            line = line[len(SM):len(line)]
            sm.smudi(line)
            already = True
        elif kl.hasKeyWord(line, HSS) and not already:
            line = line[len(HSS):len(line)]
            sm.hssum(line)
            already = True
        elif kl.hasKeyWord(line, SS) and not already:
            line = line[len(SS):len(line)]
            sm.ssum(line)
            already = True
        elif kl.hasKeyWord(line, CRA):
            line = line[len(CRA):len(line)]
            sm.compare_cmpra(line)
            already = True
        elif kl.hasKeyWord(line, CR):
            line = line[len(CR):len(line)]
            sm.compare_cmpr(line)
            already = True
        elif kl.hasKeyWord(line, CS) and not already:
            line = line[len(CS):len(line)]
            sm.compare_cmps(line)
            already = True
        elif kl.hasKeyWord(line, C) and not already:
            line = line[len(C):len(line)]
            sm.compare_cmp(line)
            already = True
        elif kl.hasKeyWord(line, VF) and not already:
            line = line[len(VF):len(line)]
            sm.varf(line)
            already = True
        elif kl.hasKeyWord(line, F) and not already:
            line = line[len(F):len(line)]
            sm.fcall(line)
            already = True
        elif kl.hasKeyWord(line, LT) and not already:
            line = line[len(LT):len(line)]
            sm.lt(line)
            already = True
        elif kl.hasKeyWord(line, GT) and not already:
            line = line[len(GT):len(line)]
            sm.gt(line)
            already = True
        elif kl.hasKeyWord(line, NE) and not already:
            line = line[len(NE):len(line)]
            sm.ne(line)
            already = True
        elif kl.hasKeyWord(line, EQ) and not already:
            line = line[len(EQ):len(line)]
            sm.eq(line)
            already = True
    else:
        if kl.endLineRespected(line):
            line = line[0:-1]
            already = False
            if kl.hasKeyWord(line, V) and not already:
                line = line[len(V):len(line)]
                sm.varn(line)
                already = True
            elif kl.hasKeyWord(line, SA) and not already:
                line = line[len(SA):len(line)]
                sm.varsa(line)
                already = True
            elif kl.hasKeyWord(line, S) and not already:
                line = line[len(S):len(line)]
                sm.vars(line)
                already = True
            elif kl.hasKeyWord(line, HSM) and not already:
                line = line[len(HSM):len(line)]
                sm.hsmudi(line)
                already = True
            elif kl.hasKeyWord(line, SM) and not already:
                line = line[len(SM):len(line)]
                sm.smudi(line)
                already = True
            elif kl.hasKeyWord(line, HSS) and not already:
                line = line[len(HSS):len(line)]
                sm.hssum(line)
                already = True
            elif kl.hasKeyWord(line, SS) and not already:
                line = line[len(SS):len(line)]
                sm.ssum(line)
                already = True
            elif kl.hasKeyWord(line, CRA):
                line = line[len(CRA):len(line)]
                sm.compare_cmpra(line)
                already = True
            elif kl.hasKeyWord(line, CR):
                line = line[len(CR):len(line)]
                sm.compare_cmpr(line)
                already = True
            elif kl.hasKeyWord(line, CS) and not already:
                line = line[len(CS):len(line)]
                sm.compare_cmps(line)
                already = True
            elif kl.hasKeyWord(line, C) and not already:
                line = line[len(C):len(line)]
                sm.compare_cmp(line)
                already = True
            elif kl.hasKeyWord(line, VF) and not already:
                line = line[len(VF):len(line)]
                sm.varf(line)
                already = True
            elif kl.hasKeyWord(line, F) and not already:
                line = line[len(F):len(line)]
                sm.fcall(line)
                already = True
            elif kl.hasKeyWord(line, LT) and not already:
                line = line[len(LT):len(line)]
                sm.lt(line)
                already = True
            elif kl.hasKeyWord(line, GT) and not already:
                line = line[len(GT):len(line)]
                sm.gt(line)
                already = True
            elif kl.hasKeyWord(line, NE) and not already:
                line = line[len(NE):len(line)]
                sm.ne(line)
                already = True
            elif kl.hasKeyWord(line, EQ) and not already:
                line = line[len(EQ):len(line)]
                sm.eq(line)
                already = True
