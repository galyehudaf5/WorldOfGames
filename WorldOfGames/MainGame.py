import live
import GuessGame
import MemoryGame
import CurrencyRouletteGame
import Score

live._welcome("Guy")
live._load_game()

if live.choice == 2:
    GuessGame._play()
elif live.choice == 1:
    MemoryGame._play()
elif live.choice == 3:
    CurrencyRouletteGame._play()

print(f'your final score is:{Score.final_score}')
