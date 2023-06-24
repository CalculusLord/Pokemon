#   -----------------------------------
#   Written by Nathanael J. Reynolds
#   name = Pokemon Match
#   version = 1.0
#   version_year = 2023
#   Description: Matches 2 or 3 Pokemon
#   based on specified parameters for
#   optimal type synergy
#   -----------------------------------
#   Version Changelog
#   2023-06-24: version 1.0 completed
#   and comments added
#   -----------------------------------

from pokedex import *

#   ----------------
#   User Parameters
#   ---------------
main_type = 'steel'                         # Types are not case-sensitive but must be included in quotes
sub_type = 'grass'                          # For no type on sub_type input: 'none' or leave quotes blank

#   Search Parameters
#   -----------------
search = 'no'                               # Toggles searching for a specific type match or browsing for matches
no_of_searches = 2                          # How many specific Pokemon to look up
search_main = 'rock'
search_sub = 'poison'
search2_main = 'water'
search2_sub = 'poison'

#   Algorithm Parameters
#   --------------------
core_size = 2                               # Size of team core to construct (can be 2 or 3)
exact_no_of_cores = 'yes'                   # Include 2 cores in 3 core queries

#   First Match Parameters
shared_weaknesses = 1                       # Number of weaknesses shared between queried Pokemon and first match
unchecked_weaknesses = 1                    # Number of weaknesses not covered by a partner's resistance
exact_no_of_shared_weaks = 'no'             # Toggles if shared_weaknesses values exact or allows less than threshold
are_no_of_unchecked_weaks_mutual = 'no'     # Checks if one or both Pokemon have a weakness unaddressed by partner

#   Second Match Parameters
trio_shared_weaks = 2
trio_unchecked_weaks = 1
exact_no_of_trio_share_weaks = 'no'
is_trio_unchecked_mutual = 'no'

#   Display Parameters
#   ------------------
show_stats = 'no'                           # Input: yes, pkmn1, pkmn2, pkmn3, pkmn1&2, pkmn1&3, pkmn2&3, or no
show_weakness = 'yes'                       # Displays weaknesses
show_resistance = 'no'                      # Displays resistances and immunities
show_covered = 'no'                         # Shows weaknesses og Pokemon covered by their partner(s) resistance
show_unchecked = 'no'                       # Show weaknesses unaddressed by partner resistance
show_shared = 'yes'                         # Displays weaknesses Pokemon share with their partner


#   ---------------------
#   Functions
#   ---------------------

def display_results(pkmn, pkmn2, pkmn3=Pokemon(main_type=pkmn_type['none'], sub_type=pkmn_type['none']),
                    core_size=core_size):
    """
    Function takes in pokemon and displays the results of the search
    :param pkmn: class
    :param pkmn2: class
    :param pkmn3: class
    :oaram core_size: int
    :return: int
    """
    add_count = 0                            # Used for match_count and ensures accurate counting of matches
    poke1def = pkmn.resist.union(pkmn.immune)
    poke2def = pkmn2.resist.union(pkmn2.immune)
    poke3def = pkmn3.resist.union(pkmn3.immune)

    #   These variables alphabetize for comparison of pokemon types used in safeguards and for index-able display
    pk1_type = list(pkmn.what_type)
    pk1_type.sort()
    type_list = list(pkmn2.what_type)
    type_list.sort()
    type2_list = list(pkmn3.what_type)
    type2_list.sort()

    #   These safeguards fully-covered 2-cores with a 3rd member
    if core_size == 3 and (pkmn.weak.difference(poke3def) == set() and pkmn3.weak.difference(poke1def) == set()):
        core_size = 2
        pkmn2 = pkmn3
        pkmn3 = Pokemon(main_type=pkmn_type['none'], sub_type=pkmn_type['none'])
        if exact_no_of_cores == 'yes':
            return add_count
    elif core_size == 3 and (pkmn2.weak.difference(poke3def) == set() and pkmn3.weak.difference(poke2def) == set()):
        if exact_no_of_cores == 'yes':
            return add_count
    elif core_size == 3 and (pkmn.weak.difference(poke2def) == set() and pkmn2.weak.difference(poke1def) == set()):
        if exact_no_of_cores == 'yes':
            return add_count

    #   These safeguards prevent 3-cores of redundant typings e.g (water, poison), (dark, dragon), (dark, dragon)
    elif core_size == 3 and (pk1_type == type_list):
        return add_count
    elif core_size == 3 and (pk1_type == type2_list):
        return add_count
    elif core_size == 3 and (type_list == type2_list):
        return add_count
    type_list = list(pkmn2.what_type)
    type_list.sort()
    type2_list = list(pkmn3.what_type)
    type2_list.sort()
    add_count = 1
    print('MATCH ', match_count)
    print('Pokemon 1 type:\t', list(pkmn.what_type))
    print('Pokemon 2 type:\t', type_list)
    if core_size == 3 and pkmn3.what_type != set():
        print('Pokemon 3 type:\t', list(pkmn3.what_type))
    if show_stats == 'yes' or show_stats == 'pkmn1' or show_stats == 'pkmn1&2' or show_stats == 'pkmn1&3':
        print('\t', list(pkmn.what_type))
        print('\t---------------')
        if show_resistance == 'yes':
            print('\tResistance:\t', pkmn.resist)
            print('\tImmunities:\t', pkmn.immune)
        if show_covered == 'yes':
            print('\tFrom Pkmn2:\t', poke2def.intersection(pkmn.weak))
            if core_size == 3 and pkmn3.what_type != set():
                print('\tFrom Pkmn3:\t', poke3def.intersection(pkmn.weak))
                print('\tCoverage:\t', poke2def.intersection(pkmn.weak).union(poke3def.intersection(pkmn.weak)))
        if show_weakness == 'yes':
            print('\n\tWeaknesses:\t', pkmn.weak)
        if show_unchecked == 'yes':
            if core_size == 3 and pkmn3.what_type != set():
                print('\tNot Pkmn2:\t', pkmn.weak.difference(poke2def))
                print('\tNot Pkmn3:\t', pkmn.weak.difference(poke3def))
            print('\tUnchecked:\t', pkmn.weak.difference(poke2def.union(poke3def)))
        if show_shared == 'yes':
            print('\tOverlap 2:\t', pkmn.weak.intersection(pkmn2.weak))
            if core_size == 3 and pkmn3.what_type != set():
                print('\tOverlap 3:\t', pkmn.weak.intersection(pkmn3.weak))
    if show_stats == 'yes' or show_stats == 'pkmn2' or show_stats == 'pkmn1&2' or show_stats == 'pkmn2&3':
        print('\n\t', type_list)
        print('\t---------------')
        if show_resistance == 'yes':
            print('\tResistance:\t', pkmn2.resist)
            print('\tImmunities:\t', pkmn2.immune)
        if show_covered == 'yes':
            print('\tFrom Pkmn1:\t', poke1def.intersection(pkmn2.weak))
            if core_size == 3 and pkmn3.what_type != set():
                print('\tFrom Pkmn3:\t', poke3def.intersection(pkmn2.weak))
                print('\tCoverage:\t', poke1def.intersection(pkmn2.weak).union(poke3def.intersection(pkmn2.weak)))
        if show_weakness == 'yes':
            print('\n\tWeaknesses:\t', pkmn2.weak)
        if show_unchecked == 'yes':
            if core_size == 3 and pkmn3.what_type != set():
                print('\tNot Pkmn1:\t', pkmn2.weak.difference(poke1def))
                print('\tNot Pkmn3:\t', pkmn2.weak.difference(poke3def))
            print('\tUnchecked:\t', pkmn2.weak.difference(poke1def.union(poke3def)))
        if show_shared == 'yes':
            print('\tOverlap 1:\t', pkmn2.weak.intersection(pkmn.weak))
            if core_size == 3 and pkmn3.what_type != set():
                print('\tOverlap 3:\t', pkmn2.weak.intersection(pkmn3.weak))
    if core_size == 3 and pkmn3.what_type != set():
        if show_stats == 'yes' or show_stats == 'pkmn3' or show_stats == 'pkmn1&3' or show_stats == 'pkmn2&3':
            print('\n\t', list(pkmn3.what_type))
            print('\t---------------')
            if show_resistance == 'yes':
                print('\tResistance:\t', pkmn3.resist)
                print('\tImmunities:\t', pkmn3.immune)
            if show_covered == 'yes':
                print('\tFrom Pkmn1:\t', poke1def.intersection(pkmn3.weak))
                print('\tFrom Pkmn2:\t', poke2def.intersection(pkmn3.weak))
                print('\tCoverage:\t', poke1def.intersection(pkmn3.weak).union(poke2def.intersection(pkmn3.weak)))
            if show_weakness == 'yes':
                print('\n\tWeaknesses:\t', pkmn3.weak)
            if show_unchecked == 'yes':
                print('\tNot Pkmn1:\t', pkmn3.weak.difference(poke1def))
                print('\tNot Pkmn2:\t', pkmn3.weak.difference(poke2def))
                print('\tUnchecked:\t', pkmn3.weak.difference(poke1def.union(poke2def)))
            if show_shared == 'yes':
                print('\tOverlap 1:\t', pkmn3.weak.intersection(pkmn.weak))
                print('\tOverlap 2:\t', pkmn3.weak.intersection(pkmn2.weak))
    print('END OF SUMMARY\n')
    return add_count


def list_sort(list_object):
    """
    match_finder outputs lists and dictionaries of tuples that need to be sorted and organized to ensure that entries
    are not repeated. This function does that
    :param list_object: list
    :return: list
    """
    sorted_list = [list(list_object[i]) for i in range(0, len(list_object))]
    for i in range(0, len(sorted_list)):
        l = sorted_list[i]
        l.sort()
        sorted_list[i] = l
    sorted_list.sort()
    return sorted_list


def match_finder(pkmn1):
    """
    This function takes in a Pokemon and returns a list of types matching the search parameters
    :param pkmn1: class
    :return: set, dict
    """
    #   ------------------
    #   Function Variables
    #   ------------------
    pkmn_match = []  # List of matches for Pokemon 1
    #   -------------
    #   Function Body
    #   -------------
    for key1 in pkmn_type:
        if key1 == 'None' or key1 == 'NONE' or key1 == 'none':  # Prevents empty set matches
            break
        for key2 in pkmn_type:                                  # Prevents double type Pokemon e.g. {'Water', 'Water'}
            if key1 == key2:
                key2 = 'None'
            pkmn2 = Pokemon(pkmn_type[key1], pkmn_type[key2])   # Creates second Pokemon
            shared_weaks = pkmn1.weak.intersection(pkmn2.weak)  # Set of shared weaknesses of between both Pokemon
            pkmn1_uncovered = pkmn1.weak.difference(pkmn2.resist.union(pkmn2.immune))
            pkmn2_uncovered = pkmn2.weak.difference(pkmn1.resist.union(pkmn1.immune))
            if exact_no_of_shared_weaks == 'no':                # Checks how many weaknesses in common of Pokemon pair
                weak_cond = len(shared_weaks) <= shared_weaknesses
            else:
                weak_cond = len(shared_weaks) == shared_weaknesses
            if weak_cond:
                if are_no_of_unchecked_weaks_mutual == 'no':    # Checks how many weaknesses left uncovered by partner
                    coverage_cond = (len(pkmn1_uncovered) == unchecked_weaknesses and len(pkmn2_uncovered) == 0) or \
                                    (len(pkmn2_uncovered) == unchecked_weaknesses and len(pkmn1_uncovered) == 0)
                elif are_no_of_unchecked_weaks_mutual == 'yes':
                    coverage_cond = len(pkmn1_uncovered) == unchecked_weaknesses and \
                                    len(pkmn2_uncovered) == unchecked_weaknesses
                if coverage_cond:
                    pkmn_match.append(pkmn2.what_type)          # Adds second Pokemon to match list
            pkmn_match = list_sort(pkmn_match)                  # Sorts list to ensure no duplicates returned
    return set(tuple(i) for i in pkmn_match)


def second_match(pkmn1, type_list):
    """
    This function matches a Pokemon with a pair of Pokemon
    :param pkmn1: class
    :param type_list: list
    """
    #   -------------------
    #   Function Variables
    #   -------------------
    pkmn_match = {tuple(type_list): []}
    type_len = len(type_list)
    pkmn2_main = type_list[0]
    pkmn2_sub = type_list[type_len - 1]
    if pkmn2_main == pkmn2_sub:
        pkmn2_sub = 'None'
    pkmn2 = Pokemon(pkmn_type[pkmn2_main], pkmn_type[pkmn2_sub])
    pair_res = pkmn1.resist.union(pkmn2.resist)
    pair_imm = pkmn1.immune.union(pkmn2.immune)
    #   -------------
    #   Function Body
    #   -------------
    for key1 in pkmn_type:
        if key1 == 'None':
            break
        for key2 in pkmn_type:
            if key1 == key2:
                key2 = 'None'
            pkmn3 = Pokemon(pkmn_type[key1], pkmn_type[key2])  # Creates third Pokemon
            tri_res = pkmn3.resist.union(pair_res)
            tri_imm = pkmn3.immune.union(pair_imm)
            total_defs = tri_res.union(tri_imm)
            pkmn1_uncovered = pkmn1.weak.difference(total_defs)
            pkmn2_uncovered = pkmn2.weak.difference(total_defs)
            pkmn3_uncovered = pkmn3.weak.difference(total_defs)
            pkmn12_weaks = pkmn1.weak.intersection(pkmn2.weak)
            pkmn13_weaks = pkmn1.weak.intersection(pkmn3.weak)
            pkmn23_weaks = pkmn2.weak.intersection(pkmn3.weak)
            if exact_no_of_trio_share_weaks == 'yes' and exact_no_of_unchecked == 'yes':
                weak_cond = len(pkmn12_weaks) == shared_weaknesses and \
                            ((len(pkmn13_weaks) == 0 and len(pkmn23_weaks) == trio_shared_weaks - shared_weaknesses) or\
                             (len(pkmn13_weaks) == trio_shared_weaks - shared_weaknesses and len(pkmn23_weaks) == 0) or\
                             ((len(pkmn13_weaks) + len(pkmn23_weaks)) == trio_shared_weaks - shared_weaknesses))
            elif exact_no_of_trio_share_weaks == 'no':
                weak_cond = len(pkmn12_weaks) == shared_weaknesses and \
                            ((len(pkmn13_weaks) == 0 and len(pkmn23_weaks) <= trio_shared_weaks - shared_weaknesses) or\
                             (len(pkmn13_weaks) <= trio_shared_weaks - shared_weaknesses and len(pkmn23_weaks) == 0) or\
                             ((len(pkmn13_weaks) + len(pkmn23_weaks)) <= trio_shared_weaks - shared_weaknesses))
            if weak_cond:
                if is_trio_unchecked_mutual == 'no':
                    coverage_cond = (len(pkmn1_uncovered) == trio_unchecked_weaks and len(pkmn2_uncovered) == 0 and len(
                        pkmn3_uncovered) == 0) or \
                                    (len(pkmn1_uncovered) == 0 and len(pkmn2_uncovered) == trio_unchecked_weaks and len(
                                        pkmn3_uncovered) == 0) or \
                                    (len(pkmn1_uncovered) == 0 and len(pkmn2_uncovered) == 0 and len(
                                        pkmn3_uncovered) == trio_unchecked_weaks) or \
                                    ((len(pkmn1_uncovered) + len(pkmn2_uncovered)) == trio_unchecked_weaks and len(
                                        pkmn3_uncovered) == 0) or \
                                    (len(pkmn1_uncovered) == 0 and (
                                                len(pkmn2_uncovered) + len(pkmn3_uncovered)) == trio_unchecked_weaks) or \
                                    ((len(pkmn1_uncovered) + len(pkmn2_uncovered) + len(
                                        pkmn3_uncovered)) == trio_unchecked_weaks)
                elif is_trio_unchecked_mutual == 'yes':
                    coverage_cond = len(pkmn1_uncovered) == trio_unchecked_weaks and \
                                    len(pkmn2_uncovered) == trio_unchecked_weaks and \
                                    len(pkmn3_uncovered) == trio_unchecked_weaks
                if coverage_cond:
                    pkmn_match[tuple(type_list)].append(pkmn3.what_type)
    pkmn_match[tuple(type_list)] = list_sort(
        pkmn_match[tuple(type_list)])  # Sorts list to ensure no duplicates returned
    return set(tuple(i) for i in pkmn_match[tuple(type_list)])


#   ---------------
#   Execute Program
#   ---------------
if __name__ == '__main__':
    pkmn = Pokemon(pkmn_type[main_type], pkmn_type[sub_type])
    first_matches = match_finder(pkmn)                          # Get matches for Pokemon
    first_matches = list(first_matches)
    first_matches = list_sort(first_matches)                    # Sort for alphabetical order of matches
    first_len = len(first_matches)                              # Stop condition
    combo_list = []                                             # Filters out duplicates for 3-match combos
    count = 0
    match_count = 1

    if search == 'yes' and no_of_searches == 1 and core_size == 2:
        pkmn2 = Pokemon(pkmn_type[search_main], pkmn_type[search_sub])
        display_results(pkmn, pkmn2)
        count = count + 1
    elif search == 'yes' and no_of_searches == 2:
        pkmn2 = Pokemon(pkmn_type[search_main], pkmn_type[search_sub])
        pkmn3 = Pokemon(pkmn_type[search2_main], pkmn_type[search2_sub])
        display_results(pkmn, pkmn2, pkmn3)
        count = count + 1
    elif search == 'yes' and no_of_searches == 1 and core_size == 3:
        pkmn2 = Pokemon(pkmn_type[search_main], pkmn_type[search_sub])
        pkmn2_type_list = list(pkmn2.what_type)
        matches = second_match(pkmn, pkmn2_type_list)
        matches = list(matches)
        matches.sort()
        for j in range(0, len(matches)):
            second = list(matches[j])
            second.sort()
            second_len = len(second)
            second_main = second[0]
            second_sub = second[second_len - 1]
            pkmn3 = Pokemon(pkmn_type[second_main], pkmn_type[second_sub])
            display_results(pkmn, pkmn2, pkmn3)
            match_count = match_count + display_results(pkmn, pkmn2, pkmn3)  # Odd notation ensures correct counting
            count = match_count - 1
    elif search == 'no' and core_size == 3:
        for i in range(0, first_len):
            first = first_matches[i]
            first_len = len(first)
            first_main = first[0]
            first_sub = first[first_len - 1]
            pkmn2 = Pokemon(pkmn_type[first_main], pkmn_type[first_sub])
            second_matches = second_match(pkmn, first)
            second_matches = list(second_matches)
            second_matches.sort()
            for j in range(0, len(second_matches)):
                second = list(second_matches[j])
                second.sort()
                second_len = len(second)
                second_main = second[0]
                second_sub = second[second_len - 1]
                combo = [list(pkmn.what_type), first, second]
                combo.sort()
                if combo not in combo_list:
                    pkmn3 = Pokemon(pkmn_type[second_main], pkmn_type[second_sub])
                    match_count = match_count + display_results(pkmn, pkmn2, pkmn3)
                    count = match_count - 1
                    combo_list.append(combo)
                else:
                    pass

    elif search == 'no' and core_size == 2:
        for i in range(0, len(first_matches)):
            pkmn2_id = list(first_matches[i])  # Grabs i-th Pokemon from first_matches
            last_index = len(pkmn2_id) - 1
            pkmn2 = Pokemon(pkmn_type[pkmn2_id[0]], pkmn_type[pkmn2_id[last_index]])
            match_count = match_count + display_results(pkmn, pkmn2)
            count = match_count - 1

    print(count, 'MATCHES FOUND')
