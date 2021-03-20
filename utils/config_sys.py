# -*- coding: utf-8 -*-

# ./utils/config_sys.py  =>  contains config system

############
# IMPORTS
############
import utils.config_base as cb

###########
# System
###########
cmd = ['log','logfile','bsl','gsv','help','view','quit']
hlp_msg = '\n  Help :  \n     -> log : change log setting \n     -> logfile : change log file path \n     -> bsl : change bypass shell limit setting \n     -> gsv : change global shell var setting \n     -> help : show this help message \n     -> view : show config values \n     -> quit : quit the \"Config SYS\" \n'

def run(param):
    status = True

    while status:
        inp = ''
        while not inp in cmd:
            inp = input('Config SYS > ')

        if inp == cmd[0]:
            already = False
            if param[0] == 'false' and not already:
               param[0] = 'true'
               cb.edit(param[0], param[1], param[2], param[3])
               already = True
            if param[0] == 'true' and not already:
                param[0] = 'false'
                cb.edit(param[0], param[1], param[2], param[3])
                already = True
        if inp == cmd[1]:
            param[1] = input('Config SYS > logfile path set > ')
            cb.edit(param[0], param[1], param[2], param[3])
        if inp == cmd[2]:
            already = False
            if param[2] == 'false' and not already:
               param[2] = 'true'
               cb.edit(param[0], param[1], param[2], param[3])
               already = True
            if param[2] == 'true' and not already:
               param[2] = 'false'
               cb.edit(param[0], param[1], param[2], param[3])
               already = True
        if inp == cmd[3]:
            already = False
            if param[3] == 'false' and not already:
               param[3] = 'true'
               cb.edit(param[0], param[1], param[2], param[3])
               already = True
            if param[3] == 'true' and not already:
               param[3] = 'false'
               cb.edit(param[0], param[1], param[2], param[3])
               already = True
        if inp == cmd[4]:
            print(hlp_msg)
        if inp == cmd[5]:
            print('Current config: \n  >log: ' + param[0] + '\n  >logfile: ' + param[1] + '\n  >bypass_shell_limit: ' + param[2] + '\n  >global_shell_var: ' + param[3] + '\n')
        if inp == cmd[6]:
            status = False
            break
