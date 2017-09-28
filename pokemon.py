#!usr/bin/env python3.4
#-*-coding:utf-8-*-
#pokemon object

from Courbe_d_experience import *
import random

class Pokemon:
    def __init__(self,**kwarg):
        try: self.PV = kwarg["PV"]
        except KeyError: self.PV = 1
        #autres stats à calquer sur ce modèle ci-dessus
        try: self.xp_courb = kwarg["xp_courb"]
        except KeyError: self.xp_courb = ExpNor
        self.xp = 0
        self.level = 0

    def nivsup (self):
        #importé depuis Monte_de_niveau.py
        #contient des erreur (lignes print)
        #convertir le code en remplaçant les variables par les attributs de l'objet
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

    def earn_xp(self):
        self.xp += self.xp_courb(self.level)
        #conditions de changement de level à placer
