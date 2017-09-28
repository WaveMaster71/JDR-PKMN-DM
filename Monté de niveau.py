# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 18:23:50 2017

@author: Wave Master
"""

def NivSup() :
    import random as rd

    PV=int(input("PV de base : "))
    Atq=int(input("Attaque de base : "))
    Def=int(input("Defense de base : "))
    AtS=int(input("Attaque Special de base : "))
    DeS=int(input("Defense Special de base : "))
    Vit=int(input("Vitesse de base : "))
    Stat=[PV,Atq,Def,AtS,DeS,Vit]
    print

    VPV=int(input("Taux de variation des PV : "))
    VAtq=int(input("Taux de variation de l'Attaque : "))
    VDef=int(input("Taux de variation de la Deffense : "))
    VAtS=int(input("Taux de variation de l'Attaque Speciale : "))
    VDeS=int(input("Taux de variation de la Defense Speciale : "))
    VVit=int(input("Taux de variation de la Vitesse : "))
    print

    k=rd.randint(0,100)

    AuPV=int(input("Augmentation minimale des PV : "))
    if k<VPV :
        AuPV+=1
    AuAtq=int(input("Augmentation minimale de l'Attaque : "))
    if k<VAtq :
        AuAtq+=1
    AuDef=int(input("Augmentation minimale de la Defense : "))
    if k<VDef :
        AuDef+=1
    AuAtS=int(input("Augmentation minimale de l'Attaque Speciale : "))
    if k<VAtS :
        AuAtS+=1
    AuDeS=int(input("Augmentation minimale de la Defense Special : "))
    if k<VDeS :
        AuDeS+=1
    AuVit=int(input("Augmentation minimale de la Vitesse : "))
    if k<VVit :
        AuVit+=1
    AuStat=[AuPV,AuAtq,AuDef,AuAtS,AuDeS,AuVit]

    for i in range(0,len(Stat)) :
        Stat[i]+=AuStat[i]

    return Stat