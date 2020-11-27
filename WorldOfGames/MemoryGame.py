import live
import Score

def _generate_sequence():
    import time
    import random
    global random_list
    random_list = []
    for i in range(0, live.difficulty):
        n = random.randint(1, 101)
        random_list.append(n)
    print(random_list)
    time.sleep(0.7)
    print("\n" * 50)
    return random_list


def _get_list_from_user():
    global user_list
    user_list = []
    while True:
        try:
             for i in range(0, live.difficulty):
                user_numbers = int(input(f'enter {live.difficulty} numbers:'))
                user_list.append(user_numbers)
                print(user_list)
        except ValueError:
            print('ENTER A NUMBER')
            continue
        return user_list

def _is_list_equal():
    print(user_list == random_list)

def add_score():
    if user_list == random_list:
        Score.add_score()

def _play():
    _generate_sequence()
    _get_list_from_user()
    _is_list_equal()
    add_score()