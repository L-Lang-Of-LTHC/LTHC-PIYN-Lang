# -*- coding: utf-8 -*-

# ./main.py  =>  contains main system

############
# IMPORTS
############
import byfile as bf
import shell as sh

###########
# System
###########
cmd = ['file','shell']
inp = ''
while not inp in cmd:
    inp = input('MAIN SYS > ')

if inp == cmd[0]:
    bf.run()
if inp == cmd[1]:
    sh.run()
