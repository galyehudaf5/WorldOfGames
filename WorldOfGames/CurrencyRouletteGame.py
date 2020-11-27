import live
import Score


def _get_money_interval():
    from forex_python.converter import CurrencyRates
    import random
    global usd_number, t, low, high, user_input
    usd_number = random.randint(1, 100)
    c = CurrencyRates()
    t = c.convert('USD', 'ILS', usd_number)
    low = t - (5-live.difficulty)
    high = t + (5-live.difficulty)
    return usd_number, t, low, high

def _get_guess_from_user():
    print(f'how much does {usd_number} USD worth in ILS? ')
    global user_input
    while True:
        try:
            user_input = int(input('enter a number:'))
        except ValueError:
            print('ENTER A NUMBER')
            continue
        if user_input >= int(low) and user_input <= int(high):
            print('TRUE')
        else:
            print('FALSE')
        return user_input

def add_score():
    if user_input >= int(low) and user_input <= int(high):
        Score.add_score()

def _play():
    _get_money_interval()
    _get_guess_from_user()
    add_score()
