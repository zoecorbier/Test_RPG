class player():
    def __init__(self, name):
        self.__name = name
        self.__pv = 1000
        self.__lvl = 1
        self.__etat = "vivants"

    def info(self):
        info = f"name: {self.__name:20}\npv: {self.__pv:6}\nlvl: {self.__lvl:2}\netat: {self.__etat:10}"
        print(info)

    def get_name(self):
        return self.__name

    def get_pv(self):
        return self.__pv

    def get_etat(self):
        return self.__etat

    def get_lvl(self):
        return self.__lvl

    def __set_pv(self, type = None, modif = None ):
        if (type == None):
            self.__pv = modif

        elif(type == "dmg"):
            self.__pv = self.__pv - modif

        elif(type == "heal"): 
             self.__pv = self.__pv + modif

    def __set_lvl(self, value):
        self.__lvl += value

    def __set_etat(self, new_etat):
        self.__etat = new_etat

    def attaque(self, target):
        dmg = self.__lvl

        if (dmg < target.get_pv()):
            target.__set_pv("dmg", dmg)
            print(f"{self.get_name()} inflige {dmg} dommages à {target.get_name()}")
        else:
            target.__set_pv(modif = 0)
            target.__set_etat("mort")
            self.__set_lvl(1)
            print(f"{target.get_name()} est mort sous les coups de {self.get_name()}")
            print(f"{self.get_name()} gagne 1 niveau")

    def heal(self, target):
        soin = self.get_lvl()

        if(target.get_etat() == "mort"):
            print("impossible de soigner les morts")
        
        else:

            if (target.get_pv() + soin >= 1000):
                print("le joueur a déjà tous ses points de vie")

                target.__set_pv(type=None, modif = 1000)
            else:
                target.__set_pv(type="heal", modif=soin)