# -*- coding: utf-8 -*-

# ./mainsys/shell.py  =>  contains shell system

############
# IMPORTS
############
import libs.readline as rl
from datetime import date as dt
import libs.sys_methods as sm
import libs.var_lib as vl

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
    while status:
        sht = str(dt.today()) + ' :> Shell > '
        line = input(sht)
        if line == ec:
            if state == 'false':
                temp = []
                for i in sm.varnlist:
                    if not i.getInshell():
                        temp.append(i)
                sm.varnlist = [vl.NumVar('DefaultNumVar_CreatedByLanguageSystem_00000000')].extend(temp)
                temp = []
                for i in sm.varslist:
                    if not i.getInshell():
                        temp.append(i)
                sm.varslist = [vl.StrVar('DefaultStrVar_CreatedByLanguageSystem_00000000')].extend(temp)
                temp = []
                for i in sm.varsalist:
                    if not i.getInshell():
                        temp.append(i)
                sm.varsalist = [vl.StrVarAll('DefaultStrVarAll_CreatedByLanguageSystem_00000000')].extend(temp)
            status = False
            break
        if line == hlp:
            print(hlp_msg)
        if line != hlp:
            rl.readline(line, True, logstate, logfile)

    print('\n >>> Shell stopped <<< \n')
    
    t = None
    while t == None:
        t = input('')
