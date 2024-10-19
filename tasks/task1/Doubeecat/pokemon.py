import random

class Pokemon :
    #values:name HP type atk defe evr effects[]
    def __init__(self,name,hp,type,atk,defe,evr):
        self.name = name
        self.hp = hp
        self.type = type
        self.atk = atk
        self.defe = defe
        self.evr = evr
        self.effects = []

    def defdamage(self,damage):
        # 伤害 = 伤害 - 防御
        nowdmg = max(0,damage - self.defe)
        self.hp = max(0,self.hp - nowdmg)
        return nowdmg

    def judgefainted(self):
        return self.hp <= 0
    
    def applyeffects(self,effect):
        self.effects.append(effect)
    
    def undoeffects(self,effect):
        self.effects.remove(effect)
    
    def endofturn(self):
        self.effects.clear()
    

class WaterPokemon(Pokemon):
    def __init__(self,name,hp,atk,defe,evr):
        super().__init__(name,hp,"water",atk,defe,evr)
    
    def defdamage(self,damage):
        val = random.random()
        typ = 0
        if val <= 0.5:
            typ = 1
        if typ == 0:
            return self.defdamage(self,damage)
        else:
            return 0
        pass

    
