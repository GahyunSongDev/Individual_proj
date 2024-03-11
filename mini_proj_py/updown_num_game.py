import random

score = 0

print("Welcome to Up&Down number game !\n")
playing_1 = input("Do you want to play? (YES/NO) ")

if playing_1.lower() != "yes":
    quit()

print("\nLet's get start !\n")

def correctness_num(c):
    if c.isdigit():
        c = int(c)
        if c <= 0:
            print("Try a number greater than 0 next time.\n")
            quit()
    else:
        print("Please type a number next time.\n")
        quit()

while True:

    user_max_num = input("\nType a number for max range you want : ")
    correctness_num(user_max_num)
    user_max_num = int(user_max_num)
    random_num = random.randint(1, user_max_num + 1)

    while True:
        user_num = input("\nMake a guess : ")
        correctness_num(user_num)
        user_num = int(user_num)

        if user_num < random_num:
            print("\nUP ^")
        elif user_num > random_num:
            print("\nDOWN v")
        elif user_num == random_num:
            print("\n\nGreat Job ! you are correct ^__^\n\n ")
            score += 1
            playing_2 = input("Do you want to play another game? : ")
            if playing_2.lower() == "yes":
                break
            else:
                print("\nThank you!\n")
                print(str("Your score is "), score, str("\n\nWe hope to see you again.\n"))
                quit()
        else:
            print("\nERROR occured. \nWe are sorry, try again !\n")
            break
        


