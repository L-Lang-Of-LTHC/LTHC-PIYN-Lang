# -*- coding: utf-8 -*-

# ./settings/checker.py  =>  contains checking system

_version_state = '[DEV]'
_version_num = '0.0.1'
_version_subnum = 'b'
_version_release_date = 'y2021/m04/d27'

_libs_list = 'Random, Binary'

_software_name = '[L Lang of LTHC] startingBlock'

_code_extension = '.llangl'

def print_info():
    print('\n  Version: ' + _version_state + ':' + _version_num + ':' + _version_subnum + ':' + _version_release_date + '\n  Current Software Name: ' + _software_name + '\n  Extension: ' + _code_extension + '\n  Current Usable Libs: ' + _libs_list)
