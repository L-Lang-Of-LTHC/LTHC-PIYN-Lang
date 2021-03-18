# -*- coding: utf-8 -*-

# ./byfile.py  =>  contains by file programming system

############
# IMPORTS
############
import libs.readline as rl

###############
# Claim file
###############

def run():
    wantedfile = ''
    wantedfile = input('File > ')
    try:
        wantedfile = open(wantedfile, 'r', encoding='utf-8')

        tlines = wantedfile.readlines()
        lines = []
        for i in tlines:
            lines.append(i.replace('\n',''))

        for i in lines:
            rl.readline(i, False)

        wantedfile.close()
    except:
        print('\nFile not found\n')

    t = None
    while t == None:
        t = input('')
