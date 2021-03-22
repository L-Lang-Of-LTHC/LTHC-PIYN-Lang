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
SS = 'SSUM'
HSS = 'HSSUM'
SM = 'SMUDI'
HSM = 'HSMUDI'

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
