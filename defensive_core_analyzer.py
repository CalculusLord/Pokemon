from Types import *

def Weaknesses(type_1, type_2 = None):
    weak = []
    for i in type_1.WEAK:
        weak.append(i)
    if type_2 is not None:
        if type_2.NAME is not type_1.NAME:
            for i in type_1.WEAK:
                if i in type_2.RESIST or i in type_2.IMMUNE:
                    weak.remove(i)
            for j in type_2.WEAK:
                if j in type_1.RESIST or j in type_1.IMMUNE:
                    pass
                else:
                    weak.append(j)
    return weak

def Resistances(type_1, type_2 = None):
    resist = []
    immune = []
    for i in type_1.RESIST:
        resist.append(i)
    for i in type_1.IMMUNE:
        immune.append(i)
    if type_2 is not None:
        if type_2.NAME is not type_1.NAME:
            for i in type_1.RESIST:
                if i in type_2.WEAK:
                    resist.remove(i)
            for j in type_2.RESIST:
                if j in type_1.WEAK:
                    pass
                else:
                    resist.append(j)
            for k in type_2.IMMUNE:
                immune.append(k)
    return resist, immune

def Coverage(pkmn1_weak,
             pkmn1_res,
             pkmn1_im,
             pkmn2_weak,
             pkmn2_res,
             pkmn2_im):

    coverage_holes_pkmn1 = []
    coverage_holes_pkmn2 = []

    for i in pkmn1_weak:
        coverage_holes_pkmn1.append(i)

    for i in pkmn1_weak:
        if i in pkmn2_res or i in pkmn2_im:
            coverage_holes_pkmn1.remove(i)

    for i in pkmn2_weak:
        coverage_holes_pkmn2.append(i)

    for i in pkmn2_weak:
        if i in pkmn1_res or i in pkmn1_im:
            coverage_holes_pkmn2.remove(i)
    return coverage_holes_pkmn1 + coverage_holes_pkmn2

def Max_Coverage(pkmn1_weak, pkmn1_res, pkmn1_im):
    total_holes = int(input('How many holes do you want to allow? '))
    for i in type:
        for j in type:
            pkmn2_weak = set(Weaknesses(type[i], type[j]))
            pkmn2_res, pkmn2_im = Resistances(type[i], type[j])
            pkmn2_res = set(pkmn2_res)
            pkmn2_im = set(pkmn2_im)
            cov = Coverage(pkmn1_weak, pkmn1_res, pkmn1_im, pkmn2_weak, pkmn2_res, pkmn2_im)
            if len(cov) <= total_holes:
                res = list(pkmn1_res) + list(pkmn2_res)
                im = list(pkmn1_im) + list(pkmn2_im)
                total_dur = []
                for c in res:
                    total_dur.append(c)
                for c in im:
                    total_dur.append(c)
                print('Type:\t', type[i].NAME, '/', type[j].NAME)
                print('Holes in coverage:\t', cov)
                print('Total Resistances: \t',  len(set(res)))
                print('Total Immunities: \t', len(set(im)))
                print('Total Type Resistance Number:\t', len(set(total_dur)))
                print('Durability Number: \t', len(res) + len(im))
                print('Resistance List: \t', sorted(res))
                print('Immunity: \t', sorted(im), '\n')

if __name__ == '__main__':
    input_type1 = input('Enter first type: ')
    input_type2 = input('Enter second type: ')
    type1 = type[input_type1]
    type2 = type[input_type2]
    pkmn1_weak = set(Weaknesses(type1, type2))
    pkmn1_res, pkmn1_im = Resistances(type1, type2)
    pkmn1_res = set(pkmn1_res)
    pkmn1_im = set(pkmn1_im)
    Max_Coverage(pkmn1_weak, pkmn1_res, pkmn1_im)

