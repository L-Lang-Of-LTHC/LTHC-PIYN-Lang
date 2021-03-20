# -*- coding: utf-8 -*-

# ./utils/logger_utils.py  =>  contains logging system

def initl(file):
    f = open(file,'x')
    f.close()

def log(file,msg):
    try:
        f = open(file,'r',encoding='utf-8')
        t = f.readlines()
        f.close
        temp = ''
        for a in t:
            temp += a
        f = open(file,'w',encoding='utf-8')
        f.write(temp + msg + '\n')
        f.close()
    except:
        print('\n  LOG ERROR  \n')
