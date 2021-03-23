# -*- coding: utf-8 -*-

# ./utils/linker.py  =>  contains file linking system

############
# IMPORTS
############
import libs.readline as rl

def link(file, mode, param=None):
    if mode == 0: #FCALL et NE, LT, GT, EQ
        run(file)
    if mode == 1: #LOOP
        for i in range(param):
            run(file)

def run(file):
    try:
        wanted = open(file, 'r', encoding='utf-8')
        tlines = wanted.readlines()
        wanted.close()

        lines = []
        for i in tlines:
            lines.append(i.replace('\n',''))

        for i in lines:
            try:
                rl.readline(i, False)
            except:
                print('\n  >>> An error blocks the normal behaviour of the program <<<  \n')
    except:
        print('\nFile not found\n')
