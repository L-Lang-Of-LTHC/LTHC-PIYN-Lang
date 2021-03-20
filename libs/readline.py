# -*- coding: utf-8 -*-

# ./libs/readline.py  =>  contains default method for analyze line

############
# IMPORTS
############
import libs.keyword_lib as kl
import libs.sys_methods as sm
import utils.logger_utils as lgu

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

def readline(line,inshell,logstate,logfile):
    if inshell:
        already = False
        if kl.hasKeyWord(line, V) and not already:
            line = line[len(V):len(line)]
            sm.varn(line)
            if logstate == 'true':
                lgu.log(logfile, 'Shell >RL> VARN')
            already = True
        elif kl.hasKeyWord(line, SA) and not already:
            line = line[len(SA):len(line)]
            sm.varsa(line)
            if logstate == 'true':
                lgu.log(logfile, 'Shell >RL> VARSA')
            already = True
        elif kl.hasKeyWord(line, S) and not already:
            line = line[len(S):len(line)]
            sm.vars(line)
            if logstate == 'true':
                lgu.log(logfile, 'Shell >RL> VARS')
            already = True
        elif kl.hasKeyWord(line, HSM) and not already:
            line = line[len(HSM):len(line)]
            sm.hsmudi(line)
            if logstate == 'true':
                lgu.log(logfile, 'Shell >RL> HSMUDI')
            already = True
        elif kl.hasKeyWord(line, SM) and not already:
            line = line[len(SM):len(line)]
            sm.smudi(line)
            if logstate == 'true':
                lgu.log(logfile, 'Shell >RL> SMUDI')
            already = True
        elif kl.hasKeyWord(line, HSS) and not already:
            line = line[len(HSS):len(line)]
            sm.hssum(line)
            if logstate == 'true':
                lgu.log(logfile, 'Shell >RL> HSSUM')
            already = True
        elif kl.hasKeyWord(line, SS) and not already:
            line = line[len(SS):len(line)]
            sm.ssum(line)
            if logstate == 'true':
                lgu.log(logfile, 'Shell >RL> SSUM')
            already = True

    else:
        if kl.endLineRespected(line):
            line = line[0:-1]
            already = False
            if kl.hasKeyWord(line, V) and not already:
                line = line[len(V):len(line)]
                sm.varn(line)
                if logstate == 'true':
                    lgu.log(logfile, 'File >RL> VARN')
                already = True
            elif kl.hasKeyWord(line, SA) and not already:
                line = line[len(SA):len(line)]
                sm.varsa(line)
                if logstate == 'true':
                    lgu.log(logfile, 'File >RL> VARSA')
                already = True
            elif kl.hasKeyWord(line, S) and not already:
                line = line[len(S):len(line)]
                sm.vars(line)
                if logstate == 'true':
                    lgu.log(logfile, 'File >RL> VARS')
                already = True
            elif kl.hasKeyWord(line, HSM) and not already:
                line = line[len(HSM):len(line)]
                sm.hsmudi(line)
                if logstate == 'true':
                    lgu.log(logfile, 'File >RL> HSMUDI')
                already = True
            elif kl.hasKeyWord(line, SM) and not already:
                line = line[len(SM):len(line)]
                sm.smudi(line)
                if logstate == 'true':
                    lgu.log(logfile, 'File >RL> SMUDI')
                already = True
            elif kl.hasKeyWord(line, HSS) and not already:
                line = line[len(HSS):len(line)]
                sm.hssum(line)
                if logstate == 'true':
                    lgu.log(logfile, 'File >RL> HSSUM')
                already = True
            elif kl.hasKeyWord(line, SS) and not already:
                line = line[len(SS):len(line)]
                sm.ssum(line)
                if logstate == 'true':
                    lgu.log(logfile, 'File >RL> SSUM')
                already = True
