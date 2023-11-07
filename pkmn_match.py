#   -----------------------------------
#   Written by Nathanael J. Reynolds
#   name = Pokemon Match
#   version = 2.0
#   version_year = 2023
#   Description: Matches 2 or 3 Pokemon
#   based on specified parameters for
#   optimal type synergy
#   -----------------------------------
#   Version Changelog
#   2023-06-24: version 1.0 completed
#   and comments added
#
#   2023-06-25: version 1.1 fixed issue
#   with depreciated value called
#   exact_no_shared_weaks
#
#   2023-07-04: version 1.2 single
#   Pokemon lookup added
#
#   2023-11-06: version 2.0 User Parameter
#   interface reordered for clarity,
#   function names made clearer in function
#   section,
#   variable names made clearer in
#   Execute Program section,
#   removed is_trio_unchecked_mutual variable
#   as has no use in three pokemon context,
#   trio_unchecked_weaks variable removed
#   in user parameters and set to
#   0 in find_third_pokemon function,
#   function variable type_list in
#   find_third_pokemon function changed
#   to pkmn_type and type_len changed to
#   no_of_pkmn_types
#   Scanning feature implemented to show
#   all possible cores that meet algorithmic
#   matching conditions for second and third
#   pokemon,
#   Hid search and no_of_searches parameters
#   out of User Parameters and into
#   Execute Program. User paramters
#   search_pkmn_2 and search_pkmn_3 replace
#   search functions for users,
#   Removed are_no_of_unchecked_weaks_mutual
#   parameter
#   These changes were made to simplify user
#   interface
#   -----------------------------------

from pokedex import *

#   ===============
#   User Parameters
#   ===============

core_size = 3              # Size of team core to construct (can be 1, 2 or 3)
exclude_perfect_2_cores = 'yes'  # excludes perfect two-pokemon cores from core_size 3 scans and searches
#   -----------------
#   First Pokemon
#   -----------------
scan = 'yes'        # (yes/no) Toggles scanning feature for all pokemon, turns off search for pokemon 2 and 3
main_type = 'dark'  # Types are not case-sensitive but must be included in quotes
sub_type = 'ice'  # For no type on sub_type input: 'none' or leave quotes blank
#   -----------------
#   Second Pokemon
#   -----------------
#   Search Parameters
#   ~~~~~~~~~~~~~~~~~
search_pkmn_2 = 'yes'    # (yes/no) determines whether to scan on pokemon 2 or input a specific type
pkmn_2_main = 'grass'
pkmn_2_sub = 'steel'
#   Algorithmic Matching Parameters
#   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
shared_weaknesses = 0                    # Number of weaknesses shared between queried Pokemon and second_pkmn match
unchecked_weaknesses = 1                 # Number of weaknesses not covered by a partner's resistance
exact_no_of_shared_weaks = 'no'          # (yes/no) Toggles if shared_weaknesses values exact or allows less than threshold
#   -----------------
#   Third Pokemon
#   -----------------
#   Search Parameters
#   ~~~~~~~~~~~~~~~~~
search_pkmn_3 = 'yes'                   # Turning on seach for pkmn 3 also turns on search for pkmn 2
pkmn_3_main = 'flying'
pkmn_3_sub = 'fire'
#   Algorithmic Matching Parameters
#   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#   the number of unchecked weaknesses in a trio is always 0
trio_shared_weaks = 0                  # Number of weaknesses shared by any constituent members of the trio
exact_no_of_trio_share_weaks = 'no'     # Toggles exact number of weaknesses shared
#   ------------------
#   Display Parameters
#   ------------------
show_stats = 'no'       # Input: yes, pkmn1, pkmn2, pkmn3, pkmn1&2, pkmn1&3, pkmn2&3, or no
show_weakness = 'yes'   # Displays weaknesses
show_resistance = 'yes' # Displays resistances and immunities
show_covered = 'yes'     # Shows weaknesses og Pokemon covered by their partner(s) resistance
show_unchecked = 'yes'  # Show weaknesses unaddressed by partner resistance
show_shared = 'yes'      # Displays weaknesses Pokemon share with their partner

#   A friendly reminder, do not change anything past this point unless you know what you are doing
#   and looking to fix bugs and/or add features. Changing anything in the code past this point
#   could break the program
#   =====================
#   Functions
#   =====================
def display_results(pkmn,
                    pkmn2=Pokemon(main_type=pkmn_type['none'], sub_type=pkmn_type['none']),
                    pkmn3=Pokemon(main_type=pkmn_type['none'], sub_type=pkmn_type['none']),
                    core_size=core_size):
    """
    Function takes in pokemon and displays the results of the search
    :param pkmn: class
    :param pkmn2: class
    :param pkmn3: class
    :oaram core_size: int
    :return: int
    """
    add_count = 0  # Used for match_count and ensures accurate counting of matches
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
        if exclude_perfect_2_cores == 'yes':
            return add_count
    elif core_size == 3 and (pkmn2.weak.difference(poke3def) == set() and pkmn3.weak.difference(poke2def) == set()):
        if exclude_perfect_2_cores == 'yes':
            return add_count
    elif core_size == 3 and (pkmn.weak.difference(poke2def) == set() and pkmn2.weak.difference(poke1def) == set()):
        if exclude_perfect_2_cores == 'yes':
            return add_count
    #   These safeguards prevent 3-cores of redundant typings e.g (water, poison), (dark, dragon), (dark, dragon)
    elif core_size >= 3 and (pk1_type == type_list):
        return add_count
    elif core_size >= 3 and (pk1_type == type2_list):
        return add_count
    elif core_size >= 3 and (type_list == type2_list):
        return add_count
    type_list = list(pkmn2.what_type)
    type_list.sort()
    type2_list = list(pkmn3.what_type)
    type2_list.sort()
    add_count = 1
    print('MATCH ', match_count)
    print('Pokemon 1 type:\t', list(pkmn.what_type))
    print('Pokemon 2 type:\t', type_list)
    if core_size >= 3 and pkmn3.what_type != set():
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
    find_second_pokemon outputs lists and dictionaries of tuples that need to be sorted and organized to ensure that entries
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


def find_second_pokemon(pkmn1):
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
        for key2 in pkmn_type:  # Prevents double type Pokemon e.g. {'Water', 'Water'}
            if key1 == key2:
                key2 = 'None'
            pkmn2 = Pokemon(pkmn_type[key1], pkmn_type[key2])  # Creates second Pokemon
            shared_weaks = pkmn1.weak.intersection(pkmn2.weak)  # Set of shared weaknesses of between both Pokemon
            pkmn1_uncovered = pkmn1.weak.difference(pkmn2.resist.union(pkmn2.immune))
            pkmn2_uncovered = pkmn2.weak.difference(pkmn1.resist.union(pkmn1.immune))
            if exact_no_of_shared_weaks == 'no':  # Checks how many weaknesses in common of Pokemon pair
                weak_cond = len(shared_weaks) <= shared_weaknesses
            else:
                weak_cond = len(shared_weaks) == shared_weaknesses
            if weak_cond:
                if (len(pkmn1_uncovered) + len(pkmn2_uncovered)) == unchecked_weaknesses:
                    pkmn_match.append(pkmn2.what_type)  # Adds second Pokemon to match list
            pkmn_match = list_sort(pkmn_match)  # Sorts list to ensure no duplicates returned
    return set(tuple(i) for i in pkmn_match)


def find_third_pokemon(pkmn1, pkmn2_type):
    """
    This function matches a Pokemon with a pair of Pokemon
    :param pkmn1: class
    :param type_list: list
    """
    #   -------------------
    #   Function Variables
    #   -------------------
    pkmn_match = {tuple(pkmn2_type): []}
    pkmn2_no_of_types = len(pkmn2_type)
    pkmn2_main = pkmn2_type[0]
    pkmn2_sub = pkmn2_type[pkmn2_no_of_types - 1]
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
            if exact_no_of_trio_share_weaks == 'yes':
                weak_cond = len(pkmn12_weaks) == shared_weaknesses and \
                            (len(pkmn13_weaks) + len(pkmn23_weaks) - len(pkmn12_weaks)) == trio_shared_weaks - shared_weaknesses
            elif exact_no_of_trio_share_weaks == 'no':
                weak_cond = len(pkmn12_weaks) == shared_weaknesses and \
                            (len(pkmn13_weaks) + len(pkmn23_weaks) - len(pkmn12_weaks)) <= trio_shared_weaks - shared_weaknesses
            if weak_cond:
                if (len(pkmn1_uncovered) + len(pkmn2_uncovered) + len(pkmn3_uncovered)) == 0:
                    pkmn_match[tuple(pkmn2_type)].append(pkmn3.what_type)
    pkmn_match[tuple(pkmn2_type)] = list_sort(
        pkmn_match[tuple(pkmn2_type)])  # Sorts list to ensure no duplicates returned
    return set(tuple(i) for i in pkmn_match[tuple(pkmn2_type)])


#   ====================
#   Execute Program
#   ====================
if __name__ == '__main__':
    count = 0
    match_count = 1
    scanner = [] # Breaks key2 for loop in order to prevent it from creating duplicate matches
    combo_list = []  # Filters out duplicate matches
    #   -------------------------------------
    #   This section is a compatibility layer
    #   that translates user parameter variables
    #   into a form the code originally written
    #   in version 1 understands
    #   --------------------------------------
    search = 'no'
    if scan == 'no':
        if core_size < 3 and search_pkmn_3 == 'yes':
            search_pkmn_3 = 'no'
        if search_pkmn_3 == 'yes':
            search = 'yes'
            no_of_searches = 2
        elif search_pkmn_2 == 'yes':
            search = 'yes'
            no_of_searches = 1
    elif scan == 'yes':
        search = 'no'
    #   ------------------------------------
    #   End compatibility layer
    #   ------------------------------------
    for key1 in pkmn_type:
        if key1 == 'None':
            break
        for key2 in pkmn_type:
            if key1 == key2:
                key2 = 'None'
            pkmn = Pokemon(pkmn_type[key1], pkmn_type[key2])
            scanner.append(pkmn.what_type)
            scanner = list_sort(scanner)
            scanner_set = set(tuple(i) for i in scanner)
            if len(scanner) > len(scanner_set):
                scanner = list(scanner_set)
                break
            if scan == 'no':
                pkmn = Pokemon(pkmn_type[main_type], pkmn_type[sub_type])
            second_pkmn_matches = find_second_pokemon(pkmn)  # Get matches for Pokemon
            second_pkmn_matches = list(second_pkmn_matches)
            second_pkmn_matches = list_sort(second_pkmn_matches)  # Sort for alphabetical order of matches
            no_of_second_pkmn_matches = len(second_pkmn_matches)  # Stop condition
            if core_size > 3 or (search == 'yes' and no_of_searches > 2):
                match_count = 0
                print('ERROR INVALID PARAMETERS')
                break
            elif core_size == 1:
                if scan == 'yes':
                    print('ERROR: CANNOT SCAN OVER ONE POKEMON')
                    match_count = 0
                    break
                display_results(pkmn)
                match_count = 0
                break
            elif core_size == 2 and search == 'no':
                for i in range(0, len(second_pkmn_matches)):
                    pkmn2_id = list(second_pkmn_matches[i])  # Grabs i-th Pokemon from second_pkmn_matches
                    first_pkmn = list(pkmn.what_type)
                    first_pkmn.sort()
                    combo = [first_pkmn, pkmn2_id]
                    combo.sort()
                    if combo not in combo_list:
                        last_index = len(pkmn2_id) - 1
                        pkmn2 = Pokemon(pkmn_type[pkmn2_id[0]], pkmn_type[pkmn2_id[last_index]])
                        match_count = match_count + display_results(pkmn, pkmn2)
                        count = match_count - 1
                        combo_list.append(combo)
            elif core_size == 2 and search == 'yes' and no_of_searches == 1:
                pkmn2 = Pokemon(pkmn_type[pkmn_2_main], pkmn_type[pkmn_2_sub])
                display_results(pkmn, pkmn2)
                count = count + 1
            elif core_size == 3 and search == 'no':
                for i in range(0, no_of_second_pkmn_matches):
                    second_pkmn = second_pkmn_matches[i]
                    second_pkmn.sort()
                    no_of_second_pkmn_matches = len(second_pkmn)
                    second_pkmn_main = second_pkmn[0]
                    second_pkmn_sub = second_pkmn[no_of_second_pkmn_matches - 1]
                    pkmn2 = Pokemon(pkmn_type[second_pkmn_main], pkmn_type[second_pkmn_sub])
                    third_pkmn_matches = find_third_pokemon(pkmn, second_pkmn)
                    third_pkmn_matches = list(third_pkmn_matches)
                    third_pkmn_matches.sort()
                    for j in range(0, len(third_pkmn_matches)):
                        third_pkmn = list(third_pkmn_matches[j])
                        third_pkmn.sort()
                        no_of_third_pkmn_matches = len(third_pkmn)
                        third_pkmn_main = third_pkmn[0]
                        third_pkmn_sub = third_pkmn[no_of_third_pkmn_matches - 1]
                        first_pkmn = list(pkmn.what_type)
                        first_pkmn.sort()
                        combo = [first_pkmn, second_pkmn, third_pkmn]
                        combo.sort()
                        if combo not in combo_list:
                            pkmn3 = Pokemon(pkmn_type[third_pkmn_main], pkmn_type[third_pkmn_sub])
                            match_count = match_count + display_results(pkmn, pkmn2, pkmn3)
                            count = match_count - 1
                            combo_list.append(combo)
                        else:
                            pass
            elif core_size == 3 and search == 'yes' and no_of_searches == 1:
                pkmn2 = Pokemon(pkmn_type[pkmn_2_main], pkmn_type[pkmn_2_sub])
                pkmn2_type_list = list(pkmn2.what_type)
                matches = find_third_pokemon(pkmn, pkmn2_type_list)
                matches = list(matches)
                matches.sort()
                for j in range(0, len(matches)):
                    third_pkmn = list(matches[j])
                    third_pkmn.sort()
                    no_of_third_pkmn_matches = len(third_pkmn)
                    third_pkmn_main = third_pkmn[0]
                    third_pkmn_sub = third_pkmn[no_of_third_pkmn_matches - 1]
                    pkmn3 = Pokemon(pkmn_type[third_pkmn_main], pkmn_type[third_pkmn_sub])
                    match_count = match_count + display_results(pkmn, pkmn2, pkmn3)  # Odd notation ensures correct counting
                    count = match_count - 1
            elif core_size == 3 and search == 'yes' and no_of_searches == 2:
                pkmn2 = Pokemon(pkmn_type[pkmn_2_main], pkmn_type[pkmn_2_sub])
                pkmn3 = Pokemon(pkmn_type[pkmn_3_main], pkmn_type[pkmn_3_sub])
                display_results(pkmn, pkmn2, pkmn3)
                count = count + 1
            else:
                match_count = 0
                print('ERROR')
                break
            if scan == 'no':
                break
        if scan == 'no':
            break
        if match_count == 0:
            break
        scanner = []
        scanner_set = {}
    print(count, " MATCHES FOUND")

