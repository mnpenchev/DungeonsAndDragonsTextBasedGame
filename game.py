from random import randint
import datetime
import time

ts = time.time()
sttime = datetime.datetime.fromtimestamp(ts).strftime('%d %m %Y %H:%M:%S')

game_running = True

print("Welcome to The road to Darromar, a turn style combat game,")
print("based on D&D realm of Faerun.")
print("You are an Adventurer, your ship arrived at Calimport last night.")
print("and your mission is to cross the Calim Dessert and reach Darromar,")
print("to meet with the rest of your party.")
print("To defeat an enemy you must reduce their health to 0 \nby selecting actions from the combat menu. ")
print("Good luck!")


def calculate_monster_attack():
    return randint(monster['attack_min'], monster['attack_max'])


def calculate_heal():
    return randint(player['heal_min'], player['heal_max'])


def calculate_player_attack():
    return randint(player['attack_min'], player['attack_max'])


def calculate_player_heavy_attack():
    return randint(player['attack_min'] / 2, player['attack_max'] * 2)


# def miss_chance():
#    return randint(1, 2)
#   if miss_chance() == 1:
#       print(player['name'] + " missed!")
#   else:

while game_running is True:  # while game is running there is a round counter
    counter = 0
    new_round = False
    player = {'name': '', 'attack_min': 10, 'attack_max': 12, 'heal_min': 15, 'heal_max': 25, 'health': 100, 'mana': 40,
              'Shield_bash': 1}
    monster = {'name': 'Ogre', 'attack_min': 10, 'attack_max': 15, 'health': 100}

    print("---" * 7)
    print("Please select action:")
    print("Enter 1 to Start a new game")
    print("Enter 2 to Show Highscores")
    print("Enter 3 to Exit Game")
    print("---" * 7)
    player_select = input()

    if player_select == '1':
        new_round = True
        print("---" * 7)
        print('Enter Player name:')  # input for the player name goes into the player list
        player["name"] = input()
        print("---" * 7)
        print(player['name'] + ' has ' + str(player['health']) + ' health and ' + str(player['mana']) + ' mana left')
        print(monster['name'] + ' has ' + str(monster['health']) + ' health left')

    elif player_select == '2':
        with open('highscores.txt', 'r') as f:  # reading the highscores from highscores.txt read only
            f.content = f.read()
            print(f.content)

    elif player_select == '3':
        new_round = False
        game_running = False

    else:
        print("Invalid input, enter number from the menu below")

    while new_round is True:  # with this while loop every new round is set
        counter = counter + 1
        player_won = False
        monster_won = False

        print("#####" * 8)  # EVERY ROUND MENU IS SET HERE
        print("Round " + str(counter) + ": Please select action:")
        print("1) Attack - Deals " + str(player['attack_min']) + " - " + str(player['attack_max']) + " damage.")

        if player['mana'] > 0:  # this is how action 2 gets hidden when run out of mana
            print("2) Heal - Restore " + str(player['heal_min']) + " - " + str(
                player['heal_max']) + " health and cost 10 mana. \n Beware! Monster will attack you while you heal!")
            if player['mana'] <= 0:
                print("Invalid Input")

        if player['Shield_bash'] > 0:
            print("3) Shield bash - Stuns the target for the current turn and deals " + str(
                int(player['attack_min'] / 2)) + " - " + str(
                int(player['attack_max'] / 2)) + " damage. \n Recharges every 5th round.")

        print("4) Heavy attack - deals " + str(int(player['attack_min'] / 2)) + " - " + str(
            int(player['attack_max'] * 2)) + " damage.")
        print("#####" * 8)

        player_choice = input()  # input numbers to select actions

        if player_choice == '1':
            Att = calculate_player_attack()
            monster['health'] = monster['health'] - Att
            print(player['name'] + " attacked the " + monster['name'] + " for " + str(Att) + " damage")
            if monster['health'] <= 0:
                player_won = True
            else:
                Matt = calculate_monster_attack()
                player['health'] = player['health'] - Matt
                print(monster['name'] + " attacked " + player['name'] + " for " + str(Matt) + " damage")
                if player['health'] <= 0:
                    monster_won = True

        elif player_choice == '2':
            if player['mana'] > 0:
                Heal = calculate_heal()
                player['health'] = player['health'] + Heal
                print(player['name'] + " Heal restored " + str(Heal) + " health and spent 10 mana.")
                player['mana'] = player['mana'] - 10

                Matt = calculate_monster_attack()
                player['health'] = player['health'] - Matt
                print(monster['name'] + " attacked " + player['name'] + " for " + str(Matt) + " damage")
                if player['health'] > 100:
                    player['health'] = 100  # no overheal allowed!
            elif player['mana'] <= 0:
                print('Not enough mana!')
                counter = counter - 1
                if player['health'] <= 0:
                    monster_won = True

        elif player_choice == '3':
            if counter % 5 == 0:
                player['Shield_bash'] = + 1
            elif player['Shield_bash'] > 0:
                Sb = calculate_player_attack() / 2
                monster['health'] = monster['health'] - Sb
                print(
                    "Monster is stunned for this round, " + player['name'] + " Shield bash done " + str(int(Sb)) + " damage to " +
                    monster['name'])
                player['Shield_bash'] = -1
            elif player['Shield_bash'] <= 0:
                print('Shield bash is still recharging!')
                counter = counter - 1
            elif monster['health'] <= 0:
                player_won = True

        elif player_choice == '4':
            heat = calculate_player_heavy_attack()
            monster['health'] = monster['health'] - heat
            print(player['name'] + " attacked the " + monster['name'] + " for " + str(heat) + " damage")
            if monster['health'] <= 0:
                player_won = True
            else:
                Matt = calculate_monster_attack()
                player['health'] = player['health'] - Matt
                print(monster['name'] + " attacked " + player['name'] + " for " + str(Matt) + " damage")
                if player['health'] <= 0:
                    monster_won = True

        else:
            print("Invalid input, please choose option from the menu below.")
            counter = counter - 1

        if player_won is False and monster_won is False:  # display health and mana after every round
            print("---" * 7)
            print(
                player['name'] + ' has ' + str(player['health']) + ' health and ' + str(player['mana']) + ' mana left')
            print(monster['name'] + ' has ' + str(monster['health']) + ' health left')

        if player_won:
            print(player['name'] + " attack killed the " + monster['name'])
            print(player['name'] + ' Wins!')
            round_result = {'name': player['name'], 'health': player['health'], 'rounds': counter, 'time': sttime}
            with open('highscores.txt', 'a') as f:
                f.write('%s\n' % round_result)
            new_round = False

        if monster_won:
            print(player['name'] + " has been killed by " + monster['name'])
            print(monster['name'] + ' Wins!')
            print("GAME OVER")
            round_result = {'name': player['name'], 'health': player['health'], 'rounds': counter, 'time': sttime}
            with open('highscores.txt', 'a') as f:
                f.write('%s\n' % round_result)
            new_round = False
