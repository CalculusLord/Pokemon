#   -----------------------------------
#   Written by Nathanael J. Reynolds
#   name = Pokemon Types
#   version = 1.0
#   version_year = 2023
#   Description: Creates objects used
#   for typings in Pokemon and creates
#   a dictionary for collecting them
#   for further future modification
#   -----------------------------------
#   Version Changelog
#   -----------------------------------
#
#   -------------
#   Pokemon Types
#   -------------
class Bug:
    def __init__(self):
        self.name = {'Bug'}
        self.weak = {'Fire', 'Flying', 'Rock'}
        self.resist = {'Fighting', 'Grass', 'Ground'}
        self.immune = set()


class Dark:
    def __init__(self):
        self.name = {'Dark'}
        self.weak = {'Fighting', 'Fairy', 'Bug'}
        self.resist = {'Ghost', 'Dark'}
        self.immune = {'Psychic'}


class Dragon:
    def __init__(self):
        self.name = {'Dragon'}
        self.weak = {'Dragon', 'Ice', 'Fairy'}
        self.resist = {'Fire', 'Water', 'Electric', 'Grass'}
        self.immune = set()


class Electric:
    def __init__(self):
        self.name = {'Electric'}
        self.weak = {'Ground'}
        self.resist = {'Electric', 'Flying', 'Steel'}
        self.immune = set()


class Fairy:
    def __init__(self):
        self.name = {'Fairy'}
        self.weak = {'Poison', 'Steel'}
        self.resist = {'Fighting', 'Bug', 'Dark'}
        self.immune = {'Dragon'}


class Fighting:
    def __init__(self):
        self.name = {'Fighting'}
        self.weak = {'Psychic', 'Flying', 'Fairy'}
        self.resist = {'Bug', 'Rock', 'Dark'}
        self.immune = set()


class Fire:
    def __init__(self):
        self.name = {'Fire'}
        self.weak = {'Ground', 'Water', 'Rock'}
        self.resist = {'Steel', 'Fire', 'Grass', 'Ice', 'Bug', 'Fairy'}
        self.immune = set()


class Flying:
    def __init__(self):
        self.name = {'Flying'}
        self.weak = {'Electric', 'Rock', 'Ice'}
        self.resist = {'Grass', 'Fighting', 'Bug'}
        self.immune = {'Ground'}


class Ghost:
    def __init__(self):
        self.name = {'Ghost'}
        self.weak = {'Ghost', 'Dark'}
        self.resist = {'Poison', 'Bug'}
        self.immune = {'Normal', 'Fighting'}


class Grass:
    def __init__(self):
        self.name = {'Grass'}
        self.weak = {'Fire', 'Ice', 'Poison', 'Flying', 'Bug'}
        self.resist = {'Water', 'Electric', 'Grass', 'Ground'}
        self.immune = set()


class Ground:
    def __init__(self):
        self.name = {'Ground'}
        self.weak = {'Water', 'Grass', 'Ice'}
        self.resist = {'Rock', 'Poison'}
        self.immune = {'Electric'}


class Ice:
    def __init__(self):
        self.name = {'Ice'}
        self.weak = {'Fire', 'Fighting', 'Rock', 'Steel'}
        self.resist = {'Ice'}
        self.immune = set()


class Normal:
    def __init__(self):
        self.name = {'Normal'}
        self.weak = {'Fighting'}
        self.resist = set()
        self.immune = {'Ghost'}


class Poison:
    def __init__(self):
        self.name = {'Poison'}
        self.weak = {'Ground', 'Psychic'}
        self.resist = {'Grass', 'Fighting', 'Poison', 'Bug', 'Fairy'}
        self.immune = set()


class Psychic:
    def __init__(self):
        self.name = {'Psychic'}
        self.weak = {'Ghost', 'Dark', 'Bug'}
        self.resist = {'Fighting', 'Psychic'}
        self.immune = set()


class Rock:
    def __init__(self):
        self.name = {'Rock'}
        self.weak = {'Water', 'Fighting', 'Steel', 'Grass', 'Ground'}
        self.resist = {'Normal', 'Fire', 'Poison', 'Flying'}
        self.immune = set()


class Steel:
    def __init__(self):
        self.name = {'Steel'}
        self.weak = {'Fire', 'Fighting', 'Ground'}
        self.resist = {'Normal', 'Grass', 'Ice', 'Flying', 'Psychic', 'Bug', 'Rock', 'Dragon', 'Steel', 'Fairy'}
        self.immune = {'Poison'}


class Water:
    def __init__(self):
        self.name = {'Water'}
        self.weak = {'Electric', 'Grass'}
        self.resist = {'Fire', 'Water', 'Ice', 'Steel'}
        self.immune = set()


class Empty:
    def __init__(self):
        self.name = set()
        self.weak = set()
        self.resist = set()
        self.immune = set()

#   ----------------------
#   Dictionary Definitions
#   ----------------------
pkmn_type = {
    "Bug": Bug(),
    "Dark": Dark(),
    "Dragon": Dragon(),
    "Electric": Electric(),
    "Fairy": Fairy(),
    "Fighting": Fighting(),
    "Fire": Fire(),
    "Flying": Flying(),
    "Ghost": Ghost(),
    "Grass": Grass(),
    "Ground": Ground(),
    "Ice": Ice(),
    "Normal": Normal(),
    "Poison": Poison(),
    "Psychic": Psychic(),
    "Rock": Rock(),
    "Steel": Steel(),
    "Water": Water(),
    "None": Empty(),
    "BUG": Bug(),
    "DARK": Dark(),
    "DRAGON": Dragon(),
    "ELECTRIC": Electric(),
    "FAIRY": Fairy(),
    "FIGHTING": Fighting(),
    "FIRE": Fire(),
    "FLYING": Flying(),
    "GHOST": Ghost(),
    "GRASS": Grass(),
    "GROUND": Ground(),
    "ICE": Ice(),
    "NORMAL": Normal(),
    "POISON": Poison(),
    "PSYCHIC": Psychic(),
    "ROCK": Rock(),
    "STEEL": Steel(),
    "WATER": Water(),
    "NONE": Empty(),
    "bug": Bug(),
    "dark": Dark(),
    "dragon": Dragon(),
    "electric": Electric(),
    "fairy": Fairy(),
    "fighting": Fighting(),
    "fire": Fire(),
    "flying": Flying(),
    "ghost": Ghost(),
    "grass": Grass(),
    "ground": Ground(),
    "ice": Ice(),
    "normal": Normal(),
    "poison": Poison(),
    "psychic": Psychic(),
    "rock": Rock(),
    "steel": Steel(),
    "water": Water(),
    "none": Empty()
}
