#Functions
from random import randint
import time
import random

def loading_dots(duration, interval):
    start_time = time.time()
    print("Loading NUMBER RACE 1")
    while time.time() - start_time < duration:
        for _ in range(10):
            print(".", end="", flush=True)
            time.sleep(interval)
def main():
    print("¡Welcome to the Number Race game!")
    print("options:")
    print("1. Play")
    print("2. Help")
    print("3. About us")
    print("4. Go out")
    
    option = int(input("Select an option (1-4): "))
    
    if option == 1:
        num_players = get_num_players()
        board_level = get_board_level()
        play_game(num_players, board_level)
    elif option == 2:
        print("Press play, select the number of players and the level you choose, play and have fun")
    elif option == 3:
        print("My name is Jeison Botina, I am a 6th semester systems engineering student at CESMAG University and I hope you are enjoying this great game made with a lot of dedication and effort.")
    elif option == 4:
        print("¡See you later.!")

def get_num_players():
    while True:
        try:
            num_players = int(input("Enter the number of players (2-4): "))
            if 2 <= num_players <= 4:
                return num_players
            else:
                print("Please enter a valid number of players.")
        except ValueError:
            print("Enter a valid numeric value.")

def get_board_level():
    print("Board levels:")
    print("1. Level Básic (Board of 20 positions)")
    print("2. Level Intermediate (Board of 30 positions)")
    print("3. Level Advanced (Board of 50 positions)")
    print("4. Level Expert (Board of 100 positions)")
    
    while True:
        try:
            level = int(input("Select a level (1-4): "))
            if 1 <= level <= 4:
                return level
            else:
                print("Please, Select a valid level.")
        except ValueError:
            print("Enter a valid numeric value.")

def play_game(num_players, board_level):
    positions = [0] * num_players
    consecutive_pairs = [0] * num_players
    meta = get_meta(board_level)
    
    while True:
        for player in range(num_players):
            input(f"player's turn {player + 1}. Press enter to roll the dice.")
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            total = dice1 + dice2
            positions[player] += total
            
            print(f"Player {player + 1} threw {dice1} y {dice2}. Advance to position {positions[player]}")
            
            if positions[player] >= meta:
                print(f"¡Player {player + 1} has reached the goal! Win!")
                return
            
            if dice1 == dice2:
                consecutive_pairs[player] += 1
                if consecutive_pairs[player] == 3:
                    print(f"¡Player {player + 1} has obtained 3 consecutive pairs! Win!")
                    return
            else:
                consecutive_pairs[player] = 0

def get_meta(board_level):
    if board_level == 1:
        return 20
    elif board_level == 2:
        return 30
    elif board_level == 3:
        return 50
    elif board_level == 4:
        return 100
loading_dots(5, 0.5)
if __name__ == "__main__":
    main()
