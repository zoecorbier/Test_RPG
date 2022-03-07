from Classes.personnage import player
import unittest

player_1 = player("boby")
player_2 = player("toto")
player_3 = player("tutu")

player_1.get_etat()
player_1.get_lvl()
player_1.get_pv()

class TestUnitaire(unittest.TestCase):

    #On vérifie que tous les personnages ont 1000 de point de vie au départ, un niveau 1 
    def test_creation(self):
        self.assertEqual(player_1.get_etat(),"vivant","Le joueur ne devrait pas être mort")
        self.assertEqual(player_1.get_lvl(),1,"Le level du joueur devrait être à 1")
        self.assertEqual(player_1.get_pv(),1000,"Le joueur devrait avoir 1000 pv")

    #On vérifie si les points de vie du joueur 2 diminu si le joueur 1 l'attaque
    def test_attaque(self):
        player_1.attaque(player_2)
        self.assertLess(player_2.get_pv(),1000,"Attention le joueur n'a pas perdu de Pv")

    #On vérifie si les points de vie du joueur 2 augmente bien si le joueur 3 le soigne
    def test_heal(self,old_pv=player_2.get_pv()):
        player_3.heal(player_2)
        self.assertGreaterEqual(old_pv,player_2.get_pv(),"Le joueur n'a pas gagné de la vie")

    #On vérifie si quand le joueur 1 tue le joueur 2 il augmente son niveau 
    def test_lvl(self,old_lv=player_2.get_lvl()):
        for i in range (1, 1001,1):
            player_1.attaque(player_2)
        self.assertGreater(old_lv,player_2.get_pv(),"Le joueur n'a pas gagné des niveaux")

    #On vérifie que le joueur 2 ne peut pas être soigné car il est mort 
    def test_mort_soin(self):
        self.assertIs(player_3.heal(player_2),'impossible de soigner les morts',"Le joueur a été soigné alors qu'il est mort")
    

    #On vérifie si un joueur ne peut pas avoir plus de 1000 points de vie 
    def test_pv_supp(self):
        player_3.heal(player_1)
        self.assertGreaterEqual(player_1.get_pv(),1000,"Le joueur a plus de 1000 points de vie")
    


if __name__ == '__main__':
    unittest.main()