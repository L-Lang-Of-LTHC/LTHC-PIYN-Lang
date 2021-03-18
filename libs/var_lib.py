# -*- coding: utf-8 -*-

# ./libs/var_lib.py  =>  contains vars definitions

##############
# CONSTANTS
##############

ALLOWED_CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,;?!:/\\\"\'`~#{([})]-_|*+-><&éèçà@^¨$£¤€=°êëîïôöâäûü ²'

#################
# Vars Classes
#################

# NumVar
class NumVar:
    def __init__(self,name,value=0):
        self.value = value
        self.name = name
    
    #GET METHOD
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    
    #SET METHOD
    def setValue(self,value):
        self.value = value
    def incValue(self):
        self.value += 1
    def decValue(self):
        self.value -= 1

# StrVar
class StrVar:
    def __init__(self, name, value=''):
        temp = ''
        for i in value:
            if i in ALLOWED_CHARS:
                temp += i
            else:
                temp += ''
        self.value = temp
        self.name = name
    
    #GET METHOD
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    
    #SET METHOD
    def setValue(self,value):
        temp = ''
        for i in value:
            if i in ALLOWED_CHARS:
                temp += i
            else:
                temp += ''
        self.value = temp
    def incValue(self):
        temp = ''
        for i in self.value:
            temp += ALLOWED_CHARS[(ALLOWED_CHARS.find(i)+1)%len(ALLOWED_CHARS)]
        self.value = temp
    def decValue(self):
        temp = ''
        for i in self.value:
            temp += ALLOWED_CHARS[(ALLOWED_CHARS.find(i)-1)%len(ALLOWED_CHARS)]
        self.value = temp

#StrVarAll
class StrVarAll:
    def __init__(self, name, value=''):
        self.value = value
        self.name = name
    
    #GET METHOD
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
    
    #SET METHOD
    def setValue(self,value):
        self.value = value
