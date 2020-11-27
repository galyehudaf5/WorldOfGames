difficulty = 1

f = open('Scores.txt', 'r')
current_score = f.read()
POINTS_OF_WINNING = (difficulty * 3) + 5
final_score = int(current_score) + POINTS_OF_WINNING
x = open('Scores.txt', 'w+')
x.write(str(final_score))