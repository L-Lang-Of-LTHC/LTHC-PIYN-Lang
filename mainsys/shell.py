# -*- coding: utf-8 -*-

# ./mainsys/shell.py  =>  contains shell system

############
# IMPORTS
############
import libs.readline as rl
from datetime import date as dt

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

def run():
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
