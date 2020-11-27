def _welcome(name):
    name = input('enter name:')
    print(f'Hello {name} and welcome to the World of Games (WoG).Here you can find many cool games to play.')


def _load_game():
    global choice, difficulty
    print('''Please choose a game to play:
       1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
       2. Guess Game - guess a number and see if you chose like the computer
       3. Currency Roulette - try and guess the value of a random amount of USD in ILS''')
    while True:
        try:
            choice = int(input('enter a number: '))
            while choice > 3 or choice < 1:
                choice = int(input('please enter a number between 1-3'))
            difficulty = int(input('Please choose game difficulty from 1 to 5:'))
            while difficulty > 5 or difficulty < 1:
                difficulty = int(input('Please choose game difficulty from 1 to 5:'))
        except ValueError:
            print('insert a number')
            continue
        return choice, difficulty







