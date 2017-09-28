# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 15:13:24 2017

@author: Wave Master
"""

import random as rd

def Damage(Prec,Puiss,N,Att,DefCi,CoefDeg,CoefCri) :
    k=rd.randint(0,200)
    if k>=Prec :
        print("Attaque échouée")
        Degats=0
    else :
        Degats=int((((N*0.4+2)*Att*Puiss)/(DefCi*50)+2)*(CoefDeg*rd.rand(0.85,1)))
        i=rd.randint(0,100)
        if i<=(15*CoefCri) :
            print("Coup critique !")
            Degats*=2
        if CoefDeg<1 :
            print("Ce n'est pas très efficace...")
        elif CoefDeg>1 :
            print("C'est super efficace !")
    return Degats

