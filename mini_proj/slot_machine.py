import random

class Slotmachine:
    def __init__(self):
        # the kind of items = 5 kinds
        self.kind_items = ["Apple", "Orange", "Melon", "Lemmon", "Strawberry"]
        # the number of reels
        self.num_of_reels = 3
        #reels
        self.reels = [0, 0, 0]


    def spin(self):
        self.reels = [random.choice(self.kind_items) for _ in range(self.num_of_reels)]
        return self.reels


    def payout(self, spin_result, m):
        if all(item == spin_result[0] for item in spin_result):
            jackpot = 100 * m
            print("\n---------------------------------------------")
            print("\nSpin Result:", spin_result)
            print("\nCogratulation ! You won $", jackpot, ".\n")
            print("---------------------------------------------\n")
            return jackpot
        elif any(spin_result.count(item) == 2 for item in spin_result):
            earned = 20 * m
            print("\n---------------------------------------------")
            print("\nSpin Result:", spin_result)
            print("\nTwo of the same item! You win $", earned, ".\n")
            print("\n---------------------------------------------")
            return earned
        else:
            earned = 0 * m
            print("\n---------------------------------------------")
            print("\nSpin Result:", spin_result)
            print("\nBetter luck next time!")
            print("\n---------------------------------------------")
            return earned


def main():
    deposit = 0
    balance = 0

    while True:

        # playing = input("\nDo you want to play ? (yes/no) ").lower()
        # if playing != "yes":
        #     print("\nBye.\n")
        #     quit()
        
        # deposit in order to play a game
        q_deposit = input("\nType amount you want to deposit ( To quit, type q ) : ")
        if q_deposit.isdigit():
            deposit = int(q_deposit)
            balance += deposit
        elif q_deposit.lower() == "q":
            print("\nBlance : " + str(balance) + "\n")
            print("\nBye.\n")
            quit()
        else :
            print("\nType number for the money you want to deposit next time ! \n")
            quit()
        
        # There are 3 options to bet -> $5, $50, $100
        opt_to_bet = [5, 50, 100]
        bet = input("\nHow much money you want to bet for this game? (choose one from 1 - 3)\n1. $5\n2. $50\n3. $100\n=> ")
        if bet == "1":
            bet = opt_to_bet[0]
            multiply = 1
        elif bet == "2":
            bet = opt_to_bet[1]
            multiply = 2
        elif bet == "3":
            bet = opt_to_bet[2]
            multiply = 3
        else :
            print("\nError occured !\n")

        # play a game if balance is more than the money you bet
        if balance >= bet:

            if bet == 5:
                balance -= 5
            elif bet == 50:
                balance -= 50
            elif bet == 100:
                balance -= 100
            else :
                print("\nError occured !\n")

            # spin the slot.
            slot = Slotmachine()
            spin_result = slot.spin()

            # win money
            win = slot.payout(spin_result, multiply)
            balance += win

            print("\n\nYour balance : " + str(balance))
            
        elif balance < bet:
            asking_playing = input("\nYou have $" + str(balance) + "\nIt is not enough for playing.\nChoose one.\n1. Deposit more money.\n2. No more playing.\n=> ")
            if asking_playing == "1":
                continue
            elif asking_playing == "2":
                print("\nWe hope to see you again ;-)\n")
                quit()
            else:
                print("\nError.\n")
                quit()
        else:
            print("\nError!\n")
            quit()

    
if __name__ == "__main__":
    main()
