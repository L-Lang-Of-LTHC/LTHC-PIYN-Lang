# -*- coding: utf-8 -*-

# ./shell.py  =>  contains shell system

############
# IMPORTS
############
import libs.readline as rl
from datetime import date as dt

##########
# Shell
##########

ec = 'stop_shell'
status = True
while status:
    sht = str(dt.today()) + ' :> Shell > '
    line = input(sht)
    if line == ec:
        status = False
        break
    rl.readline(line, True)

print('\n >>> Shell stopped <<< \n')
