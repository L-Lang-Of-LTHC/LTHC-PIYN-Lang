# -*- coding: utf-8 -*-

# ./mainsys/byfile.py  =>  contains by file programming system

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
    if wantedfile.endswith('.llangl'):
        try:
            wantedfile = open(wantedfile, 'r+', encoding='utf-8')
            wantedfile.write('')
            tlines = wantedfile.readlines()
            wantedfile.close()

            lines = []
            for i in tlines:
                lines.append(i.replace('\n',''))

            for i in lines:
                try:
                    rl.readline(i, False)
                except:
                    print('\n  >>> An error blocks the normal behaviour of the program <<<  \n')
                    print('\n >>>   ' + i + '   <<< \n')
        except:
            print('\nFile not found\n')
    else:
        print('\nFile Extension Error: the extension must be \'.llang\'')

    t = None
    while t == None:
        t = input('')
