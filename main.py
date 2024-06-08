from random import shuffle

# Asking if you want to take a test or not
'''
while True:
    y_n = input("Do you want to take a test? Answer with yes or no.\n")
    if y_n.lower() == "no":
        print("\nOkay, exiting program")
        exit()
    
    if y_n.lower() == "yes":
        print("\nOkay, starting test.\n")
        break

    print("\nPlease answer with yes or no.\n")
'''

word_list = {}

# Splitting the line into word and translation
with open("main.txt", "r", encoding="utf-8") as main:
    for line in main.readlines():
        if line:
            word_list[line.split("=")[0].strip()] = line.split("=")[1].strip()

maximum_words = len(word_list)

# Asking for the amount of words to be tested on
while True:
    try:
        amount = int(input(f"How many words do you want to be tested on? The maximum amount is {maximum_words}\n"))
    except ValueError:
        print("\nPlease enter an integer.\n")
        continue

    if amount < 0:
        print("\nI can only test you on a positive amount of words. Please enter a postive integer.\n")
        continue
    elif amount == 0:
        print("\nOkay, test completed.")
        exit()
    elif amount > maximum_words:
        print("\nSorry can't test you on more words than the maximum.") 
        print("Please enter an integer less than or equal to the maximum amount of words.\n")
        continue

    print("\nOkay, starting test\n")
    break

# Making a list of keys, shuffling it, and truncating it to the amount
key_list = list(word_list)
shuffle(key_list)
key_list = key_list[:amount]

score = 0
mistakes = []

# Testing and keeping track of mistakes
for i, word in enumerate(key_list, start=1):
    test = input(f"{i}. {word}\n")
    if test == word_list[word]:
        print("Correct\n")
        score += 1
    else:
        print("Incorrect\n")
        mistakes.append([word, test, word_list[word]])

# Printing mistakes
print("Here are your mistakes:")
for mistake in mistakes:
    print(f"{mistake[0]}: {mistake[1]} --> {mistake[2]}")

# Calculating score
print(f"\nYour score was {round(score/amount*100)}%.")