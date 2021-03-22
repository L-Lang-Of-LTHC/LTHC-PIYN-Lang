# -*- coding: utf-8 -*-

# ./mainsys/shell.py  =>  contains shell system

############
# IMPORTS
############
import libs.readline as rl
from datetime import date as dt
import libs.sys_methods as sm
import libs.var_lib as vl
import utils.logger_utils as lgu

##########
# Shell
##########
hlp_msg = ''
try:
    fhlp = open('utils/help_shell.txt','r',encoding='utf-8')

    tmpa = fhlp.readlines()
    for i in tmpa:
        hlp_msg += i

    fhlp.close()
except:
    print('\n\'utils/help_shell\' not found\n')

def run(state, logstate, logfile):
    ec = 'stop_shell'
    hlp = 'help_shell'
    status = True
    out = []
    while status:
        sht = str(dt.today()) + ' :> Shell > '
        line = input(sht)
        if line == ec:
            if state == 'false':
                temp = []
                for i in sm.varnlist:
                    if not i.getInshell():
                        temp.append(i)
                temp = [vl.NumVar('DefaultStrNumVar_CreatedByLanguageSystem_00000000')] + temp
                sm.varnlist = temp.copy()
                temp = []
                for i in sm.varslist:
                    if not i.getInshell():
                        temp.append(i)
                temp = [vl.StrVar('DefaultStrVar_CreatedByLanguageSystem_00000000')] + temp
                sm.varslist = temp.copy()
                temp = []
                for i in sm.varsalist:
                    if not i.getInshell():
                        temp.append(i)
                temp = [vl.StrVarAll('DefaultStrVarAll_CreatedByLanguageSystem_00000000')] + temp
                sm.varsalist = temp.copy()
            status = False
            break
        if line == hlp:
            print(hlp_msg)
        if line != hlp:
            if logstate == 'true':
                out.append(rl.readline(line, True, logstate, logfile))
                if len(out) >= 25:
                    msg_out = ''
                    for i in out:
                        msg_out += i + '\n'
                    lgu.log(logfile, msg_out)
                    out = []
                else:
                    rl.readline(line, True, logstate, logfile)

    print('\n >>> Shell stopped <<< \n')
    
    if logstate == 'true':
        msg_out = ''
        for i in out:
            msg_out += i + '\n'
        lgu.log(logfile, msg_out)
        out = []

    t = None
    while t == None:
        t = input('')
