from random import randint

game_running = True

game_results = []                    # the game results list, empty at the beginning
def calculate_monster_attack():
    return randint(monster['attack_min'], monster['attack_max'])
def calculate_heal():
    return randint(player['heal_min'], player['heal_max'])
def calculate_player_attack():
    return randint(player['attack_min'], player['attack_max'])

while game_running == True:
    counter = 0
    new_round = True
    player = {'name': '', 'attack_min': 10, 'attack_max': 12, 'heal_min': 15, 'heal_max':25, 'health': 100, 'mana': 40}
    monster = {'name': 'Ogre', 'attack_min': 10, 'attack_max': 15, 'health': 100}

    print("---" * 7)
    print('Enter Player name:')
    player["name"] = input()
    print("---" * 7)
    print(player['name'] + ' has ' + str(player['health']) + ' health and ' + str(player['mana']) + ' mana left')
    print(monster['name'] + ' has ' + str(monster['health']) + ' health left')

    while new_round == True:

        counter = counter + 1
        player_won = False
        monster_won = False

        print("---" * 7)
        print("Please select action:")
        print("1) Attack")
        if player['mana'] > 0:
            print("2) Heal - cost 10 mana")
            if player['mana'] <= 0:
                print("Invalid Input")
        print("3) Shield block")
        print("4) Exit Game")
        print("5) Show Highscores")
        print("---" * 7)

        player_choice = input()

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
            pass

        elif player_choice == '4':
            new_round = False
            game_running = False

        elif player_choice == '5':
            for item in game_results:
                print(item)
                print("---" * 7)
        else:
            print('Invalid input')

        if player_won == False and monster_won == False:
            print("---" * 7)
            print(player['name'] + ' has ' + str(player['health']) + ' health and ' + str(player['mana']) + ' mana left')
            print(monster['name'] + ' has ' + str(monster['health']) + ' health left')

        elif player_won:
            print(player['name'] + ' Wins!')
            round_result = {'name': player['name'], 'health': player['health'], 'rounds': counter}
            game_results.append(round_result)
            new_round = False

        if monster_won:
            print(monster['name'] + ' Wins!')
            round_result = {'name': player['name'], 'health': player['health'], 'rounds': counter}
            game_results.append(round_result)
            new_round = False

    if player_won == True or monster_won == True:
        print("---" * 7)
        print("Please select action:")
        print("1) Start a new game")
        print("2) Show Highscores")
        print("3) Exit Game")
        print("---" * 7)
        if
