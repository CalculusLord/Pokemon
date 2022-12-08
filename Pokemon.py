import numpy as np
import pandas as pd
from Types import *

# def weakness(Pokemon):
#     weak = Pokemon.TYPE.WEAK
#     for i in weak:
#         if i in Pokemon.SUB_TYPE.RESIST:
#             weak.remove(i)
#     for i in Pokemon.SUB_TYPE.WEAK:
#         if i not in weak and i not in Pokemon.TYPE.RESIST:
#             weak.append(i)
#     return weak
#
# def resistance(Pokemon):
#     resist = Pokemon.TYPE.RESIST
#     for i in resist:
#         if i in Pokemon.SUB_TYPE.WEAK:
#             resist.remove(i)
#     for i in Pokemon.SUB_TYPE.RESIST:
#         if i not in resist and i not in Pokemon.TYPE.WEAK:
#             resist.append(i)
#     return resist

class Bulbasaur:
    def __init__(self, ID=0):
        self.NAME = 'Bulbasaur'
        self.DEX = 1
        self.ID = ID
        self.HP_BASE = 45
        self.ATK_BASE = 49
        self.DEF_BASE = 49
        self.SP_ATK_BASE = 65
        self.SP_DEF_BASE = 65
        self.SPE_BASE = 45
        self.TYPE = type['Grass']
        self.SUB_TYPE = type['Poison']
        # self.WEAKNESS = weakness(pokedex[self.DEX]())
        # self.RESISTANCE = resistance(pokedex[self.DEX]())
        # self.EVOLVE = Ivysaur()
        # self.MOVE_1 = self.FILE_PATH + '/move_1'
        # self.MOVE_2 = self.FILE_PATH + '/move_1'
        # self.MOVE_3 = self.FILE_PATH + '/move_1'
        # self.MOVE_4 = self.FILE_PATH + '/move_1'
        # self.NAME = file path
        # self.IV = dictionary with elements pointing to file path data
        # self.EV = dictionary with elements pointing to file path data
        # self.MAX_HP = ((2 * self.HP_BASE + self.IV['HP'] + (self.EV['HP'])) * self.LEVEL)/100 + self.LEVEL + 10

    # def nature(self):
    #     pokemon_ledger = pd.read_csv('pokemon_ledger.csv', header=None)
    #     i = 0
    #     while True:
    #         ID = pokemon_ledger[1][i]
    #         if ID == self.ID:
    #             return pokemon_ledger[2][i]
    #         i = i+1


# class Ivysaur:
#     def __init__(self, ID=None):
#         self.NAME = 'Ivysaur'
#         self.DEX = 2
#         self.ID = ID
#         self.HP_BASE = 60
#         self.ATK_BASE = 62
#         self.DEF_BASE = 63
#         self.SP_ATK_BASE = 80
#         self.SP_DEF_BASE = 80
#         self.SPE_BASE = 60
#         self.TYPE = type['Grass']
#         self.SUB_TYPE = type['Poison']
#         self.WEAKNESS = weakness(pokedex[self.DEX])
#         self.RESISTANCE = resistance(pokedex[self.DEX])
#         self.EVOLVE = Venusaur()
#         # self.MOVE_1 = self.FILE_PATH + '/move_1'
#         # self.MOVE_2 = self.FILE_PATH + '/move_1'
#         # self.MOVE_3 = self.FILE_PATH + '/move_1'
#         # self.MOVE_4 = self.FILE_PATH + '/move_1'
#         # self.NAME = file path
#         # self.IV = dictionary with elements pointing to file path data
#         # self.EV = dictionary with elements pointing to file path data
#         # self.MAX_HP = ((2 * self.HP_BASE + self.IV['HP'] + (self.EV['HP'])) * self.LEVEL)/100 + self.LEVEL + 10
#
#     # def nature(self):
#     #     pokemon_ledger = pd.read_csv('pokemon_ledger.csv', header=None)
#     #     i = 0
#     #     while True:
#     #         ID = pokemon_ledger[1][i]
#     #         if ID == self.ID:
#     #             return pokemon_ledger[2][i]
#     #         i = i+1
#
#
# class Venusaur:
#     def __init__(self, ID=None):
#         self.NAME = 'Venusaur'
#         self.DEX = 3
#         self.ID = ID
#         self.HP_BASE = 80
#         self.ATK_BASE = 82
#         self.DEF_BASE = 83
#         self.SP_ATK_BASE = 100
#         self.SP_DEF_BASE = 100
#         self.SPE_BASE = 80
#         self.TYPE = type['Grass']
#         self.SUB_TYPE = type['Poison']
#         self.WEAKNESS = weakness(pokedex[self.DEX])
#         self.RESISTANCE = resistance(pokedex[self.DEX])
#         self.EVOLVE = None
#         # self.MOVE_1 = self.FILE_PATH + '/move_1'
#         # self.MOVE_2 = self.FILE_PATH + '/move_1'
#         # self.MOVE_3 = self.FILE_PATH + '/move_1'
#         # self.MOVE_4 = self.FILE_PATH + '/move_1'
#         # self.NAME = file path
#         # self.IV = dictionary with elements pointing to file path data
#         # self.EV = dictionary with elements pointing to file path data
#         # self.MAX_HP = ((2 * self.HP_BASE + self.IV['HP'] + (self.EV['HP'])) * self.LEVEL)/100 + self.LEVEL + 10
#
#     # def nature(self):
#     #     pokemon_ledger = pd.read_csv('pokemon_ledger.csv', header=None)
#     #     i = 0
#     #     while True:
#     #         ID = pokemon_ledger[1][i]
#     #         if ID == self.ID:
#     #             return pokemon_ledger[2][i]
#     #         i = i+1
#
# class Squirtle:
#     def __init__(self, ID=0):
#         self.NAME = 'Squirtle'
#         self.DEX = 4
#         self.ID = ID
#         self.HP_BASE = 44
#         self.ATK_BASE = 48
#         self.DEF_BASE = 65
#         self.SP_ATK_BASE = 50
#         self.SP_DEF_BASE = 64
#         self.SPE_BASE = 43
#         self.TYPE = type['Water']
#         self.SUB_TYPE = None
#         self.WEAKNESS = weakness(pokedex[self.DEX])
#         self.RESISTANCE = resistance(pokedex[self.DEX])
#         # self.EVOLVE = Wartortle()
#         # self.MOVE_1 = self.FILE_PATH + '/move_1'
#         # self.MOVE_2 = self.FILE_PATH + '/move_1'
#         # self.MOVE_3 = self.FILE_PATH + '/move_1'
#         # self.MOVE_4 = self.FILE_PATH + '/move_1'
#         # self.NAME = file path
#         # self.IV = dictionary with elements pointing to file path data
#         # self.EV = dictionary with elements pointing to file path data
#         # self.MAX_HP = ((2 * self.HP_BASE + self.IV['HP'] + (self.EV['HP'])) * self.LEVEL)/100 + self.LEVEL + 10
#
#     # def nature(self):
#     #     pokemon_ledger = pd.read_csv('pokemon_ledger.csv', header=None)
#     #     i = 0
#     #     while True:
#     #         ID = pokemon_ledger[1][i]
#     #         if ID == self.ID:
#     #             return pokemon_ledger[2][i]
#     #         i = i+1
#
#
