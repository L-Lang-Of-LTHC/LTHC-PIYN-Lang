# -*- coding: utf-8 -*-

# ./libs/libraries/binary/var_lib.py  =>  contains binary library vars definitions

##############
# CONSTANTS
##############

BIN_CHAR = '01'

#################
# Vars Classes
#################

# Bin8
class Bin8:
    def __init__(self,name,value='00000000'):
        temp = ''
        for i in value:
            if i in BIN_CHAR:
                temp += i
            else:
                temp += ''
        if len(temp) < 8:
            for i in range(8-len(temp)):
                temp = '0' + temp
        if len(temp) > 8:
            temp = temp[-8:len(temp)]
        self.value = temp
        self.name = name
    
    #GET METHOD
    def getValue(self):
        return self.value
    def getValueNum(self):
        out = 0
        for i in range(len(self.value)):
            if self.value[i] == '1':
                out += 2**(8-i-1)
        return out
    def getName(self):
        return self.name
    
    #SET METHOD
    def setValue(self, value):
        temp = ''
        for i in value:
            if i in BIN_CHAR:
                temp += i
            else:
                temp += ''
        if len(temp) < 8:
            for i in range(8-len(temp)):
                temp = '0' + temp
        if len(temp) > 8:
            temp = temp[-8:len(temp)]
        self.value = temp
    def setValueNum(self, value):
        if value >= 2**8:
            self.value = '11111111'
        else:
            if type(value) == int:
                self.value = self.conversion(value)
                temp = self.value
                if len(temp) < 8:
                    for i in range(8-len(temp)):
                        temp = '0' + temp
                if len(temp) > 8:
                    temp = temp[-8:len(temp)]
                self.value = temp
            else:
                print('\nLibrary Error: Binary: The specify value must be an integer')
    
    #Usefull method
    def conversion(self, value):
        value = abs(value)
        temp = ''
        t = 0

        while value!=0:
            t = value%2
            temp += str(int(t))
            value = (value-t) / 2

        return temp[::-1]

# Bin16
class Bin16:
    def __init__(self,name,value='0000000000000000'):
        temp = ''
        for i in value:
            if i in BIN_CHAR:
                temp += i
            else:
                temp += ''
        if len(temp) < 16:
            for i in range(16-len(temp)):
                temp = '0' + temp
        if len(temp) > 16:
            temp = temp[-16:len(temp)]
        self.value = temp
        self.name = name
    
    #GET METHOD
    def getValue(self):
        return self.value
    def getValueNum(self):
        out = 0
        for i in range(len(self.value)):
            if self.value[i] == '1':
                out += 2**(16-i-1)
        return out
    def getName(self):
        return self.name
    
    #SET METHOD
    def setValue(self, value):
        temp = ''
        for i in value:
            if i in BIN_CHAR:
                temp += i
            else:
                temp += ''
        if len(temp) < 16:
            for i in range(16-len(temp)):
                temp = '0' + temp
        if len(temp) > 16:
            temp = temp[-16:len(temp)]
        self.value = temp
    def setValueNum(self, value):
        if value >= 2**16:
            self.value = '1111111111111111'
        else:
            if type(value) == int:
                self.value = self.conversion(value)
                temp = self.value
                if len(temp) < 16:
                    for i in range(16-len(temp)):
                        temp = '0' + temp
                if len(temp) > 16:
                    temp = temp[-16:len(temp)]
                self.value = temp
            else:
                print('\nLibrary Error: Binary: The specify value must be an integer')
    
    #Usefull method
    def conversion(self, value):
        value = abs(value)
        temp = ''
        t = 0

        while value!=0:
            t = value%2
            temp += str(int(t))
            value = (value-t) / 2

        return temp[::-1]

# Bin32
class Bin32:
    def __init__(self,name,value='00000000000000000000000000000000'):
        temp = ''
        for i in value:
            if i in BIN_CHAR:
                temp += i
            else:
                temp += ''
        if len(temp) < 32:
            for i in range(32-len(temp)):
                temp = '0' + temp
        if len(temp) > 32:
            temp = temp[-32:len(temp)]
        self.value = temp
        self.name = name
    
    #GET METHOD
    def getValue(self):
        return self.value
    def getValueNum(self):
        out = 0
        for i in range(len(self.value)):
            if self.value[i] == '1':
                out += 2**(32-i-1)
        return out
    def getName(self):
        return self.name
    
    #SET METHOD
    def setValue(self, value):
        temp = ''
        for i in value:
            if i in BIN_CHAR:
                temp += i
            else:
                temp += ''
        if len(temp) < 32:
            for i in range(32-len(temp)):
                temp = '0' + temp
        if len(temp) > 32:
            temp = temp[-32:len(temp)]
        self.value = temp
    def setValueNum(self, value):
        if value >= 2**32:
            self.value = '11111111111111111111111111111111'
        else:
            if type(value) == int:
                self.value = self.conversion(value)
                temp = self.value
                if len(temp) < 32:
                    for i in range(32-len(temp)):
                        temp = '0' + temp
                if len(temp) > 32:
                    temp = temp[-32:len(temp)]
                self.value = temp
            else:
                print('\nLibrary Error: Binary: The specify value must be an integer')
    
    #Usefull method
    def conversion(self, value):
        value = abs(value)
        temp = ''
        t = 0

        while value!=0:
            t = value%2
            temp += str(int(t))
            value = (value-t) / 2

        return temp[::-1]
