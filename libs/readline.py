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

############
# METHODS
############

def readline(line,inshell):
    if inshell:
        if kl.hasKeyWord(line, V):
            line = line[len(V):len(line)]
            sm.varn(line)
        elif kl.hasKeyWord(line, S):
            line = line[len(S):len(line)]
            sm.vars(line)
    else:
        if kl.endLineRespected(line):
            line = line[0:-1]
            if kl.hasKeyWord(line, V):
                line = line[len(V):len(line)]
                sm.varn(line)
            elif kl.hasKeyWord(line, S):
                line = line[len(S):len(line)]
                sm.vars(line)
