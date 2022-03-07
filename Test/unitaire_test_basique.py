from Classes.personnage import player

player_1 = player("boby")
player_2 = player("toto")
player_3 = player("tutu")

#On vérifie que tous les personnages ont 1000 de point de vie au départ, un niveau 1 
print(player_1.info())
print(player_2.info())
print(player_3.info())

#On vérifie si les points de vie du joueur 2 diminu si le joueur 1 l'attaque
player_1.attaque(player_2)
print(player_2.info())


#On vérifie si les points de vie du joueur 2 augmente bien si le joueur 3 le soigne
player_3.heal(player_2)
print(player_2.info())

#On vérifie si quand le joueur 1 tue le joueur 2 il augmente son niveau 
for i in range (1, 1001,1):
    player_1.attaque(player_2)
print(player_1.info())
print(player_2.info())

#On vérifie que le joueur 2 ne peut pas être soigné car il est mort 
player_3.heal(player_2)

#On vérifie si un joueur ne peut pas avoir plus de 1000 points de vie 
player_3.heal(player_1)
