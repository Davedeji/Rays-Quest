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

    :param rows: an integer representing the number of rows on the game board
    :param columns: an integer representing the number of columns on the game board
    :precondition: rows is a valid positive, non-zero integer
    :precondition: columns is a valid positive, non-zero integer
    :postcondition: return a game board with rooms and descriptions
    :return: a dictionary representing the gameboard.(key: (row,column), value: room description)
    """

    rows = 25
    columns = 25
    dictionary = {}
    descriptions = ["Empty Room", "Snake hisses at you", "Chipmunk says hi", "James runs away"]
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
            elif 9 <= row <= 17 and 12 <= column <= 17:
                dictionary[(column, row)] = "mystery"
            elif column == columns - 2 and row == 1:
                dictionary[(column, row)] = "boss"
            else:
                dictionary[(column, row)] = "none"
    return dictionary


def print_board(board, character=None):
    count = 0
    symbols = {"wall": " 🈵 ", "mystery": " ✳️ ", "none": " ⏹ ", "boss": " ⚠️ "}
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


def make_character():
    """
    Create game character.

    :postcondition: return a new game character
    :return: a dictionary representing characters coordinates and health

    >>> make_character()
    {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
    """
    character = {}
    classes = get_class_names()

    character["name"] = input("Enter your characters name: ")
    print('These are the available classes:')
    for count, a_class in enumerate(classes, 1):
        print(count, a_class)
    character["class"] = classes[int(input("Choose a class:")) - 1]
    character_attack_defense_levels = get_class_attack_defense_levels(character["class"])
    character["level"] = 1
    character["currentHP"] = 10.0
    character["weapon"] = 'melee'
    character["maxHP"] = 10.0
    character['currentXP'] = 0
    character["X-coordinate"] = 0
    character["Y-coordinate"] = 0
    character['accuracy'] = character_attack_defense_levels[0]
    character['strength'] = character_attack_defense_levels[1]
    character['resistance'] = character_attack_defense_levels[2]

    return character


def enemy_generator(level: int) -> dict:
    level_one_enemies = [generate_level_one_enemy('Militia', 'spear'), generate_level_one_enemy(
        'Archer', 'Bow'), generate_level_one_enemy('Marksman', 'Cross-bow')]
    level_two_enemies = [generate_level_two_enemy('Agile', 'dagger'), generate_level_two_enemy(
        'Officer', 'axe'), generate_level_two_enemy('Seeker', 'spear')]
    level_three_enemies = [generate_level_three_enemy('Captain', 'Sword'),
                           generate_level_three_enemy('Champion', 'Sword'),
                           generate_level_three_enemy('Mercenary', 'Sword')]
    if level == 0:
        return random.choice(level_one_enemies)
    elif level == 1:
        return random.choice(level_two_enemies)
    elif level == 2:
        return random.choice(level_three_enemies)


def generate_level_one_enemy(name: str, weapon: str):
    return {'name': name, 'weapon': weapon, 'accuracy': 0.33, 'resistance': 0.33,
            'strength': 0.33, 'currentHP': 2}


def generate_level_two_enemy(name: str, weapon: str):
    return {'name': name, 'weapon': weapon, 'accuracy': 0.66, 'resistance': 0.66,
            'strength': 0.66, 'currentHP': 4}


def generate_level_three_enemy(name: str, weapon: str):
    return {'name': name, 'weapon': weapon, 'accuracy': 0.99, 'resistance': 0.99,
            'strength': 0.99, 'currentHP': 6}


def increase_level(character: dict):
    level_increase_xp = 100
    skill_multiplier = 1.5

    if character['currentXP'] >= level_increase_xp:
        character['currentXP'] -= level_increase_xp
        character['level'] += 1
        character['accuracy'] *= skill_multiplier
        character['strength'] *= skill_multiplier
        character['resistance'] *= skill_multiplier

    return


def get_class_names():
    return ['instigator', 'lurker', 'protector', 'distributor']


def get_class_descriptions():
    return ['Loves chaos, uses whatever tools at their disposal.',
            'Slips into the background, Decent at everything.',
            'The guardians! most resistant to attacks',
            'Most accurate of the bunch.']


def get_class_levels():
    return ['trainee', 'lieutenant', 'warrior']


def get_class_weapons(class_name: str):
    class_weapons = {'instigator': ['melee', 'fist', 'sword'],
                     'lurker': ['melee', 'fist', 'sword'],
                     'protector': ['melee', 'fist', 'sword'],
                     'distributor': ['melee', 'fist', 'sword']}
    return class_weapons[class_name]


def get_class_attack_defense_levels(class_name: str) -> list:
    # list formatted as [accuracy, strength, resistance]
    class_attack_defense = {'instigator': [0.66, 0.99, 0.33],
                            'lurker': [0.66, 0.66, 0.66],
                            'protector': [0.33, 0.66, 0.99],
                            'distributor': [0.99, 0.66, 0.33]}
    return class_attack_defense[class_name]


def describe_current_location(character):
    """
    Print characters location (X,Y) and description of location.

    :param board: a dictionary representing the game board
    :param character: a dictionary representing the game character
    :precondition: board must be a valid dictionary representation of a game board
    :precondition: character must be a valid dictionary representation of game character
    :postcondition: print character coordinates and room description
    """
    print("Your Coordinates are:")
    print("X:", character["X-coordinate"], "Y:", character["Y-coordinate"])
    print()
    # print(board[character["X-coordinate"], character["Y-coordinate"]])


def get_user_choice():
    """
    Get direction user would like to move in.

    :postcondition: return a validated string representing the users direction choice
    :return: a string value 1 (North),2 (East),3 (West),4 (South)
    """
    print("list of directions:")
    for number, direction in enumerate(list_of_directions(), 1):
        print(number, direction)

    choice_is_valid = False
    choice = 0

    while not choice_is_valid:
        choice = input("\nPls enter a choice between 1 and 4: ")
        choice_is_valid = str(choice).strip().isdigit() and str(choice) in "1234"

    return choice


def validate_move(rows, columns, board, character, direction):
    """
    Checks if a users intended move is within the bounds of the game board.

    :param rows: an int representing the rows of the board
    :param columns: an int representing the column of the board
    :param character: a dictionary representing the game character
    :param direction: a string representing the direction the user wishes to move in
    :precondition: rows is a valid int > 2
    :precondition: column is a valid int > 2
    :precondition: character is a valid dictionary representing the game character
    :precondition: direction is a valid string 1,2,3, or 4
    :postcondition: Compute and return the validity of the move
    :return: return a boolean True if the move is valid

    >>> game_character = make_character()
    >>> validate_move(3, 3, game_character, "2")
    True

    >>> game_character = make_character()
    >>> game_character["X-coordinate"] = 3
    >>> validate_move(3, 3, game_character, "2")
    False
    """
    direction = str(direction)
    proposed_position = (character["X-coordinate"], character["Y-coordinate"])

    if direction == "1":
        position = (character["X-coordinate"], character["Y-coordinate"] - 1)
        is_wall = check_wall(position, board)
        return not is_wall

    elif direction == "2":
        position = (character["X-coordinate"] + 1, character["Y-coordinate"])
        is_wall = check_wall(position, board)
        return not is_wall

    elif direction == "3":
        position = (character["X-coordinate"] - 1, character["Y-coordinate"])
        is_wall = check_wall(position, board)
        return not is_wall

    elif direction == "4":
        position = (character["X-coordinate"], character["Y-coordinate"] + 1)
        is_wall = check_wall(position, board)
        return not is_wall

    return True


def check_wall(character_position, board):
    # print("check Position")
    # print(board)
    # print("character position", character_position)
    # print("board position", board[character_position])
    if character_position in board:
        print(board[character_position] == 'wall')
        return board[character_position] == 'wall'
    else:
        return True

def move_character(character, direction):
    """
    Move game character.

    :param character: a dictionary containing characters X,Y coordinate
    :param direction: a string representing the users intended game move
    :precondition: character must be a valid dictionary containing the characters X,Y coordinates
    :precondition: direction must be a string containg 1 (North),2 (East),3 (West),4 (South)
    :postcondition: Update the characters location
    """
    direction = str(direction)
    if direction == "1":
        character["Y-coordinate"] -= 1

    if direction == "2":
        character["X-coordinate"] += 1

    if direction == "3":
        character["X-coordinate"] -= 1

    if direction == "4":
        character["Y-coordinate"] += 1


def list_of_directions():
    return ['north', 'east', 'west', 'south']


def check_if_goal_attained(rows, columns, character):
    """
    Move game character.

    :param rows: an int representing the rows of the board
    :param columns: an int representing the column of the board
    :param character: a dictionary containing characters X,Y coordinate
    :precondition: character must be a valid dictionary containing the characters X,Y coordinates
    :precondition: rows is a valid int > 2
    :precondition: column is a valid int > 2
    :postcondition: check if user has reached the goal and return boolrsn
    :return: a boolean. returns true if user has reached the goal

    >>> game_character = make_character()
    >>> game_character["X-coordinate"] = 3
    >>> game_character["Y-coordinate"] = 3
    >>> check_if_goal_attained(4, 4, game_character)
    True
    """
    if character["X-coordinate"] == rows - 1 and character["Y-coordinate"] == columns - 1:
        return True
    else:
        return False


def check_for_foes():
    """
    Check if the user has encountered any foes.

    Randomly returns true (25% chance) and false (75% chance) when the character moves on the game
    board.

    :postcondition: return a random boolean representing if you encounter a foe
    :return: a boolean. true if the character runs into an enemy
    """
    return random.choices((True, False), weights=[20, 80])[0]


def run_fight(character: dict, foe: dict):
    if fight_or_flee():
        attack_foe(character, foe)
    else:
        character_flees(character, foe)


def fight_or_flee():
    print('Would you like to:\n1. Fight\n2. Flee')

    fight_choice = int(input("Pls enter the corresponding number:"))
    return fight_choice == 1


def quick_sleep():
    time.sleep(1)


def attack_foe(character: dict, foe: dict):
    character_run_away = False

    while foe["currentHP"] > 0 and not character_run_away:
        print("\nNew round begins!")
        quick_sleep()

        if random.choices((True, False), weights=[foe['accuracy'] * 100, (1 - foe['accuracy']) * 100])[0]:
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
            print("\nYou miss {}".format(foe['name']))
            quick_sleep()

        print_enemy_stats(foe)
        print_character_stats(character)
        if foe["currentHP"] < 0.1:
            foe["currentHP"] = 0
            print("\nYou devastated {}.".format(foe['name']))

        else:
            character_run_away = False if int(input("\nKeep fighting or flee?\n1. Fight\n2. Flee\n")) == 1 \
                else True
    if character_run_away:
        character_flees(character, foe)


def foe_strikes(character: dict, foe: dict):
    damage = round(foe['strength'] / character['resistance'], 2)
    character["currentHP"] -= damage
    character["currentXP"] += 1
    print("\n{} strikes you with {}\n{} does {} damage".format(foe['name'], foe['weapon'],
                                                               foe['name'],
                                                               damage))


def character_strikes(character: dict, foe:dict):
    damage = round(character['strength'] / foe['resistance'], 2)
    foe["currentHP"] -= damage
    character["currentXP"] += 3
    print("\nYou struck {}\nYou did {} damage".format(foe['name'], damage))

def print_character_stats(character: dict):
    print("\nYou now have:")
    print("{} HP".format(character["currentHP"], ".2f"))
    print("{} XP".format(character["currentXP"]))
    print("\nYou are level {}.\nYou need to have 100 XP to advance to the next level".
          format(character["level"]))
    quick_sleep()


def print_enemy_stats(foe: dict):
    print("\nYour enemy has:")
    print("{} HP".format(foe["currentHP"], ".2f"))
    quick_sleep()


def character_flees(character: dict, foe: dict):
    foe_damage_as_flee = random.choices((True, False), weights=[20, 80])[0]
    if foe_damage_as_flee:
        foe_strikes(character, foe)
        quick_sleep()


def check_fight_continues(foe):
    fight_continues = foe['hp'] > 0
    foe_flees = random.choices((True, False), weights=[20, 80])[0]

    return fight_continues and not foe_flees


def guessing_game(character):
    """
    Generates a random number and asks the user to guess the number.

    :param character: a dictionary representing the game character
    :precondition: character is a valid dictionary representing the game character
    :postcondition: runs a guessing game and updates the users hp
    """
    print("You have encountered a foe")
    correct_guess = str(random.choice(range(1, 6)))

    user_guess_is_valid = False
    user_guess = 0

    while not user_guess_is_valid:
        user_guess = (input("You must guess a number between 1 & 5:"))
        user_guess_is_valid = str(user_guess).strip().isdigit() and str(user_guess) in "12345"

    if user_guess != correct_guess:
        character["Current HP"] -= 1
        print("\nYou Guessed Wrong. The correct guess was {}".format(correct_guess))
        print("Your HP is now {}".format(character["Current HP"]))
    else:
        print("\nYou Guessed right! Be on yur merry way")


def is_alive(character):
    """
    Checks if the game_character is alive (HP > 0).

    :param character: a dictionary representing the game character
    :precondition: character is a valid dictionary representing the game character
    :postcondition: Check if characters HP > 0 and return booleam
    :return: boolean value. True if the character has > 0 HP

    >>> game_character = {'X-coordinate': 0, 'Y-coordinate': 0, 'Current HP': 5}
    >>> is_alive(game_character)
    True
    """

    return character["Current HP"] > 0


def game():
    """
    Runs the game loop.
    """
    game_board = make_board()
    character = make_character()

    defeated_boss = False
    while not defeated_boss and character["currentHP"] > 0:
        print_board(game_board, character)
        describe_current_location(character)
        direction = get_user_choice()
        valid_move = validate_move(25, 25, game_board, character, direction)
        if valid_move:
            move_character(character, direction)
            there_is_a_challenger = check_for_foes()
            print("is challenger", there_is_a_challenger)
            if there_is_a_challenger:
                run_fight(character, enemy_generator(0))
            defeated_boss = False
    # game_board = make_board()
    # print_board(game_board, 25)
    # game_character = make_character()
    # enemy = enemy_generator(0)
    # # print(fight_or_flee())
    # attack_foe(game_character, enemy)






    # board = make_board(rows, columns)
    # character = make_character()
    # achieved_goal = False
    # while not achieved_goal and is_alive(character):
    #     describe_current_location(board, character)
    #     direction = get_user_choice()
    #     valid_move = validate_move(rows, columns, character, direction)
    #     if valid_move:
    #         move_character(character, direction)
    #         there_is_a_challenger = check_for_foes()
    #         if there_is_a_challenger:
    #             guessing_game(character)
    #         achieved_goal = check_if_goal_attained(rows, columns, character)
    #     else:
    #         print("\nYou can't go im that direction")
    # print("Congrats you made it to the end")


def main():
    """
    Drive the program.
    """
    game()


if __name__ == "__main__":
    main()
