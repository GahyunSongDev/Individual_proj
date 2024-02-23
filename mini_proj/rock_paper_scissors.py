import random

playing = input("\nDo you want to play? (YES?NO) ").lower()

if playing != "yes":
    print("\nBYE :->\n")
    quit()

opts = ["rock", "scissors", "paper"]
a_wins = 0
b_wins = 0
draw = 0

def rules(a, b):

    global a_wins, b_wins, draw
    
    if a == b:
        draw += 1
        print("We both picked", a, ". We are in a tie !")

    if a == opts[0]:
        if b == opts[1] :
            a_wins += 1
            print("I picked", a, "and YOU picked", b, "\nSo, I won and got 1 point !")
        elif b == opts[2] :
            b_wins += 1
            print("I picked", a, "and YOU picked", b, "\nSo, you won and got 1 point !")
    
    elif a == opts[1]: 
        if b == opts[0] :
            b_wins += 1
            print("I picked", a, "and YOU picked", b, "\nSo, you won and got 1 point !")
        elif b == opts[2] :
            a_wins += 1
            print("I picked", a, "and YOU picked", b, "\nSo, I won and got 1 point !")
    
    elif a == opts[2] :
        if b == opts[0] :
            a_wins += 1
            print("I picked", a, "and YOU picked", b, "\nSo, I won and got 1 point !")
        elif b == opts[1] :
            b_wins += 1
            print("I picked", a, "and YOU picked", b, "\nSo, you won and got 1 point !")
    
    else:
        print("ERROR !! Try again.")

while True:
    user_input = input("\nType either Rock / Paper / Scissors OR press any key to stop playing : ").lower()
    admin_opt = random.choice(opts)

    if user_input not in opts:
        print("See you next time ;-)")
        break
    
    print("\n----------------------------------------\n")
    rules(admin_opt, user_input)
    print("\n----------------------------------------\n")
    print("\nNow the score is ME vs YOU : ", a_wins, " vs ", b_wins, "and DRAW : ", draw, ".\n")

if a_wins < b_wins:
    print("\nCongratulations you win!\nI will win next time ;-`\n")
elif a_wins > b_wins:
    print("\nI win. Try to win next time :-`\n")
else:
    print("\nWe are in a tie. Try to win next time :-`\n")
    