from Classes.personnage import player

player_1 = player("boby")
player_2 = player("toto")
player_3 = player("tutu")


print(player_1.info())

print(player_2.info())

player_1.attaque(player_2)
print(player_2.info())

player_3.heal(player_2)
print(player_2.info())
print(player_3.info())




