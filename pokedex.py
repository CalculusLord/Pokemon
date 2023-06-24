#   -----------------------------------
#   Written by Nathanael J. Reynolds
#   name = Pokedex
#   version = 1.0
#   version_year = 2023
#   Description: Creates Pokemon object
#   used in Pokemon Match
#   -----------------------------------
#   Version Changelog
#   2023-06-24: First 9 Pokemon of the
#   Pokedex added
#   -----------------------------------

from pkmn_type import *


class Pokemon:
    def __init__(self, main_type, sub_type):
        """
        This class defines a pokemon using pkmn_type.pkmn_type
        :param main_type: class
        :param sub_type: class
        """
        self.what_type = main_type.name.union(sub_type.name)
        self.weak = main_type.weak.difference(
            sub_type.resist.union(sub_type.immune)).union(
            sub_type.weak.difference(main_type.resist.union(main_type.immune))
        )
        self.resist = main_type.resist.difference(sub_type.weak).union(
            sub_type.resist.difference(main_type.weak)
        )
        self.immune = main_type.immune.union(sub_type.immune)


#   --------------------
#   Pokedex Pokemon
#   --------------------
class Bulbasaur(Pokemon):
    def __init__(self, main_type=pkmn_type['grass'], sub_type=pkmn_type['poison']):
        super().__init__(main_type, sub_type)
        self.name = 'Bulbasaur'
        self.dex = 1
        self.hp = 45
        self.attack = 49
        self.defense = 49
        self.sp_attack = 65
        self.sp_defense = 65
        self.speed = 45
        self.total = self.hp + self.attack + self.defense + self.sp_attack + self.sp_defense + self.speed
        self.evolve = Ivysaur()


class Ivysaur(Pokemon):
    def __init__(self, main_type=pkmn_type['grass'], sub_type=pkmn_type['poison']):
        super().__init__(main_type, sub_type)
        self.name = 'Ivysaur'
        self.dex = 2
        self.hp = 60
        self.attack = 62
        self.defense = 63
        self.sp_attack = 80
        self.sp_defense = 80
        self.speed = 60
        self.total = self.hp + self.attack + self.defense + self.sp_attack + self.sp_defense + self.speed
        self.evolve = Venusaur()


class Venusaur(Pokemon):
    def __init__(self, main_type=pkmn_type['grass'], sub_type=pkmn_type['poison']):
        super().__init__(main_type, sub_type)
        self.name = 'Venusaur'
        self.dex = 3
        self.hp = 80
        self.attack = 82
        self.defense = 83
        self.sp_attack = 100
        self.sp_defense = 100
        self.speed = 80
        self.total = self.hp + self.attack + self.defense + self.sp_attack + self.sp_defense + self.speed


class Squirtle(Pokemon):
    def __init__(self, main_type=pkmn_type['water'], sub_type=pkmn_type['none']):
        super().__init__(main_type, sub_type)
        self.name = 'Squirtle'
        self.dex = 4
        self.hp = 44
        self.attack = 48
        self.defense = 65
        self.sp_attack = 50
        self.sp_defense = 64
        self.speed = 43
        self.total = self.hp + self.attack + self.defense + self.sp_attack + self.sp_defense + self.speed
        self.evolve = Wartortle()


class Wartortle(Pokemon):
    def __init__(self, main_type=pkmn_type['water'], sub_type=pkmn_type['none']):
        super().__init__(main_type, sub_type)
        self.name = 'Wartortle'
        self.dex = 5
        self.hp = 59
        self.attack = 63
        self.defense = 80
        self.sp_attack = 65
        self.sp_defense = 80
        self.speed = 58
        self.total = self.hp + self.attack + self.defense + self.sp_attack + self.sp_defense + self.speed
        self.evolve = Blastoise()


class Blastoise(Pokemon):
    def __init__(self, main_type=pkmn_type['water'], sub_type=pkmn_type['none']):
        super().__init__(main_type, sub_type)
        self.name = 'Blastoise'
        self.dex = 6
        self.hp = 79
        self.attack = 83
        self.defense = 100
        self.sp_attack = 85
        self.sp_defense = 105
        self.speed = 78
        self.total = self.hp + self.attack + self.defense + self.sp_attack + self.sp_defense + self.speed


class Charmander(Pokemon):
    def __init__(self, main_type=pkmn_type['fire'], sub_type=pkmn_type['none']):
        super().__init__(main_type, sub_type)
        self.name = 'Charmander'
        self.dex = 7
        self.hp = 39
        self.attack = 52
        self.defense = 43
        self.sp_attack = 60
        self.sp_defense = 50
        self.speed = 65
        self.total = self.hp + self.attack + self.defense + self.sp_attack + self.sp_defense + self.speed
        self.evolve = Charmeleon()


class Charmeleon(Pokemon):
    def __init__(self, main_type=pkmn_type['fire'], sub_type=pkmn_type['none']):
        super().__init__(main_type, sub_type)
        self.name = 'Charmeleon'
        self.dex = 8
        self.hp = 58
        self.attack = 64
        self.defense = 58
        self.sp_attack = 80
        self.sp_defense = 65
        self.speed = 80
        self.total = self.hp + self.attack + self.defense + self.sp_attack + self.sp_defense + self.speed
        self.evolve = Charizard()


class Charizard(Pokemon):
    def __init__(self, main_type=pkmn_type['fire'], sub_type=pkmn_type['flying']):
        super().__init__(main_type, sub_type)
        self.name = 'Charizard'
        self.dex = 9
        self.hp = 78
        self.attack = 84
        self.defense = 78
        self.sp_attack = 109
        self.sp_defense = 85
        self.speed = 100
        self.total = self.hp + self.attack + self.defense + self.sp_attack + self.sp_defense + self.speed


#   -------------
#   Pokedex
#   -------------
pokedex = {
    'Bulbasaur': Bulbasaur(),
    1: Bulbasaur(),
    'Ivysaur': Ivysaur(),
    2: Ivysaur(),
    'Venusaur': Venusaur(),
    3: Venusaur(),
    'Squirtle': Squirtle(),
    4: Squirtle(),
    'Wartortle': Wartortle(),
    5: Wartortle(),
    'Blastoise': Blastoise(),
    5: Blastoise(),
    'Charmander': Charmander(),
    7: Charmander(),
    'Charmeleon': Charmeleon(),
    8: Charmeleon(),
    'Charizard': Charizard(),
    9: Charizard()
}
