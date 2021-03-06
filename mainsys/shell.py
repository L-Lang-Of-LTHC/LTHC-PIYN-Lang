# -*- coding: utf-8 -*-

# ./mainsys/shell.py  =>  contains shell system

############
# IMPORTS
############
import libs.readline as rl
from datetime import date as dt
import utils.help_shell as hlpsh

##########
# Shell
##########
hlp_msg = hlpsh.get_help()

def run(mode = 0):
    if mode == 0:
        ec = 'stop_shell'
        hlp = 'help_shell'
        status = True
        while status:
            sht = str(dt.today()) + ' :> Shell > '
            line = input(sht)
            if line == ec:
                status = False
                break
            if line == hlp:
                print(hlp_msg)
            if line != hlp:
                rl.readline(line, True)
        print('\n >>> Shell stopped <<< \n')

        t = None
        while t == None:
            t = input('')
    else:
        sht = str(dt.today()) + ' :> Shell > '
        print(sht)
        print('\n >>> Shell stopped <<< \n')
