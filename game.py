from random import randint
from datetime import datetime

now = datetime.now()

game_running = True


def calculate_monster_attack():
    return randint(monster['attack_min'],
                   monster['attack_max'])  # function to randomise monster attack between min and max value


def calculate_heal():
    return randint(player['heal_min'], player['heal_max'])


def calculate_player_attack():
    return randint(player['attack_min'], player['attack_max'])


while game_running is True:  # while game is running there is a round counter and the new round is set
    counter = 0
    new_round = False
    player = {'name': '', 'attack_min': 10, 'attack_max': 12, 'heal_min': 15, 'heal_max': 25, 'health': 100, 'mana': 40}
    monster = {'name': 'Ogre', 'attack_min': 10, 'attack_max': 15, 'health': 100}

    print("---" * 7)
    print("Please select action:")
    print("1) Start a new game")
    print("2) Show Highscores")
    print("3) Exit Game")
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
        # new_round = True
    elif player_select == '3':
        new_round = False
        game_running = False
    else:
        print("Invalid input")

    while new_round is True:  # every new round is set

        counter = counter + 1
        player_won = False
        monster_won = False

        print("---" * 7)  # EVERY ROUND MENU IS SET HERE
        print("Please select action:")
        print("1) Attack")
        if player['mana'] > 0:  # this is how action 2 gets hidden when run out of mana
            print("2) Heal - cost 10 mana")
            if player['mana'] <= 0:
                print("Invalid Input")
        print("3) Shield block")
        print("4) Exit Game")
        print("---" * 7)

        player_choice = input()  # input numbers to select actions

        if player_choice == '1':
            monster['health'] = monster['health'] - calculate_player_attack()
            if monster['health'] <= 0:
                player_won = True
            else:
                player['health'] = player['health'] - calculate_monster_attack()
                if player['health'] <= 0:
                    monster_won = True

        elif player_choice == '2':
            if player['mana'] > 0:
                player['health'] = player['health'] + calculate_heal()
                player['mana'] = player['mana'] - 10
                player['health'] = player['health'] - calculate_monster_attack()
                if player['health'] > 100:
                    player['health'] = 100
            elif player['mana'] <= 0:
                print('Not enough mana!')
                if player['health'] <= 0:
                    monster_won = True

        elif player_choice == '3':
            monster['health'] = monster['health'] - calculate_player_attack() / 2
            if monster['health'] <= 0:
                player_won = True
            else:
                player['health'] = player['health'] - calculate_monster_attack() / 2
                if player['health'] <= 0:
                    monster_won = True

        elif player_choice == '4':  # exit game method
            new_round = False
            game_running = False

        else:
            print('Invalid input')

        if player_won is False and monster_won is False:  # method to display health and mana after every round
            print("---" * 7)
            print(
                player['name'] + ' has ' + str(player['health']) + ' health and ' + str(player['mana']) + ' mana left')
            print(monster['name'] + ' has ' + str(monster['health']) + ' health left')
# to do - like -> print "%s Has %s health and %s mana left." % (player['name'], str(player['health'], str(player['mana'])

        if player_won:
            print(player['name'] + ' Wins!')
            round_result = {'name': player['name'], 'health': player['health'], 'rounds': counter}
            with open('highscores.txt', 'a') as f:  # write round_result to highscores.txt file, append
                f.write('%s\n' % round_result)  # to do - add date time stamp to the result
            new_round = False

        if monster_won:
            print(monster['name'] + ' Wins!')
            round_result = {'name': player['name'], 'health': player['health'], 'rounds': counter}
            with open('highscores.txt', 'a') as f:
                f.write('%s\n' % round_result)
            new_round = False
