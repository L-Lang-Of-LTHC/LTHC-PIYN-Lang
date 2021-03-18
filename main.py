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
cmd = ['file','shell','help','quit']
status = True
help_message = '\n  => command list:\n    file : run a file\n    shell : run a shell\n    help : show this help message\n    quit : close the main system "MAIN SYS"\n'

while status:
    inp = ''
    while not inp in cmd:
        inp = input('MAIN SYS > ')

    if inp == cmd[0]:
        bf.run()
    if inp == cmd[1]:
        sh.run()
    if inp == cmd[2]:
        print(help_message)
    if inp == cmd[3]:
        status = False
