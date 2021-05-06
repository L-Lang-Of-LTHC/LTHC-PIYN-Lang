# -*- coding: utf-8 -*-

# ./utils/explorer.py  =>  contains explorer system

############
# IMPORTS
############
import libs.sys_methods as sm
import libs.var_lib as vl
import libs.libraries.binary.binary_sm as bsm

####################################################
def clear(mshell = 0):
    sm.varnlist = [vl.NumVar('DefaultNumVar_CreatedByLanguageSystem_00000000')]
    sm.varslist = [vl.StrVar('DefaultStrVar_CreatedByLanguageSystem_00000000')]
    sm.varsalist = [vl.StrVarAll('DefaultStrVarAll_CreatedByLanguageSystem_00000000')]
    sm.varflist = [vl.FuncVar('DefaultFuncVar_CreatedByLanguageSystem_00000000')]
    sm.varnames = ['DefaultNumVar_CreatedByLanguageSystem_00000000','DefaultStrVar_CreatedByLanguageSystem_00000000','DefaultStrVarAll_CreatedByLanguageSystem_00000000','DefaultFuncVar_CreatedByLanguageSystem_00000000']
    bsm.varb8list = [bsm.bvl.Bin8('DefaultBin8_CreatedByLanguageSystem_00000000')]
    bsm.varb16list = [bsm.bvl.Bin16('DefaultBin16_CreatedByLanguageSystem_00000000')]
    bsm.varb32list = [bsm.bvl.Bin32('DefaultBin32_CreatedByLanguageSystem_00000000')]
    bsm.initthis()
    if mshell != 0:
        print('\n  Variables Cleared  \n')

cmd = ['scan', 'clear', 'quit', 'help']
hlp_message = '\n  >>> help of \"Explorer SYS\" : \n       scan  : dispaly all current existing variables \n       clear : clear all current existing variables \n       help  : show this help message \n       quit  : quit the \"Explorer SYS\" \n'
def run():
    status = True
    while status:
        inp = ''
        while not inp in cmd:
            inp = input('Explorer SYS > ')
        
        if inp == cmd[0]:
            print(sm.scan())
        if inp == cmd[1]:
            clear()
            print('\n  Variables Cleared  \n')
        if inp == cmd[2]:
            status = False
            break
        if inp == cmd[3]:
            print(hlp_message)
