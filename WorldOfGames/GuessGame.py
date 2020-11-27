import live
import time
import Score
def _generate_number():
    import random
    global secret_number
    secret_number = random.randint(1, live.difficulty)
    return secret_number

def _get_guess_from_user():
    global number
    while True:
        try:
            number = int(input(f'enter a number between 1 - {live.difficulty}:'))
            while number <1 or number > live.difficulty:
                number = int(input(f'enter a number between 1 - {live.difficulty}:'))
        except ValueError:
            print('INSERT A NUMBER')
            continue
        return number


def _compare_results():
    print(secret_number == number)
    time.sleep(2)

def add_score():
    if secret_number == number:
        Score.add_score()

def _play():
    _generate_number()
    _get_guess_from_user()
    _compare_results()
    add_score()





