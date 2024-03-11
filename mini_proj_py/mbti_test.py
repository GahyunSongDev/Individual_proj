import time

print("Welcome to my MBTI test!\n")

playing = input("Do you want to test? ")

if playing.lower() != "yes":
    quit()

print("\nOkay, let's test!\n")

# Initialize boolean variables for each question
valid_input_1, valid_input_2, valid_input_3,  valid_input_4 = False, False, False, False

while not valid_input_1:
    question_1 = input("1. When faced with a social gathering, How do you usually feel ? choose one. \na. Feel energied and enthusiastic about interacting with others.\nb. prefer smaller groups or one-on-one conversation and find larger gatherings draining.\n=> ")
    if question_1.lower() == "a":
        print("You have an extraversion! (E) \n")
        first = "E"
        valid_input_1 = True
    elif question_1.lower() == "b":
        print("Your have an introversion! (I) \n")
        first = "I"
        valid_input_1 = True
    else: 
        print("Please, choose either 'a' or 'b'. \n")

while not valid_input_2:
    question_2 = input("2. When making decisions, how do you do ? choose one. \na. rely more on concrete facts, details, and practical considerations\nb. focus on possibilities, patterns, and potential future outcomes\n=> ")
    if question_2.lower() == "a":
        print("You have a sensing! (S) \n")
        second = "S"
        valid_input_2 = True
    elif question_2 == "b":
        print("Your have an intuition! (N) \n")
        second = "N"
        valid_input_2 = True
    else: 
        print("Please, choose either 'a' or 'b'. \n")

while not valid_input_3:
    question_3 = input("3. When faced with a decision, how do you tend to do ? choose one. \na. prioritize the impact on people's feelings and values, seeking harmony\nb. prioritize logic, consistency, and objective analysis\n=> ")
    if question_3.lower() == "a":
        print("You have a feeling! (F) \n")
        third = "F"
        valid_input_3 = True
    elif question_3.lower() == "b":
        print("Your have a thinking! (T) \n")
        third = "T"
        valid_input_3 = True
    else: 
        print("Please, choose either 'a' or 'b'. \n")

while not valid_input_4:
    question_4 = input("4. In your daily life, what do you prefer ? choose one. \na. to go with the flow, adapt easily to changes, and keep your options open\nb. to structure, planning, and having a clear sense of closure\n=> ")
    if question_4.lower() == "a":
        print("You have a perceiving! (P) \n")
        fourth = "P"
        valid_input_4 = True
    elif question_4.lower() == "b":
        print("Your have an judging! (J) \n")
        fourth = "J"
        valid_input_4 = True
    else: 
        print("Please, choose either 'a' or 'b'. \n")

print("Test is over !\nPlease wait for a moment.\n")
time.sleep(5)
mbti = first+second+third+fourth
print("Your MBTI is " + mbti + ".")

mbti_descriptions = {
    "ISTJ": "Practical and organized, you value structure and reliability in your approach to tasks and decisions.",
    "ISFJ": "Compassionate and detail-oriented, you prioritize harmony and care for others, often taking on supportive roles.",
    "INFJ": "Insightful and empathetic, you seek deeper connections and are driven by a sense of purpose and personal values.",
    "INTJ": "Strategic and independent, you thrive on long-term planning, intellectual pursuits, and efficient problem-solving.",
    "ISTP": "Adaptable and hands-on, you excel in troubleshooting and enjoy exploring the practical application of ideas.",
    "ISFP": "Artistic and gentle, you appreciate aesthetics, value personal expression, and seek harmony in your surroundings.",
    "INFP": "Idealistic and creative, you are driven by inner values, imagination, and a desire for authenticity.",
    "INTP": "Analytical and curious, you love exploring concepts, ideas, and possibilities, often seeking innovative solutions.",
    "ESTP": "Energetic and spontaneous, you thrive in action-oriented environments, enjoying challenges and variety.",
    "ESFP": "Sociable and lively, you embrace the present moment, enjoy social interactions, and bring enthusiasm to your pursuits.",
    "ENFP": "Enthusiastic and imaginative, you value creativity, connection, and often pursue a variety of interests with passion.",
    "ENTP": "Innovative and curious, you excel in brainstorming and enjoy exploring possibilities, often challenging the status quo.",
    "ESTJ": "Efficient and organized, you value tradition and structure, excelling in leadership roles and practical decision-making.",
    "ESFJ": "Social and nurturing, you prioritize relationships, harmony, and often take on caregiving roles within your communities.",
    "ENFJ": "Charismatic and empathetic, you inspire others and are driven by a strong sense of values, often taking on leadership roles.",
    "ENTJ": "Visionary and strategic, you excel in leadership, value efficiency, and are focused on achieving long-term goals.",
}


if mbti in mbti_descriptions:
    print(f"{mbti}'s personality : {mbti_descriptions[mbti]}\n")
else:
    print("ERROR ! Please try again later. \n")

print("Thank you so much :-) \n")
