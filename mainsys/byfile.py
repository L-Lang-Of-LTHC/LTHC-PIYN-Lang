# -*- coding: utf-8 -*-

# ./mainsys/byfile.py  =>  contains by file programming system

############
# IMPORTS
############
import libs.readline as rl

###############
# Claim file
###############

def run(logstate, logfile):
    wantedfile = ''
    wantedfile = input('File > ')
    try:
        wantedfile = open(wantedfile, 'r', encoding='utf-8')

        tlines = wantedfile.readlines()

        wantedfile.close()

        lines = []
        for i in tlines:
            lines.append(i.replace('\n',''))

        for i in lines:
            try:
                rl.readline(i, False, logstate, logfile)
            except:
                print('\n  >>> An error blocks the normal behaviour of the program <<<  \n')

    except:
        print('\nFile not found\n')

    t = None
    while t == None:
        t = input('')
