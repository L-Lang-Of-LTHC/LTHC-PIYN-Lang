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
    wantedfile = open(wantedfile)

    tlines = wantedfile.readlines()
    lines = []
    for i in tlines:
        lines.append(i.replace('\n',''))

    for i in lines:
        rl.readline(i, False)

    wantedfile.close()

    t = None
    while t == None:
        t = input('')
