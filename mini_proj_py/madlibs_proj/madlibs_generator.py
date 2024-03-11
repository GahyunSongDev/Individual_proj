# Read the story before replacing the words
from collections import OrderedDict


with open("before_story.txt", "r") as f:
    story2replace = f.read()

# Find the words that user needs to replace with
start_word = "["
end_word = "]"

first_letter = 0

#words = []   # use set() instead of list since I want to remove same words in this list set.
# Use an OrderedDict to maintain order and remove duplicates
words = OrderedDict()

# You can iterates with the element and the index of the element in 'the story2replace'
for i, letter in enumerate(story2replace):
    # when letter is equal to "["
    if letter == start_word:
        first_letter = i

    # when letter is qual to "]"
    if letter == end_word:
        word = story2replace[first_letter : i+1]
        words[word] = True
        first_letter = 0

# Convert the keys of the OrderedDict to a list
words = list(words.keys())

print("\n\n>>>>> The words that you need to replace <<<<< \n\n", words)

print("\n\n-------------------------------------------------------------------------------------------------------")
print("\n< HERE IS THE ORIGINAL STORY > \n\n", story2replace)
print("-------------------------------------------------------------------------------------------------------")

# input the words that user want to replace with the original words
replaced_words = {}
for k in words:
    replaced_word = input("\nEnter you want to replace with" + k + "-> " )
    replaced_words[k] = replaced_word   # store the words that user inputs for the replacing words

print("\n\n >>>>>  Here are the replaced words <<<<< \n\n" , replaced_words)

# print the story with the replaced words
for l in words:
    story2replace = story2replace.replace(l, replaced_words[l])

print("\n\n-------------------------------------------------------------------------------------------------------")
print("\n< HERE IS A NEW STORY WITH YOUR WORDS > \n\n", story2replace)
print("-------------------------------------------------------------------------------------------------------")

with open("story_replaced.txt", "w") as p:
    saved_file = p.write(story2replace)