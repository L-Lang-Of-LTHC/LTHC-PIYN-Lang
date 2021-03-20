# -*- coding: utf-8 -*-

# ./main.py  =>  contains main system

############
# IMPORTS
############
import mainsys.byfile as bf
import mainsys.shell as sh
import utils.explorer as ep
import utils.config_base as cb
import utils.config_sys as cs
import utils.logger_utils as lgu

###########
# System
###########
cmd = ['file','shell','help','quit','explorer','config']
status = True
help_message = '\n  => command list:\n                  file  : run a file\n                  shell : run a shell\n                  help  : show this help message\n                  quit  : close the main system "MAIN SYS"\n'
help_message += '\n       Shell command list:\n                            help_shell : show the help message of the shell if you are in shell\n                            stop_shell : quit the shell if you are in shell\n'
help_message += '\n  >>> Other \"MAIN SYS\" command:\n                               explorer : open the \"Explorer SYS\"\n                               config : open the \"Config SYS\"\n'

log, logfile, bypass_shell_limit, global_shell_var = cb.read()
print('Current config: \n  >log: ' + log + '\n  >logfile: ' + logfile + '\n  >bypass_shell_limit: ' + bypass_shell_limit + '\n  >global_shell_var: ' + global_shell_var + '\n')
lgu.initl(logfile)
print('\n\n Type help for show the help message \n\n')

while status:
    inp = ''
    while not inp in cmd:
        inp = input('MAIN SYS > ')

    if inp == cmd[0]:
        bf.run(log,logfile)
    if inp == cmd[1]:
        sh.run(global_shell_var,log,logfile)
    if inp == cmd[2]:
        print(help_message)
    if inp == cmd[3]:
        status = False
    if inp == cmd[4]:
        ep.run()
    if inp == cmd[5]:
        cs.run([log, logfile, bypass_shell_limit, global_shell_var])
        log, logfile, bypass_shell_limit, global_shell_var = cb.read()
