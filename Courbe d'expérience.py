# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 17:39:27 2017

@author: Wave Master
"""

#Expérience rapide

def ExpRap(N) :
    Exp=pow(N,3)*0.8
    return Exp


#Expérience normale

def ExpNor(N) :
    Exp=pow(N,3)
    return Exp


#Expérience lente

def ExpLen(N) :
    return pow(N,3)*1.25



#Expérience Parabolique

def ExpPar(N) :
    return pow(N,3)*1.2-pow(N,2)*15+N*100-140


#Expérience Erratique

def p(N) :
    if N%3==0 :
        return 0
    if N%3==1 :
        return 0.008
    if N%3==2 :
        return 0.014

def ExpEra(N) :
    if N<=50 :
        return pow(N,3)*((100-N)/50)
    if 51<=N<=68 :
        return pow(N,3)*((150-N)/100)
    if 69<=N<=98 :
        return pow(N,3)*(1.274-(1/50)*int(N/3)-p(N))
    if 99<=N :
        return pow(N,3)*((160-N)/100)


#Epérience Fluctuante

def ExpFlu(N) :
    if N<=15 :
        return pow(N,3)*((24+int((N+1)/3))/50)
    if 16<=N<=35 :
        return pow(N,3)*((14+N)/50)
    if 36<=N :
        return pow(N,3)*((32+int(N/2))/50)
