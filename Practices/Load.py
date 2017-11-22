import math
class Load:
    '''
    This class includes all necessory values of load calculation

    '''
    # init function to accept value list
    def __init__(self, voltages=[], currents=[], coss=[], step=0.04):
        self._voltages=voltages
        self._currents=currents
        self._coss=coss
        self._step=step
        self._loadrange=[]
        self._loadxl=[]
        self._loadl=[]
        self._loadxr=[]

    def _formatFloat(self, f):
        return(float("%.4f"%f))
    
    def _calcConfig(self, mins, maxs, starts):
        conf=[starts,  ]
        sums=0.0
        tmp=0.0
        while(sums<maxs):
            tmp=self._formatFloat(conf[(len(conf)-1)])
            sums+=tmp*3
            if(sums>=maxs):
                break
            conf.append(tmp*4)
        return conf
            
    # calculate sin value from cos
    def _calcSin(self, cos):
        return math.sqrt(1-cos**2)
    
    # calculate entire load value from voltage and current
    def _calcLoadValue(self, voltage, current):
        return 0 if current==0 else self._formatFloat(voltage/current)
        
    # calculate Xl from entire LoadValue    
    def _calcXl(self, loadValue, cos):
       return self._formatFloat(loadValue*cos)
       
    # calculate Xr from entire LoadValue
    def _calcXr(self, loadValue, cos):
        sin=self._calcSin(cos)
        return self._formatFloat(loadValue*sin)
    
    
    #calculate range value
    def _calcLoadRange(self):
        #self._loadrange.extend(map(self._calcLoadValue, self._voltages, self._currents))
        #self._loadxl=map(self._calcXl, self._loadrange, self._coss)
        #self._loadxr=map(self._calcXr, self._loadrange, self.__coss)
        for v in self._voltages:
            for i in self._currents:
                    self._loadrange.append(self._calcLoadValue(v, i))
        
        for x in self._loadrange:
            for c in self._coss:
                self._loadxl.append(self._calcXl(x, c))
                self._loadxr.append(self._calcXr(x, c))
                
        self._loadrange=[min(self._loadrange), max(self._loadrange)]
        self._loadxl=[min(self._loadxl), max(self._loadxl)]
        self._loadxr=[min(self._loadxr), max(self._loadxr)]
    
    
    
    def getLoadRange(self):
        if self._loadrange==[]:
            self._calcLoadRange()
        return self._loadrange

    
    def getLoadxlRange(self):
        if self._loadrange==[]:
            self._calcLoadRange()
        return self._loadxl

    def getLoadlRange(self, f=50):
        if self._loadrange==[]:
            self._calcLoadRange()
        for xl in self._loadxl:
            self._loadl.append(self._formatFloat(xl/(2*math.pi*f)))
        return self._loadl
        
    def getLoadxrRange(self):
        if self._loadrange==[]:
            self._calcLoadRange()
        return self._loadxr

    def getconfs(self, toget):
        if toget==[]:
            return []
        else:            
            self.getLoadRange()
            mins=min(toget)
            maxs=max(toget)
            return self._calcConfig(mins, maxs, mins)

def callForLoad(voltages, currents, coss):
    load=Load(voltages, currents, coss)
    print("The Reactor Load Value (H) Range:")
    print(load.getLoadlRange())
    print("The Resistor Load Value (Ohm) Range:")
    print(load.getLoadxrRange())
    print("The Reactor Configuration, 3 taps for each value, except for last value:")   
    print(load.getconfs(load.getLoadlRange()))
    print("The Resistort Configuration, 3 for each value, except for last value:")   
    print(load.getconfs(load.getLoadxrRange()))
    
if __name__=='__main__':
    callForLoad(voltages=[24, 800], currents=[7, 100], coss=[0.25, 0.95])
    callForLoad(voltages=[24, 800], currents=[0.7, 10], coss=[0.25, 0.95])
