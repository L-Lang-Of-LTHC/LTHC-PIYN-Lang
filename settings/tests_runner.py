# -*- coding: utf-8 -*-

# ./settings/tests_runner.py  =>  contains testing system

import libs.readline as rl
import utils.explorer as ep

test_list = ['tests/hello_world.llangl',
             'tests/test.llangl',
             'tests/test2.llangl',
             'tests/test3.llangl',
             'tests/test4.llangl',
             'tests/test5.llangl',
             'tests/test6.llangl',
             'tests/test7.llangl',
             'tests/test8.llangl',
             'tests/testA.llangl',
             'tests/testB.llangl',
             'tests/testC.llangl',
             'tests/testD.llangl',
             'tests/testE.llangl',
             'tests/testF.llangl',
             'tests/testG.llangl',
             'tests/testH.llangl',
             'tests/testI.llangl',
             'tests/testJ.llangl',
             'tests/testK.llangl',
]

def run():
    error = 0
    wantedfile = ''
    for file_from_all in test_list:
        wantedfile = file_from_all
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
                        rl.readline(i, False, 1)
                    except:
                        error += 1
                        print(f"\n  >>> An error blocks the normal behaviour of the program <<<  \n  >>> running file: {wantedfile} <<<\n  >>> Line: {i+1} <<<\n")
                print('\n' + wantedfile + ' tested\n')
            except:
                print('\nFile not found\n')
        else:
            print('\nFile Extension Error: the extension must be \'.llang\'')
    
    print('On all tested files, error found: ' + str(error))
