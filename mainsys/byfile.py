# -*- coding: utf-8 -*-

# ./mainsys/byfile.py  =>  contains by file programming system

############
# IMPORTS
############
import libs.readline as rl
import utils.explorer as ep

###############
# Claim file
###############

def run():
    wantedfile = ''
    wantedfile = input('File > ')
    if wantedfile.endswith('.llangl'):
        try:
            file = open(wantedfile, 'r+', encoding='utf-8')
            file.write('')
            tlines = file.readlines()
            file.close()

            lines = []
            for i in tlines:
                lines.append(i.replace('\n',''))

            ep.clear()

            for i in lines:
                try:
                    rl.readline(i, False)
                except:
                    print(f"\n  >>> An error blocks the normal behaviour of the program <<<  \n  >>> running file: {wantedfile} <<<\n  >>> Line: {i+1} <<<\n")
        except:
            print('\nFile not found\n')
    else:
        print('\nFile Extension Error: the extension must be \'.llang\'')

    t = None
    while t == None:
        t = input('')
