#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 13:49:50 2017

@author: weizy
"""

from Equipment import Load

def CalLoad(VoltageRange,CurrentRange,CosRange):
    loadlist=[]
    for voltage in VoltageRange:
        for current in CurrentRange:
            for cos in CosRange:
               loadlist.append(Load(voltage,current,cos))
    return loadlist

def LoadRange(loadlist):
    loadrange={
            "xlmin":0,
            "xlmax":0,
            "xrmin":0,
            "xrmax":0,
            }
    if len(loadlist)>=1:
        loadrange["xlmin"]=loadlist[0].Xl
        loadrange["xlmax"]=loadlist[0].Xl
        loadrange["xrmin"]=loadlist[0].Xr
        loadrange["xrmax"]=loadlist[0].Xr
        for load in loadlist:
            if load.Xl<loadrange["xlmin"]:
                loadrange["xlmin"]=load.Xl
            if load.Xl>loadrange["xlmax"]:
                loadrange["xlmax"]=load.Xl
            if load.Xr<loadrange["xrmin"]:
                loadrange["xrmin"]=load.Xr
            if load.Xr>loadrange["xrmax"]:
                loadrange["xrmax"]=load.Xr
    return loadrange
        

if __name__=='__main__':
    voltages=[24,800]
    currents=[7,100]
    coss=[0.25,0.95]
    loads=CalLoad(voltages,currents,coss)
    for load in loads:
        print(str(load))
    lrrange=LoadRange(loads)
    for key in lrrange:
        print("%s value is:%10.3f ohm" % (key,lrrange[key]))