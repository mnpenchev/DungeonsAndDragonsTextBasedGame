from random import randint

game_running = True

game_results = []
def calculate_monster_attack():
    return randint(monster['attack_min'], monster['attack_max'] )
def calculate_heal():
    return randint(player['heal_min'], player['heal_max'])

while game_running == True:
    counter = 0
    new_round = True
    player = {'name': '', 'attack': 10, 'heal_min': 15, 'heal_max':25, 'health': 100, 'mana': 40}
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
        print("2) Heal")
        print("3) Exit Game")
        print("4) Show Highscores")
        print("---" * 7)

        player_choice = input()

        if player_choice == '1':
            monster['health'] = monster['health'] - player['attack']
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
            elif player['mana'] <= 0:
                print('Not enough mana!')
                player['health'] = player['health'] - calculate_monster_attack()
            if player['health'] > 100:
                player['health'] = 100
            player['health'] = player['health'] - calculate_monster_attack()
            if player['health'] <= 0:
                monster_won = True

        elif player_choice == '3':
            new_round = False
            game_running = False

        elif player_choice == '4':
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