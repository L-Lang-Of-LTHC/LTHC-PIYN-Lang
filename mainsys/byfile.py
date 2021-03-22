# -*- coding: utf-8 -*-

# ./mainsys/byfile.py  =>  contains by file programming system

############
# IMPORTS
############
import libs.readline as rl
import utils.logger_utils as lgu

###############
# Claim file
###############

def run(logstate, logfile):
    wantedfile = ''
    wantedfile = input('File > ')
    out = []
    try:
        wantedfile = open(wantedfile, 'r', encoding='utf-8')

        tlines = wantedfile.readlines()

        wantedfile.close()

        lines = []
        for i in tlines:
            lines.append(i.replace('\n',''))

        for i in lines:
            try:
                if logstate == 'true':
                    out.append(rl.readline(i, False, logstate, logfile))
                    if len(out) >= 25:
                        msg_out = ''
                        for i in out:
                            msg_out += i + '\n'
                        lgu.log(logfile, msg_out)
                        out = []
                    else:
                        rl.readline(i, False, logstate, logfile)
            except:
                print('\n  >>> An error blocks the normal behaviour of the program <<<  \n')

    except:
        print('\nFile not found\n')

    if logstate == 'true':
        msg_out = ''
        for i in out:
            msg_out += i + '\n'
        lgu.log(logfile, msg_out)
        out = []

    t = None
    while t == None:
        t = input('')
