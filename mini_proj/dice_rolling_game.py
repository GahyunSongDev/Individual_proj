import random
import time

def roll():
    max_num = 6
    min_num = 1

    roll_rand = random.randint(min_num, max_num)

    return roll_rand

while True:
    players = input("How many players want to play ?\nEnter the number of player [1 < x < 5]: ")

    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            print("\nYou all are ", players, "players.\nLet's play !")
            break
        else:
            print("\nMust be between 2 ~ 4 players! \n")
    else :
        print("\nError! you typed the invalid input.\n")

win_to_score = random.randint(10, 100)
print("In this round, the goal score is", win_to_score)
players_score = [0 for _ in range(players)] # ex ) players_score = [0, 0, 0, 0] if players are 4.

while max(players_score) < win_to_score:
    winner_found = False
    for p in range (players):
        print("\n>> NOW player", p+1, " turn ! <<\n")
        current_score = 0

        want_to_play = input("Would you like to roll ? (y/n)").lower()
        if want_to_play == "y":
            print("The dice is rolling....")
            time.sleep(3)
            game = roll()
            if game != 1:
                current_score += game
                print("you rolled", game)
                players_score[p] += current_score

                if players_score[p] >= win_to_score:
                    winner_found = True

            else :
                current_score = 0
                players_score[p] = current_score
                print("\nYou rolled 1!\nI'm sorry. You got trapped and your score reset to 0.\n")
            
        else:
            print("\nBye.")
            quit()

    total_current_score = " vs ".join(map(str, players_score))
    print("\n--------------------------------------------")
    print("The current score in this round:", total_current_score)
    print("--------------------------------------------\n")
    
    for i, score in enumerate(players_score):
        if score >= win_to_score:
            print("\nCongratulations!\nPlayer", i + 1, "won this game! They came in first place with a score of", score, "\n")
            winner_found = True
            break
    