import random
import time


def playGame():
    # List to hold game input
    gameList = []

    # While allGames is False continue this loop
    allGames = False
    while not allGames:
        allGames = True
        gameList.append(input('What game would you like to play?: '))
        ask = input('Add another game? (Y/N): ')
        if ask == 'n'.lower():
            allGames = True
        elif ask == 'y'.lower():
            allGames = False
        else:
            print('That is not a valid input.')
    print(f'Picking a game from {gameList}... ')
    time.sleep(1)
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    return random.choice(gameList)

print(playGame())