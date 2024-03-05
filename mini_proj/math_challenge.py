import random, time

opr = ["+", "-", "*"]
min_num = 1
max_num = 100
num_prob = 5
score = 0
wrong = 0

def exp_gen():
    first = random.randint(min_num, max_num)
    second = random.randint(min_num, max_num)
    operator = random.choice(opr)

    expr = str(first) + operator + str(second)
    ans = eval(expr)

    return expr, ans

playing = input("\nWould you want to try this challenge? (y/n) ").lower()

if playing != "y":
    print("\nBye ;->\n")
    quit()

input("\nPress enter key whenever you are ready !\n")
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

start = time.time()

for i in range(num_prob):
    prob, answer = exp_gen()

    while True:

        question = input("Problem " + str(i+1) + ": " + prob + " = " )
        
        if question != str(answer):
            print("\nWrong. Try again\n")
            wrong += 1
        elif question == str(answer):
            score += 1
            break
        else:
            print("\nError occured!\n")
            quit()

end = time.time()
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

total = round(end-start, 2)

if total > 60:
    total_minutes = total / 60
    print("\nYou are done in", round(total_minutes, 2), "minutes.\n")
else:
    print("\nYou are done in", total, "seconds.\n")

print("You were wrong", wrong, "times, and your score is", score, "!\n")



