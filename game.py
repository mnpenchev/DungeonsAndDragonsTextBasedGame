from random import randint
import sys
import time
# https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python ***************************
from termcolor import colored


# delay print function ***** delay print function ***** delay print function ***** delay print function *****
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


# ROLL DICE FUNCTIONS ******** ROLL DICE FUNCTIONS ******** ROLL DICE FUNCTIONS ******** ROLL DICE FUNCTIONS *****
def side(sides):
    return randint(1, sides)


def dice(n, sides):
    return sum(tuple(side(sides) for i in range(n)))


# display health bars
def do_health(hero_name, current_health, maximum_health):
    healthDashes = 40
    dashConvert = int(maximum_health / healthDashes)
    currentDashes = int(current_health / dashConvert)
    remainingHealth = healthDashes - currentDashes

    healthDisplay = '#' * currentDashes
    remainingDisplay = '-' * remainingHealth
    percent = str(
        int((current_health / maximum_health) * 100)) + "%"
    print(colored(hero_name, "red"))
    print("|" + healthDisplay + " " + colored(percent, "red") + " " + remainingDisplay + "|",
          colored(maximum_health, "red"), "/", colored(current_health, "red"))


# clear console screen by adding empty lines *************************** clear console screen by adding empty lines
clear = "\n" * 100

# print the game prolog ********* print the game prolog ********* print the game prolog ********* print the game prolog
print(colored("Welcome to The road to Darromar, a turn style combat game,", 'blue'))
print(colored("based on Dungeons & Dragons realm of Faerun.\n", 'blue'))
print(colored("You are an Adventurer, your ship arrived at Calimport last night.", 'blue'))
print(colored("and your mission is to cross the Calim Dessert and reach Darromar,", 'blue'))
print(colored("to meet with the rest of your party.\n", 'blue'))
print(colored("To defeat an enemy you must reduce their health to 0 \nby selecting actions from the combat menu.\n",
              'blue'))
print(colored("Good luck!", 'red'))

# Defining player hero - class, and attributes *********************** Defining player hero - class, and attributes
## mainhero = {'name': 'Playername', 'attack_num': 2, 'attack_dice': 20, 'health': 100, 'AC': 10, 'init': 14, 'experience': 0, 'gold': 0,
##           'level': 1}
fighter = {'name': 'Korgan', 'attack_num': 3, 'attack_dice': 20, 'health': 250, 'AC': 15, 'init': 16, 'experience': 0,
           'gold': 0,
           'level': 1}
mage = {'name': 'Edwin', 'attack_num': 2, 'attack_dice': 15, 'health': 200, 'AC': 12, 'init': 10, 'experience': 0,
        'gold': 0,
        'level': 1}
cleric = {'name': 'Viconia', 'attack_num': 1, 'attack_dice': 15, 'health': 120, 'AC': 12, 'init': 11, 'experience': 0,
          'gold': 0,
          'level': 1}
rogue = {'name': 'Yoshimo', 'attack_num': 4, 'attack_dice': 15, 'health': 100, 'AC': 14, 'init': 18, 'experience': 0,
         'gold': 0,
         'level': 1}

# picking up hero ****** picking up hero ******* picking up hero ******* picking up hero ******* picking up hero *******
while True:
    delay_print("\nPick up a hero!\n")
    print("\n1) Fighter: ")
    print("Name:", fighter['name'], "\nHealth:", fighter['health'], "/ Attack: 3d15 / Armor class", fighter['AC'])
    print("\n2) Mage: ")
    print("Name:", mage['name'], "\nHealth:", mage['health'], "/ Attack: 3d15 / Armor class", mage['AC'])
    print("\n3) Priest: ")
    print("Name:", cleric['name'], "\nHealth:", cleric['health'], "/ Attack: 1d15 / Armor class", cleric['AC'])
    print("\n4) Rogue: ")
    print("Name:", rogue['name'], "\nHealth:", rogue['health'], "/ Attack: 3d15 / Armor class", rogue['AC'])
    player_class = input("\nSelect your class: ")

    if player_class == "1":
        player_class = fighter
        print("\nYou have selected the Fighter: ", fighter['name'])
        break
    if player_class == "2":
        player_class = mage
        print("\nYou have selected the Mage: ", mage['name'])
        break
    if player_class == "3":
        player_class = cleric
        print("\nYou have selected the Cleric: ", cleric['name'])
        break
    if player_class == "4":
        player_class = rogue
        print("\nYou have selected the Rogue: ", rogue['name'])
        break
    else:
        print(colored("\nPlease select a valid class.", "red"))
        continue

## for some reason level_up func not work properly with player_class['max_health'] so im using variable for max health

# mainhero_max_health = mainhero['health']
player_max_health = player_class['health']


##print(player_class['name'], ", this is where your story begins....\n")

# LEVEL UP FUNCTION **************LEVEL UP FUNCTION **************LEVEL UP FUNCTION ******************LEVEL UP FUNCTION
def level_up(player_class, player_max_health):
    while True:
        player_max_health += dice(2, 10)
        player_class['health'] = player_max_health
        player_class['attack_dice'] += dice(1, 5)
        return player_class, player_max_health


##def level_up1(mainhero, mainhero_max_health):
##    while True:
##        mainhero_max_health += dice(2, 10)
##        mainhero['health'] = player_max_health
##        mainhero['attack_dice'] += dice(1, 5)
##        return mainhero, mainhero_max_health


while True:
    # picking up an opponent # GAME LOOP ****** picking up an opponent # GAME LOOP ******picking up an opponent # GAME LOOP
    monster1 = {'name': 'Ogre', 'attack_num': 2, 'attack_dice': 20, 'health': 150, 'max_health': 150, 'AC': 15,
                'init': 13,
                'experience': 5, 'gold': dice(1, 10)}
    monster2 = {'name': 'Kobold', 'attack_num': 1, 'attack_dice': 20, 'health': 80, 'max_health': 80, 'AC': 10,
                'init': 12,
                'experience': 2, 'gold': dice(1, 10)}
    monster3 = {'name': 'Skeleton', 'attack_num': 2, 'attack_dice': 15, 'health': 100, 'max_health': 100, 'AC': 10,
                'init': 11,
                'experience': 3, 'gold': dice(1, 10)}
    monster4 = {'name': 'Goblin', 'attack_num': 2, 'attack_dice': 20, 'health': 100, 'max_health': 100, 'AC': 10,
                'init': 10,
                'experience': 3, 'gold': dice(1, 10)}
    monster5 = {'name': 'Ghast', 'attack_num': 2, 'attack_dice': 10, 'health': 60, 'max_health': 60, 'AC': 10,
                'init': 13,
                'experience': 2, 'gold': dice(1, 10)}

    ## print(mainhero['name'], 'have', str(colored(mainhero['health'], 'red')),
    ##      colored('health left', 'red'), mainhero['experience'], 'experience', mainhero['gold'], 'gold.')

    print(player_class['name'], 'have', colored(player_max_health, 'red'), "/", colored(player_class['health'], 'red'),
          colored('health', 'red'), player_class['experience'], 'experience', player_class['gold'], 'gold.')

    enemy = randint(1, 5)
    if enemy == 1:
        enemy = monster1
        print("\nYou are fighting", enemy['name'], "with", colored(enemy['health'], "red"), colored("health!", "red"))
    if enemy == 2:
        enemy = monster2
        print("\nYou are fighting", enemy['name'], "with", colored(enemy['health'], "red"), colored("health!", "red"))
    if enemy == 3:
        enemy = monster3
        print("\nYou are fighting", enemy['name'], "with", colored(enemy['health'], "red"), colored("health!", "red"))
    if enemy == 4:
        enemy = monster4
        print("\nYou are fighting", enemy['name'], "with", colored(enemy['health'], "red"), colored("health!", "red"))
    if enemy == 5:
        enemy = monster5
        print("\nYou are fighting", enemy['name'], "with", colored(enemy['health'], "red"), colored("health!", "red"))

    # Hero turn *** Hero turn **** Hero turn **** Hero turn **** Hero turn **** Hero turn **** Hero turn ****
    while True:
        print("\nPlease select action:\n")
        print("1) Normal attack")  # add info
        print("2) Heavy attack")  # add info
        print("3) Heal")  # add info
        player_select = input()

        if player_select == "1":
            enemy['health'] = enemy['health'] - dice(player_class['attack_num'], player_class['attack_dice'])
            print(clear)
            print(player_class['name'], "attacked the", enemy['name'], "for",
                  dice(player_class['attack_num'], player_class['attack_dice']), "damage")

        elif player_select == "2":
            enemy['health'] = enemy['health'] - dice(round(player_class['attack_num'] / 2),
                                                     player_class['attack_dice'] + 10)
            print(clear)
            print(player_class['name'], "attacked the", enemy['name'], "for",
                  dice(round(player_class['attack_num'] / 2), player_class['attack_dice'] + 10), "damage")

        elif player_select == "3":
            player_class['health'] = player_class['health'] + dice(player_class['attack_num'],
                                                                   player_class['attack_dice'])
            # ***** NO OVERHEAL ALLOWED! **** NO OVERHEAL ALLOWED! **** NO OVERHEAL ALLOWED! **** NO OVERHEAL ALLOWED!
            if player_class['health'] + dice(player_class['attack_num'],
                                             player_class['attack_dice']) > player_max_health:
                player_class['health'] = player_max_health
            print(clear)
            print(player_class['name'], "healed for", dice(player_class['attack_num'], player_class['attack_dice']),
                  "health")
        else:
            print(clear)
            print(colored("Invalid input, please enter option from the menu.", 'red'))
            continue

        if enemy['health'] <= 0:
            print("You have defeated", enemy['name'], "and received", enemy['experience'], "experience and",
                  enemy['gold'], "gold\n")
            player_class['experience'] = player_class['experience'] + enemy['experience']
            player_class['gold'] = player_class['gold'] + enemy['gold']
            player_class['health'] = player_class['health'] + dice(5, 10)
            print(player_class['name'], "restored", dice(5, 10), "health after the fight\n")
            if player_class['health'] + dice(player_class['attack_num'],
                                             player_class['attack_dice']) > player_max_health:
                player_class['health'] = player_max_health
            if player_class['experience'] >= 10:
                player_class['level'] += 1
                print("\nCongratulations! You reached level", player_class['level'], "!")
                print("\nYour Health is increased by 20 and attack and heal by 5!\n")
                player_class, player_max_health = level_up(player_class, player_max_health)
                player_class['experience'] = 0
            break
        # ENEMY TURN ***** ENEMY TURN ***** ENEMY TURN ***** ENEMY TURN ***** ENEMY TURN ***** ENEMY TURN ***** ENEMY TURN *****
        if enemy['health'] >= (enemy['max_health'] / 2):
            enemy_select = randint(1, 2)
        else:
            enemy_select = randint(1, 3)

        if enemy_select == 1:
            player_class['health'] = player_class['health'] - dice(enemy['attack_num'], enemy['attack_dice'])
            print(enemy['name'], "did", dice(enemy['attack_num'], enemy['attack_dice']), "damage!\n")

        elif enemy_select == 2:
            player_class['health'] = player_class['health'] - dice(round(enemy['attack_num'] / 2),
                                                                   enemy['attack_dice'] + 10)
            print(enemy['name'], "did", dice(round(enemy['attack_num'] / 2), enemy['attack_dice'] + 10), "damage!\n")

        elif enemy_select == 3:
            enemy['health'] = enemy['health'] + dice(enemy['attack_num'], enemy['attack_dice'])
            if enemy['health'] + dice(enemy['attack_num'], enemy['attack_dice']) > enemy['max_health']:
                # ************ NO OVERHEAL ALLOWED! *****NO OVERHEAL ALLOWED! *****NO OVERHEAL ALLOWED! *****NO OVERHEAL ALLOWED! *****
                enemy['health'] = enemy['max_health']
            print(enemy['name'], "healed for", dice(enemy['attack_num'], enemy['attack_dice']), "health\n")

        # display health and mana after every round ************************** display health and mana after every round ****
        if enemy['health'] >= 0 and player_class['health'] >= 0:
            do_health(player_class['name'], player_class['health'], player_max_health)
            do_health(enemy['name'], enemy['health'], enemy['max_health'])

        # in case player loose the fight, the game is over. ********** in case player LOOSE the FIGHT, the GAME IS OVER. ******
        if player_class['health'] <= 0:
            print(player_class['name'], "have been defeated.")
            break

    if player_class['health'] <= 0:
        delay_print(colored("\nYou lost your live! \n ******************** GAME OVER ********************", "red"))
        break