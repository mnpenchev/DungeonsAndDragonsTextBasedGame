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
fighter = {'name': 'Korgan', 'attack_num': 3, 'attack_dice': 10, 'max_health': 250, 'health': 250, 'AC': 15, 'dex': 16,
           'experience': 0,
           'gold': 0,
           'level': 1}
mage = {'name': 'Edwin', 'attack_num': 2, 'attack_dice': 10, 'max_health': 200, 'health': 200, 'AC': 12, 'dex': 15,
        'experience': 0,
        'gold': 0,
        'level': 1}
cleric = {'name': 'Viconia', 'attack_num': 2, 'attack_dice': 10, 'max_health': 200, 'health': 120, 'AC': 12, 'dex': 15,
          'experience': 0,
          'gold': 0,
          'level': 1}
rogue = {'name': 'Yoshimo', 'attack_num': 4, 'attack_dice': 10, 'max_health': 160, 'health': 100, 'AC': 14, 'dex': 18,
         'experience': 0,
         'gold': 0,
         'level': 1}

# picking up hero ****** picking up hero ******* picking up hero ******* picking up hero ******* picking up hero *******
while True:
    delay_print("\nPick up a hero!\n")
    print("\n1) Fighter: ")
    print("Name:", fighter['name'], "\nHealth:", fighter['health'], "/ Attack: 3d10 / Armor class", fighter['AC'])
    print("\n2) Mage: ")
    print("Name:", mage['name'], "\nHealth:", mage['health'], "/ Attack: 2d10 / Armor class", mage['AC'])
    print("\n3) Priest: ")
    print("Name:", cleric['name'], "\nHealth:", cleric['health'], "/ Attack: 2d10 / Armor class", cleric['AC'])
    print("\n4) Rogue: ")
    print("Name:", rogue['name'], "\nHealth:", rogue['health'], "/ Attack: 4d10 / Armor class", rogue['AC'])
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


##print(player_class['name'], ", this is where your story begins....\n")

# LEVEL UP FUNCTION **************LEVEL UP FUNCTION **************LEVEL UP FUNCTION ******************LEVEL UP FUNCTION
def level_up(player_class):
    player_class['max_health'] += dice(2, 10)
    player_class['health'] = player_class['max_health']
    player_class['attack_dice'] += dice(1, 5)
    return player_class


##def level_up1(mainhero):
##        mainhero['max_health'] += dice(2, 10)
##        mainhero['health'] = mainhero['max_health']
##        mainhero['attack_dice'] += dice(1, 5)
##        return mainhero


while True:
    # picking up an opponent # GAME LOOP ****** picking up an opponent # GAME LOOP ******
    monster1 = {'name': 'Ogre', 'attack_num': 2, 'attack_dice': 10, 'health': 150, 'max_health': 150, 'AC': 12,
                'dex': 13,
                'experience': 5, 'gold': dice(1, 10)}
    monster2 = {'name': 'Kobold', 'attack_num': 2, 'attack_dice': 10, 'health': 80, 'max_health': 80, 'AC': 13,
                'dex': 14,
                'experience': 2, 'gold': dice(1, 10)}
    monster3 = {'name': 'Skeleton', 'attack_num': 2, 'attack_dice': 10, 'health': 100, 'max_health': 100, 'AC': 13,
                'dex': 14,
                'experience': 3, 'gold': dice(1, 10)}
    monster4 = {'name': 'Goblin', 'attack_num': 2, 'attack_dice': 10, 'health': 100, 'max_health': 100, 'AC': 12,
                'dex': 14,
                'experience': 3, 'gold': dice(1, 10)}
    monster5 = {'name': 'Ghast', 'attack_num': 2, 'attack_dice': 10, 'health': 80, 'max_health': 80, 'AC': 12,
                'dex': 13,
                'experience': 2, 'gold': dice(1, 10)}

    ## print(mainhero['name'], 'have', str(colored(mainhero['health'], 'red')),
    ##      colored('health left', 'red'), mainhero['experience'], 'experience', mainhero['gold'], 'gold.')

    print(player_class['name'], 'have', colored(player_class['max_health'], 'red'), "/",
          colored(player_class['health'], 'red'),
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
    def combat(a, b):
        while True:
            print("\nPlease select action:\n")
            print("1) Normal attack")
            print("2) Heavy attack")
            print("3) Heal")
            player_select = input()

            if player_select == "1":
                if dice(1, 20) + a['dex'] - 7 > b['AC']:
                    b['health'] = b['health'] - dice(a['attack_num'], a['attack_dice'])
                    print(clear)
                    print(a['name'], "attacked the", b['name'], "for", dice(a['attack_num'], a['attack_dice']), "damage")
                else:
                    print(clear)
                    print(a['name'], "missed!")

            elif player_select == "2":
                if dice(1, 20) + a['dex'] - 10 > b['AC']:
                    b['health'] = b['health'] - dice(round(a['attack_num'] / 2), a['attack_dice'] + 10)
                    print(clear)
                    print(a['name'], "attacked the", b['name'], "for",
                          dice(round(a['attack_num'] / 2), a['attack_dice'] + 10), "damage")
                else:
                    print(clear)
                    print(a['name'], "missed!")

            elif player_select == "3":
                a['health'] = a['health'] + dice(a['attack_num'], a['attack_dice'])
                # ***** NO OVERHEAL ALLOWED! ****
                if a['health'] + dice(a['attack_num'],
                                      a['attack_dice']) > a['max_health']:
                    a['health'] = a['max_health']
                print(clear)
                print(a['name'], "healed for", dice(a['attack_num'], a['attack_dice']),
                      "health")
            else:
                print(clear)
                print(colored("Invalid input, please enter option from the menu.", 'red'))
                continue

            if b['health'] <= 0:
                print("You have defeated", b['name'], "and received", b['experience'], "experience and", enemy['gold'],
                      "gold\n")
                a['experience'] = a['experience'] + b['experience']
                a['gold'] = a['gold'] + b['gold']
                a['health'] = a['health'] + dice(5, 10)
                print(a['name'], "restored", dice(5, 10), "health after the fight\n")
                if a['health'] + dice(a['attack_num'], a['attack_dice']) > a['max_health']:
                    a['health'] = a['max_health']
                if a['experience'] >= 10:
                    a['level'] += 1
                    print(colored("Congratulations! You reached level", "blue"), colored(a['level'], "blue"),
                          colored("!", "blue"))
                    a = level_up(a)
                    a['experience'] = 0
                break

            if b['health'] >= (b['max_health'] / 2):
                enemy_select = randint(1, 2)
            else:
                enemy_select = randint(1, 3)

            if enemy_select == 1:
                if dice(1, 20) + b['dex'] - 7 > a['AC']:
                    a['health'] = a['health'] - dice(b['attack_num'], b['attack_dice'])
                    print(b['name'], "did", dice(b['attack_num'], b['attack_dice']), "damage!\n")
                else:
                    print(b['name'], "missed!")

            elif enemy_select == 2:
                if dice(1, 20) + b['dex'] - 10 > a['AC']:
                    a['health'] = a['health'] - dice(round(b['attack_num'] / 2),
                                                     b['attack_dice'] + 10)
                    print(b['name'], "did", dice(round(b['attack_num'] / 2), b['attack_dice'] + 10), "damage!\n")
                else:
                    print(b['name'], "missed!")

            elif enemy_select == 3:
                b['health'] = b['health'] + dice(b['attack_num'], b['attack_dice'])
                if b['health'] + dice(b['attack_num'], b['attack_dice']) > b['max_health']: b['health'] = b[
                    'max_health']
                print(b['name'], "healed for", dice(b['attack_num'], b['attack_dice']), "health\n")

            # display health after every round
            if b['health'] >= 0 and a['health'] >= 0:
                do_health(a['name'], a['health'], a['max_health'])
                do_health(b['name'], b['health'], b['max_health'])

            # in case player loose the fight, the game is over.
            if a['health'] <= 0:
                print(a['name'], "have been defeated.")
                delay_print(colored("\nYou lost your live! \n **************** GAME OVER ****************", "red"))
                break


    combat(player_class, enemy)
