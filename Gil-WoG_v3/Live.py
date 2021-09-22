import MemoryGame
import GuessGame
import CurrencyRouletteGame




def welcome(name):
    print(f"Hello {name} and welcome to the World of Games (WoG) \n Here you can find many cool games to play")


def load_game():
    gameover = 0
    diffvalid = 0
    while gameover == 0:
        try:
            choice = int(input("Please choose a game to play \n"
                               "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back \n"
                               "2. Guess Game - guess a number and see if you chose like the computer \n"
                               "3. Currency Roulette - try and guess the value of random amount of USD in ILS \n"))
            if 0 < choice < 4:

                while diffvalid == 0:
                    try:
                        diffi = int(input("Please choose game difficulty from 1 to 5 \n"))
                        if 0 < diffi < 6:
                            diffvalid = 1
                        else:
                            print("***Please enter a number between 1-5*** \n")
                    except ValueError:
                        print("***Please follow the written instructions*** \n")

                if choice == 1:
                    MemoryGame.play(diffi)
                    gameover = 1
                elif choice == 2:
                    GuessGame.play(diffi)
                    gameover = 1
                elif choice == 3:
                    CurrencyRouletteGame.play(diffi)
                    gameover = 1
            else:
                print("***Please enter a number between 1-3*** \n")

        except ValueError:
            print("***Please follow the written instructions*** \n")
