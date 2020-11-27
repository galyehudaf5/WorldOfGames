import live
def add_score():
    global final_score, current_score, POINTS_OF_WINNING
    while True:
        try:
            f = open('Scores.txt', 'r')
            current_score = f.read()
            POINTS_OF_WINNING = (live.difficulty * 3) + 5
            final_score = int(current_score) + POINTS_OF_WINNING
            x = open('Scores.txt', 'w+')
            x.write(str(final_score))
        except IOError:
            y = open('New_Scores.txt', 'w+')
            y.write('0')
            r = open('New_Scores.txt', 'r')
            current_score = r.read()
            POINTS_OF_WINNING = (live.difficulty * 3) + 5
            final_score = int(current_score) + POINTS_OF_WINNING
            z = open('New_Scores.txt', 'w+')
            z.write(str(final_score))
            continue
        return final_score, current_score, POINTS_OF_WINNING



