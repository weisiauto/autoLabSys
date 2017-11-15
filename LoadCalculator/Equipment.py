#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 12:08:42 2017

@author: weizy

Load is a base class of all equipments,the class contains Xl and Xr which
are important parameters for electrical test laboratory

A load need proper working voltage, current and cos value to calculate Xl and Xr
"""
import math

class Load: # A base class of load
 
        
    def __init__(self,Voltage=220.0,Current=1.0,Cos=1.0): 
        self.Voltage=Voltage
        self.Current=Current
        self.Cos=Cos
        
    
    @property
    def _Zx(self):
        if self.Current!=0:
            return self.Voltage/self.Current
        else:
            return 0
    
    @property
    def _Sin(self):
        if self.Cos<=1:
            return math.sqrt(1-self.Cos**2)
        else:
            return 0
        
    @property
    def Xl(self):
        return self._Zx*self.Cos
    
    @property
    def Xr(self):
        return self._Zx*self._Sin
    
    
    def __repr__(self):
        return "Equipment Xl={0.Xl!r},Xr={0.Xr!r}".format(self)
    
    def __str__(self):
        return "Equipment Xl={0.Xl!r},Xr={0.Xr!r}".format(self)


class LoadRangeCalculate:# assistant class for load calculation
    
    def __init__(self,VoltageRange=[],CurrentRange=[],CosRange=[]):
        self._VoltageRange=VoltageRange
        self._CurrentRange=CurrentRange
        self._CosRange=CosRange
        self._loadlist=[]
        self._grpValue=3
    
    def _CalLoad(self):
        for voltage in self._VoltageRange:
            for current in self._CurrentRange:
                for cos in self._CosRange:
                   self._loadlist.append(Load(voltage,current,cos))
                   
    @staticmethod
    def xlTol(freq,xl):
        return xl/(2*math.pi*freq)
    
    @staticmethod
    def lToxl(freq,l):
        return 2*math.pi*freq*l 
    
    @property
    def loadrange(self):
        self._CalLoad()
        lvalues=[float(xl.Xl) for xl in self._loadlist]
        rvalues=[float(xr.Xr) for xr in self._loadlist]
        return {
                "xlmin":min(lvalues),
                "xlmax":max(lvalues),
                "xrmin":min(rvalues),
                "xrmax":max(rvalues),
                }


            


if __name__=='__main__':
    voltages=[24,800]
    currents=[7,100]
    currents2=[0.7,10]
    coss=[0.25,0.95]
    loads=LoadRangeCalculate(voltages,currents,coss)
    loads2=LoadRangeCalculate(voltages,currents2,coss)
    for key in loads.loadrange:
        print("%s value is:%10.3f ohm" % (key,loads.loadrange[key]))
    for key in loads2.loadrange:
        print("%s value is:%10.3f ohm" % (key,loads2.loadrange[key]))
        
    