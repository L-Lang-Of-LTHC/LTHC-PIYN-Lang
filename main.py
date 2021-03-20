# -*- coding: utf-8 -*-

# ./main.py  =>  contains main system

############
# IMPORTS
############
import mainsys.byfile as bf
import mainsys.shell as sh
import utils.explorer as ep

###########
# System
###########
cmd = ['file','shell','help','quit','explorer']
status = True
help_message = '\n  => command list:\n                  file  : run a file\n                  shell : run a shell\n                  help  : show this help message\n                  quit  : close the main system "MAIN SYS"\n'
help_message += '\n       Shell command list:\n                            help_shell : show the help message of the shell if you are in shell\n                            stop_shell : quit the shell if you are in shell\n'
help_message += '\n  >>> Other \"MAIN SYS\" command:\n                               explorer : open the \"Explorer SYS\"\n'

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
    if inp == cmd[4]:
        ep.run()
