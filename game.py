"""
Your name: Adedeji Toki
Your student number: A01243794

All of your code must go in this file.
"""
import random
import sys
import time
import math


def make_board():
    """
    Create a game board (represented as a dictionary).

    :postcondition: return a game board with rooms and descriptions
    :return: a dictionary representing the gameboard.(key: (row,column), value: room description)

    >>> make_board()
    {(0, 0): 'none', (1, 0): 'none', (2, 0): 'none', (3, 0): 'none', (4, 0): 'wall', (5, 0): 'none', (6, 0): 'none', (7, 0): 'none', (8, 0): 'none', (9, 0): 'none', (10, 0): 'none', (11, 0): 'none', (12, 0): 'wall', (13, 0): 'none', (14, 0): 'none', (15, 0): 'none', (16, 0): 'none', (17, 0): 'none', (18, 0): 'none', (19, 0): 'none', (20, 0): 'none', (21, 0): 'none', (22, 0): 'none', (23, 0): 'none', (24, 0): 'none', (0, 1): 'none', (1, 1): 'none', (2, 1): 'none', (3, 1): 'none', (4, 1): 'wall', (5, 1): 'none', (6, 1): 'none', (7, 1): 'none', (8, 1): 'none', (9, 1): 'none', (10, 1): 'none', (11, 1): 'none', (12, 1): 'wall', (13, 1): 'none', (14, 1): 'none', (15, 1): 'none', (16, 1): 'none', (17, 1): 'none', (18, 1): 'none', (19, 1): 'none', (20, 1): 'none', (21, 1): 'none', (22, 1): 'none', (23, 1): 'boss', (24, 1): 'none', (0, 2): 'none', (1, 2): 'none', (2, 2): 'none', (3, 2): 'none', (4, 2): 'wall', (5, 2): 'none', (6, 2): 'none', (7, 2): 'none', (8, 2): 'none', (9, 2): 'none', (10, 2): 'none', (11, 2): 'none', (12, 2): 'wall', (13, 2): 'none', (14, 2): 'none', (15, 2): 'none', (16, 2): 'none', (17, 2): 'none', (18, 2): 'none', (19, 2): 'none', (20, 2): 'none', (21, 2): 'none', (22, 2): 'none', (23, 2): 'none', (24, 2): 'none', (0, 3): 'none', (1, 3): 'none', (2, 3): 'none', (3, 3): 'none', (4, 3): 'wall', (5, 3): 'none', (6, 3): 'none', (7, 3): 'none', (8, 3): 'none', (9, 3): 'none', (10, 3): 'none', (11, 3): 'none', (12, 3): 'wall', (13, 3): 'none', (14, 3): 'none', (15, 3): 'none', (16, 3): 'none', (17, 3): 'none', (18, 3): 'none', (19, 3): 'none', (20, 3): 'none', (21, 3): 'none', (22, 3): 'none', (23, 3): 'none', (24, 3): 'none', (0, 4): 'none', (1, 4): 'none', (2, 4): 'none', (3, 4): 'none', (4, 4): 'wall', (5, 4): 'none', (6, 4): 'none', (7, 4): 'none', (8, 4): 'wall', (9, 4): 'none', (10, 4): 'none', (11, 4): 'none', (12, 4): 'wall', (13, 4): 'wall', (14, 4): 'wall', (15, 4): 'wall', (16, 4): 'wall', (17, 4): 'wall', (18, 4): 'wall', (19, 4): 'wall', (20, 4): 'wall', (21, 4): 'wall', (22, 4): 'none', (23, 4): 'none', (24, 4): 'none', (0, 5): 'none', (1, 5): 'none', (2, 5): 'none', (3, 5): 'none', (4, 5): 'wall', (5, 5): 'none', (6, 5): 'none', (7, 5): 'none', (8, 5): 'wall', (9, 5): 'none', (10, 5): 'none', (11, 5): 'none', (12, 5): 'none', (13, 5): 'none', (14, 5): 'none', (15, 5): 'none', (16, 5): 'none', (17, 5): 'none', (18, 5): 'none', (19, 5): 'none', (20, 5): 'none', (21, 5): 'wall', (22, 5): 'none', (23, 5): 'none', (24, 5): 'none', (0, 6): 'none', (1, 6): 'none', (2, 6): 'none', (3, 6): 'none', (4, 6): 'wall', (5, 6): 'none', (6, 6): 'none', (7, 6): 'none', (8, 6): 'wall', (9, 6): 'none', (10, 6): 'none', (11, 6): 'none', (12, 6): 'none', (13, 6): 'none', (14, 6): 'none', (15, 6): 'none', (16, 6): 'none', (17, 6): 'none', (18, 6): 'none', (19, 6): 'none', (20, 6): 'none', (21, 6): 'wall', (22, 6): 'none', (23, 6): 'none', (24, 6): 'none', (0, 7): 'none', (1, 7): 'none', (2, 7): 'none', (3, 7): 'none', (4, 7): 'wall', (5, 7): 'none', (6, 7): 'none', (7, 7): 'none', (8, 7): 'wall', (9, 7): 'none', (10, 7): 'none', (11, 7): 'none', (12, 7): 'none', (13, 7): 'none', (14, 7): 'none', (15, 7): 'none', (16, 7): 'none', (17, 7): 'none', (18, 7): 'none', (19, 7): 'none', (20, 7): 'none', (21, 7): 'wall', (22, 7): 'none', (23, 7): 'none', (24, 7): 'none', (0, 8): 'none', (1, 8): 'none', (2, 8): 'none', (3, 8): 'none', (4, 8): 'wall', (5, 8): 'none', (6, 8): 'none', (7, 8): 'none', (8, 8): 'wall', (9, 8): 'none', (10, 8): 'none', (11, 8): 'none', (12, 8): 'none', (13, 8): 'none', (14, 8): 'none', (15, 8): 'none', (16, 8): 'none', (17, 8): 'none', (18, 8): 'none', (19, 8): 'none', (20, 8): 'none', (21, 8): 'wall', (22, 8): 'none', (23, 8): 'none', (24, 8): 'none', (0, 9): 'none', (1, 9): 'none', (2, 9): 'none', (3, 9): 'none', (4, 9): 'wall', (5, 9): 'none', (6, 9): 'none', (7, 9): 'none', (8, 9): 'wall', (9, 9): 'none', (10, 9): 'none', (11, 9): 'none', (12, 9): 'mystery', (13, 9): 'mystery', (14, 9): 'mystery', (15, 9): 'mystery', (16, 9): 'mystery', (17, 9): 'mystery', (18, 9): 'none', (19, 9): 'none', (20, 9): 'none', (21, 9): 'wall', (22, 9): 'none', (23, 9): 'none', (24, 9): 'none', (0, 10): 'none', (1, 10): 'none', (2, 10): 'none', (3, 10): 'none', (4, 10): 'wall', (5, 10): 'none', (6, 10): 'none', (7, 10): 'none', (8, 10): 'wall', (9, 10): 'none', (10, 10): 'none', (11, 10): 'none', (12, 10): 'mystery', (13, 10): 'mystery', (14, 10): 'mystery', (15, 10): 'mystery', (16, 10): 'mystery', (17, 10): 'mystery', (18, 10): 'none', (19, 10): 'none', (20, 10): 'none', (21, 10): 'wall', (22, 10): 'none', (23, 10): 'none', (24, 10): 'none', (0, 11): 'none', (1, 11): 'none', (2, 11): 'none', (3, 11): 'none', (4, 11): 'wall', (5, 11): 'none', (6, 11): 'none', (7, 11): 'none', (8, 11): 'wall', (9, 11): 'none', (10, 11): 'none', (11, 11): 'none', (12, 11): 'mystery', (13, 11): 'mystery', (14, 11): 'mystery', (15, 11): 'mystery', (16, 11): 'mystery', (17, 11): 'mystery', (18, 11): 'none', (19, 11): 'none', (20, 11): 'none', (21, 11): 'wall', (22, 11): 'none', (23, 11): 'none', (24, 11): 'none', (0, 12): 'none', (1, 12): 'none', (2, 12): 'none', (3, 12): 'none', (4, 12): 'wall', (5, 12): 'none', (6, 12): 'none', (7, 12): 'none', (8, 12): 'wall', (9, 12): 'none', (10, 12): 'none', (11, 12): 'none', (12, 12): 'mystery', (13, 12): 'mystery', (14, 12): 'mystery', (15, 12): 'mystery', (16, 12): 'mystery', (17, 12): 'mystery', (18, 12): 'none', (19, 12): 'none', (20, 12): 'none', (21, 12): 'wall', (22, 12): 'none', (23, 12): 'none', (24, 12): 'none', (0, 13): 'none', (1, 13): 'none', (2, 13): 'none', (3, 13): 'none', (4, 13): 'wall', (5, 13): 'none', (6, 13): 'none', (7, 13): 'none', (8, 13): 'wall', (9, 13): 'none', (10, 13): 'none', (11, 13): 'none', (12, 13): 'mystery', (13, 13): 'mystery', (14, 13): 'mystery', (15, 13): 'mystery', (16, 13): 'mystery', (17, 13): 'mystery', (18, 13): 'none', (19, 13): 'none', (20, 13): 'none', (21, 13): 'wall', (22, 13): 'none', (23, 13): 'none', (24, 13): 'none', (0, 14): 'none', (1, 14): 'none', (2, 14): 'none', (3, 14): 'none', (4, 14): 'wall', (5, 14): 'none', (6, 14): 'none', (7, 14): 'none', (8, 14): 'wall', (9, 14): 'none', (10, 14): 'none', (11, 14): 'none', (12, 14): 'mystery', (13, 14): 'mystery', (14, 14): 'mystery', (15, 14): 'mystery', (16, 14): 'mystery', (17, 14): 'mystery', (18, 14): 'none', (19, 14): 'none', (20, 14): 'none', (21, 14): 'wall', (22, 14): 'none', (23, 14): 'none', (24, 14): 'none', (0, 15): 'none', (1, 15): 'none', (2, 15): 'none', (3, 15): 'none', (4, 15): 'wall', (5, 15): 'none', (6, 15): 'none', (7, 15): 'none', (8, 15): 'wall', (9, 15): 'none', (10, 15): 'none', (11, 15): 'none', (12, 15): 'mystery', (13, 15): 'mystery', (14, 15): 'mystery', (15, 15): 'mystery', (16, 15): 'mystery', (17, 15): 'mystery', (18, 15): 'none', (19, 15): 'none', (20, 15): 'none', (21, 15): 'wall', (22, 15): 'none', (23, 15): 'none', (24, 15): 'none', (0, 16): 'none', (1, 16): 'none', (2, 16): 'none', (3, 16): 'none', (4, 16): 'wall', (5, 16): 'none', (6, 16): 'none', (7, 16): 'none', (8, 16): 'wall', (9, 16): 'none', (10, 16): 'none', (11, 16): 'none', (12, 16): 'mystery', (13, 16): 'mystery', (14, 16): 'mystery', (15, 16): 'mystery', (16, 16): 'mystery', (17, 16): 'mystery', (18, 16): 'none', (19, 16): 'none', (20, 16): 'none', (21, 16): 'wall', (22, 16): 'none', (23, 16): 'none', (24, 16): 'none', (0, 17): 'none', (1, 17): 'none', (2, 17): 'none', (3, 17): 'none', (4, 17): 'wall', (5, 17): 'none', (6, 17): 'none', (7, 17): 'none', (8, 17): 'wall', (9, 17): 'none', (10, 17): 'none', (11, 17): 'none', (12, 17): 'mystery', (13, 17): 'mystery', (14, 17): 'mystery', (15, 17): 'mystery', (16, 17): 'mystery', (17, 17): 'mystery', (18, 17): 'none', (19, 17): 'none', (20, 17): 'none', (21, 17): 'wall', (22, 17): 'none', (23, 17): 'none', (24, 17): 'none', (0, 18): 'none', (1, 18): 'none', (2, 18): 'none', (3, 18): 'none', (4, 18): 'wall', (5, 18): 'none', (6, 18): 'none', (7, 18): 'none', (8, 18): 'wall', (9, 18): 'none', (10, 18): 'none', (11, 18): 'none', (12, 18): 'none', (13, 18): 'none', (14, 18): 'none', (15, 18): 'none', (16, 18): 'none', (17, 18): 'none', (18, 18): 'none', (19, 18): 'none', (20, 18): 'none', (21, 18): 'wall', (22, 18): 'none', (23, 18): 'none', (24, 18): 'none', (0, 19): 'none', (1, 19): 'none', (2, 19): 'none', (3, 19): 'none', (4, 19): 'wall', (5, 19): 'none', (6, 19): 'none', (7, 19): 'none', (8, 19): 'wall', (9, 19): 'none', (10, 19): 'none', (11, 19): 'none', (12, 19): 'none', (13, 19): 'none', (14, 19): 'none', (15, 19): 'none', (16, 19): 'none', (17, 19): 'none', (18, 19): 'none', (19, 19): 'none', (20, 19): 'none', (21, 19): 'wall', (22, 19): 'none', (23, 19): 'none', (24, 19): 'none', (0, 20): 'none', (1, 20): 'none', (2, 20): 'none', (3, 20): 'none', (4, 20): 'none', (5, 20): 'none', (6, 20): 'none', (7, 20): 'none', (8, 20): 'wall', (9, 20): 'none', (10, 20): 'none', (11, 20): 'none', (12, 20): 'none', (13, 20): 'none', (14, 20): 'none', (15, 20): 'none', (16, 20): 'none', (17, 20): 'none', (18, 20): 'none', (19, 20): 'none', (20, 20): 'none', (21, 20): 'wall', (22, 20): 'none', (23, 20): 'none', (24, 20): 'none', (0, 21): 'none', (1, 21): 'none', (2, 21): 'none', (3, 21): 'none', (4, 21): 'none', (5, 21): 'none', (6, 21): 'none', (7, 21): 'none', (8, 21): 'wall', (9, 21): 'none', (10, 21): 'none', (11, 21): 'none', (12, 21): 'none', (13, 21): 'none', (14, 21): 'none', (15, 21): 'none', (16, 21): 'none', (17, 21): 'none', (18, 21): 'none', (19, 21): 'none', (20, 21): 'none', (21, 21): 'none', (22, 21): 'none', (23, 21): 'none', (24, 21): 'none', (0, 22): 'none', (1, 22): 'none', (2, 22): 'none', (3, 22): 'none', (4, 22): 'none', (5, 22): 'none', (6, 22): 'none', (7, 22): 'none', (8, 22): 'wall', (9, 22): 'none', (10, 22): 'none', (11, 22): 'none', (12, 22): 'none', (13, 22): 'none', (14, 22): 'none', (15, 22): 'none', (16, 22): 'none', (17, 22): 'none', (18, 22): 'none', (19, 22): 'none', (20, 22): 'none', (21, 22): 'none', (22, 22): 'none', (23, 22): 'none', (24, 22): 'none', (0, 23): 'none', (1, 23): 'none', (2, 23): 'none', (3, 23): 'none', (4, 23): 'none', (5, 23): 'none', (6, 23): 'none', (7, 23): 'none', (8, 23): 'wall', (9, 23): 'none', (10, 23): 'none', (11, 23): 'none', (12, 23): 'none', (13, 23): 'none', (14, 23): 'none', (15, 23): 'none', (16, 23): 'none', (17, 23): 'none', (18, 23): 'none', (19, 23): 'none', (20, 23): 'none', (21, 23): 'none', (22, 23): 'none', (23, 23): 'none', (24, 23): 'none', (0, 24): 'none', (1, 24): 'none', (2, 24): 'none', (3, 24): 'none', (4, 24): 'none', (5, 24): 'none', (6, 24): 'none', (7, 24): 'none', (8, 24): 'wall', (9, 24): 'none', (10, 24): 'none', (11, 24): 'none', (12, 24): 'none', (13, 24): 'none', (14, 24): 'none', (15, 24): 'none', (16, 24): 'none', (17, 24): 'none', (18, 24): 'none', (19, 24): 'none', (20, 24): 'none', (21, 24): 'none', (22, 24): 'none', (23, 24): 'none', (24, 24): 'none'}
    """
    rows = 25
    columns = 25
    dictionary = {(row, column): "none" for column in range(0, columns) for row in range(0, rows)}

    for row in range(0, rows):
        for column in range(0, columns):
            if column == 4 and row < 20:
                dictionary[(column, row)] = "wall"
            elif column == 8 and row > 3:
                dictionary[(column, row)] = "wall"
            elif column == 12 and row < 4:
                dictionary[(column, row)] = "wall"
            elif 12 <= column < 22 and row == 4:
                dictionary[(column, row)] = "wall"
            elif 20 >= row > 4 and column == 21:
                dictionary[(column, row)] = "wall"
            elif column == columns - 2 and row == 1:
                dictionary[(column, row)] = "boss"
    return dictionary


def print_board(board, character):
    """
    Prints the game board.

    :param character: a dictionary containing characters X,Y coordinate
    :param board: a dictionary representing the game board
    :precondition: character must be a valid dictionary containing the characters X,Y coordinates
    :precondition: board must be a valid dictionary representation of a game board
    :postcondition: displays the game_board for user
    """
    count = 0
    symbols = {"wall": " 🈵 ", "none": " ⏹ ", "boss": " ⚠️ "}
    print()
    for room in board:
        count += 1
        if room == (character["X-coordinate"], character["Y-coordinate"]):
            print(" 🚹 ", end='')
        else:
            print(symbols[board[room]], end='')
        if count >= math.sqrt(len(board)):
            count = 0
            print()


def check_if_boss(board, character):
    """
    Check if character is in boss room

    Checks the current location of the character to see if it is equal to the location of the
    boss on the board

    :param character: a dictionary containing characters X,Y coordinate
    :param board: a dictionary representing the game board
    :precondition: character must be a valid dictionary containing the characters X,Y coordinates
    :precondition: board must be a valid dictionary representation of a game board
    :postcondition: computes if the character is at the same location as boss
    :return: boolean value. true if the character is at the boss's location

    >>> test_character = {"X-coordinate":0, "Y-coordinate":0}
    >>> check_if_boss(make_board(), test_character)
    False

    >>> test_character = {"X-coordinate":23, "Y-coordinate":1}
    >>> check_if_boss(make_board(), test_character)
    True
    """
    room = (character["X-coordinate"], character["Y-coordinate"])
    if board[room] == "boss":
        return True
    return False


def make_character():
    """
    Create game character.

    :postcondition: return a new game character
    :return: a dictionary representing characters data.
    """
    character = {}
    classes = GET_CLASS_NAMES()
    character["name"] = check_quit(input("\nEnter your characters name: "))
    print_character_classes()
    choice = validate_num_choice("\nPls enter a valid choice: ", len(classes))
    character["class"] = classes[int(choice) - 1]
    character_attack_defense_levels = get_class_attack_defense_levels(character["class"])
    character["level"] = 1
    character["currentHP"] = 10.0
    character["weapon"] = 'melee'
    character['currentXP'] = 0
    character['levelUpXP'] = 100
    character["X-coordinate"] = 0
    character["Y-coordinate"] = 0
    character['accuracy'] = character_attack_defense_levels[0]
    character['strength'] = character_attack_defense_levels[1]
    character['weapon'] = 'spear'
    character['weaponMultiplier'] = 1
    character['resistance'] = character_attack_defense_levels[2]
    return character


def print_character_classes():
    """
    Print available character classes.

    :postcondition: prints the available classes
    """
    classes_descriptions = zip(GET_CLASS_NAMES(), GET_CLASS_DESCRIPTIONS())
    print('\nThese are the available classes:')
    quick_sleep()
    for count, (class_name, class_description) in enumerate(classes_descriptions, 1):
        print(count, class_name.upper(), ":", class_description)
        quick_sleep(0.2)


def foe_generator(level: int) -> dict:
    """
    Selects a foe from a list of foes at each level.

    :param level: an int 1,2,3,4 representing the level of the foe
    :precondition: level must be a valid integer in the range 1-4
    :postcondition: creates a new foe dictionary
    :return: a dictionary representing a random foes stats
    """
    one_enemy_names = ['Militia', 'Archer', 'Marksman']
    one_enemy_weapons = ['Spear', 'Bow', 'Cross-bow']
    two_enemy_names = ['Agile', 'Officer', 'Seeker']
    two_enemy_weapons = ['Dagger', 'Axe', 'Spear']
    three_enemy_names = ['Captain', 'Champion', 'Mercenary']
    three_enemy_weapons = ['Sword', 'Sword', 'Sword']
    level_one_enemies = list(map(generate_level_one_enemy, one_enemy_names, one_enemy_weapons))
    level_two_enemies = list(map(generate_level_two_enemy, two_enemy_names, two_enemy_weapons))
    level_three_enemies = list(map(generate_level_three_enemy, three_enemy_names,
                                   three_enemy_weapons))
    if level == 1:
        return random.choice(level_one_enemies)
    elif level == 2:
        return random.choice(level_two_enemies)
    elif level == 3:
        return random.choice(level_three_enemies)
    elif level == 4:
        return generate_boss_enemy("Megatron", "Swords and Lances")


def generate_level_one_enemy(name: str, weapon: str) -> dict:
    """
    Generates a new level one foe object.

    :param name: a string representing the name of the foe
    :param weapon: a string representing the weapon of the foe
    :precondition: name must be a valid string
    :precondition: weapon must be a valid string
    :postcondition: creates a new foe dictionary object
    :return: a dictionary representing the foes stats

    >>> generate_level_one_enemy("hah", "ABC") # doctest: +NORMALIZE_WHITESPACE
    {'name': 'hah', 'weapon': 'ABC', 'accuracy': 0.4, 'resistance': 0.4, 'strength': 0.4,
    'currentHP': 3, 'is_boss': False}
    """
    return {'name': name, 'weapon': weapon, 'accuracy': 0.4, 'resistance': 0.4,
            'strength': 0.4, 'currentHP': 3, 'is_boss': False}


def generate_level_two_enemy(name: str, weapon: str):
    """
    Generates a new level two foe object.

    :param name: a string representing the name of the foe
    :param weapon: a string representing the weapon of the foe
    :precondition: name must be a valid string
    :precondition: weapon must be a valid string
    :postcondition: creates a new foe dictionary object
    :return: a dictionary representing the foes stats

    >>> generate_level_two_enemy("hah", "ABC") # doctest: +NORMALIZE_WHITESPACE
    {'name': 'hah', 'weapon': 'ABC', 'accuracy': 0.7, 'resistance': 0.7, 'strength': 0.4,
    'currentHP': 5, 'is_boss': False}
    """
    return {'name': name, 'weapon': weapon, 'accuracy': 0.7, 'resistance': 0.7,
            'strength': 0.7, 'currentHP': 4, 'is_boss': False}


def generate_level_three_enemy(name: str, weapon: str):
    """
    Generates a new level three foe object.

    :param name: a string representing the name of the foe
    :param weapon: a string representing the weapon of the foe
    :precondition: name must be a valid string
    :precondition: weapon must be a valid string
    :postcondition: creates a new foe dictionary object
    :return: a dictionary representing the foes stats

    >>> generate_level_three_enemy("hah", "ABC") # doctest: +NORMALIZE_WHITESPACE
    {'name': 'hah', 'weapon': 'ABC', 'accuracy': 1.0, 'resistance': 1.5, 'strength': 1.5,
    'currentHP': 8, 'is_boss': False}
    """
    return {'name': name, 'weapon': weapon, 'accuracy': 1.2, 'resistance': 1.5,
            'strength': 1.2, 'currentHP': 6, 'is_boss': False}


def generate_boss_enemy(name: str, weapon: str):
    """
    Generates a new boss foe object.

    :param name: a string representing the name of the foe
    :param weapon: a string representing the weapon of the foe
    :precondition: name must be a valid string
    :precondition: weapon must be a valid string
    :postcondition: creates a new foe dictionary object
    :return: a dictionary representing the foes stats

    >>> generate_boss_enemy("hah", "ABC") # doctest: +NORMALIZE_WHITESPACE
    {'name': 'hah', 'weapon': 'ABC', 'accuracy': 1.0, 'resistance': 3.0, 'strength': 3.0,
    'currentHP': 10, 'is_boss': True}
    """
    return {'name': name, 'weapon': weapon, 'accuracy': 1.0, 'resistance': 3.0,
            'strength': 3.0, 'currentHP': 7, 'is_boss': True}


def increase_level(character: dict):
    """
    Increases the level of the game character.

    :param character: a dictionary containing characters X,Y coordinate
    :precondition: character must be a valid game character dictionary
    :postcondition: update the character dictionary to new level stats
    """
    skill_multiplier = 2

    if character['currentXP'] >= character['levelUpXP'] and character['level'] < 3:
        character['currentXP'] -= character['levelUpXP']
        character['level'] += 1
        character['currentHP'] = 10
        character['accuracy'] *= skill_multiplier
        character['strength'] *= skill_multiplier
        character['resistance'] *= skill_multiplier
        print(f"You have now leveled up to {get_class_level(character['level'])}")
        print("You have 50% more accuracy, strength, and resistance")

    return


def GET_CLASS_NAMES():
    """
    Get a list of class names.

    :return: a tuple containing all class names
    """
    classes = ('instigator', 'lurker', 'protector', 'distributor')
    return classes


def GET_CLASS_DESCRIPTIONS():
    """
    Get a list of class descriptions.

    :return: a list containing all class descriptions
    """
    return ['Loves chaos, uses whatever tools at their disposal.',
            'Slips into the background, Decent at everything.',
            'The guardians! most resistant to attacks',
            'Most accurate of the bunch.']


def get_class_level(level: int) -> str:
    """
    Get the name for the class level.

    :param level: an int representing the level of the character
    :precondition: level must be a valid integer in the range 1-3
    :postcondition: finds the name for the class level
    :return: a string representing the name of the class level

    >>> get_class_level(2)
    'lieutenant'
    """
    levels = ['trainee', 'lieutenant', 'warrior']
    return levels[level - 1]


def get_class_attack_defense_levels(class_name: str) -> list:
    """
    Get the attack and defence levels for the input class

    :param class_name: a string represting the class name
    :precondition: class_name must be a valid string representing a pre-defined class
    :postcondition: finds the attack and defense levels for the class
    :return: a list of integers in the order [accuracy, strength, resistance]

    >>> get_class_attack_defense_levels('lurker')
    [0.66, 0.66, 0.66]
    """
    class_attack_defense = {'instigator': [0.66, 0.99, 0.33],
                            'lurker': [0.66, 0.66, 0.66],
                            'protector': [0.33, 0.66, 0.99],
                            'distributor': [0.99, 0.66, 0.33]}
    return class_attack_defense[class_name]


def describe_current_location(character):
    """
    Print characters location (X,Y)

    :param character: a dictionary representing the game character
    :precondition: character must be a valid dictionary representation of game character
    :postcondition: print character coordinates
    """
    print("Your Coordinates are:")
    quick_sleep(0.5)
    print("X:", character["X-coordinate"], "Y:", character["Y-coordinate"])
    print()


def get_direction_choice():
    """
    Get direction user would like to move in.

    :postcondition: return a validated string representing the users direction choice
    :return: a string value w (up), d (right), s (down), a (left)
    """
    print("list of directions:")
    for letter, direction in zip(DIRECTION_COMMANDS(), LIST_OF_DIRECTIONS()):
        print(letter, direction)

    choice_is_valid = False
    choice = 0

    while not choice_is_valid:
        choice = check_quit(input("\nPls enter a valid choice: "))
        choice_is_valid = str(choice).strip().isalpha() and str(choice) in "wasd"
        if not choice_is_valid:
            print(red_text("Invalid Choice"))

    return choice


def check_quit(choice):
    """
    Check if user wishes to quit the game

    :param choice: a string representation of users input
    :precondition: choice must be a string
    :postcondition: quits the game if user enters q otherwise returns the input
    :return: choice if the choice is not q

    >>> check_quit("w")
    'w'
    """
    if choice.lower() == 'q' or choice.strip().lower() == 'q':
        print("\nGoodbye!")
        sys.exit()
    else:
        return choice


def validate_move(board, character, direction):
    """
    Checks if a users intended move is within the bounds of the game.

    :param board: a dictionary representing the game board
    :param character: a dictionary representing the game character
    :param direction: a string representing the direction the user wishes to move in
    :precondition: board is a valid game_board created using the make_board function
    :precondition: character is a valid dictionary representing the game character
    :precondition: direction is a valid string w,a,s, or d
    :postcondition: check if the users intended move is valid
    :return: return a boolean True if the move is valid, false if the move is invalid

    >>> game_character = {'X-coordinate': 0, 'Y-coordinate': 0}
    >>> validate_move(make_board(), game_character, "w")
    False

    >>> game_character = {'X-coordinate': 0, 'Y-coordinate': 0}
    >>> validate_move(make_board(), game_character, "d")
    True
    """
    direction = str(direction)
    direction_commands_list = DIRECTION_COMMANDS()
    if direction == direction_commands_list[0]:
        position = (character["X-coordinate"], character["Y-coordinate"] - 1)
        is_wall = check_wall_bounds(position, board)
        return not is_wall
    elif direction == direction_commands_list[1]:
        position = (character["X-coordinate"] + 1, character["Y-coordinate"])
        is_wall = check_wall_bounds(position, board)
        return not is_wall
    elif direction == direction_commands_list[2]:
        position = (character["X-coordinate"] - 1, character["Y-coordinate"])
        is_wall = check_wall_bounds(position, board)
        return not is_wall
    elif direction == direction_commands_list[3]:
        position = (character["X-coordinate"], character["Y-coordinate"] + 1)
        is_wall = check_wall_bounds(position, board)
        return not is_wall

    return True


def check_wall_bounds(destination_position, board):
    """
    Check if the intended position is a wall or outside the game board

    :param board: a dictionary representing the game board
    :param destination_position: a tuple representing the intended position of the character
    :precondition: board is a valid game_board created using the make_board function
    :precondition: destination_position is a valid tuple containing 2 ints
    :postcondition: check if the users intended move is a wall or outside the board
    :return: return a boolean True if the intended position is a wall, false otherwise

    >>> test_destination_position = (3, 3)
    >>> check_wall_bounds(test_destination_position, make_board())
    False

    >>> test_destination_position = (4, 4)
    >>> check_wall_bounds(test_destination_position, make_board())
    True
    """
    if destination_position in board:
        return board[destination_position] == 'wall'
    else:
        return True


def move_character(character, direction):
    """
    Move game character.

    :param character: a dictionary containing characters X,Y coordinate
    :param direction: a string representing the users intended game move
    :precondition: character must be a valid dictionary containing the characters X,Y coordinates
    :precondition: direction must be a string containing w (up), d (right), s (down), a (left)
    :postcondition: Update the characters location
    """
    direction = str(direction)
    if direction == "w":
        character["Y-coordinate"] -= 1

    if direction == "d":
        character["X-coordinate"] += 1

    if direction == "a":
        character["X-coordinate"] -= 1

    if direction == "s":
        character["Y-coordinate"] += 1


def LIST_OF_DIRECTIONS():
    """
    :return: a list of directions
    """
    return ['Up', 'Right', 'Left', 'Down']


def DIRECTION_COMMANDS():
    """
    :return: a list of direction commands
    """
    return ['w', 'd', 'a', 's']


def check_for_foes():
    """
    Check if the user has encountered any foes.

    Randomly returns true (25% chance) and false (75% chance) when the character moves on the game
    board.

    :postcondition: return a random boolean representing if you encounter a foe
    :return: a boolean. true if the character runs into an enemy
    """
    return random.choices((True, False), weights=[25, 75])[0]


def start_fight(character: dict, foe: dict):
    """
    Starts the fight if the player has chosen to fight the foe.

    :param character: a dictionary representing the characters stats
    :param foe: a dictionary representing the foes stats
    :precondition: character must be a valid dictionary created using the make_character function
    :precondition: foe must be a valid dictionary created using the enemy_generator function
    :postcondition: starts the fight if the player chooses to fight
    :postcondition: starts the character_flee function if the user chooses flee
    """
    print(f"\nYou have run into {foe['name']}")
    quick_sleep()
    if foe["is_boss"]:
        defeated = fight(character, foe)
        return defeated
    elif fight_or_flee():
        fight(character, foe)
    else:
        character_flees(character, foe)
    return


def fight_or_flee():
    """
    Get user choice to fight or flee

    :postcondition: computes the players choice to fight or flee
    :return: a bool. true if the player chooses to fight, false if the player chooses to flee
    """
    print('\nWould you like to:\n1. Fight\n2. Flee')
    fight_choice = validate_num_choice("Pls enter the corresponding number: ", 2)
    return int(fight_choice) == 1


def quick_sleep(timer: float = 1.0):
    """
    pauses the program for a period of time

    :param timer: length of time to sleep the program for
    :postcondition: sleep the function for the input amount of time
    """
    time.sleep(timer)


def fight(character: dict, foe: dict) -> bool:
    """
    Runs the fight between the character and foe

    :param character: a dictionary representing the characters stats
    :param foe: a dictionary representing the foes stats
    :precondition: character must be a valid dictionary created using the make_character function
    :precondition: foe must be a valid dictionary created using the enemy_generator function
    :postcondition: runs the fight between character and foe
    """
    select_attack(character)
    character_run_away = False

    while foe["currentHP"] > 0 and not character_run_away and character["currentHP"] > 0:
        print("\nNew round begins!\n")
        quick_sleep()

        if random.choices((True, False), weights=[foe['accuracy'] * 100,
                                                  (1 - foe['accuracy']) * 100])[0]:
            foe_strikes(character, foe)
            quick_sleep()
        else:
            print("\n{} misses you".format(foe['name']))
            quick_sleep()
        if random.choices((True, False), weights=[character['accuracy'] * 100,
                                                  (1 - character['accuracy']) * 100])[0]:
            character_strikes(character, foe)
            quick_sleep()
        else:
            print("You miss {}".format(foe['name']))
            quick_sleep()

        if foe["currentHP"] < 0:
            print("\nYou Killed {}.".format(foe['name']))
            print_character_stats(character)
            return True
        elif check_foe_flees():
            print(f"\n{foe['name']} runs away.")
            return True
        else:
            print_enemy_stats(foe)
            print_character_stats(character, foe['is_boss'])
            if not foe['is_boss']:
                choice = validate_num_choice("\nKeep fighting or flee?\n1. Fight\n2. Flee\n", 2)
                character_run_away = False if int(choice) == 1 \
                    else True
    if character_run_away:
        character_flees(character, foe)


def foe_strikes(character: dict, foe: dict):
    """
    Calculates the damage a strike by the foe does to character

    :param character: a dictionary representing the characters stats
    :param foe: a dictionary representing the foes stats
    :precondition: character must be a valid dictionary created using the make_character function
    :precondition: foe must be a valid dictionary created using the enemy_generator function
    :postcondition: updates the characters xp subtracting the damage done
    """
    damage = round(foe['strength'] / character['resistance'], 2)
    character["currentHP"] -= damage
    character["currentXP"] += 5
    print(red_text("{} strikes you with {}\n{} does {} damage\n".format(foe['name'],
                                                                        foe['weapon'],
                                                                        foe['name'],
                                                                        damage)))


def character_strikes(character: dict, foe: dict):
    """
    Calculates the damage a strike by the character does to foe

    :param character: a dictionary representing the characters stats
    :param foe: a dictionary representing the foes stats
    :precondition: character must be a valid dictionary created using the make_character function
    :precondition: foe must be a valid dictionary created using the enemy_generator function
    :postcondition: updates the foes xp subtracting the damage done
    """
    damage = round((character['strength'] * character['weaponMultiplier']) / foe['resistance'], 2)
    foe["currentHP"] -= damage
    character["currentXP"] += 10
    print(green_text(f"You struck {foe['name']} with {character['weapon']}\nYou did"
                     f" {damage} damage\n"))


def validate_num_choice(ask_input_string: str, max_choice: int) -> str:
    """
    Validates a number choice input by the player.

    :param ask_input_string: a string to present to the user, asking for their input
    :param max_choice: an integer representing the maximum number in the list of choices
    :precondition: ask_input_string must be a valid string
    :precondition: max_choice must be a valid int
    :postcondition: checks the user entered a valid choice, and asks for a valid choice if invalid
    :return: the user input as string
    """
    choice_is_valid = False
    choice = ""
    while not choice_is_valid:
        choice = check_quit(input(ask_input_string))
        choice_is_valid = str(choice).strip().isdigit() and 0 < int(choice) <= max_choice
        if not choice_is_valid:
            print(red_text("Invalid Choice"))

    return choice


def select_attack(character):
    """
    Select a weapon from the available weapons.

    :param character: a string to present to the user, asking for their input
    :precondition: character must be a valid dictionary representation of the game character
    :postcondition: checks the user entered a valid choice, and asks for a valid choice if invalid
    :return: the user input as string
    """
    all_attacks = ATTACKS()
    available_attacks = all_attacks[str(character['level'])]
    attacks_zip = {}
    print("\nNO Attack - strength:")
    for number, attack in zip("123456789", available_attacks):
        print(number, attack, "-", all_attacks[str(character['level'])][attack])
        attacks_zip[number] = attack
    choice = validate_num_choice("\nPls enter a weapon choice: ", len(available_attacks))
    character['weaponMultiplier'] = available_attacks[attacks_zip[choice]]
    character['weapon'] = attacks_zip[choice]

    return


def ATTACKS():
    """
    Get a dictionary of character attacks.

    :return: a dictionary of attacks split by character level
    """
    attacks = {
        '1': {'melee': 1, "Special spear": 1.2},
        '2': {'melee': 1, "spear": 1.1, "Special dagger": 1.2},
        '3': {'melee': 1, "spear": 1.1, "crossbow": 1.2, "Special sword": 1.5},
    }
    return attacks


def green_text(text):
    """
    Format text to print green text

    :return: a string of text formatted to print green text
    """
    return f"\033[1;32;40m{text}\033[0m"


def red_text(text):
    """
    Format text to print red text

    :return: a string of text formatted to print red text
    """
    return f"\033[1;31;40m{text}\033[0m"


def print_game_start():
    """
    Print player introduction to game
    """
    print("So boom, You're awoken by the sound of loud thunders.")
    quick_sleep(3)
    print("You have 10hp.")
    quick_sleep()
    print("Your goal is to get to the north east end of the map and defeat the boss.")
    quick_sleep(3)
    print("Follow the prompts provided by the game to get started.")
    quick_sleep(3)
    print("Bon Voyage!!")
    quick_sleep()
    print("🚹 - Your character")
    print("🈵 - Walls")
    print("⚠️ - Final Boss")
    return


def print_character_stats(character: dict, is_boss: bool = False):
    """
    Print character HP, XP and level
    """
    print("\nYou now have:")
    print("{:.2f} HP".format(character["currentHP"]))
    print("{} XP".format(character["currentXP"]))
    if not is_boss and character["currentXP"] < character['levelUpXP'] and character['level'] < 3:
        print(f"\nYou are a(n) {get_class_level(character['level'])}.\nYou need to have"
              f" {character['levelUpXP']} XP to advance to the next level\n")
    quick_sleep()


def print_enemy_stats(foe: dict):
    """
    Print foes HP
    """
    print("\nYour enemy has:")
    print("{:.2f} HP".format(foe["currentHP"]))
    quick_sleep()


def character_flees(character: dict, foe: dict):
    """
    Runs the character flee sequence

    :param character: a dictionary representing the characters stats
    :param foe: a dictionary representing the foes stats
    :precondition: character must be a valid dictionary created using the make_character function
    :precondition: foe must be a valid dictionary created using the enemy_generator function
    :postcondition: run the foe strike function if the character is struck as they run away
    """
    foe_damage_as_flee = random.choices((True, False), weights=[20, 80])[0]
    if foe_damage_as_flee:
        foe_strikes(character, foe)
        quick_sleep()
    return


def check_foe_flees():
    """
    Check if the foe flees.

    :postcondition: compute the random chance (20%) of the foe fleeing
    :return: a boolean. true if the foe flees, false otherwise
    """
    foe_flees = random.choices((True, False), weights=[20, 80])[0]
    return foe_flees


def game_finish(win: bool):
    """
    Print end to game sequence
    """
    if win:
        print('''
        
                                         .''.
               .''.             *''*    :_\/_:     .
              :_\/_:   .    .:.*_\/_*   : /\ :  .'.:.'.
          .''.: /\ : _\(/_  ':'* /\ *  : '..'.  -=:o:=-
         :_\/_:'.:::. /)\*''*  .|.* '.\'/.'_\(/_'.':'.'
         : /\ : :::::  '*_\/_* | |  -= o =- /)\    '  *
          '..'  ':::'   * /\ * |'|  .'/.\'.  '._____
              *        __*..* |  |     :      |.   |' .---"|
               _*   .-'   '-. |  |     .--'|  ||   | _|    |
            .-'|  _.|  |    ||   '-__  |   |  |    ||      |
            |' | |.    |    ||       | |   |  |    ||      |
         ___|  '-'     '    ""       '-'   '-.'    '`      |____
        jgs~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
        ------------------------------------------------
        
        ''')
    else:
        print("You lost. Better luck next time")


def game():
    """
    Runs the game loop.
    """
    print_game_start()
    game_board = make_board()
    character = make_character()
    print_board(game_board, character)
    defeated_boss = False

    while not defeated_boss and character["currentHP"] > 0:
        increase_level(character)
        describe_current_location(character)
        direction = get_direction_choice()
        valid_move = validate_move(game_board, character, direction)
        if valid_move:
            move_character(character, direction)
            print_board(game_board, character)
            boss_in_room = check_if_boss(game_board, character)
            if boss_in_room:
                defeated_boss = start_fight(character, foe_generator(4))
            else:
                there_is_a_challenger = check_for_foes()
                if there_is_a_challenger:
                    start_fight(character, foe_generator(character['level']))
        else:
            print_board(game_board, character)
            print(red_text("Invalid Move"))
    game_finish(defeated_boss)


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()
