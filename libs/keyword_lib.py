# -*- coding: utf-8 -*-

# ./libs/keyword_lib.py  =>  contains default method for analyze instructions keywords

def hasKeyWord(line, keyword):
    if line[0:len(keyword)] == keyword: 
        return True
    else: 
        return False

def endLineRespected(line):
    if len(line) > 0:
        if line[-1] in ';^': 
            return True
        else: 
            print('Expected \';\' or \'^\' at the end of the following line: \n  >> ' + line + ' << \n')
            return False
