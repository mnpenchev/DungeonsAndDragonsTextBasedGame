from random import randint
import sys
import time
# https://stackoverflow.com/questions/287871/how-to-print-colored-text-in-terminal-in-python ***************************
from termcolor import colored


# delay print function *************************************************************************************************
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)


# clear console screen by adding empty lines ***************************************************************************
clear = "\n" * 100

# print the game prolog ********* print the game prolog ********* print the game prolog ********* print the game prolog
print(colored("Welcome to The road to Darromar, a turn style combat game,", 'blue'))
print(colored("based on D&D realm of Faerun.", 'blue'))
print('')
print(colored("You are an Adventurer, your ship arrived at Calimport last night.", 'blue'))
print(colored("and your mission is to cross the Calim Dessert and reach Darromar,", 'blue'))
print(colored("to meet with the rest of your party.", 'blue'))
print('')
print(colored("To defeat an enemy you must reduce their health to 0 \nby selecting actions from the combat menu.",
              'blue'))
print('')
print(colored("Good luck!", 'red'))

# Defining player hero - class, and attributes *************************Defining player hero - class, and attributes
warrior = {'name': 'Korgan the Dwarf', 'attack_min': 10, 'attack_max': 15, 'heal_min': 10, 'heal_max': 25,
           'health': 150, 'mana': 40, 'experience': 0, 'gold': 0, 'level': 1}
mage = {'name': 'Edwin the Red wizard', 'attack_min': 20, 'attack_max': 45, 'heal_min': 30, 'heal_max': 45,
        'health': 200, 'mana': 80, 'experience': 0, 'gold': 0, 'level': 1}
priest = {'name': 'Viconia the Dark elf', 'attack_min': 10, 'attack_max': 15, 'heal_min': 25, 'heal_max': 35,
          'health': 120, 'mana': 80, 'experience': 0, 'gold': 0, 'level': 1}
rogue = {'name': 'Yoshimo the Black heart', 'attack_min': 20, 'attack_max': 25, 'heal_min': 10, 'heal_max': 15,
         'health': 100, 'mana': 40, 'experience': 0, 'gold': 0, 'level': 1}

# picking up hero ****** picking up hero ******* picking up hero ******* picking up hero ******* picking up hero *******
while True:
    delay_print("\nPick up your hero!\n")
    print("\n1) Warrior: ")
    print("Health: ", warrior['health'], " Attack min: ", warrior['attack_min'], " Attack max: ", warrior['attack_max'])
    print("Mana: ", warrior['mana'], " Heal min: ", warrior['heal_min'], "Heal max: ", warrior['heal_max'])
    print("\n2) Mage: ")
    print("Health: ", mage['health'], " Attack min: ", mage['attack_min'], " Attack max: ", mage['attack_max'])
    print("Mana: ", mage['mana'], " Heal min: ", mage['heal_min'], "Heal max: ", mage['heal_max'])
    print("\n3) Priest: ")
    print("Health: ", priest['health'], " Attack min: ", priest['attack_min'], " Attack max: ", priest['attack_max'])
    print("Mana: ", priest['mana'], " Heal min: ", priest['heal_min'], "Heal max: ", priest['heal_max'])
    print("\n4) Rogue: ")
    print("Health: ", rogue['health'], " Attack min: ", rogue['attack_min'], " Attack max: ", rogue['attack_max'])
    print("Mana: ", rogue['mana'], " Heal min: ", rogue['heal_min'], "Heal max: ", rogue['heal_max'])
    player_class = input("\nSelect your class: ")

    if player_class == "1":
        player_class = warrior
        print("\nYou have selected the Warrior: ", warrior['name'])
        break
    if player_class == "2":
        player_class = mage
        print("\nYou have selected the Mage: ", mage['name'])
        break
    if player_class == "3":
        player_class = priest
        print("\nYou have selected the Priest: ", priest['name'])
        break
    if player_class == "4":
        player_class = rogue
        print("\nYou have selected the Rogue: ", rogue['name'])
        break
    else:
        print("\nPlease select a valid class.")
        continue
player_max_health = player_class['health']

print(player_class['name'], ", this is where your story begins....")

# LEVEL UP FUNCTION **************LEVEL UP FUNCTION **************LEVEL UP FUNCTION ******************LEVEL UP FUNCTION
def level_up(player_class, player_max_health):
    while True:
        player_max_health += 20
        player_class['health'] = player_max_health
        player_class['attack_min'] += 5
        player_class['attack_max'] += 5
        player_class['heal_min'] += 5
        player_class['heal_max'] += 5
        return player_class, player_max_health


# calculate player ATTACK and HEAL functions ******* calculate player ATTACK and HEAL functions ***********************
def calculate_player_heal():
    return randint(player_class['heal_min'], player_class['heal_max'])


def calculate_player_attack():
    return randint(player_class['attack_min'], player_class['attack_max'])


def calculate_player_heavy_attack():
    return randint(player_class['attack_min'] / 2, player_class['attack_max'] * 2)


player_normal_attack = calculate_player_attack()
player_heal = calculate_player_heal()
player_heavy_attack = calculate_player_heavy_attack()


while True:
# picking up an opponent # GAME LOOP ****** picking up an opponent # GAME LOOP ******picking up an opponent # GAME LOOP
    enemy1 = {'name': 'Ogre', 'attack_min': 20, 'attack_max': 25, 'heal_min': 10, 'heal_max': 15,
              'health': 150, 'max_health': 150, 'mana': 20, 'experience': 5, 'gold_min': 5, 'gold_max': 12}
    enemy2 = {'name': 'Kobold', 'attack_min': 10, 'attack_max': 15, 'heal_min': 20, 'heal_max': 25,
              'health': 80, 'max_health': 80, 'mana': 80, 'experience': 2, 'gold_min': 1, 'gold_max': 3}
    enemy3 = {'name': 'Skeleton', 'attack_min': 10, 'attack_max': 15, 'heal_min': 25, 'heal_max': 35,
              'health': 100, 'max_health': 100, 'mana': 40, 'experience': 3, 'gold_min': 2, 'gold_max': 4}
    enemy4 = {'name': 'Fire Mephit', 'attack_min': 20, 'attack_max': 25, 'heal_min': 10, 'heal_max': 15,
              'health': 100, 'max_health': 100, 'mana': 80, 'experience': 3, 'gold_min': 4, 'gold_max': 5}
    enemy5 = {'name': 'Ghast', 'attack_min': 10, 'attack_max': 15, 'heal_min': 50, 'heal_max': 15,
              'health': 60, 'max_health': 60, 'mana': 80, 'experience': 2, 'gold_min': 1, 'gold_max': 3}

    print(player_class['name'], 'have', str(colored(player_class['health'], 'red')),
          colored('health and', 'red'), str(colored(player_class['mana'], 'blue')), colored(' mana left', 'blue'), player_class['experience'], 'experience', player_class['gold'], 'gold.')

    enemy = randint(1, 5)
    if enemy == 1:
        enemy = enemy1
        print("\nYou are fighting", enemy['name'], "with", enemy['health'], "health!")
    if enemy == 2:
        enemy = enemy2
        print("\nYou are fighting", enemy['name'], "with", enemy['health'], "health!")
    if enemy == 3:
        enemy = enemy3
        print("\nYou are fighting", enemy['name'], "with", enemy['health'], "health!")
    if enemy == 4:
        enemy = enemy4
        print("\nYou are fighting", enemy['name'], "with", enemy['health'], "health!")
    if enemy == 5:
        enemy = enemy5
        print("\nYou are fighting", enemy['name'], "with", enemy['health'], "health!")


# Calculate enemy attack and heal functions *************************** Calculate enemy attack and heal functions

    def calculate_enemy_heal():
        return randint(enemy['heal_min'], enemy['heal_max'])


    def calculate_enemy_attack():
        return randint(enemy['attack_min'], enemy['attack_max'])


    def calculate_enemy_heavy_attack():
        return randint(enemy['attack_min'] / 2, enemy['attack_max'] * 2)


    def calculate_enemy_gold_drop():
        return randint(enemy['gold_min'], enemy['gold_max'])


    enemy_normal_attack = calculate_enemy_attack()
    enemy_heal = calculate_enemy_heal()
    enemy_heavy_attack = calculate_enemy_heavy_attack()
    enemy_gold_drop = calculate_enemy_gold_drop()

# Hero turn *** Hero turn **** Hero turn **** Hero turn **** Hero turn **** Hero turn **** Hero turn **** Hero turn ****
    while True:
        print("\nPlease select action:\n")
        print("1) Normal attack")
        print("2) Heavy attack")
        print("3) Heal")
        player_select = input()

        if player_select == "1":
            enemy['health'] = enemy['health'] - player_normal_attack
            print(clear)
            print(player_class['name'], "attacked the", enemy['name'], "for", str(player_normal_attack), "damage")

        elif player_select == "2":
            enemy['health'] = enemy['health'] - player_heavy_attack
            print(clear)
            print(player_class['name'], "attacked the", enemy['name'], "for", str(player_heavy_attack), "damage")

        elif player_select == "3":
            player_class['health'] = player_class['health'] + player_heal
# ************ NO OVERHEAL ALLOWED! *****NO OVERHEAL ALLOWED! *****NO OVERHEAL ALLOWED! *****NO OVERHEAL ALLOWED! *****
            if player_class['health'] + player_heal > player_max_health:
                player_class['health'] = player_max_health
            print(clear)
            print(player_class['name'], "healed for", player_heal, "health")
        else:
            print(clear)
            print(colored("Invalid input, please enter option from the menu.", 'red'))
            continue
# in case player loose the fight, the game is over. ********** in case player LOOSE the FIGHT, the GAME IS OVER. ******
        if player_class['health'] <= 0:
            print(player_class['name'], "have been defeated.")
            break
# in case player win the fight, the game continue. ******************in case player win the fight, the game continue.***
        elif enemy['health'] <= 0:
            print("You have defeated", enemy['name'], "and received", enemy['experience'], "experience and",
                  enemy_gold_drop, "gold")
            player_class['experience'] = player_class['experience'] + enemy['experience']
            player_class['gold'] = player_class['gold'] + enemy_gold_drop
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
            player_class['health'] = player_class['health'] - enemy_normal_attack
            print(enemy['name'], "did", str(enemy_normal_attack), "damage!\n")

        elif enemy_select == 2:
            player_class['health'] = player_class['health'] - enemy_heavy_attack
            print(enemy['name'], "did", str(enemy_heavy_attack), "damage!\n")

        elif enemy_select == 3:
            enemy['health'] = enemy['health'] + enemy_heal
            if enemy['health'] + enemy_heal > enemy['max_health']:
# ************ NO OVERHEAL ALLOWED! *****NO OVERHEAL ALLOWED! *****NO OVERHEAL ALLOWED! *****NO OVERHEAL ALLOWED! *****
                enemy['health'] = enemy['max_health']
            print(enemy['name'], "healed for", enemy_heal, "health\n")

# display health and mana after every round ************************** display health and mana after every round ****
        if enemy['health'] >= 0 and player_class['health'] >= 0:
            print("#" * 60)
            print(player_class['name'], 'have', str(colored(player_class['health'], 'red')),
                  colored(' health and ', 'red'), str(
                    colored(player_class['mana'], 'blue')), colored(' mana left', 'blue'))
            print(enemy['name'], ' have ', str(colored(enemy['health'], 'red')), colored(' health left', 'red'))
            print("#" * 60)

# in case player loose the fight, the game is over. ********** in case player LOOSE the FIGHT, the GAME IS OVER. ******
        if player_class['health'] <= 0:
            print(player_class['name'], "have been defeated.")
            break
# in case player win the fight, the game continue. ******************in case player win the fight, the game continue.***
        elif enemy['health'] <= 0:
            print("You have defeated", enemy['name'], "and received", enemy['experience'], "experience and",
                  enemy_gold_drop, "gold")
            player_class['experience'] = player_class['experience'] + enemy['experience']
            player_class['gold'] = player_class['gold'] + enemy_gold_drop
            player_class['health'] = player_max_health
            if player_class['experience'] >= 10:
                player_class['level'] += 1
                print("Congratulations! You reached level", player_class['level'], "!")
                print("Your Health is increased by 20 and attack and heal by 5!")
                player_class, player_max_health = level_up(player_class, player_max_health)
                player_class['experience'] = 0
            break

    if player_class['health'] <= 0:
        print("\nYou lost your live! \n ***** GAME OVER *****")
        break
