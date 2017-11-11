# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 17:17:01 2017

@author: weizy
"""

class Celsius:
    def __init__(self,value=26.0):
        self.value=float(value)
    def __get__(self,instance,owner):
        return self.value
    def __set__(self,instance,value):
        self.value=float(value)
    
class Fahrenheit:
    def __get__(self,instance,owner):
        return instance.cel * 1.8+32
    def __set__(self,instance,value):
        instance.cel=(float(value)-32)/1.8

class Temperature:
    cel=Celsius()
    fah=Fahrenheit()

if __name__=='__main__':
    temp=Temperature()
    assert temp.cel==26.0
    assert temp.fah==78.80000000000001