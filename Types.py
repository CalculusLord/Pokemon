class Bug_Type:
    def __init__(self):
        self.NAME = 'Bug'
        self.WEAK = ['Fire', 'Flying', 'Rock']
        self.RESIST = ['Fighting', 'Grass', 'Ground']
        self.IMMUNE = []

class Dark_Type:
    def __init__(self):
        self.NAME = 'Dark'
        self.WEAK = ['Fighting', 'Fairy', 'Bug']
        self.RESIST = ['Ghost', 'Dark']
        self.IMMUNE = ['Psychic']

class Dragon_Type:
    def __init__(self):
        self.NAME = 'Dragon'
        self.WEAK = ['Dragon', 'Ice', 'Fairy']
        self.RESIST = ['Fire', 'Water', 'Electric', 'Grass']
        self.IMMUNE = []

class Electric_Type:
    def __init__(self):
        self.NAME = 'Electric'
        self.WEAK = ['Ground']
        self.RESIST = ['Electric', 'Flying', 'Steel']
        self.IMMUNE = []

class Fairy_Type:
    def __init__(self):
        self.NAME = 'Fairy'
        self.WEAK = ['Poison', 'Steel']
        self.RESIST = ['Fighting', 'Bug', 'Dark']
        self.IMMUNE = ['Dragon']

class Fighting_Type:
    def __init__(self):
        self.NAME = 'Fighting'
        self.WEAK = ['Psychic', 'Flying', 'Fairy']
        self.RESIST = ['Bug', 'Rock', 'Dark']
        self.IMMUNE = []

class Fire_Type:
    def __init__(self):
        self.NAME = 'Fire'
        self.WEAK = ['Ground', 'Water', 'Rock']
        self.RESIST = ['Steel', 'Fire', 'Grass', 'Ice', 'Bug', 'Fairy']
        self.IMMUNE = []

class Flying_Type:
    def __init__(self):
        self.NAME = 'Flying'
        self.WEAK = ['Electric', 'Rock', 'Ice']
        self.RESIST = ['Grass', 'Fighting', 'Bug']
        self.IMMUNE = ['Ground']

class Ghost_Type:
    def __init__(self):
        self.NAME = 'Ghost'
        self.WEAK = ['Ghost', 'Dark']
        self.RESIST = ['Poison', 'Bug']
        self.IMMUNE = ['Normal', 'Fighting']

class Grass_Type:
    def __init__(self):
        self.NAME = 'Grass'
        self.WEAK = ['Fire', 'Ice', 'Poison', 'Flying', 'Bug']
        self.RESIST = ['Water', 'Electric', 'Grass', 'Ground']
        self.IMMUNE = []

class Ground_Type:
    def __init__(self):
        self.NAME = 'Ground'
        self.WEAK = ['Water', 'Grass', 'Ice']
        self.RESIST = ['Rock', 'Poison']
        self.IMMUNE = ['Electric']

class Ice_Type:
    def __init__(self):
        self.NAME = 'Ice'
        self.WEAK = ['Fire', 'Fighting', 'Rock', 'Steel']
        self.RESIST = ['Ice']
        self.IMMUNE = []

class Normal_Type:
    def __init__(self):
        self.NAME = 'Normal'
        self.WEAK = ['Fighting']
        self.RESIST = []
        self.IMMUNE = ['Ghost']

class Poison_Type:
    def __init__(self):
        self.NAME = 'Poison'
        self.WEAK = ['Ground', 'Psychic']
        self.RESIST = ['Grass', 'Fighting', 'Poison', 'Bug', 'Fairy']
        self.IMMUNE = []

class Psychic_Type:
    def __init__(self):
        self.NAME = 'Psychic'
        self.WEAK = ['Ghost', 'Dark', 'Bug']
        self.RESIST = ['Fighting', 'Psychic']
        self.IMMUNE = []

class Rock_Type:
    def __init__(self):
        self.NAME = 'Rock'
        self.WEAK = ['Water', 'Fighting', 'Steel', 'Grass', 'Ground']
        self.RESIST = ['Normal', 'Fire', 'Poison', 'Flying']
        self.IMMUNE = []

class Steel_Type:
    def __init__(self):
        self.NAME = 'Steel'
        self.WEAK = ['Fire', 'Fighting', 'Ground']
        self.RESIST = ['Normal', 'Grass', 'Ice', 'Flying', 'Psychic', 'Bug', 'Rock', 'Dragon', 'Steel', 'Fairy']
        self.IMMUNE = ['Poison']

class Water_Type:
    def __init__(self):
        self.NAME = 'Water'
        self.WEAK = ['Electric', 'Grass']
        self.RESIST = ['Fire', 'Water', 'Ice', 'Steel']
        self.IMMUNE = []

type = {
    "Bug": Bug_Type(),
    "Dark": Dark_Type(),
    "Dragon": Dragon_Type(),
    "Electric": Electric_Type(),
    "Fairy": Fairy_Type(),
    "Fighting": Fighting_Type(),
    "Fire": Fire_Type(),
    "Flying": Flying_Type(),
    "Ghost": Ghost_Type(),
    "Grass": Grass_Type(),
    "Ground": Ground_Type(),
    "Ice": Ice_Type(),
    "Normal": Normal_Type(),
    "Poison": Poison_Type(),
    "Psychic": Psychic_Type(),
    "Rock": Rock_Type(),
    "Steel": Steel_Type(),
    "Water": Water_Type(),
    # "bug": Bug_Type(),
    # "dark": Dark_Type(),
    # "dragon": Dragon_Type(),
    # "electric": Electric_Type(),
    # "fairy": Fairy_Type(),
    # "fighting": Fighting_Type(),
    # "fire": Fire_Type(),
    # "flying": Flying_Type(),
    # "ghost": Ghost_Type(),
    # "grass": Grass_Type(),
    # "ground": Ground_Type(),
    # "ice": Ice_Type(),
    # "normal": Normal_Type(),
    # "poison": Poison_Type(),
    # "psychic": Psychic_Type(),
    # "rock": Rock_Type(),
    # "steel": Steel_Type(),
    # "water": Water_Type()
}