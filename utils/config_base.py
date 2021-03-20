# -*- coding: utf-8 -*-

# ./utils/config_base.py  =>  contains config system

def read():
    try:
        f = open('utils/config.txt','r')
        lines = f.readlines()
        f.close()
        l = lines[0].replace('\n','')
        l2 = lines[1].replace('\n','')
        bsl = lines[2].replace('\n','')
        gsv = lines[3].replace('\n','')
        return (l,l2,bsl,gsv)
    except:
        print('\n  No config file finded  \n')
        return ('false','log_default.txt','false','true')

def edit(_log, _logfile, _bypass_shell_limit, _global_shell_var):
    try:
        lines = _log + '\n' + _logfile + '\n' + _bypass_shell_limit + '\n' + _global_shell_var
        f = open('utils/config.txt','w')
        f.write(lines)
        f.close()
    except:
        print('\n  No config file finded  \n')
