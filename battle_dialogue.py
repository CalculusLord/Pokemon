def weak_res_dialogue(Pokemon, Move_type):
    if Move_type in Pokemon.weakness():
        for i in Pokemon.TYPE.WEAK:
            if i in Pokemon.SUB_TYPE.WEAK:
                print("It's extremely effective!!!")
                return 4
        print("It's super effective!")
        return 2
    elif Move_type in Pokemon.resistance():
        for i in Pokemon.TYPE.RESIST:
            if i in Pokemon.SUB_TYPE.RESIST:
                print("It's was barely effective...")
                return 1 / 4
        print("It's not very effective.")
        return 1 / 2
    elif Move_type in Pokemon.immunity():
        print("It has no effect...")
        return 0
    else:
        return 1
