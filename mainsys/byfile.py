# -*- coding: utf-8 -*-

# ./mainsys/byfile.py  =>  contains by file programming system

############
# IMPORTS
############
import libs.readline as rl
import libs.sys_methods as sm

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

            libs = [0, 0]

            islibs = 0

            for i in lines:
                if i == '#LIBINC;' and islibs == 0:
                    islibs = 1
                if i == '#INC Random;' and islibs == 1:
                    libs[0] = 1
                if i == '#INC Binary;' and islibs == 1:
                    libs[1] = 1
                if i == '#ENDINC;' and islibs == 1:
                    break
            
            rl.initlibs(libs)

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
    sm.varnames = ['DefaultNumVar_CreatedByLanguageSystem_00000000','DefaultStrVar_CreatedByLanguageSystem_00000000','DefaultStrVarAll_CreatedByLanguageSystem_00000000','DefaultFuncVar_CreatedByLanguageSystem_00000000']
