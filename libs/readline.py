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

L = 'LOOP'

# libs
RNDN = 'RND'
RNDS = 'RNDS'
RNDA = 'RNDA'

B8 = 'BIN8'
B16 = 'BIN16'
B32 = 'BIN32'

############
# METHODS
############

def initlibs(libs):
    if sm.libsincluded == 0:
        if libs[0] == 1:
            sm.libs[0] = 1
        else:
            sm.libs[0] = 0
        if libs[1] == 1:
            sm.libs[1] = 1
        else:
            sm.libs[1] = 0
        sm.libsincluded == 1

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
        elif kl.hasKeyWord(line, L) and not already:
            line = line[len(L):len(line)]
            sm.loop(line)
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
            elif kl.hasKeyWord(line, L) and not already:
                line = line[len(L):len(line)]
                sm.loop(line)
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
            if sm.libs[0] == 1:
                try:
                    if lrn.ishere == 'yes':
                        pass
                except:
                    try:
                        import libs.libraries.random.rand_sys as lrn
                    except:
                        print('\nLibrary Including Error: verify if you have the L Lang Of LTHC included Random library')
                if kl.hasKeyWord(line, RNDS) and not already:
                    line = line[len(RNDS):len(line)]
                    lrn.readline(line, 1)
                    already = True
                elif kl.hasKeyWord(line, RNDA) and not already:
                    line = line[len(RNDA):len(line)]
                    lrn.readline(line, 2)
                    already = True
                elif kl.hasKeyWord(line, RNDN) and not already:
                    line = line[len(RNDN):len(line)]
                    lrn.readline(line, 0)
                    already = True
            if sm.libs[1] == 1:
                already = False
                if ':r' in line and not already:
                    runBin(line, 0)
                    already = True
                if not ':r' in line and not already:
                    runBin(line, 1)

def runBin(line, mode):
    if mode == 0:
        if sm.libs[0] == 1 and sm.libs[1] == 1:
                try:
                    if lcbr.ishere == 'yes':
                        pass
                except:
                    try:
                        import libs.libraries.crossed.binary_random.rand_bin as lcbr
                    except:
                        print('\nLibrary Including Error: verify if you have the L Lang Of LTHC included Crossed Random and Binary library system')
                if kl.hasKeyWord(line, B8):
                    line = line[len(B8):len(line)]
                    lcbr.readline(line, 0)
                elif kl.hasKeyWord(line, B16):
                    line = line[len(B16):len(line)]
                    lcbr.readline(line, 1)
                elif kl.hasKeyWord(line, B32):
                    line = line[len(B32):len(line)]
                    lcbr.readline(line, 2)
    if mode == 1:
        if sm.libs[1] == 1:
            try:
                if lbsm.ishere == 'yes':
                    pass
            except:
                try:
                    import libs.libraries.binary.binary_sm as lbsm
                except:
                    print('\nLibrary Including Error: verify if you have the L Lang Of LTHC included Binary library')
            if kl.hasKeyWord(line, B8):
                line = line[len(B8):len(line)]
                lbsm.readline(line, 0)
            elif kl.hasKeyWord(line, B16):
                line = line[len(B16):len(line)]
                lbsm.readline(line, 1)
            elif kl.hasKeyWord(line, B32):
                line = line[len(B32):len(line)]
                lbsm.readline(line, 2)
