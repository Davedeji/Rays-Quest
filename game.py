"""
Your name: Adedeji Toki
Your student number: A01243794

All of your code must go in this file.
"""
import random
import sys
import time
import math
from itertools import count


def make_board():
    """
    Create a game board (represented as a dictionary).

    :postcondition: return a game board with rooms and descriptions
    :return: a dictionary representing the gameboard.(key: (row,column), value: room description)
    """
    rows = 25
    columns = 25
    board = {(row, column): "none" for column in range(0, columns) for row in range(0, rows)}

    for row in range(0, rows):
        for column in range(0, columns):
            if column == 4 and row < 20:
                board[(column, row)] = "wall"
            elif column == 8 and row > 3:
                board[(column, row)] = "wall"
            elif column == 12 and row < 4:
                board[(column, row)] = "wall"
            elif 12 <= column < 22 and row == 4:
                board[(column, row)] = "wall"
            elif 20 >= row > 4 and column == 21:
                board[(column, row)] = "wall"
            elif column == columns - 2 and row == 1:
                board[(column, row)] = "boss"
    return board


def print_board(board, character):
    """
    Prints the game board.

    :param character: a dictionary containing characters X,Y coordinate
    :param board: a dictionary representing the game board
    :precondition: character must be a valid dictionary containing the characters X,Y coordinates
    :precondition: board must be a valid dictionary representation of a game board
    :postcondition: displays the game_board for user
    """
    counter = 0
    symbols = {"wall": " 🈵 ", "none": " ⏹ ", "boss": " ⚠️ "}
    print()
    for room in board:
        counter += 1
        if room == (character["X-coordinate"], character["Y-coordinate"]):
            print(" 🚹 ", end='')
        else:
            print(symbols[board[room]], end='')
        if counter >= math.sqrt(len(board)):
            counter = 0
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
    for number, (class_name, class_description) in enumerate(classes_descriptions, 1):
        print(number, class_name.upper(), ":", class_description)
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
    for number, attack in zip(count(start=1, step=1), available_attacks):
        print(number, attack, "-", all_attacks[str(character['level'])][attack])
        attacks_zip[number] = attack
    choice = validate_num_choice("\nPls enter a weapon choice: ", len(available_attacks))
    character['weaponMultiplier'] = available_attacks[attacks_zip[int(choice)]]
    character['weapon'] = attacks_zip[int(choice)]

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
    print("You can enter 'q' at any point to quit the game")
    quick_sleep()
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
