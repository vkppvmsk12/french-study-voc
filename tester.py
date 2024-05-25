import random

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
with open("voc.txt", "r") as voc:
    for line in voc.readlines():
        word_list[line.split("=")[0].strip()] = line.split("=")[1].strip()

maximum_words = len(word_list)

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

key_list = list(word_list)
random.shuffle(key_list)
key_list = key_list[:amount]

score = 0
mistakes = []

for word in key_list:
    test = input(f"What is the translation of {word}?\n")
    if test == word_list[word]:
        print("Correct\n")
        score += 1
    else:
        print("Incorrect\n")
        mistakes.append([word, test, word_list[word]])

print("\nHere are your mistakes:")
for mistake in mistakes:
    print(f"{mistake[0]}: {mistake[1]} --> {mistake[2]}")

print(f"\nYour score was {round(score/amount*100)}%.")