import time

count_Gold = 0
goal = ["right", "up", "left", "up", "left", "left", "down", "right"]       # the direction to get a gold = right->up->left->up->left->left->down->right


name = input("What is your name? ")

while name:

    print("\nHello", name)
    playing = input("\nDo want to go on an advanture to find a gold? (YES/NO) ").lower()

    # When user does not want to play
    if playing != "yes":
        print("\nBye ;-|", name)
        quit()

    # declare variables for directions
    count_R = 0
    count_L = 0
    count_U = 0
    count_D = 0
    user = []

    # functions 
    # Fail to get a gold.
    def fail():
        user.pop()
        print("\nI'm sorry you can't take the gold. Try again.")

    def error():
        print("\nError occured! Try next time.")

    def mining():
        print("\nYou are mining now....")
        time.sleep(5)
        print("*****************************************")

    def success():
        global count_Gold
        count_Gold += 1
        print("\n\nCongratulation ! You found the gold.")

    def final_q(a):
        # When it's fail to get a gold
        if a == "1":
            mining()
            fail()
        
        # When it's succes to get a gold
        elif a == "2":
            mining()
            success()
        
        # Error
        else:
            error()

    while True:

        user_Q = input("\nType the direction you want (Right / Left / Up / Down): ").lower()
        user.append(user_Q)

        # type right
        if user_Q == "right":
            count_R +=  1
            print(user)
            
            # When user type "right" in the begining
            if user[0] == "right" and count_R < 2 and user == ["right"]:
                continue

            # last step to find golds
            elif user[7] == "right" and count_R == 2 and user == goal:
                q1 = input("\nThere are two moutains you can choose to mine gold. Which one do you want?\n1. first mountain.\n2. seconde mountain.\n=> ")
                
                # choose 1
                if q1 == "1":
                    q_2 = input("\nYou choosethe first mountain. In order to mine golds in this mountain, you need a tool.\nwhich one do you want?\n1. I don't need a tool. I want to use my hand.\n2. a gold pan and a shovel.\n=> ")
                    
                    # whether success or fail 
                    final_q(q_2)
                    print("\nYou currently have", count_Gold, "golds.")
                    print("*****************************************")
                    break

                # choose 2
                elif q1 == "2":
                    q_3 = input("\nYou choose the seconde mountain. In order to mine golds in this mountain, you need a tool.\nwhich one do you want?\n1. I don't need a tool. I want to use my hand.\n2. Rock hammers & Picks..\n=> ")
                    
                     # whether success or fail 
                    final_q(q_3)
                    print("\nYou currently have", count_Gold, "golds.")
                    print("*****************************************")
                    break
                else:
                    error()
                    quit()

            # go back to the start page   
            else:
                fail()
                break
        
        # type lift
        elif user_Q == "left":
            count_L +=  1
            print(user)

            # types left first time
            if user[2] == "left" and count_L == 1 and user == ["right", "up", "left"]:
                q_4 = input("\nYou came to river. How do you want to cross this river?\n1. Make a raft. 2. Swim accross\n=> ")

                if q_4 == "1":
                    print("\nGreat, you made a nice raft !")
                    continue
                elif q_4 == "2":
                    print("\nYou swam accross this river and were eaten by alligator. Try again")
                    #user.pop()
                    #count_L -= 1
                    break
                else:
                    error()
                    quit()
                    
            # types left second time
            elif user[4] == "left" and count_L == 2 and user == ["right", "up", "left", "up", "left"]:
                q_5 = input("\nYou are half way to get the mountains that have golds.\nDo you want to take a rest? (YES/NO) ").lower()

                if q_5 == "yes":
                    print("\nYou are taking a break.")
                    time.sleep(5)
                    print("\nYou are recharged with energy. Keep going!")
                    continue                          
                elif q_5 == "no":
                    print("\nYou are exhausted, so you can't take even on step now.\n Take some rest for 20 seconds!")
                    time.sleep(20)
                    print("\nYou are recharged with energy. Keep going!")
                    continue
                else:
                    error()
                    quit()

            # when user types third time
            elif user[5] == "left" and count_L == 3 and user == ["right", "up", "left", "up", "left", "left"]:
                print("\nYou're almost there! Good luck.")
                continue

            else:
                fail()
                break

        # type up
        if user_Q == "up":
            count_U += 1
            print(user)

            # type up the first time
            if user[1] == "up" and count_U == 1 and user == ["right", "up"]:
                print("\nGreat!")
                continue

            # type up second time
            elif user[3] == "up" and count_U == 2 and user == ["right", "up", "left", "up"]:
                q_7 = input("\nYou are on the right direction. There is a well around the bush.\nDo you want to come to get some drink? (YES/NO) ")

                if q_7 == "yes":
                    print("Lucky! >_< There's a big well and have a lot of water.\nYou drank some water.")
                    continue
                elif q_7 == "no":
                    print("\nYou are dehydrated. Try next time.")
                    quit()
                else:
                    error()
                    quit()

            else:
                fail()
                break

        # type down
        if user_Q == "down":
            count_D += 1
            print(user)

            # type down first time
            if user[6] == "down" and count_D == 1 and user == ["right", "up", "left", "up", "left", "left", "down"]:
                print("\nYou can see two mountains in the distance. Keep going !! ")

            else:
                fail()
                break

        else:
            error()
            quit()
