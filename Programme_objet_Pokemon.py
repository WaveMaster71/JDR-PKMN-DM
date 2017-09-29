# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 08:06:53 2017

@author: Wave Master
"""

import random as rd

open("C:\Users\Wave Master\Desktop\RP PKMN DM\Gestion personnage\Courbe_d_experience.py")

class Pokemon :
    def __init__(self,**kwarg) :

        try : self.Nom = kwarg["Nom"]
        except KeyError :
            self.Nom = "Sansnom"
        try : self.Exp = kwarg["Exp"]
        except KeyError :
            self.Exp = 0
        try : self.N = kwarg["N"]
        except KeyError :
            self.N = 1
        
        try : self.PV = kwarg["PV"]
        except KeyError :
            self.PV = 5
        try : self.Atq = kwarg["Atq"]
        except KeyError :
            self.Atq = 1
        try : self.Def = kwarg["Def"]
        except KeyError :
            self.Def = 1
        try : self.AtS = kwarg["AtS"]
        except KeyError :
            self.AtS = 1
        try : self.DeS = kwarg["DeS"]
        except KeyError :
            self.DeS = 1
        try : self.Vit = kwarg["Vit"]
        except KeyError :
            self.Vit = 1
        
        try : self.Exp_courbe = kwarg["Exp_courbe"]
        except KeyError :
            self.Exp_courbe = ExpNor(self.N)
        
        try : self.VPV = kwarg["VPV"]
        except KeyError :
            self.VPV = 0
        try : self.VAtq = kwarg["VAtq"]
        except KeyError :
            self.VAtq = 0
        try : self.VDef = kwarg["VDef"]
        except KeyError :
            self.VDef = 0
        try : self.VAtS = kwarg["VAtQ"]
        except KeyError :
            self.VAtS = 0
        try : self.VDeS = kwarg["VDeS"]
        except KeyError :
            self.VDeS = 0
        try : self.VVit = kwarg["VVit"]
        except KeyError :
            self.VVit = 0
        
        try : self.AuPV = kwarg["AuPV"]
        except KeyError :
            self.AuPV = 0
        try : self.AuAtq = kwarg["AuAtq"]
        except KeyError :
            self.AuAtq = 0
        try : self.AuDef = kwarg["AuDef"]
        except KeyError :
            self.AuDef = 0
        try : self.AuAtS = kwarg["AuAtQ"]
        except KeyError :
            self.AuAtS = 0
        try : self.AuDeS = kwarg["AuDeS"]
        except KeyError :
            self.AuDeS = 0
        try : self.AuVit = kwarg["AuVit"]
        except KeyError :
            self.AuVit = 0

    def nivsup(self) :
        
        k=rd.randint(0,100)

        if k<self.VPV :
            self.AuPV+=1
        if k<self.VAtq :
            self.AuAtq+=1
        if k<self.VDef :
            self.AuDef+=1
        if k<self.VAtS :
            self.AuAtS+=1
        if k<self.VDeS :
            self.AuDeS+=1
        if k<self.VVit :
            self.AuVit+=1

        self.PV+=self.AuPV
        self.Atq+=self.AuAtq
        self.Def+=self.AuDef
        self.AtS+=self.AuDeS
        self.Vit+=self.AuVit
        
        return self.PV, self.Atq, self.Def, self.AtS, self.DeS, self.Vit
    
    def earn_Exp(self,ennemy,coeff=1) :
        self.Exp += coeff*Ennemy.ExpBase*(Ennemy.N/7)
        require_Exp = self.Exp_courbe((self.N)+1)
        while self.Exp >= require_Exp:
            self.N += 1
            require_Exp = self.Exp_courbe((self.N)+1)
            self.nivsup()