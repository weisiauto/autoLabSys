# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import time as t

class MyTimer:
    
    def __init__(self):
        self.unit=['year','month','day','hour','minite','sencond']
        self.prompt="Not started!\n"
        self.lasted=[]
        self.start=0
        self.stop=0
    
    def begin(self):
        self.start=t.localtime()
        print("Timer started\n")
        
    def end(self):
        self.stop= t.localtime()
        self._calc()
        print("Timer stopped\n")
    
    def _calc(self):
        self.lasted=[]
        self.prompt="It worked\n"
        for index in range(6):
            self.lasted.append(self.stop[index]-self.start[index])
            self.prompt+=str(self.lasted[index])+self.unit[index]
        print(self.prompt)
    def __str__(self):
        return self.prompt
    __repr__=__str__
    

if __name__=='__main__':
    t1=MyTimer()
    t1
    t1.begin()
    t.sleep(5)
    t1.end()
    assert t1.lasted[5]==5
    